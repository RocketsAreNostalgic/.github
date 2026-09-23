#!/usr/bin/env python3
"""Run the checked-in liveness workflow's real Bash step against read-only API fixtures."""
import json
import os
import pathlib
import subprocess
import tempfile
import textwrap
from datetime import datetime, timedelta, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/release-liveness-observer.yml"
SCRIPT = textwrap.dedent(WORKFLOW.read_text().split("        run: |\n", 1)[1])
SHA = "a" * 40
OTHER = "b" * 40
REPO = "RocketsAreNostalgic/probe"
NOW = datetime.now(timezone.utc)

MOCK = r'''#!/usr/bin/env python3
import json, os, sys, base64, pathlib
f=json.loads(pathlib.Path(os.environ['FIXTURE']).read_text())
argv=sys.argv[1:]
def write(v):
    print(json.dumps(v) if not isinstance(v,str) else v)
def get(path):
    if path.endswith('/git/tags/'+ 'c'*40): return {'object':{'type':'commit','sha':f.get('tag_sha','a'*40)}}
    if '/pulls/' in path and path.rsplit('/',1)[-1].isdigit(): return {'labels':[{'name':x} for x in f['labels']]}
    if '/actions/runs?' in path: return [{'workflow_runs':f.get('runs',[])}]
    if path.endswith('/pulls'): return [f['prs']]
    if '/contents/' in path: return {'content':base64.b64encode(json.dumps({'.':'1.2.3'}).encode()).decode()}
    if path=='repos/RocketsAreNostalgic/probe': return {'default_branch':'main'}
    raise RuntimeError('Unexpected GH GET: '+path)
if pathlib.Path(sys.argv[0]).name == 'gh':
    assert argv[0]=='api' and '--method' not in argv or ('--method' in argv and argv[argv.index('--method')+1]=='GET'), argv
    path=next(x for x in argv[1:] if x.startswith('repos/'))
    if f.get('gh_fail') and f['gh_fail'] in path:
        print('mock GH API failure',file=sys.stderr); sys.exit(1)
    v=get(path)
    if '--jq' in argv:
        q=argv[argv.index('--jq')+1]
        if q=='.default_branch': write(v['default_branch'])
        elif q=='.content': write(v['content'])
        elif q=='[.labels[].name]': write([x['name'] for x in v['labels']])
        else: raise RuntimeError(q)
    else: write(v)
elif pathlib.Path(sys.argv[0]).name == 'curl':
    url=argv[-1]; target=pathlib.Path(argv[argv.index('--output')+1])
    kind='release' if '/releases/tags/' in url else 'tag' if '/git/ref/tags/' in url else None
    assert kind, url
    if f.get('curl_fail')==kind: sys.exit(7)
    status=f.get(kind+'_status',200 if f.get(kind) is not None else 404)
    target.write_text(json.dumps(f.get(kind,{})))
    print(status,end='')
else: raise RuntimeError(argv)
'''

def base():
    return {
        "prs": [{"number": 3, "title": "chore(main): release 1.2.3", "merged_at":
                 (NOW-timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                 "merge_commit_sha": SHA, "labels": []}],
        "labels": ["autorelease: pending"], "tag": None, "release": None, "runs": [],
    }

def published(f):
    f.update(labels=["autorelease: tagged"], tag={"object": {"type": "commit", "sha": SHA}},
             release={"tag_name": "v1.2.3", "draft": False,
                      "published_at": "2026-09-23T00:00:00Z", "target_commitish": SHA})

def run(name, fixture, expected_state=None, error=None):
    with tempfile.TemporaryDirectory() as td:
        directory=pathlib.Path(td)
        (directory/'fixture.json').write_text(json.dumps(fixture))
        for tool in ('gh','curl'):
            p=directory/tool; p.write_text(MOCK); p.chmod(0o755)
        env={**os.environ,'PATH':td+':'+os.environ['PATH'],'FIXTURE':str(directory/'fixture.json'),
             'GITHUB_REPOSITORY':REPO,'GITHUB_RUN_ID':'99','GH_TOKEN':'fixture-only',
             'GITHUB_OUTPUT':str(directory/'output'),'GITHUB_STEP_SUMMARY':str(directory/'summary'),
             'RAN_GRACE_MINUTES':'60','RAN_MANIFEST_PATH':'.release-please-manifest.json',
             'RAN_RELEASE_PR_TITLE_PREFIX':'chore(main): release ',
             'RAN_ACTIVE_WORKFLOW_NAMES':'Release Please'}
        p=subprocess.run(['bash','-euo','pipefail','-c',SCRIPT],env=env,text=True,capture_output=True)
        output=(directory/'output').read_text() if (directory/'output').exists() else ''
        summary=(directory/'summary').read_text() if (directory/'summary').exists() else ''
        ok=(p.returncode==0 and 'state='+expected_state in output) if expected_state else (p.returncode!=0 and error in (p.stdout+p.stderr+summary))
        print(('PASS' if ok else 'FAIL')+' '+name+': '+(output.strip() or (p.stdout+p.stderr+summary)[-220:].strip()))
        if not ok: raise AssertionError((name,p.returncode,p.stdout,p.stderr,summary))

for profile in ('A','B'):
    f=base(); published(f); run('published Profile '+profile,f,'published')
f=base(); published(f); f['labels']=['autorelease: pending']; run('stale published release with unsettled PR label',f,error='labels remain unsettled')
f=base(); published(f); f['labels']=['autorelease: pending']; f['prs'][0]['merged_at']=(NOW-timedelta(minutes=10)).strftime('%Y-%m-%dT%H:%M:%SZ'); run('published with transitional label inside grace',f,'pending')
f=base(); published(f); f['labels']=['autorelease: pending']; f['runs']=[{'id':12,'name':'Release Please','status':'in_progress','created_at':'2026-09-20T00:00:00Z','updated_at':'2026-09-20T00:00:00Z'}]; run('published with label transition and exact active run',f,'pending')
f=base(); f['release']={'tag_name':'v1.2.3','draft':True,'published_at':None}; run('hidden/unpublished draft stale',f,error='stranded')
f=base(); f['prs'][0]['merged_at']=(NOW-timedelta(minutes=10)).strftime('%Y-%m-%dT%H:%M:%SZ'); run('grace',f,'pending')
f=base(); f['runs']=[{'id':12,'name':'Release Please','status':'in_progress','created_at':'2026-09-20T00:00:00Z','updated_at':'2026-09-20T00:00:00Z'}]; run('exact candidate active',f,'pending')
f=base(); run('stranded stale',f,error='stranded')
f=base(); f['labels']=['release: reconciled']; run('exact candidate reconciled',f,'reconciled')
f=base(); f['labels']=['release: reconciled','autorelease: pending']; run('conflicting reconciliation labels',f,error='stranded')
f=base(); published(f); f['tag']['object']['sha']=OTHER; run('wrong final tag',f,error='not exact candidate')
f=base(); published(f); f['labels'].append('autorelease: abandoned'); run('candidate abandoned after discovery',f,error='became autorelease: abandoned')
f=base(); published(f); f['tag']={'object':{'type':'tag','sha':'c'*40}}; run('annotated tag peeled',f,'published')
f=base(); f['prs'].append(dict(f['prs'][0],number=4)); run('ambiguous merged candidates',f,error='found 2')
f=base(); f['release_status']=403; run('release permission/API failure',f,error='HTTP 403')
f=base(); f['tag_status']=500; run('tag API failure',f,error='HTTP 500')
f=base(); f['curl_fail']='release'; run('release transport failure',f,error='transport layer')
f=base(); f['gh_fail']='/actions/runs'; run('Actions API failure',f,error='mock GH API failure')
f=base(); f['runs']=[{'id':14,'name':'Quality','status':'in_progress'}, {'id':15,'name':'Release Please','status':'completed','updated_at':'2026-09-20T00:00:00Z'}]; run('unrelated/completed old runs',f,error='stranded')
f=base(); published(f); f['tag']=None; run('published object missing final tag',f,error='no final Git tag')

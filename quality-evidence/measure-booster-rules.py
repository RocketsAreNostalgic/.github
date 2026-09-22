#!/usr/bin/env python3
"""Audit aid for repeating baseline, naming/Yoda/alignment probes and fix measurements.
Usage: python3 measure-booster-rules.py LAB_ROOT PHP_BINARY MATCHING_VENDOR_DIR
LAB_ROOT contains seven exact source snapshots named as in the accompanying JSON.
Uses only the external quality toolchain; never installs/runs consumer dependencies.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import collections, difflib, hashlib, json, os, subprocess, xml.etree.ElementTree as ET
import sys, tempfile
ROOT=Path(sys.argv[1]).resolve()
PHP=Path(sys.argv[2]).resolve()
VENDOR=Path(sys.argv[3]).resolve()
META=json.loads(Path(__file__).with_name('booster-rule-results.json').read_text())['repositories']
for repo, meta in META.items():
 snapshot=ROOT/repo
 assert (snapshot/'.git').exists(), 'Use disposable exact-revision Git checkouts'
 head=subprocess.run(['git','-C',str(snapshot),'rev-parse','HEAD'],check=True,capture_output=True,text=True).stdout.strip()
 assert head == meta['sha'], f'{repo}: checkout HEAD {head} != expected {meta["sha"]}'
 status=subprocess.run(['git','-C',str(snapshot),'status','--porcelain=v1','--untracked-files=all','--ignored'],check=True,capture_output=True,text=True).stdout
 assert status == '', f'{repo}: checkout must contain only tracked clean revision bytes before probing'
 assert not (snapshot/'audit-strict.xml').exists(), 'Reserved audit filename already exists'
(ROOT/'snapshots.json').write_text(json.dumps({repo: {'sha': meta['sha']} for repo, meta in META.items()}, indent=2, sort_keys=True)+'\n')

SEED=json.loads(Path(__file__).with_name('booster-rule-results.json').read_text())
php_version=subprocess.run([str(PHP),'-r','echo PHP_VERSION;'],check=True,capture_output=True,text=True).stdout
assert ('PHP '+php_version) == SEED['runtime'], f'PHP runtime {php_version} != reviewed {SEED["runtime"]}'
composer_json=json.loads((VENDOR/'composer/installed.json').read_text())
packages=composer_json.get('packages', composer_json)
installed={p['name']:{'version':p.get('version'),'reference':(p.get('source') or {}).get('reference')} for p in packages}
for name, expected in SEED['tools'].items():
 actual=installed.get(name)
 assert actual is not None, f'Missing reviewed tool {name}'
 assert actual['version'] == expected['version'] and actual['reference'] == expected['reference'], f'{name}: installed identity differs from reviewed evidence'

OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
ENV={'PATH':str(PHP.parent)+':/usr/bin:/bin','HOME':tempfile.mkdtemp(prefix='booster-rule-home-')}
NAMES=['WordPress.NamingConventions.ValidFunctionName','WordPress.NamingConventions.ValidVariableName']
YODA=['WordPress.PHP.YodaConditions']
ALIGN=['Generic.Formatting.MultipleStatementAlignment','WordPress.Arrays.MultipleStatementAlignment']
RESTORE=['WordPress.NamingConventions.ValidFunctionName.MethodNameInvalid',NAMES[1],YODA[0]]

def run(repo, label, tool, cfg, args=()):
 cmd=[str(PHP),str(VENDOR/'bin'/tool),'--standard='+cfg,'--parallel=4','-q',*args]
 p=subprocess.run(cmd,cwd=ROOT/repo,env=ENV,capture_output=True,text=True,timeout=900)
 (OUT/(repo+'-'+label+'.log')).write_text(p.stdout+p.stderr)
 if p.returncode not in (0,1,2,3): raise RuntimeError(repo+' '+label+' '+str(p.returncode)+' '+p.stdout[-1000:]+p.stderr[-1000:])
 return p

def summary(report):
 groups={};files=[]
 for path,row in report['files'].items():
  files.append(path)
  for m in row['messages']:
   code=m['source']; g=groups.setdefault(code,{'errors':0,'warnings':0,'fixable':0,'files':set(),'examples':[]})
   g['errors' if m['type']=='ERROR' else 'warnings']+=1;g['fixable']+=int(m['fixable']);g['files'].add(path)
   if len(g['examples'])<3:g['examples'].append({'path':path,'line':m['line'],'message':m['message']})
 for g in groups.values():g['files']=sorted(g['files'])
 return {'totals':report['totals'],'files':sorted(files),'diagnostics':groups}

def measure(repo):
 meta=META[repo];dest=ROOT/repo;cfg=meta['config']; result={'sha':meta['sha']}
 original={str(p.relative_to(dest)):p.read_bytes() for p in dest.rglob('*.php')}
 p=run(repo,'baseline','phpcs',cfg,['--report=json']); baseline=json.loads(p.stdout);result['baseline']=summary(baseline);result['baseline']['exit']=p.returncode
 print(repo,'baseline',baseline['totals'],len(baseline['files']),flush=True)
 tree=ET.parse(dest/cfg);root=tree.getroot()
 for rule in list(root.findall('rule')):
  if rule.get('ref') in RESTORE and rule.findtext('severity')=='0':root.remove(rule)
  else:
   for ex in list(rule.findall('exclude')):
    if ex.get('name') in RESTORE:rule.remove(ex)
 rule=ET.SubElement(root,'rule',{'ref':ALIGN[0]});props=ET.SubElement(rule,'properties');ET.SubElement(props,'property',{'name':'error','value':'true'})
 rule=ET.SubElement(root,'rule',{'ref':ALIGN[1]});ET.SubElement(rule,'type').text='error'
 candidate='audit-strict.xml';tree.write(dest/candidate,encoding='unicode')
 try:
  p=run(repo,'strict','phpcs',candidate,['--sniffs='+','.join(NAMES+YODA+ALIGN),'--report=json']);result['strict']=summary(json.loads(p.stdout));result['strict']['exit']=p.returncode
  print(repo,'strict',result['strict']['totals'],flush=True)
  result['fixes']={}
  for label,sniffs in [('alignment',ALIGN),('yoda',YODA)]:
   args=['--sniffs='+','.join(sniffs)]
   p=run(repo,label+'-fix','phpcbf',candidate,args);changed=[];adds=deletes=0
   for name,data in original.items():
    updated=(dest/name).read_bytes()
    if updated!=data:
     a=b=0
     for line in difflib.ndiff(data.decode().splitlines(),updated.decode().splitlines()):
      if line.startswith('+ '):a+=1
      if line.startswith('- '):b+=1
     changed.append({'path':name,'added_lines':a,'removed_lines':b});adds+=a;deletes+=b
   first={name:hashlib.sha256((dest/name).read_bytes()).hexdigest() for name in original}
   p2=run(repo,label+'-second','phpcbf',candidate,args)
   stable=all(first[name]==hashlib.sha256((dest/name).read_bytes()).hexdigest() for name in original)
   check=run(repo,label+'-after','phpcs',candidate,[*args,'--report=json']);after=summary(json.loads(check.stdout))
   result['fixes'][label]={'first_exit':p.returncode,'second_exit':p2.returncode,'stable':stable,'changed_files':changed,'added_lines':adds,'removed_lines':deletes,'remaining':after['totals'],'check_exit':check.returncode}
   for name,data in original.items():(dest/name).write_bytes(data)
   print(repo,label,'files',len(changed),'lines',adds,deletes,'stable',stable,flush=True)
 finally:
  for name,data in original.items():(dest/name).write_bytes(data)
  (dest/candidate).unlink(missing_ok=True)
 (OUT/(repo+'.json')).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 return repo
with ThreadPoolExecutor(max_workers=3) as pool:
 for repo in pool.map(measure,META):print('DONE',repo,flush=True)



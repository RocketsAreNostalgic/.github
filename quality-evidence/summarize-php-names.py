#!/usr/bin/env python3
"""Audit aid joining a local AST inventory to local PHPCS probe output.

Usage: python3 summarize-php-names.py LAB_ROOT RAW_INVENTORY OUTPUT_JSON
LAB_ROOT is the disposable tree used by measure-booster-rules.py, including its
results/*-strict.log JSON reports and snapshots.json revision metadata.
This is a bounded static inventory, not a complete PHP call-graph analysis.
"""
from collections import Counter, defaultdict
from pathlib import Path
import hashlib
import json
import re
import sys

lab, raw, output = map(Path, sys.argv[1:])
data = json.loads(raw.read_text())
assert not data['errors'], data['errors']
metadata = json.loads((lab / 'snapshots.json').read_text())
assert {r['repo'] for r in data['files']} == set(metadata), 'Snapshot repository set differs from revision metadata'
parser_identity=data.get('toolchain',{}).get('parser')
assert parser_identity and parser_identity.get('name') == 'nikic/php-parser', 'AST inventory parser identity missing'
assert parser_identity.get('version') == 'v5.8.0' or parser_identity.get('version') == '5.8.0', f'Unexpected parser version: {parser_identity}'
import subprocess
for repo, meta in metadata.items():
    snapshot = lab / repo
    assert (snapshot / '.git').exists(), f'{repo}: snapshot must be a Git checkout'
    actual = subprocess.run(
        ['git', '-C', str(snapshot), 'rev-parse', 'HEAD'],
        check=True, capture_output=True, text=True
    ).stdout.strip()
    assert actual == meta['sha'], f'{repo}: snapshot HEAD {actual} != recorded {meta["sha"]}'
    status = subprocess.run(
        ['git', '-C', str(snapshot), 'status', '--porcelain=v1', '--untracked-files=all'],
        check=True, capture_output=True, text=True
    ).stdout
    assert status == '', f'{repo}: snapshot must remain clean while inventory is summarized'
    expected = subprocess.run(
        ['git', '-C', str(snapshot), 'ls-files', '-z', '--', '*.php'],
        check=True, capture_output=True
    ).stdout.decode().split('\0')
    expected = {path for path in expected if path}
    actual_files = {row['file'] for row in data['files'] if row['repo'] == repo}
    assert actual_files == expected, f'{repo}: AST inventory path set differs from tracked PHP set'
runtime = lambda path: not path.startswith(('tests/', 'scripts/'))
coord = lambda row: (row['repo'], row['file'], row['line'], row['name'])
for row in data['files']:
    assert hashlib.sha256((lab / row['repo'] / row['file']).read_bytes()).hexdigest() == row['sha256']
methods = {coord(row): row for row in data['methods']}
diagnostics = []
selected = set()
flagged_methods = []
variable_lines = defaultdict(set)
property_lines = set()
for repo in metadata:
    report = json.loads((lab / 'results' / (repo + '-strict.log')).read_text())
    for file, details in report['files'].items():
        selected.add((repo, file))
        for message in details['messages']:
            if not message['source'].startswith('WordPress.NamingConventions.'):
                continue
            row = dict(message, repo=repo, file=file)
            diagnostics.append(row)
            if row['source'].endswith('.MethodNameInvalid'):
                name = re.search(r'Method name "([^"]+)"', row['message']).group(1)
                flagged_methods.append(methods[(repo, file, row['line'], name)])
            elif '.ValidVariableName.' in row['source']:
                name = re.search(r'"\$([^" ]+)"', row['message']).group(1)
                if '.UsedPropertyNotSnakeCase' not in row['source']:
                    variable_lines[(repo, file, name)].add(row['line'])
                    property_lines.add((repo, file, row['line'], name))

flagged_properties = [r for r in data['properties'] if coord(r) in property_lines]
flagged_parameters = [r for r in data['parameters'] if coord(r) in property_lines]
flagged_variables = [r for r in data['variables'] if set(r['lines']) & variable_lines[(r['repo'], r['file'], r['name'])]]
production_classes = {r['class']: r for r in data['classes'] if runtime(r['file']) and not r['class'].startswith('@')}
assert len(production_classes) == sum(runtime(r['file']) and not r['class'].startswith('@') for r in data['classes'])
class_methods = defaultdict(set)
for row in data['methods']:
    if runtime(row['file']):
        class_methods[row['class']].add(row['name'])

def ancestors(class_name, visited=None):
    visited = set() if visited is None else visited
    if class_name in visited:
        return set()
    visited.add(class_name)
    direct = set(production_classes.get(class_name, {}).get('parents', []))
    return direct | set().union(*(ancestors(p, visited) for p in direct)) if direct else set()

camel_methods = [r for r in data['methods'] if re.search('[A-Z]', r['name']) and not r['name'].startswith('__')]
flagged_coords = {coord(r) for r in flagged_methods}
unreported_runtime_methods = [r for r in camel_methods if runtime(r['file']) and coord(r) not in flagged_coords]
contracts = []
for row in camel_methods:
    if not runtime(row['file']):
        continue
    for parent in ancestors(row['class']):
        owner = production_classes.get(parent)
        if owner and owner['repo'] != row['repo'] and row['name'] in class_methods[parent]:
            contracts.append({'owner_repo': owner['repo'], 'contract': parent, 'consumer_repo': row['repo'], 'class': row['class'], 'method': row['name'], 'file': row['file'], 'line': row['line']})

flagged_names = {row['name'] for row in camel_methods if runtime(row['file'])}
cross_calls = []
for row in data['calls']:
    target = production_classes.get(row['target'])
    if target and target['repo'] != row['repo'] and row['method'] in flagged_names:
        cross_calls.append(dict(row, target_repo=target['repo']))
string_candidates = [r for r in data['strings'] if r['value'] in flagged_names or ('::' in r['value'] and r['value'].rsplit('::', 1)[-1] in flagged_names)]
external_ancestors = Counter(p for c in production_classes.values() for p in c['parents'] if p not in production_classes)
external_method_candidates = [dict(r, external_ancestors=sorted(p for p in ancestors(r['class']) if p not in production_classes)) for r in camel_methods if runtime(r['file']) and any(p not in production_classes for p in ancestors(r['class']))]

summary = {'revisions': {repo: meta['sha'] for repo, meta in metadata.items()}, 'method': {
    'parser': f"{parser_identity['name']} {parser_identity['version']} @ {parser_identity.get('reference')}",
    'scope': f"All {len(data['files'])} tracked PHP files parsed; counts of flagged declarations retain the original PHPCS scope and inline exceptions. A separate camelCase candidate inventory includes methods skipped by WPCS inheritance heuristics; magic methods starting __ are excluded.",
    'caller_resolution': 'Static class calls, $this, directly typed parameters/properties and immediately instantiated receivers only. Does not resolve flow, chained returns, aliases, dynamic dispatch, reflection or PHP embedded in strings.',
    'variable_groups': 'Distinct file / lexical function-or-closure scope / name groups with at least one reported variable occurrence. Captures may be separate groups; not unique logical symbols or edit counts.',
    'string_candidates': 'Exact method-name or Class::method string literals up to 160 bytes; includes callback, reflection, mocks and unrelated data. Requires review.',
    'visibility': 'PHP public visibility is not proof of an externally supported API; interfaces, anonymous classes and test doubles are included.',
    'scope_limits': 'Runtime here means outside tests/ and scripts/, not a public API classification. Generated Release Updater ArchiveSafety is parsed for callers but excluded from flagged-declaration counts by current PHPCS selection.'
}, 'totals': {'php_files_parsed': len(data['files']), 'php_files_in_phpcs_scope': len(selected), 'naming_diagnostics': len(diagnostics), 'methods': len(flagged_methods), 'runtime_camelcase_method_candidates': sum(runtime(r['file']) for r in camel_methods), 'runtime_camelcase_methods_absent_from_diagnostics': len(unreported_runtime_methods), 'properties': len(flagged_properties), 'parameters': len(flagged_parameters), 'variable_scope_name_groups': len(flagged_variables), 'cross_package_contract_implementations': len(contracts), 'resolved_cross_package_call_candidates': len(cross_calls), 'string_candidates': len(string_candidates), 'named_argument_sites': len(data['named_arguments']), 'camelcase_named_argument_sites': sum(bool(re.search('[A-Z]', r['name'])) for r in data['named_arguments'])}, 'diagnostics_by_source': dict(sorted(Counter(r['source'] for r in diagnostics).items())), 'repositories': {}}

for repo in metadata:
    rdata = {'methods': {}, 'properties': {}, 'parameters': {}, 'variable_scope_name_groups': {}, 'named_argument_sites': 0, 'camelcase_named_argument_sites': 0}
    for label, values in [('methods', flagged_methods), ('properties', flagged_properties), ('parameters', flagged_parameters)]:
        for location in ['runtime', 'tests_scripts']:
            rows = [r for r in values if r['repo'] == repo and runtime(r['file']) == (location == 'runtime')]
            rdata[label][location] = dict(sorted(Counter(r.get('visibility') or 'function_closure' for r in rows).items()))
    rdata['variable_scope_name_groups'] = dict(sorted(Counter(('parameter' if r['parameter'] else 'other') + ('_runtime' if runtime(r['file']) else '_tests_scripts') for r in flagged_variables if r['repo'] == repo).items()))
    rdata['all_runtime_camelcase_methods'] = dict(sorted(Counter(r['visibility'] for r in camel_methods if r['repo'] == repo and runtime(r['file'])).items()))
    rdata['runtime_camelcase_methods_absent_from_diagnostics'] = sum(r['repo'] == repo for r in unreported_runtime_methods)
    rdata['named_argument_sites'] = sum(r['repo'] == repo for r in data['named_arguments'])
    rdata['camelcase_named_argument_sites'] = sum(r['repo'] == repo and bool(re.search('[A-Z]', r['name'])) for r in data['named_arguments'])
    rdata['excluded_php_files'] = sorted(r['file'] for r in data['files'] if r['repo'] == repo and (repo, r['file']) not in selected)
    summary['repositories'][repo] = rdata

summary['unreported_runtime_method_reasons'] = dict(sorted(Counter('outside_current_phpcs_scope' if (r['repo'], r['file']) not in selected else 'wpcs_inheritance_heuristic' if production_classes.get(r['class'], {}).get('parents') else 'other' for r in unreported_runtime_methods).items()))
summary['cross_package_contracts'] = sorted(contracts, key=lambda r: (r['owner_repo'], r['consumer_repo'], r['class'], r['method']))
edges = defaultdict(list)
for row in cross_calls:
    edges[(row['repo'], row['target_repo'])].append(row)
summary['cross_package_call_edges'] = [{'caller_repo': a, 'target_repo': b, 'candidate_sites': len(rows), 'runtime_sites': sum(runtime(r['file']) for r in rows), 'examples': sorted(rows, key=lambda r: (r['file'], r['line']))[:5]} for (a, b), rows in sorted(edges.items())]
summary['external_runtime_ancestors'] = dict(sorted(external_ancestors.items()))
summary['camelcase_methods_with_external_ancestor'] = sorted(external_method_candidates, key=lambda r: (r['repo'], r['file'], r['line']))
summary['public_runtime_methods'] = sorted([dict(r, reported_by_phpcs=coord(r) in flagged_coords) for r in camel_methods if 'public' == r['visibility'] and runtime(r['file'])], key=lambda r: (r['repo'], r['file'], r['line']))
summary['public_runtime_properties'] = sorted([r for r in flagged_properties if 'public' == r['visibility'] and runtime(r['file'])], key=lambda r: (r['repo'], r['file'], r['line']))
summary['string_candidate_examples'] = sorted(string_candidates, key=lambda r: (r['repo'], r['file'], r['line']))[:30]
output.write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
print(json.dumps(summary['totals'], indent=2))

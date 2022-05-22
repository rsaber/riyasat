# temporary megration script

import os, yaml, json, sys

file = sys.argv[1]

with open(file, 'r') as f:
    parsed = json.load(f)

just_entries = {}

for entry in parsed['entries']:
    n = entry['netlify_file']
    
    key = n['file']
    just_entries[key] = {} 

    just_entries[key]['type'] =  entry['type']
    just_entries[key]['link'] = f"{n['base']}/{n['bucket']}/{n['file']}"
    just_entries[key]['caption'] =  entry['caption']
    just_entries[key]['subcaption'] =  entry['subcaption']

    del entry['netlify_file']

as_yaml = yaml.dump(just_entries, sort_keys=False)
print(as_yaml)

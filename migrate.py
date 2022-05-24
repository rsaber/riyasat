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
    just_entries[key]['caption'] = entry['caption'] if 'caption' in entry else False
    just_entries[key]['subcaption'] =  entry['subcaption'] if 'subcaption' in entry else False

    del entry['netlify_file']

full_dict = {
    "template": "main.jinja",
    "navbar": "!include header.yaml",
    "type": "photojournal",
    "title": parsed['title'],
    "contents": {
        "title": parsed['title'],
        "camera": parsed['camera'],
        "date": parsed['date'],
        "description": parsed['description'],
        "entries": just_entries
    }
}

as_yaml = yaml.dump(full_dict, sort_keys=False)
print(as_yaml)

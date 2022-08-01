# temporary migration script

import os, yaml, json, sys

file = sys.argv[1]

with open(file, 'r') as f:
    imagenames = f.readlines()

just_entries = {}

for imagename in imagenames:
    key = imagename.strip()
    just_entries[key] = {} 

    just_entries[key]['type'] = "image"
    just_entries[key]['link'] = f"https://lens-img-alpha.netlify.app/{file}/{imagename.strip()}"
    just_entries[key]['caption'] = imagename.strip()
    just_entries[key]['subcaption'] = "TestSubcaption"

full_dict = {
    "template": "main.jinja",
    "navbar": "!include header.yaml",
    "type": "photojournal",
    "title": sys.argv[1],
    "contents": {
        "title": sys.argv[1],
        "camera": "camera",
        "date": 'date',
        "description": "description",
        "entries": just_entries
    }
}

as_yaml = yaml.dump(full_dict, sort_keys=False)
print(as_yaml)

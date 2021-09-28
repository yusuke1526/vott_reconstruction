import json
import glob

VOTT_FILE = 'hoge.vott'

vott = open(VOTT_FILE, 'r')
vott_dict = json.load(vott)
vott_ids = set(vott_dict['assets'].keys())
print(len(vott_dict['assets']))

paths = glob.glob('*.json')
json_ids = set(map(lambda x: x.split('-')[0], paths))

diff = json_ids - vott_ids

for id in diff:
    print(id)
    f = open(f'{id}-asset.json', 'r')
    d = json.load(f)
    asset = d['asset']
    new_asset = {
        "format": "jpg",
        "id": asset['id'],
        "name": asset['name'],
        "path": asset['path'],
        "size": {
            "width": asset['width'],
            "height": asset['height']
        },
        "state": asset['state'],
        "type": asset['type'],
    }
    vott_dict['assets'][id] = new_asset

print(len(vott_dict['assets']))
new_file = open(f'{VOTT_FILE}.new', 'w')
json.dump(vott_dict, new_file, indent=4)
    
        
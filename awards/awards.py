import json
from file_handler import f_read_json
from os.path import expanduser, join

def add_award(name, award):
    data = f_read_json('awards')
    if award not in data:
        data[award] = {}
    if name in data[award]:
        data[award][name] += 1
    else:
        data[award][name] = 1
    with open(join(expanduser('~'), '.klb/points'), 'w+') as f:
        json.dump(data, f)

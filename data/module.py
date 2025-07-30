# Data handling and persistance
import json
# Go from != null to reading an empty pre defined data-structure
# Startup procedure (initialize default settings and empty data)
def update(d:dict):
    if open('save.json').read().strip() != 'null':
        data = json.load(open('save.json','r'))
        f = {'Game':[i for i in d['Game'] if i['Id'] not in [k['Id'] for k in data['Game']]]}
        new = {'Game': data['Game'] + f['Game'], 'User': d['User']}
        json.dump(new,open('save.json','w'),indent=4)
    else:
        json.dump(d,open('save.json','w'),indent=4)
    return
def recall() -> dict:
    if open('save.json').read().strip() != 'null':
        return json.load(open('save.json','r'))
    else:   
        return {}
def clean():
    # Needs some work
    json.dump(None,open('save.json','w'))
    return
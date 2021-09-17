import json

def hae_postinumerot():
    with open('postinumerot.json') as f:
        tiedoston_sisalto = f.read()

    postinumerot = json.loads(tiedoston_sisalto)

    for key, value in postinumerot.items():
        if value == 'SMART POST' or value == 'SMART-POST' or value == 'SMARTPSOT':
            postinumerot[key] = 'SMARTPOST'

    return postinumerot


    
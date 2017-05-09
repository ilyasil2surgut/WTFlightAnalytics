import json
import urllib.request
"""
http://localhost:8111/mission.json
http://localhost:8111/map_obj.json
http://localhost:8111/map_info.json
http://localhost:8111/hudmsg
http://localhost:8111/indicators
http://localhost:8111/state
"""
def grabjson(url="http://localhost:8111"):
    """
    Grab a json file from web source
    :param url: str
    :return: dict
    """
    try:
        with urllib.request.urlopen(url) as source:
            return json.loads(source.read().decode())
    except:
        print("Couldn't connect to web source")
        return {"valid":False}

def retrievedata(url="http://localhost:8111"):
    urls=["/state","/indicators"]
    out={}
    for end in urls:
        a=grabjson(url+end)
        if a["valid"]:out.update(grabjson(url+end))
    return out
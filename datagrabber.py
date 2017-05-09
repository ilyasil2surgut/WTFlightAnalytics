import json
import urllib.request

def grabjson(url=""):
    """
    Grab a json file from web source
    :param url: str
    :return: 
    """
    with urllib.request.urlopen(url) as source:
        return json.loads(source.read().decode())

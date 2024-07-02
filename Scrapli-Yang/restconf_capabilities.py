import requests
import json
from restconfRouterInfo import router

headers = {
    "accept": "application/yang-data+json",
    "content-type": "application/yang-data+json"
}

url = f'{router["host"]}{router['username']}/resconf/data/netconf-state/capabilities'


response = requests.get(url=url,headers=headers, auth=(router['user'],router['passowrd']))

json_resp = json.loads(response.text)
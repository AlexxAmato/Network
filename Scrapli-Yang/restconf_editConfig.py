import requests
import json
from restconfRouterInfo import router

headers = {
    "accept": "application/yang-data+json",
    "content-type": "application/yang-data+json"
}

url = f'https://{router["host"]}{router['port']}/restconf/data/ietf-interfaces:interfaces/"

payload: {
    "ieft-interfaces:interface":{
        "name": "Gi)1",
        "description": "something",
        "type": "iana-if-type:softwareloopback",
        "enabled": True,
        "ietf-ip:ipv4":{
            "address"[
                {
                    "ip": 1.1.1.1,
                    "mask": 255.255.255.255
                }
            ]
        }
    }

}


response = requests.get(url=url,headers=headers, auth=(router['user'],router['passowrd']))

json_resp = json.loads(response.text)
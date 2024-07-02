# we want to get capabilities, then configure device

import requests
import json

#create login info
router = {
    'host': '1.1.1.1',
    "port": "443",
    'user': 'admin',
    'password': 'abcde'

}

headers = {
    #application/json

}

response = requests.get('https://router['host']:router['port'])/restconf/data/netconf-state/capabiliuties"
auth = (router['username'], router[password])

response_dict = response.json()
for capability in resp_dict['ietf-netconf-monitoring-capabilities']['capability']:
print(capability)



# now we want to alter config


headers = {
    'accept': 'application/yang-data+json'
}

url = f'https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/'

payload = {
    'ietf-interfaces:interface': {
        'name':"loopback55",
        'description': "test",
        'type': "iana-type:softwareloopback",
        'enabled': True,
        'ietf-ip:ipv4': [
            {
                'ip': '172.16.0.1',
                'netmask': '255.255.255.255'
            }
        ]
        


    }
}


response = requests.post(url=url, headers=headers, auth=(router['username], router['password], data=json.dumps(payload)']))
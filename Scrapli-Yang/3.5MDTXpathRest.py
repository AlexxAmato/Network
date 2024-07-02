import requests
import json

router = {
    'ip': '1.1.1.1',
    'port': '443',
    'username': 'admin',
    'password': 'abcd'
}

#first establish connection to the device 

headres = {
    'accept': 'application/yang-data+json',
    'content-type' : 'application/yang-data+json'
}

module = 'Cisco-ios-xe-mdt-cfg:mdt-config-data'

url = f'http://{router['host']}{router['port']}/restconf/data/{module}'

payload = {
    "mdt-config-data": {
        'subscription-id': 100,
        "base": {
            'stream': 'yang-push',
            'encoding': 'encode-kvgpb',
            'xpath': '/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds',
            'period': 1000
        },
        'mdt-recievers': {
            'address': "1.2.3.4",
            "port": 42518,
            'protocol': 'grpc-tcp'
        }
    }
}
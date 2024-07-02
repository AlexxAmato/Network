from ncclient import manager
import xmltodict
from lxml.etree import fromstring

# you create a rpc variable and use 

router = {
    'host': '1.1.1.1',
    'port': "1000",
    'user': 'admin',
    'password': 'null'


}

#subs are a list of strings
with manager.connect(**router) as m:
    subs = ['/memeory-ios-xe-oper:memory-statistics/memory-statistic']
    for sub in subs:
        rpc = f'''
            <establish-subscription xmlns='urn:ietf:params:xml:ns:ietf-event-notifications'
            xmsns:yp='urn:ietf:params:xml:ns:yangietf-yang-push'>
            <stream>yp:yang-push</stream>
            <yp:xpath-filter>{sub}</yp:xpath-filter>
            <yp:period>500</yp:period>
            <extablish-subscription>

 '''
        

    response = m.dispatch(fromstring(rpc))
    python_resp = xmltodict.parse(response.xml)

    while True:
        sub_data = m.take_notification()
        python_sub_data = xmltodict.parse(sub_data.notification.xml)
        
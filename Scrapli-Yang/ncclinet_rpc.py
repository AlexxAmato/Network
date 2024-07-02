#this uses a yang model taken in previous step and creates an rpc for it.


from ncclient import manager
import xmltodict
import logging 

logging.basicConfig(level=logging.DEBUG)


router = {
    "host": "ios-xe-management-latest.cisco.com",
    "port": "830",
    "username": "developer",
    "password": "bad"

}

int_filter = """
<filter>
 <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"
   <interface>
     <name>Gigabitethernet2</name>
   </interface>
 </interfaces>
 <interfaces-state xmlns"urn:ietf:params:xml:ns:yang:ietf-interfaces"
   <interface>
     <name>gigabitethernet2</name>
   </interface>
 </interfaces-state>
"""


with manager.connect(**router) as m:
    netconf_response = m.get(int_filter)
    
    
python_response = xmltodict.parse(netconf_response.xml)["rpy-reply"]["data"]
 
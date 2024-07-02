# implement device management using netmiko


from netmiko import ConnectHandler

# set up router login info, you'll need to add
#device type
router = {
    'host': '1.1.1.1',
    'port': 8181,
    'username': 'admin',
    'password': '12345',
    'device_type': 'cisco_ios'
}

#set up configs, these will be used later, need to be 
#a list of ONE string
configs = ['int loopback55, ipaddress 1.2.3.4 255.255.255.255, no shut']

#you log in w/ ConnectHandler class
#store this into a variable

try:
    c = ConnectHandler(**router)
    c.enable()
    c.send_config_set(configs)
    response = c.send_command('show ip int brief')
    c.disconnect
except Exception as ec:
    print(ex)
else:
    print(response)
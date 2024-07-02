from netmiko import Netmiko
import os

my_device = { 
    "host" : "2.2.2.2",
    "username" : "soem",
    "password" : "ncdhsb",
    "secret" : "djbcjhb",
    "device_type" : "cisco_ios"
}  

net_conn = Netmiko(**my_device)#establishes ssh connecton
output = net_conn.send_command() #pass in cli commands for show commands
print(output)


#sends config commands and prints their outputs
conf_commands = ['logging buffered 5000', 'logging console']
output = net_connect.send_config_set(conf_commands) #
print(output)


for device in (cisco, juniper, arista):
    net_conn = Netmiko(**my_device) #establishes ssh connecton
    output = net_conn.send_command() #pass in cli commands for show commands
    print(output)


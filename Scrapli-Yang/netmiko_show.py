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
net_conn.send_command_timing("disable")
print(net_conn.find_prompt())

output = net_conn.send_command() #pass in cli commands for show commands
print(output)

#net_conn.enable() # getting to exec mode 


# for loop for mutiple devices 


for device in (cisco, juniper, arista):
    net_conn = Netmiko(**my_device) #establishes ssh connecton
    output = net_conn.send_command() #pass in cli commands for show commands
    print(output)


    output = net_conn.send_command("sh arp", use_textfsm=True)# textfsm this formats the string output to a structured list
    #NTC templates for fsm need to be in home directory, anywhere else and code wont work
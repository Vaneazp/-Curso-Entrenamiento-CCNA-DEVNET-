from netmiko import ConnectHandler

# Detalles del router
router = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.101',  
    'username': 'admin',
    'password': 'cisco123',
    'secret': 'cisco123',  
}


net_connect = ConnectHandler(**router)
net_connect.enable()


config_commands = [
    'router ospf 123',
    'router-id 1.1.1.1', 
    'network 0.0.0.0 255.255.255.255 area 0',
    'passive-interface default',
    'no passive-interface GigabitEthernet0/1',
]


output = net_connect.send_config_set(config_commands)


show_output = net_connect.send_command('show running-config | section router ospf')
print(show_output)

net_connect.disconnect()

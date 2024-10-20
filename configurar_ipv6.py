from netmiko import ConnectHandler

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
    'interface Loopback33',
    'ipv6 address 3001:ABCD:ABCD:2::2/64',
    'shutdown', 
]


output = net_connect.send_config_set(config_commands)


show_output = net_connect.send_command('show ipv6 interface brief')
print(show_output)

net_connect.disconnect()

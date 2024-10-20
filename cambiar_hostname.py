from ncclient import manager

router = {
    'host': '192.168.1.101',  # IP de tu router
    'port': 830,
    'username': 'admin',
    'password': 'cisco123',
    'hostkey_verify': False
}

# XML para cambiar el hostname
hostname_config = '''
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>VANESSA-ZUNIGA</hostname>
  </native>
</config>
'''

with manager.connect(**router) as m:
    netconf_reply = m.edit_config(target='running', config=hostname_config)
    print(netconf_reply)

from ncclient import manager

router = {
    'host': '192.168.1.101',  # Cambia por la IP de tu router
    'port': 830,
    'username': 'admin',
    'password': 'cisco123',
    'hostkey_verify': False
}

# XML para crear la interfaz Loopback 22
loopback_config = '''
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>22</name>
        <ip>
          <address>
            <primary>
              <address>22.22.22.22</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
'''

with manager.connect(**router) as m:
    netconf_reply = m.edit_config(target='running', config=loopback_config)
    print(netconf_reply)

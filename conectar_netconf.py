from ncclient import manager

# Detalles de conexión al router CSR1000v
router = {
    'host': '192.168.1.101',  # IP de tu router
    'port': 830,
    'username': 'admin',
    'password': 'cisco123',
    'hostkey_verify': False
}

# Establecer la conexión con NETCONF
with manager.connect(**router) as m:
    print("Conexión NETCONF establecida")
    print(m.server_capabilities)

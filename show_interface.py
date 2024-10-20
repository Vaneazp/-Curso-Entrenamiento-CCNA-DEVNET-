from genie.testbed import load


testbed = load('testbed.yml')


router = testbed.devices['csr1000v']
router.connect()

output = router.parse('show ipv6 interface brief')


with open('/path/al/directorio/ipv6_interfaces_output.txt', 'w') as f:
    f.write(str(output))


router.disconnect()

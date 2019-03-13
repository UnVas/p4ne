from pysnmp.hlapi import *

snmp_object_1 = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_object_2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

ip = '10.31.70.107'

result1 = getCmd(SnmpEngine(),
  CommunityData('public', mpModel=0),
  UdpTransportTarget((ip, 161)),
  ContextData(),
  ObjectType(snmp_object_1))

result2 = nextCmd(SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget((ip, 161)),
    ContextData(),
    ObjectType(snmp_object_2),
    lexicographicMode=False)


print("\nRequesting System Description from '%s'..." % ip)
for e in result1:
    #print(list(e)[3])
    for str in list(e)[3]:
        print(str)

print("\n\nRequesting MIB")
for e in result2:
    #print(list(e)[3])
    for str in list(e)[3]:
        print(str)


from ipaddress import IPv4Network, IPv4Address
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        while True:
            r_addr = random.randint(0x0B000000, 0xDF000000)
            r_mask = random.randint(8, 24)
            iptemp = IPv4Address(r_addr)
            if not iptemp.is_private:
                IPv4Network.__init__(self, (r_addr, r_mask), strict = False)
                break
    def key_value(self):
        return int(self.prefixlen)*2**32 + int(self.network_address)

def sortkeyfunc(x):
    return x.key_value()

list_ip = []
N = 10
for i in range(0, N):
    list_ip.append(IPv4RandomNetwork())
    # print(list_ip[i].key_value())

list_ip.sort(key=sortkeyfunc)

for i in range(0, N):
    print(list_ip[i])
#a = IPv4RandomNetwork()
#print(a)


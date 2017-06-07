import xml.etree.ElementTree as etree
import ipaddress

# initializing empty list for objects parsed from XML
ip4blocks = []
ip4networks = []

blocks = 0
networks = 0


class IP4Obj:
    def __init__(self, ip4range, name=None, vlan=None):
        net = ipaddress.ip_network(ip4range, False)
        self.address = net[0]
        self.netmask = net.netmask
        if net.prefixlen == 32:
            self.router = net[0]
        else:
            self.router = net[1]
        self.name = name
        self.vlan = vlan


tree = etree.parse('input.xml')
root = tree.getroot()

# requires Python 3.2 or higher
xmlblocks = (root.iter(tag="ip4-block"))
xmlnetwork = (root.iter(tag="ip4-network"))


for b in xmlblocks:
    blocks += 1
    ip4blocks.append(IP4Obj(b.get('range'), b.get('name')))

for n in xmlnetwork:
    networks += 1
    ip4networks.append(IP4Obj(n.get('range'), n.get('name'), n.get('vlan')))

# Showing the number of times iterated, to be removed
print(blocks)
print(networks)

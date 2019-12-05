import ipaddress

class IPv4Network(object):

    def __init__(self, ipv4network):
        self.ipv4network = ipaddress.ip_interface(ipv4network)
        self.address = ipaddress.ip_interface(ipv4network).ip
        self.mask = ipaddress.ip_interface(ipv4network).network
        self.broadcast = ipaddress.ip_interface(ipv4network).network.broadcast_address
        self.allocated = list(ipaddress.ip_interface(ipv4network).network.hosts())

    def hosts(self):
        self.ipv4network



import ipaddress

class IPv4Network(object):
    def __init__(self, ipv4network):
        self.ipv4network = ipaddress.ip_interface(ipv4network)
        self.address = str(ipaddress.ip_interface(ipv4network).ip)
        self.mask = ipv4network.split('/')[1]
        self.broadcast = str(ipaddress.ip_interface(ipv4network).network.broadcast_address)
        self.allocated_list = []
        self.allocated = tuple(self.allocated_list)
        self.unassigned_list = []
        for ip in ipaddress.ip_interface(self.ipv4network).network.hosts():
            self.unassigned_list.append(str(ip))
        self.unassigned = tuple(self.unassigned_list)
    def hosts(self):
        for ip in ipaddress.ip_interface(self.ipv4network).network.hosts():
            print(ip)
    def allocate(self, allocated_ip_address):
        self.allocated_list.append(allocated_ip_address)
        self.allocated = tuple(self.allocated_list)
        self.unassigned_list.remove(allocated_ip_address)
        self.unassigned = tuple(self.unassigned_list)




class IPv4Network:
    def __init__(self, ipv4network):
        self.ipv4network = ipv4network
        self.address = ''
        self.mask = ''
        self.broadcast = ''
        self.allocated = ()

    def hosts(self):
        self.ipv4network


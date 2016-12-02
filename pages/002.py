from page import Page

class IPPage(Page):
    def __init__(self):
        super(IPPage, self).__init__("002")
        self.in_index = False
        self.is_enabled=False
        self.title = "IP Address Finder"

    def generate_content(self):
        import socket
        import fcntl
        import struct
        
        def get_ip_address(ifname):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', ifname[:15])
            )[20:24])
        self.content = "IP Addresses"
        self.content+= "\n\n"
        try:
            self.content+= "lo: "+get_ip_address('lo')
        except IOError:
            self.content+= "lo: ERROR"
        self.content+= "\n"
        try:
            self.content+= "eth0: "+get_ip_address('eth0')
        except IOError:
            self.content+= "eth0: ERROR"

instance = IPPage()

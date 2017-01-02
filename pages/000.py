import os
from page import Page
from random import choice
import config

class TestPage(Page):
    def __init__(self):
        super(TestPage, self).__init__("000")
        self.title = "About "+config.NAME
        self.is_enabled = False

    def generate_content(self):
        from cupt.cupt import curses_colors
        self.add_rainbow_text(config.NAME + " v" + config.VERSION)
        self.add_newline()
        self.add_newline()
        self.add_rainbow_text("FOREGROUNDS")
        self.add_newline()
        for i,c in enumerate(curses_colors):
            if i%6 == 0 and i>0:
                self.add_newline()
            self.move_cursor(x=12*(i%6))
            self.start_fg_color(c)
            self.add_wrapped_text(c+" ")
        self.end_fg_color()
        self.add_newline()
        self.add_newline()
        self.add_rainbow_text("BACKGROUNDS")
        self.add_newline()
        for i,c in enumerate(curses_colors):
            if i%6 == 0 and i>0:
                self.add_newline()
            self.move_cursor(x=12*(i%6))
            self.start_bg_color(c)
            self.add_wrapped_text(c+" ")
        self.end_bg_color()
        self.add_newline()
        self.add_newline()


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
        self.add_rainbow_text("IP ADDRESSES")
        self.add_newline()
        try:
            self.add_text("lo: "+get_ip_address('lo'))
        except IOError:
            self.add_text("lo: ERROR")
        self.add_newline()
        try:
            self.add_text("eth0: "+get_ip_address('eth0'))
        except IOError:
            self.add_text("eth0: ERROR")

test_page = TestPage()

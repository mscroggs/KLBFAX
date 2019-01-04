from page import Page
import config

class TestPage(Page):
    def __init__(self):
        super(TestPage, self).__init__("000")
        self.title = "About "+config.NAME
        self.enabled = False
        self.background_loaded = True # DO NOT COPY THIS LINE INTO A NEW PAGE!

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
            self.add_wrapped_text(c)
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
            self.add_wrapped_text(c)
        self.end_bg_color()
        self.add_newline()
        self.add_newline()
        '''
        import curses

        def main(stdscr):
            curses.start_color()
            curses.use_default_colors()
            for i in range(0, curses.COLORS):
                curses.init_pair(i + 1, i, -1)
            try:
                for i in range(0, 255):
                    stdscr.addstr(str(i), curses.color_pair(i))
            except curses.ERR:
                # End of screen reached
                pass
            stdscr.getch()

        curses.wrapper(main)
        '''
        import curses
        self.add_wrapped_text("Colour system: " + str(curses.COLORS))
        self.add_newline
        self.add_newline

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
            self.add_text("lo: "+get_ip_address(b'lo'))
        except IOError:
            self.add_text("lo: ERROR")
        self.add_newline()
        try:
            self.add_text("eth0: "+get_ip_address(b'eth0'))
        except IOError:
            self.add_text("eth0: ERROR")
        self.add_newline()

        try:
            self.add_text("wlan0: "+get_ip_address(b'wlan0'))
        except IOError:
            self.add_text("wlan0: ERROR")

        from ceefax import Ceefax

        self.add_newline()
        self.add_newline()

        self.add_text(config.NAME+" has been running since "+Ceefax().start_time.strftime("%y-%m-%d %H:%M"))


test_page = TestPage()

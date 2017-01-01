from math import floor
import logging
import config
from cupt import CuPT
    
class Page(object):
    def __init__(self, number):
        self.content = ""
        self.is_enabled = True
        self.in_index = True
        self.index_num = None
        self.tagline = config.NAME + ": The World at Your Fingertips"
        self.number = str(number)
        self.loaded = False
        self.background_loaded = False
        self.background_error = None
        self.title = ""
        self.duration_sec = config.default_page_duration_sec
        self.exception = None
        from ceefax import Ceefax
        self.cupt = CuPT(Ceefax().scr)

    def move_cursor(self, x=None, y=None):
        self.cupt.move_cursor(x=x,y=y)

    def start_fg_color(self, color):
        self.cupt.start_fg_color(color)

    def start_bg_color(self, color):
        self.cupt.start_bg_color(color)

    def end_fg_color(self):
        self.cupt.end_fg_color()

    def end_bg_color(self):
        self.cupt.end_bg_color()

    def add_block(self, block, *args, **kwargs):
        bg = None
        if "bg" in kwargs:
            bg = kwargs["bg"]
        self.cupt.add_block(block, *args, bg=bg)

    def add_title(self, title, bg="BLUE", fg="YELLOW", font="size7"):
        if font=="size7":
            from printer import instance as prinstance
        elif font=="size7condensed":
            from printer import thin_instance as prinstance
        elif font=="size7extracondensed":
            from printer import extrathin_instance as prinstance
        elif font=="size4":
            from printer import size4_instance as prinstance
        elif font=="size4bold":
            from printer import size4bold_instance as prinstance
        else:
            raise ValueError("Undefined font.")
        title_block = prinstance.text_to_ascii(title)
        self.cupt.add_blocked_block(title_block, fg=fg, bg=bg)

    def add_text(self, text):
        self.cupt.add_text(text)

    def add_newline(self):
        self.cupt.add_newline()

    def add_wrapped_text(self, text, pre=0):
        self.cupt.add_text(text, True, pre=pre)

    def loop(self):
        pass

    def keyboard_handler(self):
        pass

    def now(self):
        return config.now()

    def background(self):
        """This function will be run every so often in the background. Use it for (eg) downloading weather data."""
        pass

    def generate_content(self):
        """This function will be run every time the page is loaded."""
        pass

    def show(self):
        self.cupt.show_page_number(self.number)
        self.cupt.show_tagline(self.tagline)
        self.cupt.show()

    def reload(self):
        self.cupt.clear_content()
        self.generate_content()
        self.loaded = True

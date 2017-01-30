from math import floor
import logging
import config
from cupt import CuPT

class Page(object):
    def __init__(self, number):
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

    def start_random_fg_color(self):
        from cupt.cupt import non_dark_colors
        from random import choice
        self.cupt.start_fg_color(choice(non_dark_colors))

    def start_random_bg_color(self):
        from cupt.cupt import non_dark_colors
        from random import choice
        self.cupt.start_bg_color(choice(non_dark_colors))

    def end_fg_color(self):
        self.cupt.end_fg_color()

    def end_bg_color(self):
        self.cupt.end_bg_color()

    def add_block(self, block, *args, **kwargs):
        bg = None
        if "bg" in kwargs:
            bg = kwargs["bg"]
        self.cupt.add_block(block, *args, bg=bg)

    def add_title(self, title, bg="BLUE", fg="YELLOW", font="size7", pre=0, fill=True):
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
        title_block = prinstance.text_to_ascii(title,fill=fill)
        self.cupt.add_blocked_block(title_block, fg=fg, bg=bg, pre=pre)

    def add_rainbow_title(self, title, font="size7", pre=0, fill=True):
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
        title_block = prinstance.text_to_ascii(title, fill=fill)
        self.cupt.add_blocked_block(title_block, rainbow=True,pre=pre)

    def add_text(self, text, fg=None, bg=None):
        if fg is not None:
            self.start_fg_color(fg)
        if bg is not None:
            self.start_bg_color(bg)
        self.cupt.add_text(text)
        if fg is not None:
            self.end_fg_color()
        if bg is not None:
            self.end_bg_color()

    def add_rainbow_text(self, text):
        from cupt.cupt import non_dark_colors
        from random import choice
        for c in text:
            self.start_fg_color(choice(non_dark_colors))
            self.cupt.add_text(c)
        self.end_fg_color()

    def add_newline(self):
        self.cupt.add_newline()

    def add_wrapped_text(self, text, pre=0, fg=None, bg=None):
        if fg is not None:
            self.start_fg_color(fg)
        if bg is not None:
            self.start_bg_color(bg)
        self.cupt.add_text(text, True, pre=pre)
        if fg is not None:
            self.end_fg_color()
        if bg is not None:
            self.end_bg_color()

    def print_image(self,image,y_coord=0,x_coord=0):
        self.move_cursor(y=y_coord,x=x_coord)
        color_codes = {"k": "BLACK",  "K": "GREY",
                       "r": "RED",    "R": "LIGHTRED",
                       "o": "ORANGE", "y": "YELLOW",
                       "g": "GREEN",  "G": "LIGHTGREEN",
                       "c": "CYAN",   "C": "LIGHTCYAN",
                       "b": "BLUE",   "B": "LIGHTBLUE",
                       "m": "MAGENTA","p": "PINK",
                       "w": "WHITE",  "W": "BRIGHTWHITE",
                       "d": "DEFAULT","-": "BLACK"}
        lines = image.split("\n")[1:-1]
        for l in range(len(lines)//2):
            for c in range(len(lines[2*l])):
                c1 = lines[2*l][c]
                c2 = lines[2*l+1][c]
                self.start_fg_color(color_codes[c1])
                self.start_bg_color(color_codes[c2])
                self.add_text(u"\u2580")
                self.end_bg_color()
                self.end_fg_color()
            self.move_cursor(y=y_coord + l+1, x=x_coord)

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

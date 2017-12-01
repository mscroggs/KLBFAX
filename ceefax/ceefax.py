# width:79
# height: 30
import config
import points
import os
from page import PageManager
import curses

def is_page_file(f):
    if not os.path.isfile(os.path.join(config.pages_dir, f)):
        return False
    if "_" in f:
        return False
    if "pyc" in f:
        return False
    return True


def get_ceefax(test=None):
    if Ceefax._instance is None:
        Ceefax._instance = Ceefax(test)
    return Ceefax._instance

class CursesScreen:
    def __enter__(self):
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        curses.start_color()
        curses.use_default_colors()
        self.stdscr.keypad(1)
        self.old = curses.curs_set(0)
        SCREEN_HEIGHT, SCREEN_WIDTH = config.HEIGHT, config.WIDTH
        return self.stdscr

    def __exit__(self,a,b,c):
        curses.nocbreak()
        curses.curs_set(self.old)
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()


class Ceefax:
    _instance = None
    def __init__(self, test=None):
        self.start_time = config.now()
        if config.NAME == "KLBFAX":
            points.add_one_random(printing=True)
        if not os.path.isdir(config.config_dir):
            os.mkdir(config.config_dir)
        self.scr = None
        self.test = test

    def begin(self):
        with CursesScreen() as self.scr:
            import locale
            locale.setlocale(locale.LC_ALL,"")
            self.page_manager = PageManager(self.scr)
            self.scr.keypad(1)
            curses.resizeterm(config.HEIGHT,config.WIDTH)
            self.scr.refresh()
            self.start_loop()

    def start_loop(self):
        self.page_manager.start_loop(self.test)

    def kill(self):
        raise KeyboardInterrupt


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


def get_ceefax():
    if Ceefax._instance is None:
        Ceefax._instance = Ceefax()
    return Ceefax._instance
    

class Ceefax:
    _instance = None
    def __init__(self):
        if config.NAME == "KLBFAX":
            points.add_one_random(printing=True)
        if not os.path.isdir(config.config_dir):
            mkdir(config.config_dir)
        self.scr = None

    def begin(self):
        import locale
        locale.setlocale(locale.LC_ALL,"")
        self.scr = curses.initscr()
        self.page_manager = PageManager(self.scr)

        curses.start_color()
        curses.use_default_colors()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.scr.keypad(1)
        curses.resizeterm(config.HEIGHT,config.WIDTH)
        self.scr.refresh()
        self.start_loop()

    def end(self):
        curses.endwin()
        self.scr.keypad(0)
        curses.nocbreak()
        curses.curs_set(1)
        curses.echo()

    def start_loop(self):
        from time import sleep
        try:
            self.page_manager.start_loop()
        except Exception as e:
            import sys
            import traceback
            exc_type, exc_obj, tb = sys.exc_info()
            print traceback.print_tb(tb)
            print(type(e))
            print(e)
            sleep(5)
            self.end()

    def kill(self):
        raise KeyboardInterrupt


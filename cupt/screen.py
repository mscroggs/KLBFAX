import curses
import autoconfig
from .cupt import CuPT

class Screen:
    def __enter__(self):
        import locale
        locale.setlocale(locale.LC_ALL,"")

        self.scr = curses.initscr()
        self.cupt = CuPT(self.scr)

        curses.start_color()
        curses.use_default_colors()
        curses.noecho()
        curses.cbreak()
        self.old = curses.curs_set(0)

        self.scr.keypad(1)
        curses.resizeterm(autoconfig.HEIGHT,autoconfig.WIDTH)
        self.scr.refresh()
        return self

    def getch(self):
        return self.scr.getch()

    def __exit__(self,a,b,c):
        curses.nocbreak()
        curses.curs_set(self.old)
        self.scr.keypad(0)
        curses.echo()
        curses.endwin()

class DummyScreen:
    def __init__(self):
        self.scr = None
        self.cupt = CuPT(self.scr)

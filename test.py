

import curses
import locale

locale.setlocale(locale.LC_ALL, '')    # set your locale

scr = curses.initscr()
scr.clear()
scr.addstr(0, 0, u'\u3042'.encode('utf-8'))
scr.refresh()
# here implement simple code to wait for user input to quit
scr.endwin()

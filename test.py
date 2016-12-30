from cupt import CuPT
import curses
from time import sleep
scr = curses.initscr()
curses.start_color()
curses.use_default_colors()

cupt = CuPT(scr)
cupt.add_text("HELLO, Does this work??")
cupt.add_newline()
cupt.add_text("HELLO, Does this work??")
cupt.add_newline()
cupt.add_newline()

cupt.show()

sleep(10)

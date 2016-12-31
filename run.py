#!/usr/bin/env python
try:
    with open("/home/pi/ceefax/temp","w") as f:
        f.write("NO")
except:
    pass

import config
from points import add_one_random
from ceefax import Ceefax
from os.path import expanduser, join, isdir
from os import mkdir

c = Ceefax()
#c.disable_curses()
c.begin()

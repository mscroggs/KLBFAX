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

import sys

test = None

for i,a in enumerate(sys.argv):
    if a in ["-t","--test","-T"] and i+1 < len(sys.argv):
        test = sys.argv[i+1]

c = Ceefax(test)
#c.disable_curses()
c.begin()

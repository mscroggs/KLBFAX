#!/usr/bin/env python3
from ceefax import Ceefax
from os.path import expanduser, join, isdir
from os import mkdir

import sys

test = None

for i,a in enumerate(sys.argv):
    if a in ["-t","--test","-T"] and i+1 < len(sys.argv):
        test = sys.argv[i+1]

c = Ceefax(test)
c.begin()

#!/usr/bin/env python

import ceefax
from page import Page
from os.path import isfile
from random import random
import sys
import select

name_page = Page("???")

ceefax.pageFactory.show_random()

loops_done = 0

while True:
    loops_done += 1
    if loops_done % 10 == 0:
        reload(ceefax)

    REFRESH_RATE_SECS = 30
    input_fd, _, _ = select.select([sys.stdin], [], [], REFRESH_RATE_SECS)

    if (input_fd):
        name = sys.stdin.readline().strip()
        if len(name) == 3:
            page = ceefax.pageFactory.load(name)
            page.show()
        elif name == "00488a0488":
            from os import system
            print("Restarting")
            system("python /home/pi/player/off.py;sudo shutdown -r now")
            break
        elif name == "0026360488":
            from os import system
            print("Pulling newest version.")
            try:
                system("cd /home/pi/ceefax;git pull")
            except:
                pass
        else:
            if isfile("/home/pi/cards/"+name):
                with open("/home/pi/cards/"+name) as f:
                    i = 0
                    for line in f.readlines():
                        line = line.strip("\n")
                        if line != "":
                            if i == 0:
                                name = line
                            i += 1
            greeting = "Hello"
            if random() < 0.01:
                greeting = "Bello"
            if random() < 0.01:
                name = "Jigsaw"
            name_page.content=greeting+" "+name+"!"
            name_page.show()
    else:
        ceefax.pageFactory.show_random()

#!/usr/bin/env python

import ceefax
from os.path import isfile
import sys
import select
import page
import log_setup
from random import choice
from points import add_points

house = choice(["Ravenclaw","Gryffindor","Slytherin","Hufflepuff"])
add_points(house,1)
print("1 point to "+house+"!")

log_setup.read_from_file()
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
        if len(name)<=3:
            while len(name)<3:
                name = "0"+name
            ceefax.pageFactory.get_reloaded_page(name).show()
        elif name == "....":
            break
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
                    name = f.read().strip("\n")
                name_page = page.NamePage(name)
            else:
                name_page = page.NamePage(name,False)
            name_page.show()
                
    else:
        ceefax.pageFactory.show_random()

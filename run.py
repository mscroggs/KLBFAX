#!/usr/bin/env python

import ceefax
from os.path import isfile,expanduser,join,isdir
from os import mkdir
import sys
import select
import page
import log_setup
from random import choice
from points import add_points
import now

if not isdir(join(expanduser('~'),'.klb')):
    mkdir(join(expanduser('~'),'.klb'))

house = choice(["Ravenclaw","Gryffindor","Slytherin","Hufflepuff","Squib","Durmstrang"])
add_points(house,1)
if house == "Hufflepuff":
    print("1 point to "+house+"! GO PUFFS!")
else:
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
                oldname = name
                with open("/home/pi/cards/"+name) as f:
                    lines = f.readlines()
                    name = lines[0].strip("\n")
                    try:
                        house = lines[1].strip("\n")
                        extra = ""
                    except:
                        house = None
                        extra = "Error finding your house. Please report to Scroggs."
                if house is not None and "used" not in lines:
                    with open("/home/pi/cards/"+oldname,"a") as f:
                        f.write("\nused")
                    time = now.now().strftime("%H")
                    if time in ["08","09"]:
                        if time == "08": t_points = 20
                        else: t_points = 10
                        add_points(house,t_points)
                        extra = str(t_points) + " points to " + house + "!"
                name_page = page.NamePage(name,extra=extra)
            else:
                name_page = page.NamePage(name,large=False)
            name_page.show()
                
    else:
        ceefax.pageFactory.show_random()

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
                    name = f.read().split("\n")[0]
                    time = now.now().strftime("%H")
                    extra = time
                    for i in range(100):
                        print time
                    if time in ["08","16"]:
                      try:
                        house = f.read().split("\n")[0]
                        if time == "08": t_points = 20
                        else: t_points = 10
                        add_points(house,t_points)
                        extra = str(t_points) + " points to " + house + "!"
                      except:
                        extra = "Could not add points. Please ask Scroggs about this"
                name_page = page.NamePage(name)
                name_page.extra = extra
            else:
                name_page = page.NamePage(name,False)
            name_page.show()
                
    else:
        ceefax.pageFactory.show_random()

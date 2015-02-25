from time import strftime,sleep
from random import choice
import ceefax
from colours import Background,Foreground
from os.path import isfile
from random import random
from math import floor
import sys, select

def display(number,page,tagline="KLBFAX: The world at your fingertips"):
    out=["                                                     "+number+" KLBFAX "+strftime("%a %d %b %H:%M")]
    out+=page
    for i in range(0,28):
        if i<len(out):
            print(out[i])
        else:
            print("")
    before = int(floor((79-len(tagline))/2))
    after = 79-len(tagline)-before
    tagline_print=" "*before+tagline+" "*after
    print(Background.BLUE+Foreground.YELLOW+tagline_print+Background.DEFAULT+Foreground.DEFAULT)

number = ceefax.load_me
page = ceefax.page.split("\n")
tag = ceefax.tag
display(number,page,tag)

while True:
    i, o, e = select.select( [sys.stdin], [], [], 30 )

    if (i):
        name = sys.stdin.readline().strip()
        if name == "00488a0488":
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
                    i=0
                    for line in f.readlines():
                        line = line.strip("\n")
                        if line!="":
                            if i==0:
                                name = line
                            i+=1
            greeting = "Hello"
            if random()<0.01:
                greeting = "Bello"
            if random()<0.01:
                name = "Jigsaw"
            page = [greeting+" "+name+"!"]
            display("???",page)
    else:
        try:
            reload(ceefax)
        except:
            pass
        number = ceefax.load_me
        page = ceefax.page.split("\n")
        tag = ceefax.tag
        display(number,page,tag)

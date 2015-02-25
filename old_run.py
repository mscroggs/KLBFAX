from time import strftime,sleep
from random import choice
import ceefax
from colours import Background,Foreground
from os.path import isfile
from random import random
import thread
import threading

def raw_input_with_timeout(prompt, timeout=30.0):
    print prompt,    
    timer = threading.Timer(timeout, thread.interrupt_main)
    astring = None
    try:
        timer.start()
        astring = raw_input(prompt)
    except KeyboardInterrupt:
        pass
    timer.cancel()
    return astring

astring = None

while True:
    try:
        reload(ceefax)
    except:
        pass
    if astring is None:
        number = choice(ceefax.pages.keys())
        page = ceefax.pages[number].split("""
""")
    else:
        number = "???"
        name = "someone"
        if isfile("/home/pi/cards/"+astring):
            with open("/home/pi/cards/"+astring) as f:
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



    out=["                                                     "+number+" KLBFAX "+strftime("%a %d %b %H:%M")]
    out+=page
    for i in range(0,28):
        if i<len(out):
            print(out[i])
        else:
            print("")
    print(Background.BLUE+Foreground.YELLOW+"                KLBFAX: The world at your fingertips                            "+Background.DEFAULT+Foreground.DEFAULT)

    astring = raw_input_with_timeout("")
        

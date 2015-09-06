#!/usr/bin/env python

import ceefax
from os.path import isfile, expanduser, join, isdir
from os import mkdir
import page
import log_setup
from random import choice
from points import add_points
import points
import now
import Keyboard
import thread_communication

if not isdir(join(expanduser('~'), '.klb')):
    mkdir(join(expanduser('~'), '.klb'))

house = choice(["Ravenclaw", "Gryffindor", "Slytherin", "Hufflepuff", "Squib",
                "Durmstrang"])

add_points(house, 1)
if house == "Hufflepuff":
    print("1 point to "+house+"! GO PUFFS!")
else:
    print("1 point to "+house+"!")

log_setup.read_from_file()


class Main(object):
    def __init__(self):
        pass

    loops_done = 0

    def standard_loop(self):
        ceefax.pageFactory.show_random()

        self.loops_done += 1
        if self.loops_done % 10 == 0:
            reload(ceefax)

        REFRESH_RATE_SECS = 30
        ceefax.sleep(REFRESH_RATE_SECS)

    def current_loop(self):
        self.standard_loop()

main = Main()


def test_loop():
    # this loops hijacts the main executaion for a bit, and then returns
    # back
    thread_communication.should_interrupt = False
    main.current_loop = main.standard_loop
    print "broke out of the main loop!"
    ceefax.sleep(2)


Keyboard.start_keyboard_thread()
Keyboard.subscribe(ceefax.name_page_handler)

while True:
    main.current_loop()

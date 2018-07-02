from page import Page
from random import choice
import config
import json
import logging
import sys
from helpers.file_handler import f_read_json

class BdayPage(Page):
    def __init__(self, page_num):
        super(BdayPage, self).__init__(page_num)
        self.title = "Birthdays"

    def background(self):
        birthdays = f_read_json("birthdays.json")
        more_birthdays = {
                    "Kathleen Lonsdale": (1, 28),
                    "Martin Gardner": (10, 21),
                    "Jesus": (12, 25),
                    "Jigsaw": (1, 3),
                    "The Queen": (4, 21),
                    "Richard Gere & Van Morrison & Jeff Hardy & Herman von Helmholtz & Pepe Reina": (8, 31),
                    "Barry Gibb & Rocky Marciano & Romeo Beckham & Conway Twitty & Engelbert Humperdinck": (9, 1),
                    "Keanu Reeves & Lennox Lewis & Bill Shankly & Kier Starmer & Eric Allman": (9, 2)
        }

        for birth in more_birthdays:
            birthdays[birth] = more_birthdays[birth]

        self.c_b = {}
        self.months = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

        for i in range(1,13):
            self.c_b[i] = {}

        for person in birthdays:
            bp = birthdays[person]
            if bp is not None:
                if bp[1] not in self.c_b[bp[0]]:
                    self.c_b[bp[0]][bp[1]] = person
                else:
                    self.c_b[bp[0]][bp[1]] += " & " + person



    def generate_content(self):
        from random import choice
        s_day = config.now().day
        s_mon = config.now().month

        day = s_day
        mon = s_mon

        ind = 0

        while True:
            if day == s_day and mon == s_mon:
                if day in self.c_b[mon]:
                    self.add_rainbow_title("Happy Birthday")
                    self.add_newline()
                    self.add_rainbow_title(choice(self.c_b[mon][day].split(" & "))+"!")
                    self.add_newline()
                    self.start_random_fg_color()
                    for i,line in enumerate([
                        "   .-'\"'-.  ",
                        "  / #     \ ",
                        " : #       :",
                        "  \       / ",
                        "   \     /  ",
                        "    `'q'`   ",
                        "      (     ",
                        "       )    ",
                        "      (     ",
                        "       )    "]):
                        self.move_cursor(x=0,y=i+16)
                        self.add_text(line)
                    self.start_random_fg_color()
                    for i,line in enumerate([
                        "  .-'\"'-.   ",
                        " / #     \  ",
                        ": #       : ",
                        " \       /  ",
                        "  \     /   ",
                        "   `'p'`    ",
                        "     )      ",
                        "    (       ",
                        "     )      ",
                        "    (       "]):
                        self.move_cursor(x=60,y=i+16)
                        self.add_text(line)
                    self.end_fg_color()
                    ind = 13
                    self.move_cursor(y=16)

                else:
                    self.add_title("Birthdays",bg="BLACK",fg="GREEN")
            elif day in self.c_b[mon]:
                self.move_cursor(x=ind)
                self.start_bg_color("GREEN")
                self.start_fg_color("BLACK")
                self.add_text(str(day) + " "+self.months[mon])
                self.end_fg_color()
                self.end_bg_color()
                self.move_cursor(x=ind+15)
                self.add_text(self.c_b[mon][day])
                self.add_newline()
            day += 1
            if day > 31:
                day = 1
                mon += 1
                if mon > 12:
                    mon -= 12
            if mon==s_mon and day==s_day:
                break


bdaypage = BdayPage("102")

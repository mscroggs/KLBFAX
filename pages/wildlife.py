#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page import Page
from random import choice
import config

hashtag = "#EMFwildlife"

def only_az(text):
    out = ""
    for char in text.lower():
        if char in "abcdefghijklmnopqrstuvwxyz":
            out += char
    return out

def split_az(text):
    out = []
    next = ""
    for char in text.lower()+".":
        if char in "abcdefghijklmnopqrstuvwxyz":
            next += char
        else:
            if next != "":
                out.append(next)
            next = ""
    return out

def wildlife_content(self, ls, titlebit="Most seen"):
    self.add_title(hashtag, font="size4bold")
    self.add_title("  "+titlebit, font="size4", fg="BLACK", bg="YELLOW")

    for animal,number in ls:
        self.add_text(animal)
        self.move_cursor(x=10)
        self.add_text(" ("+str(number)+") " + "☻"*number,fg=choice(["RED","YELLOW","CYAN","PINK","GREEN"]))
        self.add_newline()

    self.move_cursor(x=0,y=24)
    self.add_text(" "*config.WIDTH)
    self.add_newline()
    self.add_text("Tweet names of animals you see with the hashtag "+hashtag)
    self.add_newline()
    self.add_text(" "*config.WIDTH)

class WildlifePage(Page):
    def __init__(self, num):
        super(WildlifePage, self).__init__(num)
        self.importance = 5
        self.counts = {}
        self.counts_todaystart = {}
        self.counts_hourstart = {}
        self.animals = []
        self.seen = ""
        self.title = "Wildlife"
        self.today = config.now().strftime("%Y-%m-%d")
        self.hour = config.now().strftime("%Y-%m-%d %H")
        self.index_num = "220-222"

        self.ordered = []
        self.ordered_today = []
        self.ordered_hour = []

    def background(self):
        if len(self.counts) == 0:
            from helpers.file_handler import load_file
            self.animals = load_file("wildlife.txt").split("\n")
            for animal in self.animals:
                if animal != "":
                    self.counts[animal] = 0
                    self.counts_todaystart[animal] = 0
                    self.counts_hourstart[animal] = 0

        from helpers import tweet_handler
        results = tweet_handler.search(hashtag)

        today = config.now().strftime("%Y-%m-%d")
        hour = config.now().strftime("%Y-%m-%d %H")
        if today != self.today:
            self.counts_todaystart = {i:self.counts[i] for i in self.animals}
        if hour != self.hour:
            self.counts_hourstart = {i:self.counts[i] for i in self.animals}

        for result in results:
            if result["id_str"] == self.seen:
                break
            tweet = split_az(result["full_text"])
            az_tweet = only_az(result["full_text"])
            for animal in self.animals:
                if animal.lower() in tweet or (len(animal)>4 and only_az(animal) in az_tweet):
                    self.counts[animal] += 1
        if len(results) > 0:
            self.seen = results[0]["id_str"]

        self.ordered = list(self.counts.items())
        self.ordered_today = [(i,j-self.counts_todaystart[i]) for i,j in self.counts.items()]
        self.ordered_hour = [(i,j-self.counts_hourstart[i]) for i,j in self.counts.items()]

        self.ordered.sort(key=lambda x:-x[1])
        self.ordered_today.sort(key=lambda x:-x[1])
        self.ordered_hour.sort(key=lambda x:-x[1])

    def generate_content(self):
        wildlife_content(self, self.ordered)

class WildlifeTodayPage(Page):
    def __init__(self, num, mainpage):
        super(WildlifeTodayPage, self).__init__(num)
        self.importance = 5
        self.title = "Wildlife Today"
        self.mainpage = mainpage
        self.in_index = False

    def generate_content(self):
        wildlife_content(self, self.mainpage.ordered_today, "today")

class WildlifeHourPage(Page):
    def __init__(self, num, mainpage):
        super(WildlifeHourPage, self).__init__(num)
        self.importance = 5
        self.title = "Wildlife This Hour"
        self.mainpage = mainpage
        self.in_index = False

    def generate_content(self):
        wildlife_content(self, self.mainpage.ordered_hour, "this hour")

page1 = WildlifePage("220")
page2 = WildlifeTodayPage("221",page1)
page3 = WildlifeHourPage("222",page1)

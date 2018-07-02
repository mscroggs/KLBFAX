#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
from random import shuffle,choice

class EachWithHisPage(Page):
    def __init__(self, page_num):
        super(EachWithHisPage, self).__init__(page_num)
        self.title = "Merry lads' checklist"
        self.tagline = "Shall we play 'barley bay'?"

    def generate_content(self):

        def width_of_word(word):
            width = len(word)*5 \
            - sum(map(word.upper().count, u"!:,‘’.'I’"))*3
            - sum(map(word.upper().count, u"-()1"))*2
            - sum(map(word.upper().count, u"T"))*1
            + sum(map(word.upper().count, u"MW"))*1
            return width

        each_with_his = ["bonny lass",
        "bagpipe song",
        "month of May",
        "honest bob",
        "box of frogs",
        "lump of clay",
        "Theresa May",
        "Holland clogs",
        "wagon wheel",
        "trusty squad",
        "rusty rhod",
        "epipen",
        "turmeric in the porridge",
        "knave whipsnade",
        "Myleene Klass",
        "piece of mesh",
        "toot",
        "Wayward Ho!",
        "Restaurant",
        "month of June",
        "last of May",
        "ballpoint person",
        "Worcester sauce",
        "Twisted flax",
        "Silent sword",
        "ex le chiffre",
        "mathstadon",
        "Roger Moore",
        "Starbucks card",
        "Cushy cloth",
        "Floral bush",
        "fumblebee",
        "Matthew Scroggs",
        "Alan Clarke",
        "Field of wheat",
        "hare & hound",
        "nitwit speed",
        "wholesome horse",
        "Muller light",
        "birthday bear",
        "resume",
        "bleedin' box",
        "sodding log",
        "uncle Glenn",
        "beans on toast",
        "Christmas tree",
        "Captain Magenta",
        "Galilei... oh",
        "London brick",
        "Elton John",
        "Brail rail",
        "cup of tea",
        "fledgling flint",
        "Swedish broad",
        "wireless mouse",
        "shitfaced Steve",
        "Jackson Lamb",
        "bassless beat",
        "Camden Lock",
        "Twilight moon",
        "Pint of ducks",
        "Breaking Bad",
        "Auld Lang Syne",
        "Steam-ed ham",
        "ruined roast",
        "merry lad",
        "burma sauce"
        ]
        self.add_title("Each with his...")

        words = choice(each_with_his).split(" ")

        self.add_newline()
        chars_left = 80
        line = ""
        self.move_cursor(y=7,x=0)
        for word in words:
            if chars_left - width_of_word(word) <= 0:
                chars_left = 80
                self.add_title(line,bg="YELLOW",fg="BLACK",font="size4")
                line = word + " "
            else:
                line = line + word + " "
            chars_left = chars_left - width_of_word(word) - 3
        self.add_title(line,bg="YELLOW",fg="BLACK",font="size4")


eachwithhis_page = EachWithHisPage("114")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
import time
from functions import replace

class SportIndex(Page):
    def __init__(self, page_num):
        super(SportIndex, self).__init__(page_num)
        self.title = "Sport Index"
        self.importance = 2
        self.in_index = True

    def generate_content(self):
        global news_list
        self.add_title("Sport Index")
        for n,desc in news_list:
            self.add_text(str(n)+" ",fg="RED")
            self.add_text(desc)
            self.add_newline()

news_list = []

class SportPage(Page):
    def __init__(self, page_num, url, title):
        global news_list
        news_list.append((page_num,title))
        super(SportPage, self).__init__(page_num)
        self.top_title = title
        self.title = title
        self.url = url
        self.importance = 1
        self.in_index = False
        self.tagline = "From BBC Sport"

    def background(self):
        import feedparser
        rss_url = self.url
        feed = feedparser.parse(rss_url)
        if 'entries' in feed and len(feed['entries']) > 0:
            item = feed['entries'][0]
            self.words = replace(item["title"]).split(" ")
        else:
            self.words = []

        if len(feed) > 1:
            self.entries = [replace(item["title"]) for item in feed['entries'][1:21]]
        else:
            self.entries = []




    def generate_content(self):

        def width_of_word(word):
            width = len(word)*5 \
            - sum(map(word.upper().count, u"!:,‘’.'I’"))*3
            - sum(map(word.upper().count, u"-()1"))*2
            - sum(map(word.upper().count, u"T"))*1
            + sum(map(word.upper().count, u"MW"))*1
            return width


        self.add_title(self.top_title,bg="BLACK",fg="LIGHTRED")
        self.add_newline()
        chars_left = 80
        line = ""
        self.move_cursor(y=7,x=0)
        for word in self.words:
            if chars_left - width_of_word(word) <= 0:
                chars_left = 80
                self.add_title(line,bg="YELLOW",fg="BLACK",font="size4")
                line = word + " "
            else:
                line = line + word + " "
            chars_left = chars_left - width_of_word(word) - 3
        self.add_title(line,bg="YELLOW",fg="BLACK",font="size4")
        for item in self.entries:
            self.add_text(" - "+ item)
            self.add_newline()

sport_page16 = SportPage(316, "http://feeds.bbci.co.uk/sport/rss.xml?edition=uk", "Top Stories")
sport_page17 = SportPage(317, "http://feeds.bbci.co.uk/sport/football/rss.xml?edition=uk", "Football")
sport_page18 = SportPage(318, "http://feeds.bbci.co.uk/sport/cricket/rss.xml?edition=uk", "Cricket")
sport_page19 = SportPage(319, "http://feeds.bbci.co.uk/sport/rugby-union/rss.xml?edition=uk", "Rugby Union")
sport_page20 = SportPage(320, "http://feeds.bbci.co.uk/sport/formula1/rss.xml?edition=uk", "Formula 1")
sport_page21 = SportPage(321, "http://feeds.bbci.co.uk/sport/golf/rss.xml?edition=uk", "Golf")
sport_page22 = SportPage(322, "http://feeds.bbci.co.uk/sport/tennis/rss.xml?edition=uk", "Tennis")
sport_page23 = SportPage(323, "http://feeds.bbci.co.uk/sport/rugby-league/rss.xml?edition=uk", "Rugby League")
sport_page24 = SportPage(324, "http://feeds.bbci.co.uk/sport/athletics/rss.xml?edition=uk", "Athletics")
sport_page25 = SportPage(325, "http://feeds.bbci.co.uk/sport/snooker/rss.xml?edition=uk", "Snooker")
sport_page26 = SportPage(326, "http://feeds.bbci.co.uk/sport/american-football/rss.xml?edition=uk", "American Football")
sport_page27 = SportPage(327, "http://feeds.bbci.co.uk/sport/curling/rss.xml?edition=uk", "Curling")
sport_page28 = SportPage(328, "http://feeds.bbci.co.uk/sport/northern-ireland/gaelic-games/rss.xml?edition=uk", "Gaelic Games")
sport_page29 = SportPage(329, "http://feeds.bbci.co.uk/sport/table-tennis/rss.xml?edition=uk", "Table Tennis")


index = SportIndex(315)


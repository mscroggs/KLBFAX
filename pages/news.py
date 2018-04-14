#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
import time
from functions import replace

class NewsIndex(Page):
    def __init__(self, page_num):
        super(NewsIndex, self).__init__(page_num)
        self.title = "News Index"
        self.in_index = True

    def generate_content(self):
        global news_list
        self.add_title("News Index")
        for n,desc in news_list:
            self.add_text(str(n)+" ",fg="RED")
            self.add_text(desc)
            self.add_newline()

news_list = []

class NewsPage(Page):
    def __init__(self, page_num, url, title, bit="title"):
        global news_list
        news_list.append((page_num,title))
        super(NewsPage, self).__init__(page_num)
        self.bit = bit
        self.top_title = title
        self.title = title
        self.url = url
        self.in_index = False

    def background(self):
        import feedparser
        rss_url = self.url
        feed = feedparser.parse(rss_url)
        if 'entries' in feed and len(feed['entries']) > 0:
            item = feed['entries'][0]
            self.words = replace(item[self.bit]).split(" ")
        else:
            self.words = []

        if len(feed) > 1:
            self.entries = [replace(item[self.bit]) for item in feed['entries'][1:21]]
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

        import random
        newsreaders = ['Huw Edwards','Lizo from Newsround','Moira Stuart','Nick Owen','Aiming Homes','Michael Burke','Trevor Martdonald','Sam Brown','Mart Pice','Jon Snow','Jeremy Paxperson']
        self.tagline = "Presented by " + random.choice(newsreaders)

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

news_page = NewsPage(301, "http://feeds.bbci.co.uk/news/rss.xml?edition=uk", "News")
news_page2 = NewsPage(302, "http://feeds.bbci.co.uk/sport/0/rss.xml?edition=uk", "Sport")
news_page3 = NewsPage(303, "http://blog.emfcamp.org/rss", "emfcamp.org")
news_page4 = NewsPage(304, "http://www.metoffice.gov.uk/public/data/PWSCache/WarningsRSS/Region/UK", "Weather warnings")
news_page5 = NewsPage(305, "http://www.dailymail.co.uk/tvshowbiz/index.rss", "Showbiz News")

index = NewsIndex(300)

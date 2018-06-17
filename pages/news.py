#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
import time
from functions import replace

class NewsIndex(Page):
    def __init__(self, page_num):
        super(NewsIndex, self).__init__(page_num)
        self.title = "News Index"
        self.importance = 2
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
        self.importance = 1
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

news_page1 = NewsPage(301, "http://feeds.bbci.co.uk/news/rss.xml?edition=uk", "Top Stories")
news_page2 = NewsPage(302, "http://feeds.bbci.co.uk/news/technology/rss.xml?edition=uk", "Technology")
news_page3 = NewsPage(303, "http://feeds.bbci.co.uk/news/business/rss.xml?edition=uk", "Business")
news_page4 = NewsPage(304, "http://www.ledburyreporter.co.uk/news/rss/", "Local News")
news_page5 = NewsPage(305, "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml?edition=uk", "Science")
news_page6 = NewsPage(306, "http://feeds.bbci.co.uk/news/politics/rss.xml?edition=uk", "Politics")
news_page7 = NewsPage(307, "http://feeds.bbci.co.uk/news/education/rss.xml?edition=uk", "Education")
news_page8 = NewsPage(308, "https://www.theguardian.com/uk/rss", "The Guardian")
news_page9 = NewsPage(309, "http://www.independent.co.uk/news/rss", "The Independent")
news_page10 = NewsPage(310, "http://www.telegraph.co.uk/newsfeed/rss/news_breaking.xml", "The Telegraph")
news_page11 = NewsPage(311, "http://blog.emfcamp.org/rss", "emfcamp.org")
news_page12 = NewsPage(312, "http://www.metoffice.gov.uk/public/data/PWSCache/WarningsRSS/Region/UK", "Weather warnings")
news_page13 = NewsPage(313, "http://www.dailymail.co.uk/tvshowbiz/index.rss", "Showbiz")

index = NewsIndex(300)
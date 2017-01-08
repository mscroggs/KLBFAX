#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
import time
from functions import klb_replace


class NewsPage(Page):
    def __init__(self, page_num, url, title):
        super(NewsPage, self).__init__(page_num)
        self.top_title = title
        self.title = "Marts"
        self.url = url
        if page_num == 300:
            self.in_index = True
            self.index_num = "300-306"
        else:
            self.in_index = False

    def background(self):
        import feedparser
        rss_url = self.url
        self.feed = feedparser.parse(rss_url)

        item = feed['entries'][0]
        self.words = item['title'].split(" ")

        self.entries = [klb_replace(item['title']) for item in feed['entries'][1:]]


    def generate_content(self):
        import random
        newsreaders = ['Huw Edwards','Lizo from Newsround','Moira Stuart','Nick Owen','Aiming Homes','Michael Burke','Trevor Martdonald','Sam Brown','Mart Pice','Jon Snow','Jeremy Paxperson']
        self.tagline = "Presented by " + random.choice(newsreaders)

        self.add_title(self.top_title,bg="BLACK",fg="LIGHTRED")

        self.add_newline()
        chars_left = 80
        line = ""
        for word in self.words:
            if chars_left - len(word)*5 <= 0:
                chars_left = 80
                self.add_title(line+" ",bg="YELLOW",fg="BLACK",font="size4")
                line = word + " "
            else:
                line = line + word + " "
            chars_left = chars_left - (len(word) + 1)*5
        self.add_title(line+" ",bg="YELLOW",fg="BLACK",font="size4")
        for item in self.entries:
            self.add_text(" - "+ item)
            self.add_newline()

news_page = NewsPage(300, "http://feeds.bbci.co.uk/news/rss.xml?edition=uk", "Newsmart")
news_page2 = NewsPage(301, "http://feeds.bbci.co.uk/sport/0/rss.xml?edition=uk", "Sportsmart")
news_page3 = NewsPage(302, "http://mscroggs.co.uk/blog/rss.xml", "mscroggs.co.ukmart")
news_page4 = NewsPage(303, "http://www.metoffice.gov.uk/public/data/PWSCache/WarningsRSS/Region/UK", "Weatherwarningmart")
news_page5 = NewsPage(304, "http://open.live.bbc.co.uk/weather/feeds/en/2643743/3dayforecast.rss", "Forecastmart")
news_page6 = NewsPage(305, "http://radiomart.nl/feed/", "Martradiomart")
news_page7 = NewsPage(306, "https://twitrss.me/twitter_user_to_rss/?user=mathslogicbot", "Truthmart")

news_pageX = NewsPage(707, "http://chalkdustmagazine.com/feed/", "Chalkmart")

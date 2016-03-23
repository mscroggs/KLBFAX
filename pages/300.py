#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from page import Page
from printer import instance as printer
from printer import size4_instance as size4_printer
from colours import colour_print
import time
from functions import klb_replace


class NewsPage(Page):
    def __init__(self, page_num, url, title):
        super(NewsPage, self).__init__(page_num)
        self.title = "Marts"
        self.url = url
        if page_num == 300:
            self.in_index = True
            self.index_num = "300-301, 303-306"
        else:
            self.in_index = False

    def generate_content(self):
        import urllib2
        import feedparser
        import random
        newsreaders = ['Huw Edwards','Lizo from Newsround','Moira Stuart','Nick Owen','Aiming Homes','Michael Burke','Trevor Martdonald','Sam Brown','Mart Pice','Jon Snow','Jeremy Paxperson']
        tag = "Presented by " + random.choice(newsreaders)
        content = self.colours.colour_print_join([
                        (printer.text_to_ascii(self.title)+"",
                            self.colours.Background.BLACK,
                            self.colours.Foreground.RED+self.colours.Style.BOLD)                            
                    ],"","")   

        rss_url = self.url
        feed = feedparser.parse(rss_url)

        ticker = 0
        for item in feed['entries']:
            if ticker == 0:
                content += "\n"
                words = item['title'].split(" ")
                chars_left = 80
                line = ""
                for word in words:
                    if chars_left - len(word)*5 <= 0:
                        chars_left = 80
                        content += self.colours.colour_print_join([
                        (size4_printer.text_to_ascii(line,False)+"",
                          self.colours.Background.YELLOW+self.colours.Style.BLINK,
                          self.colours.Foreground.BLACK)                            
                        ]," "," ")
                        content += "\n"     
                        line = word + " "
                    else:
                        line = line + word + " "
                    chars_left = chars_left - (len(word) + 1)*5       
                content += self.colours.colour_print_join([
                (size4_printer.text_to_ascii(line,False)+"",
                  self.colours.Background.YELLOW+self.colours.Style.BLINK,
                  self.colours.Foreground.BLACK)                            
                ]," "," ")                    
            else:
                content += "\n  - "
                content += item['title']
            ticker+=1
                    
        content += "\n"
        
        self.content = klb_replace(content)
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
news_page = NewsPage(300, "http://feeds.bbci.co.uk/news/rss.xml?edition=uk", "Newsmart")
news_page2 = NewsPage(301, "http://feeds.bbci.co.uk/sport/0/rss.xml?edition=uk", "Sportsmart")
news_pageX = NewsPage(708, "http://chalkdustmagazine.com/feed/", "Chalkmart")
#news_page3 = NewsPage(302, "http://m.highways.gov.uk/feeds/rss/AllEvents.xml", "Roadmart")
news_page4 = NewsPage(303, "http://www.metoffice.gov.uk/public/data/PWSCache/WarningsRSS/Region/UK", "Weatherwarningmart")
news_page5 = NewsPage(304, "http://open.live.bbc.co.uk/weather/feeds/en/2643743/3dayforecast.rss", "Forecastmart")
news_page6 = NewsPage(305, "http://radiomart.nl/feed/", "Martradiomart")
news_page7 = NewsPage(306, "https://twitrss.me/twitter_user_to_rss/?user=mathslogicbot", "Truthmart")








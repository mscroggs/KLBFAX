#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page

class ChartPage(Page):
    def __init__(self, page_num, title, rss):
        super(ChartPage, self).__init__(page_num)
        self.title = title
        self.importance = 2
        self.rss = rss
        self.in_index = False

    def background(self):

        def fix(text):
            text = "&".join(text.split("&amp;"))
            text = "'".join(text.split("&#39;"))
            return text

        import feedparser
        feed = feedparser.parse(self.rss)
        self.tagline = feed["entries"][0]["summary"]
        self.entries = []
        for item in feed["entries"][1:]:
            self.entries.append(fix(item["title"]).split(") ",1)[1].split(" - "))

    def generate_content(self):
        import random

        self.add_title(self.title, font='size4')

        for i,(artist, song) in enumerate(self.entries):
            self.add_text(str(i+1)+" ", fg="RED")
            if i < 9:
                self.add_text(" ")
            self.add_text(artist, fg="YELLOW")
            self.add_text(" " + song, fg="GREEN")
            self.add_newline()

page1 = ChartPage(337, "UK Top 40", "http://www.uktop40.co.uk/official_top_40.rss")
page2 = ChartPage(338, "UK Top 40 Albums", "http://www.uktop40.co.uk/official_top_40_albums.rss")


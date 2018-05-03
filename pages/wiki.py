#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
import time
from functions import strip_tags_and_replace

class WikiPage(Page):
    def __init__(self, page_num, url, title, dyk=False, new=False):
        super(WikiPage, self).__init__(page_num)
        self.importance = 1
        self.top_title = title
        self.title = title
        self.url = url
        self.in_index = False
        self.tagline = "From Wikipedia"
        self.dyk = dyk
        self.new = new

    def background(self):
        import feedparser
        rss_url = self.url
        feed = feedparser.parse(rss_url)
        if 'entries' in feed and len(feed['entries']) > 0 and "summary" in feed["entries"][0]:
            if self.dyk:
                self.text = [strip_tags_and_replace(i["summary"]) for i in feed["entries"]]
            elif self.new:
                self.text = [strip_tags_and_replace(i["title"]) for i in feed["entries"]]
            else:
                self.text = strip_tags_and_replace(feed['entries'][0]["summary"])
        else:
            if self.dyk or self.new:
                self.text = [""]
            else:
                self.text = "Could not load article"




    def generate_content(self):
        self.add_title(self.top_title,bg="BLACK",fg="LIGHTRED",font='size4')
        if self.dyk or self.new:
            for t in self.text:
                if self.dyk:
                    self.add_wrapped_text("..."+t[13:])
                    self.add_newline()
                else:
                    self.add_wrapped_text(t)
                self.add_newline()
        else:
            self.add_wrapped_text(self.text)

wiki_page3 = WikiPage(103, "https://en.wikipedia.org/w/api.php?action=featuredfeed&feed=onthisday&feedformat=atom","On this Day...")
wiki_page4 = WikiPage(104, "https://en.wikipedia.org/w/api.php?action=featuredfeed&feed=featured&feedformat=atom","Article of the Day")
wiki_page5 = WikiPage(105, "http://feeds.feedburner.com/enwp/DidYouKnow?format=xml","Did you know...",dyk=True)
wiki_page6 = WikiPage(106, "https://en.wikipedia.org/w/index.php?title=Special:NewPages&feed=rss","New on Wikipedia",new=True)

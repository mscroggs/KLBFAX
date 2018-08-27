#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page import Page

class LottoPage(Page):
    def __init__(self, page_num, url, title):
        super(LottoPage, self).__init__(page_num)
        self.importance = 3
        self.top_title = title
        self.title = title
        self.url = url
        self.in_index = True
        self.tagline = "Don't win a little..."

    def background(self):
        import feedparser
        import datetime
        rss_url = self.url
        feed = feedparser.parse(rss_url)
        date = datetime.datetime.strptime(feed["entries"][0]["title"][34:],"%m/%d/%Y")
        info = feed["entries"][0]["summary"]
        self.numbers = info.split(": ")[1].split(";")[0].split(",")
        self.bonus = info.split(";")[1].split(".")[0]
        self.jackpot = info.split(": ")[2].split(".")[0]
        self.date = datetime.datetime.strftime(date,"%a %-d %b")


    def generate_content(self):
        self.add_title(self.top_title)

        self.move_cursor(y=8)
        self.add_title(self.date,font='size4',fg="BLACK",bg="WHITE")

        col = "CYAN"
        for i,n in enumerate(self.numbers):
            self.move_cursor(y=12)
            self.add_title(n,pre=11*i,fg="BLACK",bg=col,fill=False,font='size4')
            if col=="CYAN":
                col = "YELLOW"
            else:
                col = "CYAN"
        self.move_cursor(y=12)
        self.add_title(self.bonus,pre=68,fg="BLACK",bg="RED",fill=False,font='size4')

        self.move_cursor(y=20)
        self.add_title(u"Jackpot: £"+"{:.2}".format(float(self.jackpot[1:])//1000000) + "m",font='size4',fg="BLACK",bg="YELLOW")

Lotto_page = LottoPage(555, "https://www.thelotterycentre.com/en/feed/lotto/1/?name=British_Lotto","Lotto Results")

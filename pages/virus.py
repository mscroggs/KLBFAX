#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page import Page
from helpers import url_handler

class VirusGraphPage(Page):
    def __init__(self, page_num, cname, shortname=None):
        super(VirusGraphPage, self).__init__(page_num)
        self.importance = 4
        self.title = "COVID19 in " + cname
        self.cname = cname
        if shortname is None:
            self.shortname = cname
        else:
            self.shortname = shortname
        self.in_index = False
        self.tagline = "Uh oh"

    def background(self):
        self.xs = []
        self.ys = []
        data = url_handler.load_json("https://pomber.github.io/covid19/timeseries.json")[self.cname]
        for item in data:
            self.xs.append(item["date"])
            self.ys.append(item["confirmed"])

    def generate_content(self):
        import datetime
        self.add_title("COVID19 in " + self.shortname, font='size4bold')
        self.plot(range(len(self.ys)), self.ys, 4, 0, 
                  width=80, height=23, ytitle="Confirmed cases", 
                  xlabels=[(i, datetime.datetime.strptime(self.xs[i], '%Y-%m-%d').strftime('%-d-%b-%y'))
                           for i in range(0, len(self.ys), len(self.ys)//5)], 
                  point=None, line="r")


p0 = VirusGraphPage("560", "United Kingdom", "UK")
p0.importance = 5
p1 = VirusGraphPage("561", "US")
p2 = VirusGraphPage("562", "China")
p3 = VirusGraphPage("563", "Italy")
p4 = VirusGraphPage("564", "France")

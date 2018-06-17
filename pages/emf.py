#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
import time
from functions import strip_tags_and_replace
from random import shuffle

class WikiListPage(Page):
    def __init__(self, page_num, url, title, ):
        global pagelist
        pagelist[page_num] = title
        super(WikiListPage, self).__init__(page_num)
        self.importance = 3
        self.top_title = title
        self.title = title
        self.url = url
        self.in_index = False
        self.tagline = "From the EMF wiki"

    def background(self):
        from helpers import url_handler
        self.data = url_handler.load_json(self.url)["results"]

    def generate_content(self):
        self.add_title(self.top_title,bg="BLACK",fg="LIGHTRED",font='size4')
        villages = list(self.data.keys())
        shuffle(villages)
        for i,village in enumerate(villages):
            self.add_text(village.split(":")[-1])
            if i%2==0:
                self.move_cursor(x=35)
                self.add_text(" ")
            else:
                self.add_newline()

class IndexPage(Page):
    def __init__(self, page_num, pagelist):
        super(IndexPage, self).__init__(page_num)
        self.pagelist = pagelist
        self.importance = 2
        self.title = "EMF Information"

    def generate_content(self):
        self.add_title("EMF Information",bg="BLACK",fg="LIGHTRED",font='size4')
        for i in self.pagelist:
            self.add_text(str(i)+" ",fg="RED")
            self.add_text(self.pagelist[i])
            self.add_newline()

pagelist = {}

village_page = WikiListPage(701, "https://wiki.emfcamp.org/wiki/Special:Ask/-5B-5BCategory:Villages-5D-5D/-3F%3D-20Village-23/-3FVillageName%3DName/-3FDescription/mainlabel%3D-20Village/limit%3D100/offset%3D0/format%3Djson","List of Villages")
team_page = WikiListPage(702, "https://wiki.emfcamp.org/wiki/Special:Ask/-5B-5BCategory:Teams-5D-5D/-3FTeamDesc%3DDescription/-3FTeamLead%3DLead/-3FTeamDeputy%3DDeputy/mainlabel%3DTeam/limit%3D100/offset%3D0/format%3Djson","List of Teams")

index = IndexPage(700, pagelist)

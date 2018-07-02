#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
import time
from helpers import url_handler

class FootballPage(Page):
    def __init__(self):
        super(FootballPage, self).__init__("150")
        self.title = "World Cup latest scores"

    def background(self):
        self.results = url_handler.load_json('http://worldcup.sfg.io/matches')

    def generate_content(self):
        self.add_title("World Cup scores")
        first = True
        for i in self.results[::-1]:
            if i["winner"] is not None:
                c1 = i["home_team"]["country"]
                s1 = i["home_team"]["goals"]
                c2 = i["away_team"]["country"]
                s2 = i["away_team"]["goals"]
                self.add_text(" "*(32-len(c1)))
                if s1 > s2:
                    self.add_text(c1,fg="GREEN")
                elif s1==s2:
                    self.add_text(c1,fg="BLUE")
                else:
                    self.add_text(c1)
                self.add_text(" "+str(s1))
                self.add_text(" ")
                self.add_text(str(s2)+" ")
                if s1 < s2:
                    self.add_text(c2,fg="GREEN")
                elif s1==s2:
                    self.add_text(c2,fg="BLUE")
                else:
                    self.add_text(c2)
                self.add_newline()
                if first:
                    first = False
                    homeg = []
                    for e in i["home_team_events"]:
                        if e["type_of_event"]=="goal":
                            homeg.append(e["player"]+" "+e["time"])
                    awayg = []
                    for e in i["away_team_events"]:
                        if e["type_of_event"]=="goal":
                            awayg.append(e["time"]+" "+e["player"])
                    for i in range(max(len(homeg),len(awayg))):
                        if i<len(homeg):
                            h = homeg[i]
                        else:
                            h = ""
                        if i<len(awayg):
                            a = awayg[i]
                        else:
                            a = ""
                        self.add_text(" "*(32-len(h))+h)
                        self.add_text("     "+a)
                        self.add_newline()
                    self.add_newline()

class FootballPage2(Page):
    def __init__(self):
        super(FootballPage2, self).__init__("151")
        self.title = "World Cup groups"

    def background(self):
        self.results = url_handler.load_json('http://worldcup.sfg.io/teams/group_results')

    def generate_content(self):
        self.add_title("World Cup groups")
        i = 0
        for group in self.results:
            try:
                group = group["group"]
            except:
                continue
            self.move_cursor(x=1+28*(i%3),y=8+(i//3)*6)
            self.add_text("Group "+group["letter"],fg="YELLOW")
            self.move_cursor(x=1+28*(i%3)+14)
            self.add_text(" ")
            self.add_text("Pts")
            self.add_newline()
            self.move_cursor(x=1+28*(i%3))
            for tn,team in enumerate(group["teams"]):
                team = team["team"]
                c = team["country"]
                if tn <= 1:
                    self.add_text(c,fg="GREEN")
                else:
                    self.add_text(c)
                self.move_cursor(x=1+28*(i%3)+14)
                self.add_text("  ")
                self.add_text(str(team["points"]))
                self.add_newline()
                self.move_cursor(x=1+28*(i%3))
            i += 1

football_page = FootballPage()
football_page2 = FootballPage2()

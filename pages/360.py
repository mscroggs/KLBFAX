#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import sub
from page import Page
import tweepy
import json
try:
    from html import unescape
except:
    try:
        import html.parser
        def unescape(string):
            return html.parser.HTMLParser().unescape(string)
    except:
        import HTMLParser
        def unescape(string):
            return HTMLParser.HTMLParser().unescape(string)

def strip_tags(string):
    return sub(r'<[^>]*?>', '', string)

class WhoPage(Page):
    def __init__(self,page_num):
        super(WhoPage, self).__init__(page_num)
        self.title = "Who is Peter?"
        self.tagline = "@who_is_peter"

    def background(self):
        import urllib2
        from datetime import datetime
        import re

        try:
            with open("/home/pi/login.json") as f:
                details = json.load(f)
        except:
            try:
                self.tweets
            except:
                self.tweets = []
            return
        auth = tweepy.OAuthHandler(details['app_key'], details['app_secret'])
        auth.set_access_token(details['oauth_token'], details['oauth_token_secret'])

        api = tweepy.API(auth)

        peter_replies = api.search(q="@who_is_peter",show_user=True,count=15)
        self.tweets = []
        for tweet in peter_replies:
            who_id = tweet.in_reply_to_status_id
            reply_username =  tweet.author.screen_name
            reply_text = tweet.text
            if who_id > 0:
                try:
                    who = api.get_status(who_id)
                    #print who.text
                    original_id = who.in_reply_to_status_id
                    original = api.get_status(original_id)
                    original_text = original.text
                    original_username = original.author.screen_name
                    created_at = original.created_at
                    original0_id = original.in_reply_to_status_id
                    original0_text = ""
                    if original0_id > 0:
                        try:
                            original0 = api.get_status(original0_id)
                            original0_text = original0.text
                            original0_username = original0.author.screen_name
                            created_at = original0.created_at
                        except:
                            pass
                    this = []
                    this.append(datetime.strftime(datetime.strptime(str(created_at), '%Y-%m-%d %H:%M:%S'),"%a %d %b, %H:%M"))
                    this.append(original0_username)
                    this.append(re.sub("http.\S+","[link]",original0_text))
                    this.append(original_username)
                    this.append(re.sub("http.\S+","[link]",original_text))
                    this.append(reply_username)
                    this.append(reply_text.replace("@who_is_Peter",""))
                    self.tweets.append(this)

                except:
                    continue

    def generate_content(self):
        self.add_title("Who is peter?",font="size4",fg="GREEN",bg="BRIGHTWHITE")

        twitter = """
--G-----G--
-GGGGGGGGG-
-G-------G-
-G-G---G-G-
-G-------G-
-G-GGGGG-G-
-G-------G-
-GGGGGGGGG-
"""
        self.print_image(twitter,0,69)
        self.move_cursor(x=0)

        t_count = 0
        for t in self.tweets:
            if t_count < 4:
                if t_count == 0:
                    dash = ""
                else:
                    dash = u"─"
                self.start_fg_color("GREEN")
                self.add_text("[ " + t[0] + " ]" + dash*56) # date
                self.start_fg_color("DEFAULT")
                self.add_newline()
                if t[1] != "":
                    self.start_fg_color("LIGHTCYAN")
                    self.add_text("@" + t[1] + ": ")
                    self.end_fg_color()
                    self.add_text(t[2])
                    self.add_newline()
                self.start_fg_color("YELLOW")
                self.add_text("@" + t[3] + ": ")
                self.end_fg_color()
                self.add_wrapped_text(t[4])
                self.add_newline()
                self.start_fg_color("PINK")
                self.add_text("@who_is_peter: Who?")
                self.end_fg_color()
                self.add_newline()
                self.start_fg_color("YELLOW")
                self.add_text("@" + t[5] + ": ")
                self.end_fg_color()
                self.add_wrapped_text(t[6])
                self.add_newline()
                #self.add_text("----------------")
                #self.add_newline()
                t_count = t_count + 1

page = WhoPage("360")

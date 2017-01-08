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

        try:
            with open("/home/pi/login.json") as f:
                details = json.load(f)
        except:
            return
        auth = tweepy.OAuthHandler(details['app_key'], details['app_secret'])
        auth.set_access_token(details['oauth_token'], details['oauth_token_secret'])



        api = tweepy.API(auth)

        #public_tweets = api.home_timeline()
        self.peter_replies = api.search(q="@who_is_peter",show_user=True,count=15)

    def generate_content(self):
        self.add_title("Who is Peter?")
        for tweet in self.peter_replies:
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
                            continue

                    self.add_text(str(created_at))
                    self.add_newline()
                    if original0_text != "":
                        self.start_fg_color("LIGHTCYAN")
                        self.add_text("@" + original0_username + ": ")
                        self.end_fg_color()
                        self.add_text(original0_text)
                        self.add_newline()
                    self.start_fg_color("YELLOW")
                    self.add_text("@" + original_username + ": ")
                    self.end_fg_color()
                    self.add_text(original_text)
                    self.add_newline()
                    self.start_fg_color("PINK")
                    self.add_text("@who_is_peter: Who?")
                    self.end_fg_color()
                    self.add_newline()
                    self.start_fg_color("YELLOW")
                    self.add_text("@" + reply_username + ": ")
                    self.end_fg_color()
                    self.add_text(reply_text.replace("@who_is_Peter",""))
                    self.add_newline()
                    self.add_text("----------------")
                    self.add_newline()
                except:
                    continue

page = WhoPage("307")


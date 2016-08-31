from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from time import strftime
import screen
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

    def generate_content(self):
        import urllib2
        content = colour_print(printer.text_to_ascii("Who is Peter?",fill=False))
        content += "\n\n"

        
        try:
            with open("/home/pi/login.json") as f:
                details = json.load(f)
        except:
            pass
        auth = tweepy.OAuthHandler(details['oauth_token'], details['oauth_token_secret'])
        auth.set_access_token(details['app_key'], details['app_secret'])



        api = tweepy.API(auth)

        #public_tweets = api.home_timeline()
        peter_replies = api.search(q="@who_is_peter",show_user=True,count=15)
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
                            continue

                    content += str(created_at) + "\n"
                    if original0_text != "":
                        content +=  self.colours.Foreground.CYAN + self.colours.Style.BOLD + "@" + original0_username + ": " + self.colours.Style.DEFAULT + self.colours.Foreground.DEFAULT + original0_text + "\n"
                    content += self.colours.Foreground.YELLOW + self.colours.Style.BOLD + "@" + original_username + ": " + self.colours.Style.DEFAULT + self.colours.Foreground.DEFAULT + original_text + "\n"
                    content += self.colours.Foreground.MAGENTA + self.colours.Style.BOLD + "@who_is_Peter: Who?" + self.colours.Style.DEFAULT + self.colours.Foreground.DEFAULT + "\n"
                    content += self.colours.Foreground.YELLOW + self.colours.Style.BOLD + "@" + reply_username + ":" + self.colours.Style.DEFAULT + self.colours.Foreground.DEFAULT + reply_text.replace("@who_is_Peter","") + "\n"
                    content += "----------------" + "\n"
                except:# Exception,e:
                    #content += str(e)
                    continue

        self.content = content + "\n"

page = WhoPage("307")

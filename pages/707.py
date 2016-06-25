from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from time import strftime
import screen
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

class ChalkPage(Page):
    def __init__(self,page_num):
        super(ChalkPage, self).__init__(page_num)
        self.title = "chalkdust"
        self.tagline = "@chalkdustmag"

    def generate_content(self):
        import urllib2
        content = colour_print(printer.text_to_ascii("G-research!",fill=False))
        content += "\n  &\n"
        content += colour_print(printer.text_to_ascii("?-research!",fill=False))        

        response = urllib2.urlopen("https://twitter.com/chalkdustmag")
        html = unescape(response.read().decode("utf-8"))
        html = " ".join(html.split("\n"))
        tweets = html.split('<div class="ProfileTweet-contents">')
        for tweet in tweets[1:]:
            tweet = tweet.split('<p class="ProfileTweet-text js-tweet-text u-dir"')[1]
            tweet = tweet.split('</p>')[0]
            tweet = strip_tags(tweet)
            tweet = tweet.split('>')[1]
            while len(tweet) > screen.WIDTH:
                content += "\n"
                content += tweet[:screen.WIDTH]
                tweet = tweet[screen.WIDTH:]
            content += "\n"+tweet+"\n"
        
        self.content = content + "\n\n\n    sponsor Chalkdust"

page = ChalkPage("707")

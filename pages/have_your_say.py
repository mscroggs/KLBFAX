from page import Page
from cupt.cupt import non_dark_colors
from random import choice

class TwitterPage(Page):
    def __init__(self, page_num, n, tpage=None):
        if tpage is None:
            self.tpage = self
        else:
            self.tpage = tpage
        self.start_n = n
        super(TwitterPage, self).__init__(page_num)
        self.title = "Have Your Say"
        if n == 0:
            self.importance = 5
            self.index_num = "200-209"
        else:
            self.importance = 2
            self.in_index = False
        self.lines = []
        self.tweet = "Tweet @EMFFAX to have your comment appear here"

    def background(self):
        from helpers import tweet_handler

        try:
            results = tweet_handler.search("@EMFFAX")
        except tweet_handler.NoTwitter:
            self.lines = ["Twitter login failed..."]
            return

        self.lines = []

        for tweet in results:
            col = choice(non_dark_colors)
            text = tweet["text"]
            while "http" in text:
                tsp = text.split("http",1)
                text = tsp[0] + "<url>"
                if " " in tsp[1]:
                    text += tsp[1].split(" ",1)[1]
            if text[:8] == "@EMFFAX ":
                text = text[8:]
            text = text.replace("@EMFFAX","EMFFAX")
            for i in range(0,len(text),80):
                self.lines.append((text[i:i+80],col,False))
            self.lines.append(("@" + tweet["user"]["screen_name"] + " " + " ".join(tweet["user"]["created_at"].split(" ")[:4]),col,True))
            self.lines.append(("",col,True))

    def generate_content(self):
        self.add_title("Have your say",font="size4")
        self.add_newline()
        for line, col, fg in self.lines[21*self.start_n:21*(self.start_n+1)]:
            if fg:
                self.add_text(line, fg=col)
            else:
                self.add_text(line, bg=col)
            self.add_newline()

tpage = TwitterPage("200",0)
tpage1 = TwitterPage("201",1,tpage)
tpage2 = TwitterPage("202",2,tpage)
tpage3 = TwitterPage("203",3,tpage)
tpage4 = TwitterPage("204",4,tpage)
tpage5 = TwitterPage("205",5,tpage)
tpage6 = TwitterPage("206",6,tpage)
tpage7 = TwitterPage("207",7,tpage)
tpage8 = TwitterPage("208",8,tpage)
tpage9 = TwitterPage("209",9,tpage)


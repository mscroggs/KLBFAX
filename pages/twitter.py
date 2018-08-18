from page import Page

class TwitterPage(Page):
    def __init__(self, page_num, n, tpage=None):
        if tpage is None:
            self.tpage = self
            self.main = True
        else:
            self.tpage = tpage
            self.main = False
        self.start_n = n
        super(TwitterPage, self).__init__(page_num)
        self.importance = 5
        self.title = "#emfcamp"

        if n == 0:
            self.importance = 5
            self.index_num = "210-219"
            self.lines = []
        else:
            self.importance = 2
            self.in_index = False

    def generate_content(self):
        from helpers import tweet_handler

        self.add_title("#emfcamp",font="size4")
        self.move_cursor(y=3,x=70)
        self.add_text("Page "+str(self.start_n+1)+"/10",fg="BLUE",bg="YELLOW")
        self.add_newline()
        try:
            results = tweet_handler.search("emfcamp")
        except tweet_handler.NoTwitter:
            self.add_text("Twitter login failed...")
            return

        if self.main:
            self.lines = []
            for tweet in results:
                if "retweeted_status" not in tweet:
                    self.lines.append([("@" + tweet["user"]["screen_name"] + " ", "YELLOW"),
                                       (" ".join(tweet["created_at"].split(" ")[:4]), "BLUE")])
                    text = tweet["full_text"]
                    while "http" in text:
                        tsp = text.split("http",1)
                        text = tsp[0] + "<url>"
                        if " " in tsp[1]:
                            text += tsp[1].split(" ",1)[1]

                    for i in range(0,len(text),80):
                        self.lines.append([(text[i:i+80], "WHITE")])
                    self.lines.append([])

        for line in self.tpage.lines[21*self.start_n:21*(self.start_n+1)]:
            for text,col in line:
                self.add_text(text, fg=col)
            self.add_newline()

tpage = TwitterPage("210",0)
tpage1 = TwitterPage("211",1,tpage)
tpage2 = TwitterPage("212",2,tpage)
tpage3 = TwitterPage("213",3,tpage)
tpage4 = TwitterPage("214",4,tpage)
tpage5 = TwitterPage("215",5,tpage)
tpage6 = TwitterPage("216",6,tpage)
tpage7 = TwitterPage("217",7,tpage)
tpage8 = TwitterPage("218",8,tpage)
tpage9 = TwitterPage("219",9,tpage)


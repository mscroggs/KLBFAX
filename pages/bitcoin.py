from page import Page

class BitPage(Page):
    def __init__(self,page_num):
        global pagelist
        super(BitPage, self).__init__(page_num)
        self.importance = 3
        self.title = "Bitcoin"
        self.in_index = False
        self.tagline = "From ounce.me"

    def background(self):
        import feedparser
        feed = feedparser.parse("http://feeds.feedburner.com/OuncemeQuotesFullFeed")
        for e in feed["entries"]:
            if "Total Number " in e["title"]:
                self.total = e["title"].split("=")[1]
                while self.total[0] == " ":
                    self.total = self.total[1:]
            if "MtGox" in e["title"]:
                self.valDOL = e["title"].split("|")[0].split("$")[1]
                while self.valDOL[0] == " ":
                    self.valDOL = self.valDOL[1:]
                while self.valDOL[-1] == " ":
                    self.valDOL = self.valDOL[:-1]

    def generate_content(self):
        self.add_title("Bitcoin",font='size4')
        self.add_newline()
        self.add_title("1BTC = $"+self.valDOL,font='size4',fg="BLACK",bg="YELLOW")
        self.add_newline()
        self.add_title("Total Number of",font='size4',fg="BLACK",bg="BLUE")
        self.add_title("Bitcoins:",font='size4',fg="BLACK",bg="BLUE")
        self.move_cursor(y=14)
        self.add_title(self.total,font='size4',fg="BLACK",bg="YELLOW",pre=37)

index = BitPage(341)

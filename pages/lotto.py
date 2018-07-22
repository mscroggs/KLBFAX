from page import Page

class LottoPage(Page):
    def __init__(self, page_num, url, title):
        super(LottoPage, self).__init__(page_num)
        self.importance = 3
        self.top_title = title
        self.title = title
        self.url = url
        self.in_index = True
        self.tagline = "Don't win a little..."

    def background(self):
        import feedparser
        rss_url = self.url
        feed = feedparser.parse(rss_url)
        info = feed["entries"][0]["summary"]
        self.numbers = info.split(": ")[1].split(";")[0].split(",")
        self.bonus = info.split(";")[1].split(".")[0]
        self.jackpot = info.split(": ")[2].split(".")[0]


    def generate_content(self):
        self.add_title(self.top_title)

        col = "BLUE"
        for i,n in enumerate(self.numbers):
            self.move_cursor(y=8)
            self.add_title(n,pre=11*i,fg="BLACK",bg=col,fill=False,font='size4')
            if col=="BLUE":
                col = "YELLOW"
            else:
                col = "BLUE"
        self.move_cursor(y=8)
        self.add_title(self.bonus,pre=68,fg="BLACK",bg="RED",fill=False,font='size4')

        self.move_cursor(y=16)
        self.add_title("Jackpot: "+self.jackpot,font='size4',fg="BLACK",bg="YELLOW")

Lotto_page = LottoPage(555, "https://www.thelotterycentre.com/en/feed/lotto/1/?name=British_Lotto","Lotto Results")

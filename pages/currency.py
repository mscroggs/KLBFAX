from page import Page

class CurrencyPage(Page):
    def __init__(self, page_num, url, c1, c2):
        global pagelist
        super(CurrencyPage, self).__init__(page_num)
        self.importance = 1
        self.top_title = c1[0]+" vs "+c2[0]
        self.title = c1[3]+" vs "+c2[3]
        pagelist[page_num] = (c1,c2)
        self.url = url
        self.in_index = False
        self.tagline = "From fxexchangerate.com"
        self.c1 = c1
        self.c2 = c2

    def background(self):
        if self.c1[0] != self.c2[0]:
            import feedparser
            rss_url = self.url
            feed = feedparser.parse(rss_url)
            s = feed["entries"][0]["summary"]
            self.a = s.split("<br")[0].split("=")[1]
            while self.a[0] == " ":
                self.a = self.a[1:]
            self.a = self.a.split(" ")[0]
            self.b = s.split("<br")[1].split("=")[1]
            while self.b[0] == " ":
                self.b = self.b[1:]
            self.b = self.b.split(" ")[0]
        else:
            self.a = "1"
            self.b = "1"

    def generate_content(self):
        self.add_title(self.top_title,bg="BLACK",fg="RED",font='size4')
        self.add_title(self.c1[1]+"1"+self.c1[2]+" = "+self.c2[1]+self.a+self.c2[2],font='size4',fg="BLACK",bg="YELLOW")
        self.add_title(self.c2[1]+"1"+self.c2[2]+" = "+self.c1[1]+self.b+self.c1[2],font='size4',fg="BLACK",bg="LIGHTBLUE")

class IndexPage(Page):
    def __init__(self, page_num, pagelist):
        super(IndexPage, self).__init__(page_num)
        self.pagelist = pagelist
        self.importance = 1
        self.title = "Money"

    def generate_content(self):
        self.add_title("Currencies",bg="BLACK",fg="LIGHTRED",font='size4bold')
        c1 = None
        x = 0
        y = 7
        self.add_text("341",fg="RED")
        self.add_text(" Bitcoin")
        self.add_newline()
        self.add_text("342",fg="RED")
        self.add_text(" Bitcoin vs USD")
        self.add_newline()
        self.add_text("343",fg="RED")
        self.add_text(" Bitcoin vs GBP")
        self.add_newline()
        self.add_text("344",fg="RED")
        self.add_text(" Bitcoin vs EUR")
        for i,page in enumerate(self.pagelist):
            d = self.pagelist[page]
            if c1 != d[0][3]:
                c1 = d[0][3]
                y += 1
                if y>25:
                    y = 4
                    x += 28
                self.move_cursor(x=x,y=y)
                self.add_text(c1,fg="YELLOW")
            y += 1
            if y>26:
                y = 4
                x += 28
            self.move_cursor(x=x,y=y)
            self.add_text(str(page),fg="RED")
            self.add_text(" vs "+d[1][3])

currencies = [
        ("GBP","£","","British Pound"),
        ("EUR","€","","Euro"),
        ("USD","$","","US Dollar"),
        ("NZD","NZ$","","New Zealand Dollar"),
        ("AUD","AU$","","Australian Dollar"),
        ("JPY","¥","","Japanese Yen"),
        ("NOK","","kr","Norwegian Krone"),
        ("VND","₫","","Vietnam Dong"),
        ("RUB","","₽","Russian Rouble"),
        ("CHF","Fr.","","Swiss Franc"),
        ("GBP","SCOT£","","Scottish Pound")
    ]

pagelist = {}
pages = []
pn = 345
for i,a in enumerate(currencies):
    for b in currencies[i+1:]:
        pages.append(CurrencyPage(pn, "http://"+a[0].lower()+".fxexchangerate.com/"+b[0].lower()+".xml",a,b))
        pn += 1

index = IndexPage(340, pagelist)
index.index_num = "340-399"

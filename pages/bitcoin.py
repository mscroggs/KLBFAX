from page import Page
from helpers import url_handler
import config

class BitPage(Page):
    def __init__(self,page_num):
        super(BitPage, self).__init__(page_num)
        self.importance = 4
        self.title = "Bitcoin"
        self.in_index = False
        self.tagline = "Powered by CoinDesk"

    def background(self):
        self.feed = url_handler.load_json("https://api.coindesk.com/v1/bpi/currentprice.json")

    def generate_content(self):
        self.add_title("Bitcoin",font='size4bold')
        self.add_newline()
        self.add_title("1BTC = $"+self.feed["bpi"]["USD"]["rate"],font='size4',fg="BLACK",bg="YELLOW")
        self.add_newline()
        self.add_title("1BTC = £"+self.feed["bpi"]["GBP"]["rate"],font='size4',fg="BLACK",bg="CYAN")
        self.add_newline()
        self.add_title("1BTC = €"+self.feed["bpi"]["EUR"]["rate"],font='size4',fg="BLACK",bg="ORANGE")
        self.add_newline()

class BitGraphPage(Page):
    def __init__(self,page_num, c,cname):
        super(BitGraphPage, self).__init__(page_num)
        self.importance = 4
        self.title = "Bitcoin vs "+cname
        self.c = c
        self.cname = cname
        self.in_index = False
        self.tagline = "Powered by CoinDesk"

    def background(self):
        self.xs = []
        self.ys = []
        year = config.now().year-1
        month = config.now().month
        for i in range(12):
            strm = str(month)
            if len(strm) == 1:
                strm = "0"+strm
            date = str(year)+"-"+strm+"-01"
            data = url_handler.load_json("https://api.coindesk.com/v1/bpi/historical/close.json?start="+date+"&end="+date)
            self.xs.append(date)
            self.ys.append(data["bpi"][date])
            month += 1
            if month == 13:
                month = 1
                year += 1

    def generate_content(self):
        self.add_title("Bitcoin vs "+self.cname,font='size4bold')
        self.plot(range(12),self.ys,4,0,height=23,ytitle=self.c,xtitle="Date",xlabels=[(i,self.xs[i]) for i in range(0,12,3)],point=None,line="r")

p1 = BitPage("341")
p2 = BitGraphPage("342","USD","US Dollar")
p3 = BitGraphPage("343","GBP","Pound")
p4 = BitGraphPage("344","EUR","Euro")

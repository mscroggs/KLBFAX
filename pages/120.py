from page import Page
import datetime

class OllyPage(Page):
    def __init__(self, page_num,who,when,numb=None):
        super(OllyPage, self).__init__(page_num)
        self.title = "Countdowns"
        self.who = who
        self.when = when
        if numb is None:
            self.in_index = False
        else:
            self.in_index = True
            self.index_num = numb


    def generate_content(self):
        delta = self.when - datetime.datetime.now()
        hs = delta.seconds/3600
        ds = delta.days
        if ds > 0:
            left = str(ds) + " day"
            left2 = str(hs) + " hour"
            if ds!=1: left += "s"
            if hs!=1: left2 += "s"
            self.add_title(self.who+" Leaves In",fg="LIGHTGREEN",bg="BLACK")
            self.add_title(left,fg="PINK",bg="BLACK")
            self.add_title(left2,fg="BRIGHTWHITE",bg="BLACK")
        else:
            delta = datetime.datetime.now() - self.when
            hs = delta.seconds/3600
            ds = delta.days

            left = str(ds) + " day"
            left2 = str(hs) + " hour"
            if ds!=1: left += "s"
            if hs!=1: left2 += "s"
            self.add_title(self.who+" Left",fg="LIGHTGREEN",bg="BLACK")
            self.add_title(left,fg="PINK",bg="BLACK")
            self.add_title(left2,fg="BRIGHTWHITE",bg="BLACK")
            self.add_title("ago",fg="LIGHTGREEN",bg="BLACK")

j_page = OllyPage("120","Jigsaw",datetime.datetime(2016, 3, 24, 17, 0),"120-122")
o_page = OllyPage("121","Olly",datetime.datetime(2016, 3, 24, 17, 0))
b_page = OllyPage("122","Belgin",datetime.datetime(2018, 8, 31, 16, 0))

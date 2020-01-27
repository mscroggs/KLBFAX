from page import Page
from helpers.time import datetime
import config

class CountdownPage(Page):
    def __init__(self, page_num,who,when,numb=None):
        super(CountdownPage, self).__init__(page_num)
        self.title = "Countdowns"
        self.who = who
        self.when = when
        if numb is None:
            self.in_index = False
        else:
            self.in_index = True
            self.index_num = numb

        self.in_index = False

    def generate_content(self):
        delta = self.when - config.now()
        hs = delta.seconds//3600
        ds = delta.days
        if ds >= 0:
            left = str(ds) + " day"
            left2 = str(hs) + " hour"
            if ds!=1: left += "s"
            if hs!=1: left2 += "s"
            self.add_title(left,fg="PINK",bg="BLACK")
            self.add_title(left2,fg="BRIGHTWHITE",bg="BLACK")
            self.add_title("Until "+self.who,fg="LIGHTGREEN",bg="BLACK")
        else:
            delta = config.now() - self.when
            hs = delta.seconds//3600
            ds = delta.days

            left = str(ds) + " day"
            left2 = str(hs) + " hour"
            if ds!=1: left += "s"
            if hs!=1: left2 += "s"
            self.add_title(left,fg="PINK",bg="BLACK")
            self.add_title(left2,fg="BRIGHTWHITE",bg="BLACK")
            self.add_title("Since "+self.who+" started",fg="LIGHTGREEN",bg="BLACK")

def next(month, day, hour, min):
    diff = None
    year = config.now().year
    while diff is None or diff.days < 0:
        out = datetime(year, month, day, hour, min)
        diff = out - config.now()
        year += 1
    return out

page1 = CountdownPage("120","Christmas",next(12, 25, 0, 0),"120-129")
page2 = CountdownPage("121","EMF2018",datetime(2018, 8, 31, 11, 0))
page3 = CountdownPage("122","EMF2020",datetime(2020, 8, 21, 11, 0))
page4 = CountdownPage("123","Pi Day",next(3, 14, 0, 0))
page5 = CountdownPage("124","May Day",next(5, 1, 0, 0))
page6 = CountdownPage("125","Ed Balls Day",next(4, 28, 0, 0))
page7 = CountdownPage("126","Next year",next(1, 1, 0, 0))
page8 = CountdownPage("127","US Election",datetime(2020, 11, 3, 0, 0))
page9 = CountdownPage("128","UK leaves the EU",datetime(2020, 1, 31, 23, 0))
page10 = CountdownPage("129","MathsJam",datetime(2019, 11, 30, 12, 0))

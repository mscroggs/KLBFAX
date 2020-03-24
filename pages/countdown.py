# -*- coding: utf-8 -*-
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

        #self.in_index = False

    def generate_content(self):

        def width_of_word(word,font="size4"):
            if font=="size7":
                width = len(word)*7 \
                - sum(map(word.count, u"|"))*6 \
                - sum(map(word.count, u"'"))*5 \
                - sum(map(word.count, u"I!:."))*4 \
                - sum(map(word.count, u"1()-#&"))*3 \
                - sum(map(word.count, u"LJ/"))*1 \
                + sum(map(word.count, u"N"))*1 \
                + sum(map(word.count, u"WM"))*2
            else:
                width = len(word)*5 \
                - sum(map(word.count, u"|"))*4 \
                - sum(map(word.count, u"!:,‘’.'I’"))*3 \
                - sum(map(word.count, u"-()1"))*2 \
                - sum(map(word.count, u"T"))*1 \
                + sum(map(word.count, u"MW"))*1 \
                - sum(map(word.count, u"il"))*3 \
                - sum(map(word.count, u"fjt"))*2 \
                - sum(map(word.count, u"abcdeghknopqrsuvxyz"))*1 \
                + sum(map(word.count, u"mw"))*1
            return width

        def center_pad(center,chars_left,right=False):
            if center:
                if right:
                    return ((chars_left+2)//2 + (chars_left+2)%2)*"|"
                else:
                    return ((chars_left+2)//2)*"|"
            else:
                return ""

        def add_title_wrapped(text,max_width=config.WIDTH,bg="YELLOW",fg="BLACK",font="size4",fill=True,pre=0,center=False):
            chars_left = max_width
            line = ""
            #self.move_cursor(y=y,x=x)
            text = text.split(" ")
            first_line = True
            for word in text:
                if (chars_left - width_of_word(word,font) <= 0) and not first_line:
                    # Print old line and start new line.
                    self.add_title(center_pad(center,chars_left) + line[:-1] + center_pad(center,chars_left,right=True),bg=bg,fg=fg,font=font,fill=fill,pre=pre)
                    chars_left = max_width
                    line = word + " "
                else:
                    # Add word to line
                    line = line + word + " "
                    first_line = False
                chars_left = chars_left - width_of_word(word,font) - 3

            # Print final line.
            self.add_title(center_pad(center,chars_left) + line[:-1] + center_pad(center,chars_left,right=True),bg=bg,fg=fg,font=font,fill=fill,pre=pre)






        delta = self.when - config.now()
        hs = delta.seconds//3600
        ds = delta.days
        days = "DAY"
        hours = "hr"

        if ds >= 0:
            if ds!=1: days += "S"
            if hs!=1: hours += "s"
            self.add_title("Countdown to...",font="size4",fg="ORANGE",bg="BRIGHTWHITE")
            color = "RED"
        else:
            delta = config.now() - self.when
            hs = delta.seconds//3600
            ds = delta.days
            if ds!=1: days += "S"
            if hs!=1: hours += "s"
            self.add_title("Time since...",font="size4",fg="ORANGE",bg="BRIGHTWHITE")
            color = "BLUE"

        book_width = 30
        book_height = 34
        top_margin = 7
        left_margin = 49#(config.WIDTH-book_width)//2

        book = "x"*book_width + "\n" + ("x" + "-"*(book_width-2) + "x" + "\n")*(book_height-2) + "x"*book_width + "\n"
        book=(book).replace(" ","-").replace("x","w")
        self.print_image(book,top_margin,left_margin) #y,x)

        left_margin = 1
        self.move_cursor(y=8)
        add_title_wrapped(self.who,font="size4",fg="BLACK",bg="YELLOW",pre=left_margin+2,fill=False,max_width=44,center=True)


        left_margin = 49
        self.move_cursor(y=8)

        add_title_wrapped(str(ds),font="size7",fg=color,bg="BRIGHTWHITE",pre=left_margin+2,fill=False,max_width=26,center=True)
        add_title_wrapped(days,font="size4",fg="BLACK",bg="BRIGHTWHITE",pre=left_margin+2,fill=False,max_width=26,center=True)
        add_title_wrapped(str(hs) + "|" + hours,font="size4",fg="BRIGHTWHITE",bg="BLACK",pre=left_margin+2,fill=False,max_width=26,center=True)


def next(month, day, hour, min):
    diff = None
    year = config.now().year
    while diff is None or diff.days < 0:
        out = datetime(year, month, day, hour, min)
        diff = out - config.now()
        year += 1
    return out

page1 = CountdownPage("120","Christmas",next(12, 25, 0, 0),"120-129")
page2 = CountdownPage("121","Lockdown",datetime(2020, 3, 23, 20, 30))
page3 = CountdownPage("122","EMF2020",datetime(2020, 8, 21, 11, 0))
page4 = CountdownPage("123","Pi Day",next(3, 14, 0, 0))
page5 = CountdownPage("124","May Day",next(5, 1, 0, 0))
page6 = CountdownPage("125","Ed Balls Day",next(4, 28, 0, 0))
page7 = CountdownPage("126","Next year",next(1, 1, 0, 0))
page8 = CountdownPage("127","US Election",datetime(2020, 11, 3, 0, 0))
page9 = CountdownPage("128","UK left the EU",datetime(2020, 1, 31, 23, 0))
page10 = CountdownPage("129","MathsJam",datetime(2019, 11, 30, 12, 0))

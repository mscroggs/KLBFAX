from page import Page


class PointsPage(Page):
    def __init__(self):
        super(PointsPage, self).__init__("130")
        self.title = "House Points"
        self.index_num = "130-131"

    def generate_content(self):
        self.add_title("house points")

        self.start_fg_color("GREEN")
        self.add_text("Year")
        pos = (6,17,27,38,48,59,65)
        for p,t in zip(pos,["Gryffindor","Slytherin","Hufflepuff","Ravenclaw","Durmstrang","Squib","Peeves"]):
            self.move_cursor(x=p)
            self.add_text(t)
        self.end_fg_color()
        self.add_newline()
        for ls in [
                ("2015a",(692,  525,1155, 702, 440, 513,   0)),
                ("2015b",(3382, 408,4614,3591, 606,2174,  38)),
                ("2016a",(1621, 378,3640,3407, 202,3744,  30)),
                ("2016b",(1428,1609,3789,3609, 366, 434,   0)),
                ("2017a",(1323,3145, 576,2374, 106, 183,   0)),
                ("2017b",(1700,1991, 893,2345,  70, 594,   0))
                  ]:
            self.start_fg_color("GREEN")
            self.add_text(ls[0])
            self.end_fg_color()
            for p,t in zip(pos,ls[1]):
                self.move_cursor(p)
                if t == max(ls[1]):
                    self.start_fg_color("RED")
                self.add_text(str(t))
                if t == max(ls[1]):
                    self.end_fg_color()
            self.add_newline()

p_page = PointsPage()

from page import Page
from math import floor
from helpers.file_handler import f_read_json
import config

def points_format(points,log=0):
    points = int(points)
    points /= 10**log
    points = int(floor(points))
    return str(points)

class PointsPage(Page):
    def __init__(self):
        super(PointsPage, self).__init__("131")
        self.title = "House Points"
        self.in_index = False

    def background(self):
        import os
        files = ["points","events","emails"]
        if config.NAME == "KLBFAX" and config.MAIN == True:
            from points import add_points
            os.system("scp mscroggs:~/.klb/points /home/pi/.klbtemp/points > /dev/null 2>&1")
            with open("/home/pi/.klbtemp/points") as f:
                for line in f:
                    lsp = line.strip("\n").split(",")
                    add_points(lsp[0],int(lsp[1]),lsp[2])
            with open("/home/pi/.klbtemp/points","w") as f:
                pass
            os.system("scp /home/pi/.klbtemp/points mscroggs:~/.klb/points > /dev/null 2>&1")
            for f in files:
                os.system("scp /home/pi/.klb/"+f+" mscroggs:~/.klbdump/"+f+" > /dev/null 2>&1")
        else:
            for f in files:
                os.system("scp mscroggs:~/.klbdump/"+f+" /home/pi/.klb/"+f+" > /dev/null 2>&1")

    def generate_content(self):
        import json
        from operator import itemgetter
        data = f_read_json('points')
        larg = 0
        seco = 0
        for house in data:
            pts = int(data[house])
            if pts>larg:
                seco = larg
                larg = pts
            elif pts>seco:
                seco = pts
        log = len(str(seco))-3

        points_names = ["points","decapoints","hectopoints","kilopoints"]

        if log>=len(points_names):
            log = len(points_names)-1
        if log<0:
            log = 0

        if "Gryffindor" in data: g = points_format(data["Gryffindor"],log)
        else:                    g = "0"
        if "Hufflepuff" in data: h = points_format(data["Hufflepuff"],log)
        else:                    h = "0"
        if "Slytherin" in data:  s = points_format(data["Slytherin"],log)
        else:                    s = "0"
        if "Squib" in data:     sq = points_format(data["Squib"],log)
        else:                   sq = "0"
        if "Ravenclaw" in data:  r = points_format(data["Ravenclaw"],log)
        else:                    r = "0"
        if "Durmstrang" in data: d = points_format(data["Durmstrang"],log)
        else:                    d = "0"
        if "Postdoc" in data: po = points_format(data["Postdoc"],log)
        else:                 po = "0"

        self.add_title(points_names[log])
        self.add_text("What do points mean?")

        self.move_cursor(x=0, y=8)
        self.add_title(g,fg="YELLOW",bg="RED",fill=False)
        self.move_cursor(x=0, y=15)
        self.add_text("Gryffindor",fg="YELLOW",bg="RED")

        self.move_cursor(x=27, y=8)
        self.add_title(s,fg="GREEN",bg="GREY",fill=False,pre=27)
        self.move_cursor(x=27, y=15)
        self.add_text("Slytherin",fg="GREEN",bg="GREY")

        self.move_cursor(x=54, y=8)
        self.add_title(sq,fg="PINK",bg="BLUE",fill=False,pre=54)
        self.move_cursor(x=54, y=15)
        self.add_text("Squib",fg="PINK",bg="BLUE")

        self.move_cursor(x=0, y=16)
        self.add_title(r,fg="BRIGHTWHITE",bg="BLUE",fill=False)
        self.move_cursor(x=0, y=23)
        self.add_text("Ravenclaw",fg="BRIGHTWHITE",bg="BLUE")

        self.move_cursor(x=27, y=16)
        self.add_title(h,fg="YELLOW",bg="GREY",fill=False,pre=27)
        self.move_cursor(x=27, y=23)
        self.add_text("Hufflepuff",fg="YELLOW",bg="GREY")

        if config.NAME == "KLBFAX":
            self.move_cursor(x=54, y=16)
            self.add_title(d,fg="RED",bg="GREEN",fill=False,pre=54)
            self.move_cursor(x=54, y=23)
            self.add_text("Durmstrang",fg="RED",bg="GREEN")
        else:
            self.move_cursor(x=54, y=16)
            self.add_title(po,fg="RED",bg="GREEN",fill=False,pre=54)
            self.move_cursor(x=54, y=23)
            self.add_text("Postdoc",fg="RED",bg="GREEN")

        self.add_newline()

        sorted_pts = sorted(data.items(),key=itemgetter(1),reverse=True)

        self.add_rainbow_text("Full List")
        self.add_newline()
        i=0
        for house,points in sorted_pts:
            i+=1
            self.add_text(house, fg="YELLOW")
            self.add_text(" ")
            self.add_text(str(points), fg="GREEN")
            if i%5==0:  self.add_newline()
            else:       self.add_text("  ")


pp = PointsPage()

import config
from page import Page
from math import floor
from helpers.file_handler import f_read_json

def points_format(points,log=0):
    points = int(points)
    points /= 10**log
    points = int(floor(points))
    return str(points)

class PointsPage(Page):
    def __init__(self):
        super(PointsPage, self).__init__("132")
        self.title = "Flat Points"
        if config.NAME == "28JHFAX":
            self.in_index = True
            self.tagline = "Visit Hufflepuff Intranet (192.168.0.27) to add points"
        else:
            self.in_index = False
            self.tagline = "Via 28JHFAX"
        self.is_enabled = True

    def generate_content(self):
        import json
        from operator import itemgetter
        data = f_read_json('flat_points')
        larg = 0
        seco = 0
        for house in data:
            pts = int(data[house])
            if pts>larg:
                seco = larg
                larg = pts
            elif pts>seco:
                seco = pts
        log = len(str(seco))-3

        points_names = ["points","decapoints","hectopoints","kilopoints"]

        if log>=len(points_names):
            log = len(points_names)-1
        if log<0:
            log = 0

        if "mike" in data:    mike = points_format(data["mike"],log)
        else:                 mike = "0"
        if "scroggs" in data: scroggs = points_format(data["scroggs"],log)
        else:                 scroggs = "0"
        if "adam" in data:    adam = points_format(data["adam"],log)
        else:                 adam = "0"
        if "alan" in data:    alan = points_format(data["alan"],log)
        else:                 alan = "0"

        self.add_title("Flat "+points_names[log])

        self.move_cursor(x=0,y=7)
        self.add_title(mike, bg="LIGHTGREEN",fg="BLACK")
        self.move_cursor(x=2,y=13)
        self.add_text("Mike", fg="LIGHTGREEN")

        self.move_cursor(x=40,y=7)
        self.add_title(scroggs, bg="LIGHTBLUE",fg="BLACK",pre=40)
        self.move_cursor(x=42,y=13)
        self.add_text("Scroggs", fg="LIGHTBLUE")

        self.move_cursor(x=0,y=15)
        self.add_title(adam, bg="YELLOW",fg="BLACK")
        self.move_cursor(x=2,y=21)
        self.add_text("Adam", fg="YELLOW")

        self.move_cursor(x=40,y=15)
        self.add_title(alan, bg="PINK",fg="BLACK",pre=40)
        self.move_cursor(x=42,y=21)
        self.add_text("Alan", fg="PINK")

p_page = PointsPage()

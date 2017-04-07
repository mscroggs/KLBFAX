from page import Page
from math import floor
from file_handler import f_read_json
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
        files = ["points"]
        if config.NAME == "KLBFAX":
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

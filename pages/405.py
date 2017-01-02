import config
from page import Page
from math import floor
from file_handler import f_read_json

def points_format(points,log=0):
    points = int(points)
    points /= 10**log
    points = int(floor(points))
    return str(points)

class PointsPage(Page):
    def __init__(self):
        super(PointsPage, self).__init__("405")
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


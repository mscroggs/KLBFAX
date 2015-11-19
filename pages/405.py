import os
from os.path import join,expanduser
from page import Page
from printer import instance as printer
from math import floor
from file_handler import f_read_json

def points_format(points,log=0):
    points = int(points)
    points /= 10**log
    points = int(floor(points))
    return str(points)

class PointsPage(Page):
    def __init__(self, page_num):
        super(PointsPage, self).__init__(page_num)
        self.title = "Flat Points"
        if os.getenv("SLAVE"):
            self.is_index = True
        else:
            self.is_index = False
        self.is_enabled = True
        self.tagline = "Visit Hufflepuff Intranet (192.168.0.27) to add points"

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

        content = self.colours.colour_print(printer.text_to_ascii("Flat "+points_names[log]))
        content += "\n\n"
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii(mike,False)+"\n  Mike",
                            self.colours.Background.GREEN+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK),
                        (printer.text_to_ascii(scroggs,False)+"\n Scroggs",
                            self.colours.Background.BLUE+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK)
                    ],"   ","   ")
        content += "\n\n"
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii(adam,False)+"\n  Adam",
                            self.colours.Background.YELLOW+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK),
                        (printer.text_to_ascii(alan,False)+"\n  Alan",
                            self.colours.Background.MAGENTA,
                            self.colours.Foreground.BLACK)
                    ],"   ","   ")
        self.content = content

page_number = os.path.splitext(os.path.basename(__file__))[0]
p_page = PointsPage(page_number)


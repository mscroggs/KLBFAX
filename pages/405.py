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
            self.is_enabled = True
            self.is_index = True
        else:
            self.is_enabled = False
            self.is_index = False
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
        log = len(str(seco))-2
        
        points_names = ["points","decapoints","hectopoints","kilopoints"]

        if log>=len(points_names):
            log = len(points_names)-1
        if log<0:
            log = 0

        if "Mike" in data:    mike = points_format(data["Mike"],log)
        else:                 mike = "0"
        if "Scroggs" in data: scroggs = points_format(data["Scroggs"],log)
        else:                 scroggs = "0"
        if "Adam" in data:    adam = points_format(data["Adam"],log)
        else:                 adam = "0"
        if "Alan" in data:    alan = points_format(data["Alan"],log)
        else:                 alan = "0"

        content = self.colours.colour_print(printer.text_to_ascii(points_names[log]))
        content += "\n\n"
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii(mike,False)+"\nMike",
                            self.colours.Background.WHITE,
                            self.colours.Foreground.RED),
                        (printer.text_to_ascii(scroggs,False)+"\nScroggs",
                            self.colours.Background.BLUE+self.colours.Style.BLINK,
                            self.colours.Foreground.YELLOW+self.colours.Style.BOLD)
                    ],"   ","   ")
        content += "\n\n"
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii(adam,False)+"\nAdam",
                            self.colours.Background.BLUE,
                            self.colours.Foreground.YELLOW),
                        (printer.text_to_ascii(alan,False)+"\nAlan",
                            self.colours.Background.RED,
                            self.colours.Foreground.MAGENTA)
                    ],"   ","   ")
        self.content = content

page_number = os.path.splitext(os.path.basename(__file__))[0]
p_page = PointsPage(page_number)


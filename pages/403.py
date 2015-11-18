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
        self.title = "House Points"

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

        content = self.colours.colour_print(printer.text_to_ascii(points_names[log]))
        content += "\nWhat do points mean?\n"

        content += self.colours.colour_print_join([
                        (printer.text_to_ascii(g,False)+"\nGryffindor",
                            self.colours.Background.RED,
                            self.colours.Foreground.YELLOW+self.colours.Style.BOLD),
                        (printer.text_to_ascii(s,False)+"\nSlytherin",
                            self.colours.Style.BLINK,
                            self.colours.Foreground.GREEN),
                        (printer.text_to_ascii(sq,False)+"\nSquib",
                            self.colours.Background.BLUE,
                            self.colours.Foreground.MAGENTA)
                    ]," "," ")
        content += "\n"
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii(r,False)+"\nRavenclaw",
                            self.colours.Background.BLUE,
                            self.colours.Foreground.WHITE+self.colours.Style.BOLD),
                        (printer.text_to_ascii(h,False)+"\nHufflepuff",
                            self.colours.Style.BLINK,
                            self.colours.Foreground.YELLOW+self.colours.Style.BOLD),
                        (printer.text_to_ascii(d,False)+"\nDurmstrang",
                            self.colours.Background.GREEN,
                            self.colours.Foreground.RED)
                    ]," "," ")
        content += "\n"
        sorted_pts = sorted(data.items(),key=itemgetter(1),reverse=True)

        content += "Full List\n"
        i=0
        for house,points in sorted_pts:
            i+=1
            content += self.colours.Foreground.YELLOW + house + self.colours.Foreground.DEFAULT
            content += " "
            content += self.colours.Foreground.GREEN + str(points) + self.colours.Foreground.DEFAULT
            if i%4==0:  content += "\n"
            else:       content += "  "

        self.content = content

page_number = os.path.splitext(os.path.basename(__file__))[0]
p_page = PointsPage(page_number)

class SecretPage(Page):
    def __init__(self, page_num):
        super(SecretPage, self).__init__(page_num)
        self.title = "Secret Page"
        self.is_enabled = False

    def generate_content(self):

        content = self.colours.colour_print(printer.text_to_ascii("secret page"))
        content += "\n\n"
        content += "You have found the secret page! 10 points to Hufflepuff!\n\n"
        content += self.colours.colour_print(printer.text_to_ascii("go puffs!"))
        content += "Hufflepuff are cheating! 10 points from Hufflepuff!\n\n"

        self.content = content

s_page = SecretPage("042")

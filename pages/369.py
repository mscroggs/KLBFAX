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

class OllyPage(Page):
    def __init__(self, page_num):
        super(OllyPage, self).__init__(page_num)
        self.title = "Countdown to Olly Leaving"

    def generate_content(self):
        import datetime
        delta = datetime.datetime(2016, 3, 24,17,0) - datetime.datetime.now()
        left = str(delta.days) + " days"
        left2 = str(delta.seconds/3600) + " hours"
        content = self.colours.colour_print(printer.text_to_ascii("Olly Leaves In"),foreground=self.colours.Foreground.GREEN+self.colours.Style.BOLD,background=self.colours.Background.BLACK)
        content += "\n\n"
        content += self.colours.colour_print(printer.text_to_ascii(left),foreground=self.colours.Foreground.MAGENTA+self.colours.Style.BOLD,background=self.colours.Background.BLACK)
        content += "\n\n"
        content += self.colours.colour_print(printer.text_to_ascii(left2),foreground=self.colours.Foreground.WHITE+self.colours.Style.BOLD,background=self.colours.Background.BLUE)
        self.content = content

page_number = os.path.splitext(os.path.basename(__file__))[0]
o_page = OllyPage(page_number)


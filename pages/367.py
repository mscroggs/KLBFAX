from page import Page
from printer import instance as printer
import datetime
from random import randrange,choice
from screen import WIDTH

class WheresOllyPage(Page):
    def __init__(self, page_num):
        super(WheresOllyPage, self).__init__(page_num)
        self.title = "Where's Olly?"

    def generate_content(self):
        content = self.colours.colour_print(printer.text_to_ascii("Where's Olly?"),foreground=self.colours.Foreground.GREEN+self.colours.Style.BOLD,background=self.colours.Background.BLACK)
        n = randrange(400)
        for i in range(400):
            if 4*i % WIDTH < 3:
                content += "\n"
            if i==n:
                content += "OLLY"
            else:
                content += choice(["OILY","YLLO"])
        self.content = content

b_page = WheresOllyPage("367")


import os
from page import Page
from colours import colour_print
from printer import instance as printer
#from random import randrange

title = colour_print(printer.text_to_ascii("Pi", padding={"left": 32}))

class PiPage(Page):
    def __init__(self,page_num):
        super(PiPage, self).__init__(page_num)
        self.title = "Pi"

    def generate_content(self):
        with open("pages/pi.txt") as f:
            pi = f.read()
        self.content = title + "\n"
        for i in range(100):
            line = pi[80*i:80*i+80]
            self.content += line + "\n"      

sub_page = PiPage("314")

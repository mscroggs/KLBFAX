import os
from page import Page
from colours import colour_print
from printer import instance as printer
from random import randrange

page_number = os.path.splitext(os.path.basename(__file__))[0]

class SuckPage(Page):
    def __init__(self,page_num):
        super(SuckPage, self).__init__(page_num)
        self.title = "Important Information"

    def generate_content(self):
        n = randrange(3)
        if n==1:
            self.content = colour_print(
                printer.text_to_ascii("imperial suck(s)"))
            self.content += "\n\n (Except for Kuru,\n  love from Scroggs)"
        elif n==2:
            self.content = colour_print(
                printer.text_to_ascii("B&Q suck(s)"))
        elif n==3:
            self.content = colour_print(
                printer.text_to_ascii("Dell suck(s)"))

sub_page = SuckPage(page_number)

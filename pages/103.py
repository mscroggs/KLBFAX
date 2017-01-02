import os
from page import Page
from random import randrange

class SuckPage(Page):
    def __init__(self):
        super(SuckPage, self).__init__("103")
        self.title = "Important Information"
        self.in_index = False

    def generate_content(self):
        n = randrange(3)
        if n==0:
            self.add_title("imperial suck(s)")
            self.add_newline()
            self.add_text("(Except for Kuru,\n  love from Scroggs)")
        elif n==1:
            self.add_title("B&Q suck(s)")
        elif n==2:
            self.add_title("Dell suck(s)")

sub_page = SuckPage()

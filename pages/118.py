from page import Page
from random import randrange

class SuckPage(Page):
    def __init__(self):
        super(SuckPage, self).__init__("118")
        self.title = "Laptop"
        self.in_index = False

    def generate_content(self):
        self.add_title("has Adam's",bg="YELLOW",fg="BLACK")
        self.add_title("Laptop arrived?",bg="YELLOW",fg="BLACK")
        self.add_title("YES!",bg="GREEN",fg="BLACK")
        self.add_title("only 44 days to arrive",bg="LIGHTBLUE",fg="BLACK")

sub_page = SuckPage()

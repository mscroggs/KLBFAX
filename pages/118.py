import os
from page import Page
from colours import colour_print
from printer import instance as printer
from random import randrange
import colours

page_number = os.path.splitext(os.path.basename(__file__))[0]

class SuckPage(Page):
    def __init__(self,page_num):
        super(SuckPage, self).__init__(page_num)
        self.title = "Laptop"

    def generate_content(self):
        self.content = colour_print(
            printer.text_to_ascii("has Adam's"),colours.Foreground.BLACK,colours.Background.YELLOW)
        self.content += "\n"
        self.content += colour_print(
            printer.text_to_ascii("Laptop arrived?"),colours.Foreground.BLACK,colours.Background.YELLOW)
        self.content += "\n"
        self.content += colour_print(
            printer.text_to_ascii("no"),colours.Foreground.BLACK,colours.Background.RED)

sub_page = SuckPage(page_number)

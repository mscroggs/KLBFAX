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
        from datetime import date
        days = 31 + (date.today() - date(2016,6,15)).days
        self.content = colour_print(
            printer.text_to_ascii("has Adam's"),colours.Foreground.BLACK,colours.Background.YELLOW)
        self.content += "\n"
        self.content += colour_print(
            printer.text_to_ascii("Laptop arrived?"),colours.Foreground.BLACK,colours.Background.YELLOW)
        self.content += "\n"
        self.content += colour_print(
            printer.text_to_ascii("YES!"),colours.Foreground.BLACK,colours.Background.RED)
        self.content += colour_print(
            printer.text_to_ascii("Only 44 days to arrive"),colours.Foreground.BLACK,colours.Background.BLUE+colours.Style.BLINK)

sub_page = SuckPage(page_number)

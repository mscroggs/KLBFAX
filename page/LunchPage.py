from page import Page
from printer import instance as printer
import colours

def colour_print(text):
    return colours.colour_print(text, colours.Background.YELLOW+colours.Style.BLINK, colours.Foreground.BLACK)


class LunchPage(Page):
    def __init__(self):
        super(LunchPage, self).__init__("???")
        self.name = "Lunch"
        self.content = colour_print(printer.text_to_ascii("Lunchtime!"))
        self.loaded = True

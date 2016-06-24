from page import Page
from printer import instance as printer
import colours
import now

def colour_print(text, col=colours.Background.YELLOW):
    return colours.colour_print(text, col+colours.Style.BLINK, colours.Foreground.BLACK)


class LunchPage(Page):
    def __init__(self):
        super(LunchPage, self).__init__("???")
        self.name = "Lunch"
        self.content = colour_print(printer.text_to_ascii("Lunchtime!"))
        if now.now().strftime("%a")=="Fri":
            self.content += "\n"
            self.content += colour_print(printer.text_to_ascii("It's Fancy Friday!"),colours.Background.RED)
        self.content += "\n"
        self.content += colour_print(printer.text_to_ascii(“HUDA HUNGRY!”),colours.Background.BLUE+colours.Style.BLINK)
        self.loaded = True

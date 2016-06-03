from page import Page
from printer import instance as printer
import colours
import now

def colour_print(text, col=colours.Background.BLUE):
    return colours.colour_print(text, col+colours.Style.BLINK, colours.Foreground.BLACK)


class PubPage(Page):
    def __init__(self):
        super(PubPage, self).__init__("???")
        self.name = "Pub"
        self.content = colour_print(printer.text_to_ascii("It's Friday Afternoon!"),colours.Background.RED)
        self.content += "\n"
        self.content += colour_print(printer.text_to_ascii("Go to the pub!"))
        self.loaded = True

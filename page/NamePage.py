from random import random
from page import Page
from printer import instance as printer
import colours

def colour_print(text):
    return colours.colour_print(text, colours.Background.WHITE, colours.Foreground.BLACK)

class NamePage(Page):
    def __init__(self, name):
        super(NamePage, self).__init__("???")
        self.name = name
        self.title = "Greeting"
        self.reload()

    def generate_content(self):
        name = self.name

        greeting = "Hello"

        if random() < 0.01:
            greeting = "Bello"
        if random() < 0.01:
            name = "Jigsaw"

        self.content = colour_print(printer.text_to_ascii(greeting))
        self.content += "\n  "
        self.content += colour_print(printer.text_to_ascii(name + "!"))


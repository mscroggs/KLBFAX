from random import random
from page import Page
import printer
import colours

class NamePage(Page):
    def __init__(self, name):
        super(NamePage, self).__init__("???")
        self.name = name
        self.title = "Greeting"
        self.reload()

    def generate_content(self):
        name = self.name

        greeting = printer.instance.text_to_ascii("asu")
        self.content = colours.colour_print(greeting)

        if random() < 0.01:
            greeting = "Bello"
        if random() < 0.01:
            name = "Jigsaw"

        self.content += name + "!"

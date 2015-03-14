from random import random
from page import Page
from printer import Printer


class NamePage(Page):
    def __init__(self, name):
        super(NamePage, self).__init__("???")
        self.name = name
        self.reload()

    def generate_content(self):
        name = self.name
        # greeting = "Hello"
        greeting = Printer.instance

        if random() < 0.01:
            greeting = "Bello"
        if random() < 0.01:
            name = "Jigsaw"

        self.content = greeting + " " + name + "!"

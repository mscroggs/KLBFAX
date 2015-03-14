from random import random
from page import Page
import printer


class NamePage(Page):
    def __init__(self, name):
        super(NamePage, self).__init__("???")
        self.name = name
        self.title = "Greeting"
        self.reload()

    def generate_content(self):
        name = self.name
        # greeting = "Hello"
        greeting = printer.instance.text_to_ascii("Hello")

        if random() < 0.01:
            greeting = "Bello"
        if random() < 0.01:
            name = "Jigsaw"

        self.content = greeting + " " + name + "!"

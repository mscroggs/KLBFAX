from random import random,randint,choice
from page import Page
from printer import instance as printer
import colours
from points import add_points

def colour_print(text):
    return colours.colour_print(text, colours.Background.RED, colours.Foreground.BLACK)


class NamePage(Page):
    def __init__(self, name, large=True,extra=""):
        super(NamePage, self).__init__("???")
        self.name = name
        self.title = "Greeting"
        self.large = large
        self.extra = extra
        self.duration_sec = 5
        self.reload()

    def generate_content(self):
        extra = ""
        name = self.name
        from page import greetings

        greeting = greetings.random()
        if "Rafael" in name:
            if random()<0.6:
                greeting = "Muy Feo"
                add_points("Gryffindor",-1)
                extra = "\n\n-1 points to Gryffindor!"

        if random() < 0.01:
            name = "Jigsaw"
            add_points("Slytherin",10)

            extra = "\n\n10 points to Slytherin!"
        if random() < 0.01:
            name = "Fake Belgin"
            add_points("Squiberin",10)

            extra = "\n\n10 points to Squiberin!"
        extra += "\n\n"+self.extra
        self.content = colour_print(printer.text_to_ascii(greeting))
        self.content += "\n\n"
        if self.large: self.content += colour_print(printer.text_to_ascii(name + "!"))
        else: self.content += name
        self.content += extra

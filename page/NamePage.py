from random import random,randint,choice
from page import Page
from printer import instance as printer
import colours

def colour_print(text):
    return colours.colour_print(text, colours.Background.RED, colours.Foreground.BLACK)

class NamePage(Page):
    def __init__(self, name,large=True):
        super(NamePage, self).__init__("???")
        self.name = name
        self.title = "Greeting"
        self.large = large
        self.reload()

    def generate_content(self):
        name = self.name
        greetings = ["Hi","Hello","Bonjour","Bello"]

        greeting = choice(greetings)
    
        if random() < 0.01:
            name = "Jigsaw"
        if random() < 0.1:
            letters = ["#","a","b","c","d","e","f","g","h","i","j","k","1","2","3","4","0"]
            name[randint(0,len(name)-1)]=choice(letters)

        self.content = colour_print(printer.text_to_ascii(greeting))
        self.content += "\n\n"
        if self.large: self.content += colour_print(printer.text_to_ascii(name + "!"))
        else: self.content += name

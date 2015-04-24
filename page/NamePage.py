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
        greetings = ["Hi","Hello","Bonjour","Bello","Merhaba",
                     "nuqneH","Hola","Salut","Hallo","Hey",
                     "Yo","Dia dhuit","Salve","Ciao",u"\u4eca\u65e5\u306f",
                     "Shwmae","\u0417\u0434\u0440\u0430\u0432\u0441\u0442\u0432\u0443\u0439\u0442\u0435!"
                     "\u4f60\u597d"]

        greeting = choice(greetings)
        #greeting = greetings[-1]
        if "Rafael" in name:
            greeting = "Feo"
    
        if random() < 0.01:
            name = "Jigsaw"

        self.content = colour_print(printer.text_to_ascii(greeting))
        self.content += "\n\n"
        if self.large: self.content += colour_print(printer.text_to_ascii(name + "!"))
        else: self.content += name

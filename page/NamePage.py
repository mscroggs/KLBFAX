from random import random,randint,choice
from page import Page
from printer import instance as printer
import colours
from points import add_points 

def colour_print(text):
    return colours.colour_print(text, colours.Background.RED, colours.Foreground.BLACK)

class NamePage(Page):
    def __init__(self, name,large=True,extra=""):
        super(NamePage, self).__init__("???")
        self.name = name
        self.title = "Greeting"
        self.large = large
        self.extra = extra
        self.reload()

    def generate_content(self):
        extra = ""
        name = self.name
        greetings = ["Hi","Hello","Bonjour","Bello","Merhaba",
                     "nuqneH","Hola","Salut","Hallo","Hey",
                     "Yo","Dia dhuit","Salve","Ciao",u"\u4eca\u65e5\u306f",
                     "Shwmae",u"\u0417\u0434\u0440\u0430\u0432\u0441\u0442\u0432\u0443\u0439\u0442\u0435!"
                     u"\u4f60\u597d", "Booyakasha"]

        greeting = choice(greetings)
        #greeting = greetings[-1]
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

from page import Page

class NamePage(Page):
    def __init__(self, _name, large=True,extra=""):
        super(NamePage, self).__init__("???")
        self.name = _name
        self.title = "Greeting"
        self.large = large
        self.extra = extra
        self.duration_sec = 5
        self.background_loaded = True

    def generate_content(self):
        extra = ""
        _name = self.name
        from functions import greetings
        from random import random, choice
        greeting = greetings.random()
        if "Sean" in _name:
            _name = choice(["Sean","Sean the Sheep","Sean of the Dead"])
        if "Eleanor" in _name:
            if random()<0.01:
                _name = "Eleanorovirus"
                add_points("Slytherin",-10)
                extra = "\n\n-10 points to Slytherin!"
        if "Rafael" in _name:
            if random()<0.6:
                greeting = "Muy Feo"
                add_points("Gryffindor",-1)
                extra = "\n\n-1 points to Gryffindor!"

        if random() < 0.01:
            _name = "Jigsaw"
            add_points("Slytherin",10)

            extra = "\n\n10 points to Slytherin!"
        if random() < 0.01:
            _name = "Fake Belgin"
            add_points("Squiberin",10)

            extra = "\n\n10 points to Squiberin!"
        extra += "\n\n"+self.extra
        self.add_title(greeting)
        self.add_newline()
        if self.large:
            self.add_title(_name+"!")
        else:
            self.add_text(_name+"!")
        self.add_newline()
        self.add_wrapped_text(extra)

from page import Page

class GamePage(Page):
    def __init__(self, number, text, options=[]):
        super(GamePage, self).__init__(number)
        self.title = "Choose your own adventure"
        self.in_index = False
        self.text = text
        self.importance = 0
        self.options = options

    def generate_content(self):
        from random import shuffle
        self.add_title("Choose your adventure",font="size4")
        self.add_newline()
        self.add_wrapped_text(self.text)
        if len(self.options)>0:
            self.add_newline()
            self.add_newline()
            self.add_text("What do you want to do?")
            self.add_newline()
            shuffle(self.options)
            for o,n in self.options:
                self.add_text("  "+o)
                self.add_text(" Go to "+n,fg="RED")
                self.add_newline()

page00 = GamePage("900","You wake up in an unfamiliar room.",[("Go back to sleep.","901")])
page00.in_index = True
page00.importance = 4
page01 = GamePage("901","You sleep forever. GAME OVER")

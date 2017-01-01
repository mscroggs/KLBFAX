from page import Page
import config

class LunchPage(Page):
    def __init__(self):
        super(LunchPage, self).__init__("???")
        self.name = "Lunch"
        self.background_loaded = True

    def generate_content(self):
        self.add_title("Lunchtime!",fg="RED",bg="BLACK")
        if config.now().strftime("%a")=="Fri":
            self.add_newline()
            self.add_title("It's Fancy Friday!",bg="RED",fg="BLACK")
            self.add_newline()
            self.add_text("Press 7 to pick a restaurant!")
            self.add_newline()
            self.add_text("Press 8 to pick a restaurant if you are Olly!")
        self.add_newline()
        self.add_title("HUDA HUNGRY", fg="RED",bg="BLACK")

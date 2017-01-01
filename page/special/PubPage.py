from page import Page

class PubPage(Page):
    def __init__(self):
        super(PubPage, self).__init__("???")
        self.name = "Pub"
        self.background_loaded = True

    def generate_content(self):
        self.add_title("It's Friday Afternoon!",fg="RED",bg="BLACK")
        self.add_newline()
        self.add_title("Go to the pub!", fg="BLUE",bg="BLACK")
        self.loaded = True


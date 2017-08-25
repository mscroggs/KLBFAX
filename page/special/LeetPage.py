from page import Page
import config

class LeetPage(Page):
    def __init__(self):
        super(LeetPage, self).__init__("???")
        self.name = "13:37"
        self.background_loaded = True

    def generate_content(self):
        self.add_title("LE:ET",fg="RED",bg="BLACK")

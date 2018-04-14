from page import Page

class PiPage(Page):
    def __init__(self):
        super(PiPage, self).__init__("314")
        self.title = "Pi"

    def generate_content(self):
        from random import randrange
        self.add_title("Pi",font="size4")
        from helpers.file_handler import load_file
        pi = load_file("pi.txt")
        self.add_wrapped_text(pi)

sub_page = PiPage()

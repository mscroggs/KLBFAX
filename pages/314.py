from page import Page

class PiPage(Page):
    def __init__(self):
        super(PiPage, self).__init__("314")
        self.title = "Pi"

    def generate_content(self):
        self.add_title("Pi",font="size4")
        from file_handler import load_file
        self.add_wrapped_text(load_file("pi.txt"))

sub_page = PiPage()

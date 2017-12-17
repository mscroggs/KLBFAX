from page import Page

class ePage(Page):
    def __init__(self):
        super(ePage, self).__init__("271")
        self.title = "e"

    def generate_content(self):
        self.add_title("e",font="size4")
        from file_handler import load_file
        pi = load_file("e.txt")
        self.add_wrapped_text(pi)

sub_page = ePage()

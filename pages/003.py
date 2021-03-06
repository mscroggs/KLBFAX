from page import Page

class LiPage(Page):
    def __init__(self):
        super(LiPage, self).__init__("003")
        self.in_index = False
        self.is_enabled = False
        self.title = "License"


    def generate_content(self):
        from random import randrange
        self.add_title("License",font="size4")
        from file_handler import load_file
        li = load_file("../LICENSE.txt")
        c = load_file("../contributors.txt").split("\n")
        while "" in c:
            c.remove("")
        li = li.replace("The KLBFAX contributors",", ".join(c))
        self.add_wrapped_text(li)

sub_page = LiPage()

from page import Page


class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Python"
        self.tagline = "Python"

    def generate_content(self):
        self.add_title("Python")
        self.add_newline()
        self.add_block("""
            000000000000000
            00  00000000000
            00  00000000000
            000000000000000
                     000000
    00000000000000000000000 1111111
    00000000000000000000000 1111111
    0000000000000000000000  1111111
    000000000             111111111
    0000000  1111111111111111111111
    0000000 11111111111111111111111
    0000000 11111111111111111111111
            111111
            111111111111111
            11111111111  11
            11111111111  11
            111111111111111
""","BLUE","YELLOW")

page = JigPage("405")

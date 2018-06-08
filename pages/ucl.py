from page import Page

class UCLPage(Page):
    def __init__(self):
        super(UCLPage, self).__init__("211")
        self.title = " Library Spaces"
        self.tagline = "Does UCL have a space problem?"
        self.station = station
        self.importance = 5

    def generate_content(self):




        self.add_title("Library Spaces",font="size4")

        self.start_fg_color("BRIGHTWHITE")
        self.add_text("Hello")
        self.end_fg_color()

train01 = UCLPage()


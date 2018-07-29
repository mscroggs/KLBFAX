from page import Page

class PointsPage(Page):
    def __init__(self):
        super(PointsPage, self).__init__("888")
        self.importance = 2
        self.title = "Subtitles"

    def generate_content(self):
        self.move_cursor(y=22)
        self.add_title("    subtitles",fg="BLACK", bg="BRIGHTWHITE",font="size4")

p = PointsPage()

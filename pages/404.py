from page import Page

class PointsPage(Page):
    def __init__(self):
        super(PointsPage, self).__init__("404")
        self.title = "Page Not Found"
        self.in_index=False

    def generate_content(self):
        self.add_title("404")
        self.add_title("PAGE NOT FOUND")

p = PointsPage()

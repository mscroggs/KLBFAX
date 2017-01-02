from page import Page

class PointsPage(Page):
    def __init__(self):
        super(PointsPage, self).__init__("508")
        self.title = "Resource Limit"
        self.in_index=False

    def generate_content(self):
        self.add_title("508")
        self.add_title("Resource Limit Is Reached")

p = PointsPage()

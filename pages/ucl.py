from page import Page

class UCLPage(Page):
    def __init__(self):
        super(UCLPage, self).__init__("211")
        self.title = "Library Spaces"
        self.tagline = "Does UCL have a space problem?"
        self.importance = 5


    def background(self):
        from helpers import url_handler
        info = url_handler.load("http://www.ucl.ac.uk/ls/space-availability/live.php?loc=all")
        self.data = []
        for i in info.split("<h3>")[1:]:
            location = i.split("</h3>")[0]
            spaces = i.split("<li")[1].split(">")[1].split("<")[0]
            self.data.append([location,spaces])

    def generate_content(self):
        self.add_title("Library Spaces",font="size4")

        self.start_fg_color("BRIGHTWHITE")
        self.end_fg_color()
        for location,spaces in self.data:
            self.add_text(location)
            self.move_cursor(x=50)
            self.add_text(" "+spaces.split("(")[0],fg="BLUE")
            self.add_newline()

train01 = UCLPage()


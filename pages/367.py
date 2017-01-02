from page import Page
import datetime
from random import randrange,choice
from config import WIDTH

class WheresOllyPage(Page):
    def __init__(self):
        super(WheresOllyPage, self).__init__("367")
        self.title = "Where's Olly?"

    def generate_content(self):
        self.add_title("Where's Olly?",fg="LIGHTGREEN",bg="BLACK")
        n = randrange(400)
        content = ""
        for i in range(400):
            if 4*i % WIDTH < 3 and i>0:
                content += "\n"
            if i==n:
                content += "OLLY"
            else:
                content += choice(["OILY","YLLO","YOLO"])
        self.add_text(content)

b_page = WheresOllyPage()

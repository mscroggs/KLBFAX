import os
from page import Page
from ceefax import Ceefax
from random import shuffle
from config import NAME
from file_handler import f_read_json
from datetime import datetime

class OxmasPage(Page):
    def __init__(self, n):
        super(OxmasPage, self).__init__(n)
        self.title = "Oxmas Attendees"
        if NAME!="602FAX":
            self.is_enabled = False
            self.in_index = False

    def generate_content(self):
        self.add_title("OXMAS", fg="GREEN",bg="BLACK")
        db = f_read_json("db.json")
        i = 0
        for person in db:
            if person["coming"] == "yes":
                self.add_text(person["name"][1] + " (" + person["name"][0] + ")")
                if person["santa"] == "yes":
                    self.start_fg_color("RED")
                    self.add_text(" S")
                    self.end_fg_color()
                if i%2==0:
                    self.move_cursor(x=35)
                else:
                    self.add_newline()
                i += 1

i_p = OxmasPage("710")

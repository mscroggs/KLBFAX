import os
from page import Page

class TestPage(Page):
    def __init__(self):
        super(TestPage, self).__init__("002")
        self.in_index = False
        self.is_enabled=False
        self.title = "Error log"

    def generate_content(self):
        self.add_rainbow_text("ERROR LOG")
        self.add_newline()

        from error import error_list
        for e in error_list:
            self.add_text(e.as_string())
            self.add_newline()
            self.add_text(e.short_traceback())
            self.add_newline()
            self.add_newline()

instance = TestPage()

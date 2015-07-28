import os
import screen
from page import Page

from random import choice

uni_chars = []+range(1000,10000)

class TestPage(Page):
    def __init__(self):
        super(TestPage, self).__init__("001")
        self.in_index = False
        self.title = "Unicode Test Page"
        self.start = 0

    def generate_content(self):
        self.content="\nUNICODE TEST PAGE\n"
        for i in range(self.start,self.start+200):
            if i<len(uni_chars):
                ch = uni_chars[i]
            else:
                ch = choice(uni_chars)
            uni_chars.remove(ch)
            self.content += str(ch)+" "+unichr(ch)
            j += 1
            if j % 9 != 0: self.content += "  "
            else: self.content += "\n"



        self.start = i

instance = TestPage()

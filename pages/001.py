import os
import screen
from page import Page

from random import choice

uni_chars = [str(i) for i in []]
#uni_chars += ["000"+str(i) for i in range(1,10)]
#uni_chars += ["00"+str(i) for i in range(10,100)]
#uni_chars += ["0"+str(i) for i in range(100,1000)]
uni_chars += range(1,10000)


class TestPage(Page):
    def __init__(self):
        super(TestPage, self).__init__("001")
        self.in_index = False
        self.title = "Unicode Test Page"

    def generate_content(self):
        self.content="\nUNICODE TEST PAGE\n"
        j = 0
        try:
            self.start += 0
        except:
            self.start = 0
        for i in range(self.start,self.start+200):
            if i<len(uni_chars):
                ch = uni_chars[i]
            else:
                ch = choice(uni_chars)
            self.content += str(ch)+" "+unichr(ch)
            j += 1
            if j % 9 != 0: self.content += "  "
            else: self.content += "\n"



        self.start = i

instance = TestPage()

import os
import screen
from page import Page

from random import choice

uni_chars = range(33,127)+range(161,175)+range(176,179)+range(180,185)+range(186,190)
uni_chars += range(191,222)+range(223,254)+[255,402,915,920,931,934,937,945,946,948,949,956,960]
uni_chars += [963,964,966]
#uni_chars += ["000"+str(i) for i in range(1,10)]
#uni_chars += ["00"+str(i) for i in range(10,100)]
#uni_chars += ["0"+str(i) for i in range(100,1000)]
uni_chars += range(3780,10000)


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
            self.start = choice(range(0,10000,500))
        for i in range(self.start,self.start+201):
            if i<len(uni_chars):
                ch = uni_chars[i]
            else:
                ch = choice(uni_chars)
            self.content += "0"*(4-len(str(ch)))+str(ch)+" "+unichr(ch)
            j += 1
            if j % 9 != 0: self.content += "  "
            else: self.content += "\n"



        self.start = i

instance = TestPage()

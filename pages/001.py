import os
import screen
from page import Page

from random import choice

uni_chars = range(33,127)+range(161,175)+range(176,179)+range(180,185)+range(186,190)
uni_chars += range(191,222)+range(223,254)+[255,402,915,920,931,934,937,945,946,948,949,956,960]
uni_chars += [963,964,966]
uni_chars += [8226,8252,8319,8359,8486,8490,8491]+range(8592,8598)+[8616,8712,8729,8730,8735,8745,8776,8801,8804,8805]
uni_chars += [8962,8976,8992,8993,9149,9472,9474,9484,9488,9492,9496,9500,9508,9516,9524,9532]
uni_chars += range(9552,9581)+[9608,9604,9612,9616,9617,9618,9619,9644,9650,9654,9658,9660,9664,9668,9670,9675]
uni_chars += [9688,9689,9786,9787,9788,9792,9794,9824,9827,9829,9830,9834,9835]


class TestPage(Page):
    def __init__(self):
        super(TestPage, self).__init__("001")
        self.in_index = False
        self.is_enabled=False
        self.title = "Unicode Test Page"

    def generate_content(self):
        self.content="\nUNICODE TEST PAGE\n"
        j = 0
        try:
            self.start += 0
        except:
            self.start = 0
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

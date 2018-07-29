from page import Page

def listrange(*args):
    return list(range(*args))

uni_chars = listrange(33,127)+listrange(161,175)+listrange(176,179)+listrange(180,185)+listrange(186,190)
uni_chars += listrange(191,222)+listrange(223,254)+[255,402,915,920,931,934,937,945,946,948,949,956,960]
uni_chars += [963,964,966]
uni_chars += [8226,8252,8319,8359,8486,8490,8491]+listrange(8592,8598)+[8616,8712,8729,8730,8735,8745,8776,8801,8804,8805]
uni_chars += [8962,8976,8992,8993,9149,9472,9474,9484,9488,9492,9496,9500,9508,9516,9524,9532]
uni_chars += listrange(9552,9581)+[9608,9604,9612,9616,9617,9618,9619,9644,9650,9654,9658,9660,9664,9668,9670,9675]
uni_chars += [9688,9689,9786,9787,9788,9792,9794,9824,9827,9829,9830,9834,9835]


class TestPage(Page):
    def __init__(self):
        super(TestPage, self).__init__("001")
        self.in_index = False
        self.enabled=False
        self.title = "Unicode Test Page"

    def generate_content(self):
        self.add_rainbow_text("UNICODE TEST PAGE")
        self.add_newline()
        j = 0
        for i,ch in enumerate(uni_chars):
            self.start_fg_color("GREEN")
            self.add_text("0"*(4-len(str(ch)))+str(ch))
            self.end_fg_color()
            try:
                self.add_text(unichr(ch))
            except:
                self.add_text(chr(ch))
            j += 1
            if j % 13 != 0:
                self.add_text(" ")
            else:
                self.add_newline()
        #self.add_text(u"HELLO╹┓╵┌")
instance = TestPage()

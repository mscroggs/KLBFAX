from page import Page


class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Trophy"
        self.tagline = "GO NONPUFFS!"

    def generate_content(self):
        self.add_block("""
                   000001111111100000
                   000000001100000000
             240000000000110011000000000042
             2400  000000000000000000  0042
             2400   0000111111110000   0042
             24 00  0000100000000000  00 42
             24 00   00000000000000   00 42
             24  00   001111111100   00  42
             24   00   0100110010   00   42
             24    000  01111110  000    42
             24      000 000000 000      42
             24        0000000000        42
             24           0000           42
             24           0000           42
                      333333333333
                      333333333333
                      333333333333
                     33333333333333
                    3333333333333333
""", "WHITE", "RED", "WHITE", "GREY", "BLUE")

page = JigPage("403")

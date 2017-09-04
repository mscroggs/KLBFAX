from page import Page


class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Trophy"
        self.tagline = "GO PUFFS!"

    def generate_content(self):
        self.add_block("""
                   000001111111100000
                   000000001100000000
             230000000000110011000000000032
             2300  000000000000000000  0032
             2300   0000111111110000   0032
             23 00  0000100000000000  00 32
             23 00   00000000000000   00 32
             23  00   001111111100   00  32
             23   00   0100110010   00   32
             23    000  01111110  000    32
             23      000 000000 000      32
             23        0000000000        32
             23           0000           32
             23           0000           32
                      333333333333
                      333333333333
                      333333333333
                     33333333333333
                    3333333333333333
""", "WHITE", "RED", "GREEN", "GREY")

page = JigPage("403")

from page import Page

class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Squirrel"
        self.tagline = "As found in Belgin's garden"

    def generate_content(self):
        from random import choice
        squ = """
          00000000000
      00000000       0000000           0
        000000             0000      0000  00
              00            00       00 0 0
             000          000     0000    00
            000          000  000000       0000
          000          000000000              00
        000           000000               00 00
      000            0000                 000 00
     000            0000             000      00
    00             000             0000000    00
   00             000                 000000000  00
  00              00                     00    0000
  00             000               000     00000  0
  00             00            000000000000    00  0
  00             00              0000     0000 000 0
  0             00                 00      000000 00
  00            00                  00      00   00
  00            00                  00      00000
    0        00000                0000000
     00000000    00                   00
                 0000000000000000  000
"""
        a = choice([
                           ("Waspy",squ,"ORANGE"),
                           ("Hazer",squ,"YELLOW"),
                           ("Yupeng",squ[::-1],"ORANGE"),
                           ("Chunxin",squ[::-1],"YELLOW"),
                           ("Q-bert",squ,"LIGHTGREEN"),
                           ("Jigsaw",squ[::-1],"PINK"),
                           ("Meatball","\n".join([a[::-1] for a in squ.split("\n")]),"PINK"),
                           ("Merlin","\n".join([a[::-1] for a in squ.split("\n")])[::-1],"PINK"),
                           ("Quickdraw","\n".join([a for a in squ.split("\n")]),"PINK"),
                           ("Wild Squirrel fled","","")
                          ])

        self.add_title(a[0])
        self.add_block(a[1],a[2])

page = JigPage("409")

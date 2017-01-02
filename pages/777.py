from page import Page

class PointsPage(Page):
    def __init__(self):
        super(PointsPage, self).__init__("777")
        self.title = "The Team"
        self.in_index=False

    def generate_content(self):
        self.add_title("THE TEAM")

        self.add_block("""

      000000000        000 000         000 000        010101010
     00000    00     00010001000     00020002000     010     010
     000       0     1 000 000 1       000 000       10  2 2  01
     0  1   1  0     11  111  11      2       2      01       10
     0    1    0      111111111       222222222      10  222  01
       Scroggs       SpinnyGinny         Adam            Huda
    
      222222222                      11000100011
     22       22        1   1        00020002000
        0   0                        1 000 000 1
                         000         1  2   2  1
        00000           0   0        1   222   1
         Sam             Tom            Belgin 

Thank you everyone here for contributing to KLBFAX!

""","RED","GREEN","BLUE")

ppp = PointsPage()

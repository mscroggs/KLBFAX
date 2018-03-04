from page import Page
from random import shuffle
import config

class TeamPage(Page):
    def __init__(self):
        super(TeamPage, self).__init__("777")
        self.title = "Contributors"

    def generate_content(self):
        self.add_title("Contributors")

        team = [
                ["Scroggs", "  rrrrrrrrrrrr  \n"
                            " rrrrrrrr   rrr \n"
                            "rrrrrr       rrr\n"
                            "rrrr          rr\n"
                            "rrr  gg  gg    r\n"
                            "rr             r\n"
                            "r      gg      r\n"
                            "r              r\n"],

                ["Gin",     "  ggggg  ggggg  \n"
                            "ggg rrggggrr ggg\n"
                            "b ggggg  ggggg b\n"
                            "b              b\n"
                            "bb            bb\n"
                            " bb  bbbbbb  bb \n"
                            "  bbbb    bbbb  \n"
                            "   bbbbbbbbbb   "],

                ["Adam",    "  ggggg  ggggg  \n"
                            "ggg wwggggww ggg\n"
                            "  ggggg  ggggg  \n"
                            "                \n"
                            "                \n"
                            "         rr     \n"
                            "      rrrr      \n"
                            "                "],

                ["Huda",    "  rgrgrgrgrgrg  \n"
                            " rgrgrgrgrgrgrg \n"
                            "rgr          grg\n"
                            "gr    b  b    gr\n"
                            "rg            rg\n"
                            "gr   b    b   gr\n"
                            "rg    bbbb    rg\n"
                            "gr            gr"],

                ["Sam",     "   bbbbbbbbbb   \n"
                            " bbb        bbb \n"
                            " b            b \n"
                            "     W    W     \n"
                            "                \n"
                            "                \n"
                            "     WWWWWW     \n"
                            "                "],

                ["Tom",     "                \n"
                            "                \n"
                            "     g    g     \n"
                            "                \n"
                            "      rrrr      \n"
                            "     r    r     \n"
                            "                \n"
                            "                "],

                ["Belgin",  "  bbbbbbbbbbbb  \n"
                            "bbbbbbbbbbbbbbbb\n"
                            "bbwwwww  wwwwwbb\n"
                            "www ggwwwwgg www\n"
                            "bbwwwww  wwwwwbb\n"
                            "b              b\n"
                            "b    w    w    b\n"
                            "b     wwww     b"]

            ]
        shuffle(team)

        for i,t in enumerate(team[:24]):
            row = i // 8
            col = i % 8
            self.print_compressed_image(t[1],8+row*7,col*10)
            self.move_cursor(y=12+row*7,x=col*10)
            self.add_text(t[0])

        self.add_newline()
        self.add_newline()
        self.add_text("To contribute to "+config.NAME+", go to github.com/mscroggs/KLBFAX")

ppp = TeamPage()

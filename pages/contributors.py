from page import Page
from random import shuffle
import config

class TeamPage(Page):
    def __init__(self):
        super(TeamPage, self).__init__("777")
        self.title = "Contributors"
        self.importance = 3
        self.in_index = False

    def generate_content(self):
        self.add_title("Contributors")

        team = [
                ["Scroggs", "  rrrrrr \n"
                            " rrrrrrrr\n"
                            "rrrrrr rr\n"
                            "rrrr    r\n"
                            "rr    g r\n"
                            "r g     r\n"
                            "r   g   r\n"
                            "r       r\n"],

                ["Gin",     " ggg ggg \n"
                            "gg rgr gg\n"
                            "bggg gggb\n"
                            "b       b\n"
                            "b       b\n"
                            " b bbb b \n"
                            " bbb bbb \n"
                            "  bbbbb  "],

                ["Adam",    "gggg gggg\n"
                            "g wgggw g\n"
                            "gggg gggg\n"
                            "         \n"
                            "         \n"
                            "     rr  \n"
                            "   rrr   \n"
                            "         "],

                ["Huda",    " grgrgrg \n"
                            " rgrgrgr \n"
                            "rg     gr\n"
                            "g  b b  g\n"
                            "r       r\n"
                            "g  b b  g\n"
                            "r   b   r\n"
                            "g       g"],

                ["Sam",     "  bbbbb  \n"
                            "bb     bb\n"
                            "b       b\n"
                            "  W   W  \n"
                            "         \n"
                            "         \n"
                            "  WWWWW  \n"
                            "         "],

                ["Tom",     "         \n"
                            "         \n"
                            "  g   g  \n"
                            "         \n"
                            "   rrr   \n"
                            "  r   r  \n"
                            "         \n"
                            "         "],

                ["Belgin",  "  bbbbb  \n"
                            "bbbbbbbbb\n"
                            "bbww wwbb\n"
                            "wwgwwwgww\n"
                            "bbww wwbb\n"
                            "b       b\n"
                            "b w   w b\n"
                            "b  www  b"],

                ["TD",      " bbbbbbb \n"
                            "bbbbbbbbb\n"
                            "bbb   bbb\n"
                            "bb     bb\n"
                            "b W   W b\n"
                            "b       g\n"
                            "g w   w g\n"
                            "g  www  g"],

                ["Alan",    " mmmmmmm \n"
                            "mmmmmmmmm\n"
                            "mmm   mmm\n"
                            "mm     mm\n"
                            "m  c c  m\n"
                            "m       m\n"
                            "m       m\n"
                            "m   rr  m"]

            ]
        shuffle(team)

        for i,t in enumerate(team[:24]):
            row = i // 6
            col = i % 6
            self.print_image(t[1].replace(" ","-"),8+row*6,col*14)
            self.move_cursor(y=12+row*6,x=1+col*14)
            self.add_text(t[0])

        self.add_newline()
        self.add_newline()
        self.add_text("To contribute to "+config.NAME+", go to github.com/mscroggs/KLBFAX")

ppp = TeamPage()

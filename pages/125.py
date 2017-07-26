from page import Page
import datetime

class OllyPage(Page):
    def __init__(self, page_num, numb):
        super(OllyPage, self).__init__(page_num)
        self.title = "Ghosts"
        self.in_index = True
        self.index_num = numb


    def generate_content(self):

        self.add_title("Ghosts",fg="BRIGHTWHITE",bg="BLACK")
        twitter = """
-----------
--WWWWWWW--
--WWWWWWW--
-W-------W-
-W-------W-
-W-R---R-W-
-W-------W-
-W-------W-
-W---R---W-
-W--RRR--W-
-W---R---W-
-W-------W-
-WW-W-W-WW-
-W-W-W-W-W-
"""
        self.print_image(twitter,0,69)
        self.move_cursor(x=0)

        self.add_newline()

        ghosts = [["Jigsaw",datetime.datetime(2016, 3, 24, 17, 0)],
                  ["Olly",  datetime.datetime(2016, 3, 24, 17, 0)],
                  ["Adam",  datetime.datetime(2017, 4, 28, 17, 0)],
                 ]

        alive =  [["Belgin",datetime.datetime(2018, 8, 31, 16, 0)]]

        i = 0
        for ghost in ghosts:
            delta = ghost[1] - datetime.datetime.now()
            hs = delta.seconds/3600
            ds = delta.days

            self.move_cursor(x=0,y=8+4*i)
            self.add_title(ghost[0],bg="WHITE",fg="BLACK",font="size4",pre=0)
            self.move_cursor(x=0,y=8+4*i)
            self.add_title(str(-ds),bg="YELLOW",fg="BLACK",font="size4",pre=50)
            i+=1
ghosts_page = OllyPage("125","125")

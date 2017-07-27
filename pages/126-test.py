from page import Page
import datetime

class OllyPage(Page):
    def __init__(self, page_num, numb):
        super(OllyPage, self).__init__(page_num)
        self.title = "Countdown"
        self.in_index = True
        self.index_num = numb


    def generate_content(self):

        self.add_title("Countdowns",fg="BRIGHTWHITE",bg="BLACK")
        twitter = """
-----------
--WWWWWWW--
--WWWWWWW--
-W-------W-
-W---B---W-
-W---B---W-
-W---B---W-
-W---BBB-W-
-W-------W-
-W-------W-
-W-------W-
-W-------W-
-WWWWWWWWW-
--WWWWWWW--
"""
        self.print_image(twitter,0,69)
        self.move_cursor(x=0)

        #self.add_newline()

        ghosts =  [ ["Anna",   datetime.datetime(2017, 8, 31, 16, 0)],
                    ["Rafeal", datetime.datetime(2017,12, 25, 16, 0)],
                    ["Belgin", datetime.datetime(2018, 8, 31, 16, 0)],
                    ["Scroggs",datetime.datetime(2019, 3, 31, 17, 0)], ]

        i = 0
        for ghost in ghosts:
            delta = ghost[1] - datetime.datetime.now()
            hs = delta.seconds/3600
            ds = delta.days

            self.move_cursor(x=0,y=7+4*i)
            self.add_title(ghost[0],bg="WHITE",fg="BLACK",font="size4",pre=10)
            self.move_cursor(x=0,y=7+4*i)
            self.add_title(str(ds),bg="YELLOW",fg="BLACK",font="size4",pre=50)
            i+=1
ghosts_page = OllyPage("996","996")

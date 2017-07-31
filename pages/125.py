from page import Page
import datetime
import random

class OllyPageN(Page):
    def __init__(self, page_num, page_name, numb=None):
        super(OllyPageN, self).__init__(page_num)
        self.title = "Countdowns/Ghosts"
        self.page_name = page_name
        if numb is None:
            self.in_index = False
        else:
            self.in_index = True
            self.index_num = numb


    def generate_content(self):

        self.add_title(self.page_name,fg="BRIGHTWHITE",bg="BLACK")
        ghost = """
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
        clock = """
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

        if self.page_name == "Ghosts":
            self.print_image(ghost,0,69)
        else:
            self.print_image(clock,0,69)
        self.move_cursor(x=0)

        #self.add_newline()

        people = [["Scroggs",datetime.datetime(2019, 3, 22, 17, 0)],
                  ["Belgin", datetime.datetime(2018, 9, 22, 16, 0)],
                  ["Rafeal", datetime.datetime(2017,12, 25, 16, 0)],
                  ["Anna",   datetime.datetime(2017,11, 1,  16, 0)],
                  ["Adam",   datetime.datetime(2017, 6, 20, 17, 0)],
                  ["Mart",   datetime.datetime(2016, 12,19, 17, 0)],
                  ["Huda",   datetime.datetime(2016, 11,25, 17, 0)],
                  ["Sam",    datetime.datetime(2016, 9, 26, 17, 0)],
                  ["Jigsaw", datetime.datetime(2016, 6, 2 , 17, 0)],
                  ["Olly",   datetime.datetime(2016, 6, 2 , 17, 0)],
                  ["Ali",    datetime.datetime(2015, 2, 20, 17, 0)],
                 ]

        ghosts = [person for person in people if (person[1] - datetime.datetime.now()).days < 0]
        alive  = [person for person in people if (person[1] - datetime.datetime.now()).days >= 0]

        if self.page_name == "Ghosts":
            display_list = ghosts
        else:
            display_list = alive

        # Pick 5 from display list
        display_five = random.sample(display_list,min(5,len(display_list)))
        display_five_sorted = sorted(display_five, key=lambda x: abs((x[1] - datetime.datetime.now()).days) )


        i = 0
        for item in display_five_sorted:
            delta = item[1] - datetime.datetime.now()
            #hs = delta.seconds/3600
            ds = delta.days

            self.move_cursor(x=0,y=7+4*i)
            self.add_title(item[0],bg="WHITE",fg="BLACK",font="size4",pre=10)
            self.move_cursor(x=0,y=7+4*i)
            self.add_title(str(abs(ds)),bg="YELLOW",fg="BLACK",font="size4",pre=50)
            i+=1
countdown_page = OllyPageN("125","Countdown","125-126")
ghosts_page = OllyPageN("126","Ghosts")

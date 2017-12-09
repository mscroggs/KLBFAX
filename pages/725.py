from __future__ import division

import os
from page import Page
from ceefax import Ceefax
from random import shuffle
from datetime import datetime

class AdventPage(Page):
    def __init__(self, n):
        super(AdventPage, self).__init__(n)
        self.title = "Advent Calendar"
        if datetime.now().month == 12:
            self.in_index = True
            self.is_enabled = True
        else:
            self.in_index = False
            self.is_enabled = False

    def generate_content(self):
        self.add_title("Advent calendar", font="size4")

        #for i in range(3):
        #    for j in range(7):
        #        self.add_text("xxxxxxxxx "*8)
        #        self.add_newline()
        #    self.add_newline()
        #return

        ls = [
              ( 1,"bwbbwbbbb\nbbbbbwbwb\nbbwbwbbbb\nwbbbbbbwb\nbbwbbbbbw\nbbbbbwbbb\nwwwwwwwww"),
              ( 2,"wwwwwwggw\nwwwwggggw\nwgwgggggw\nwwrrggwww\nwgrrrwwww\nwggwggwww\nwgwwwggww"),
              ( 3,"wwgggggww\nwggrrrggw\nggrrwrrgg\ngrrwwwrrg\nggrrwrrgg\nwggrkrggw\nwwgkgkgww"),
              ( 4,"bbbkwkbbb\nbbbwwwbbb\nkbbbwbbbb\nbkbwkwbkk\nbbwwwwwbb\nbbwwkwwbb\nbbbwwwbbb"),
              ( 5,"kkkkkwwwk\nkkkkkwwwk\nkkkkkrrrk\nkkkkkrrrk\nkkkkkrrrk\nkkkrrrrrk\nkkkkrrrkk"),
              ( 6,"kkkgggkkk\nkkgggggkk\nkkkgggkkk\nkkgggggkk\nkgggggggk\nkkkrrrkkk\nkkkrrrkkk"),
              ( 7,"wwwrrwwww\nwwrrrrwww\nwbbrrbbww\nwbbrrbbww\nwrrrrrrww\nwbbrrbbww\nwbbrrbbww"),
              ( 8,"kkwrrwkkk\nkkwwkwwkk\nkkrwkrwkk\nkkkkkrrkk\nkkkkkwrkk\nkkkkkwwkk\nkkkkkrwkk"),
              ( 9,"kkkkkkkkk\nkkkkkrwwk\nkkkkrrwkk\nkkkrrrkkk\nkkrrrrkkk\nkrrrrrkkk\nkwwwwwkkk"),
              (10,"bbwbwbwbb\nbbwbwbwbb\nwbbwwwbbw\nbwwwwwwwb\nwbbwwwbbw\nbbwbwbwbb\nbbwbwbwbb"),
              (11,"wwwwywwww\nwwwyyywww\nwwyyyyyww\nwwyyyyyww\nwwyyyyyww\nwwyyyyyww\nwyyyyyyyw"),
              (12,"bbbrrrrrw\nbbrrrrrww\nbbwwwwwbb\nbwwkpkwwb\nbwwprpwwb\nbwwwwwwwb\nbbwwwwwbb"),
              (13,"wwwwwwwww\nrwgrrggwr\nrrrrggrrr\nrrrggrrrr\nrrggrrgrr\nrwgrrggwr\nwwwwwwwww"),
              (14,"wwwwwwwww\nwwwkkkwww\nwwkkwkkww\nwwkwowkww\nwwkwwwkww\nwwkwwwkww\nwookkkoow"),
              (15,"kkkggrkkk\nkkwwrggkk\nkwwwwwgwk\nwoowwoowo\noooowoooo\nkoooooook\nkkoooookk"),
              (16,"kkkkkkkkk\nkkkkykkkk\nkkyyyyykk\nkkkyyykkk\nkkyykyykk\nkkkkkkkkk\nkkkkkkkkk"),
              (17,"ykykkkkkk\nyyyookkkk\nkkokokkkk\nkkoooorkk\nooooookkk\noookkkkkk\nookkkkkkk"),
              (18,"kkkoookkk\nkkowowokk\nkkkoookkk\nkooowoook\nkkkoookkk\nkkookookk\nkookkkook"),
              (19,"kkkkokkkk\nkkkkokkkk\nkkkoyokkk\nkkkoyokkk\nkkkkwkkkk\nkkkrrrkkk\nkkkrrrkkk"),
              (20,"bbkkkkkbb\nbkkkkkkkb\nbbwwwwwbb\nbwwkwkwwb\nbwooowwwb\nbwkwwwkwb\nbbwkkkwbb"),
              (21,"bbbbbbwbb\nbwbbbbgbb\nwgwbbwgwb\ngggbbgggb\nwgwbbbgbb\ngggbbbgbb\nwwwwwwwww"),
              (22,"kkyyyyykk\nkyykkkyyk\nkkyyyyykk\nkkkkkkkkk\nkkyyyyykk\nkyypppyyk\nkypkpkpyk"),
              (23,"bkbkkrkrk\nkbkkrkrkr\nbkbkrkkkr\nkgkkkyyyk\ngkgkyykkk\ngggkkkyyk\ngkgkyyykk"),
              (24,"kkkkkkykk\nkkkkkkkkk\nkykkykykk\nykykyroyk\nkyoyryyyy\nkyrrroryk\nkoooooook")
             ]

        colmap = {"b":"BLUE","w":"WHITE","r":"RED","g":"GREEN","k":"BLACK","y":"YELLOW","p":"PINK","o":"ORANGE"}

        now = datetime.now()

        shuffle(ls)
        for number,(a,b) in enumerate(ls):
            if now.month == 12 and now.day >= a:
                open = True
            else:
                open = False
            text = str(a) + " "*80
            row = number // 8
            col = number % 8
            for i,line in enumerate(b.split("\n")):
                self.move_cursor(y=4+row*8+i, x=col*10)
                for j,char in enumerate(line):
                    if open:
                        self.start_bg_color(colmap[char])
                        if char == "w":
                            self.start_fg_color("BLACK")
                    else:
                        self.start_bg_color("GREY")
                    self.add_text(text[9*i+j])
                    self.end_bg_color()
                    if char == "w":
                        self.end_fg_color()

cal = AdventPage("725")


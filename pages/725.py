import os
from re import sub
from page import Page
import colours
from colours import colour_print
from printer import instance as printer
from datetime import datetime

class AdventPage(Page):
    def __init__(self,page_num):#, page_num, station, code, hogwarts=False, to=None):
        super(AdventPage, self).__init__(page_num)
        self.title = "Advent Calendar"
        self.in_index = False
        self.tagline = "Advent Calendar"
        self.refresh()

    def generate_content(self):
        D = colours.Background.DEFAULT + colours.Style.DEFAULT
        B = colours.Background.BLACK + colours.Style.BLINK
        content = colour_print(
            printer.text_to_ascii("ADVENT CALENDAR",fill=False,padding={"left": 8}),
            foreground=colours.Style.BOLD+colours.Foreground.GREEN,
            background=colours.Background.RED) + "\n\n"
        lines = [" "," "," "]
        days_done = 0
        for day in _arrangement:
            d = str(day)
            if len(d)<2:
                d = "0" + d
            if day > self.time:
                lines[0] += B+" "*7
                lines[1] += B+" "*7
                lines[2] += B+" "*5 +d
            else:
                for i in range(3):
                    for j,col in enumerate(_pics[day][i]):
                        lines[i] += _cols[col] + colours.Foreground.BLACK

                        if i==0:
                            lines[i] += _pics[day][3][j]
                        elif i==1 and len(_pics[day])>4:
                            lines[i] += _pics[day][4][j]
                        elif i==2 and j in [5,6]:
                            lines[i] += d[j-5]
                        else:
                            lines[i] += " "
                        lines[i] += D
                    lines[i] += colours.Foreground.DEFAULT
            for i in range(3):
                lines[i] += D+" "*3

            days_done += 1
            if days_done > 6:
                content += "\n".join(lines)+"\n\n"
                days_done = 0
                lines = [" "," "," "]
        content += "\n".join(lines)+"\n\n"
        lines = [" "," "," "]
        
        self.content = content

    def refresh(self):
        time = datetime.now()
        if time.month == 11 or (time.month == 10 and time.date > 25):
            self.in_index = True
            self.is_enabled = True
            if time.month == 11:
                self.time = time.day
            else:
                self.time = 0
        else:
            self.in_index = False
            self.is_enabled = False
            self.time = 0 

_cols = {"B":colours.Background.BLUE,
         "G":colours.Background.GREEN,
         "R":colours.Background.RED,
         "O":colours.Background.YELLOW,
         "L":colours.Background.BLACK+colours.Style.BLINK,
         "Y":colours.Background.YELLOW+colours.Style.BLINK,
         "W":colours.Background.WHITE}


_pics = {1:["BBWBBWB",
            "WBBWBBB",
            "BBBBBWB",
            "   Snow"],
         2:["WWWGWWW",
            "WWGGGWW",
            "WGGGGGW",
            "   Tree"],
         3:["WGRGRGW",
            "WRGWGRW",
            "WGRGRGW",
            " Wreath"],
         4:["BBBBBBB",
            "BBBBBBB",
            "WWWWWWW",
            "  Snowy",
            "  Scene"],
         5:["WWWWWWW",
            "WWWWWWW",
            "WWWWWWW",
            "Heavy  ",
            "   Snow"],
         6:["WWRBRWW",
            "WWBBBWW",
            "WWRBRWW",
            "Present"],
         7:["BBBWBBB",
            "BBWLWBB",
            "BBWWWBB",
            "Snowman"],
         8:["LLLYLLL",
            "LLYYYLL",
            "LLYYYLL",
            "   Star"],
         9:["WWWYWWW",
            "WWWOWWW",
            "WWWOWWW",
            " Candle"],
        10:["WWOOGWW",
            "WWOOOWW",
            "WWOOOWW",
            " Orange"],
        11:["LLWWWLL",
            "LLRRRLL",
            "LRRRRLL",
            "Stockin",
            "      g"],
        12:["RWRRRWR",
            "RRRRRRR",
            "RWRRRWR",
            "Cracker"],
        13:["WWWYYYR",
            "WWYYYOW",
            "WYYORRW",
            "  Robin"],
        14:["BWBWBWB",
            "BBWWWBB",
            "BWBWBWB",
            "Snowfla",
            "     ke"],
        15:["LWGRGWL",
            "LYYYYYL",
            "LYYYYYL",
            "Pudding"],
        16:["WWWWWWW",
            "LRLGLYL",
            "WWWWWWW",
            "  Fairy",
            " Lights"],
        17:["WWYYWWW",
            "WWWYYRW",
            "WYOYYWW",
            "Reindee",
            "      r"],
        18:["WGGWGGW",
            "GGGGGGG",
            "WGGWGGW",
            "  Holly"],
        19:["BBWOWBB",
            "BBLWLBB",
            "BBLLLBB",
            "Penguin"],
        20:["LLLRRWL",
            "LLRRRLL",
            "LLWWWLL",
            "    Hat"],
        21:["WWWWWWW",
            "WWWWWWW",
            "WWWWWWW",
            "V.Heavy",
            "   Snow"],
        22:["LWRWLLL",
            "LRLRLLL",
            "LLLWLLL",
            "  Candy",
            "   Cane"],
        23:["WBBBWBW",
            "WBBBBBW",
            "WWOWWOW",
            "    Toy",
            "  Train"],
        24:["WWRRRWW",
            "WWRRRWW",
            "WWRRRWW",
            " Bauble"],
        25:["WWWOOWW",
            "WWOOOOW",
            "WOOOOWW",
            " Turkey"]
        }

_arrangement = [15, 22, 17, 21, 7, 10, 1, 13, 24, 19, 8, 9, 3, 23, 16, 11, 25, 14, 20, 4, 12, 18, 5, 6, 2]

advent_page = AdventPage("725")

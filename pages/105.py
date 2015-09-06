from page import Page
from colours import colour_print
from printer import instance as printer
from random import choice
from datetime import date
import json
import config
import logging
import sys

birthday_file = config.birthday_file

try:
    with open(birthday_file) as f:
        birthdays = json.load(f)

except IOError as e:
    logging.critical("""Birthday file failed to load. Try running in DEVELOP
                     mode""")
    logging.critical(e)
    sys.exit()


more_birthdays = {
            "Kathleen Lonsdale": (1, 28),
            "Jesus": (12, 25),
            "Jigsaw": (1, 3),
            "ScroggsBot": (1, 10)
}

for birth in more_birthdays:
    birthdays[birth] = more_birthdays[birth]

c_b = {}

months = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

for i in range(1,13):
    c_b[i] = {}

for person in birthdays:
    bp = birthdays[person]
    if bp is not None:
        if bp[1] not in c_b[bp[0]]:
            c_b[bp[0]][bp[1]] = person
        else:
            c_b[bp[0]][bp[1]] += " & " + person

class BdayPage(Page):
    def __init__(self, page_num):
        super(BdayPage, self).__init__(page_num)
        self.title = "Birthdays"

    def generate_content(self):
        R = choice(self.colours.Foreground.list)+self.colours.Style.BOLD
        G = choice(self.colours.Foreground.list)+self.colours.Style.BOLD
        D = self.colours.Foreground.DEFAULT+self.colours.Style.DEFAULT
        prefixes = []
        s_day = date.today().day
        s_mon = date.today().month

        day = s_day
        mon = s_mon

        while True:
            if day == s_day and mon == s_mon:
                if day in c_b[mon]:
                    content = colour_print(printer.text_to_ascii("Happy Birthday"),rainbow=True)+"\n\n"
                    content += colour_print(printer.text_to_ascii(c_b[mon][day]+"!"),rainbow=True)+"\n\n"
                    prefixes += [R+"   .-'\"'-.  "+G+"            "+D]
                    prefixes += [R+"  / #     \ "+G+"            "+D]
                    prefixes += [R+" : #       :"+G+"  .-'\"'-.   "+D]
                    prefixes += [R+"  \       / "+G+" / #     \  "+D]
                    prefixes += [R+"   \     /  "+G+": #       : "+D]
                    prefixes += [R+"    `'q'`   "+G+" \       /  "+D]
                    prefixes += [R+"      (     "+G+"  \     /   "+D]
                    prefixes += [R+"       )    "+G+"   `'p'`    "+D]
                    prefixes += [R+"      (     "+G+"     )      "+D]
                    prefixes += [R+"       )    "+G+"    (       "+D]
                    prefixes += [R+"            "+G+"     )      "+D]
                else:
                    content = colour_print(printer.text_to_ascii("Birthdays"),background=self.colours.Background.BLACK,foreground=self.colours.Foreground.GREEN)+"\n\n"
            elif day in c_b[mon]:
                if len(prefixes)>0:
                    content += prefixes[0]
                    prefixes = prefixes[1:]
                content += self.colours.Background.GREEN + self.colours.Foreground.BLACK
                content += str(day) + " "+months[mon]
                content += self.colours.Background.DEFAULT + self.colours.Foreground.DEFAULT
                content += " "*(15-len(str(day)+months[mon])) + c_b[mon][day]
                content += "\n"
            day += 1
            if day > 31:
                day = 1
                mon += 1
                if mon > 12:
                    mon -= 12
            if mon==s_mon and day==s_day:
                break

        self.content = content

bdaypage = BdayPage("105")

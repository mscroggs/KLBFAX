from page import Page
from colours import colour_print
from printer import instance as printer
from random import choice
import screen
from datetime import date

with open(join(expanduser('~'),'.klb/birthdays.json')) as f:
    birthdays = json.load(f)


more_birthdays = {
            "Kathleen Lonsdale":(1,28),
            "Jesus":(12,25),
            "Jigsaw":(1,3),
            "ScroggsBot":(1,10)
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
    def __init__(self,page_num):
        super(BdayPage, self).__init__(page_num)
        self.title = "Birthdays"
      
    def generate_content(self):

        s_day = date.today().day
        s_mon = date.today().month

        day = s_day
        mon = s_mon

        while True:
            if day == s_day and mon == s_mon:
                if day in c_b[mon]:
                    content = colour_print(printer.text_to_ascii("Happy Birthday"),background=self.colours.Background.BLACK,foreground=self.colours.Foreground.GREEN)+"\n\n"
                    content = colour_print(printer.text_to_ascii(c_b[mon][day]),background=self.colours.Background.BLACK,foreground=self.colours.Foreground.GREEN)+"\n\n"
                else:
                    content = colour_print(printer.text_to_ascii("Birthdays"+),background=self.colours.Background.BLACK,foreground=self.colours.Foreground.GREEN)+"\n\n"
            elif day in c_b[mon]:
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

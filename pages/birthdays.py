from page import Page
from random import choice
import config
from helpers.file_handler import f_read_json

class BdayPage(Page):
    def __init__(self, page_num):
        super(BdayPage, self).__init__(page_num)
        self.title = "Birthdays"
        self.importance = 4

    def background(self):
        birthdays = f_read_json("birthdays.json")
        more_birthdays = {
                    "Kathleen Lonsdale": (1, 28, 1903),
                    "Martin Gardner": (10, 21, 1914),
                    "Jesus": (12, 25, 0),
                    "Jigsaw": (1, 3),
                    "The Queen": (4, 21, 1926),
                    "Keir Starmer" : (9,2, 1962),
                    "Admiral Pocock": (3, 6, 1706),
                    "Papa Bouba Diop": (1, 28, 1978)
        }

        for birth in more_birthdays:
            birthdays[birth] = more_birthdays[birth]

        self.c_b = {}
        self.c_b_age = {}
        self.months = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

        for i in range(1,13):
            self.c_b[i] = {}
            self.c_b_age[i] = {}

        for person, value in sorted(birthdays.items()):
            bp = birthdays[person]
            if bp is not None:
                if bp[1] not in self.c_b[bp[0]]:
                    self.c_b[bp[0]][bp[1]] = person
                    if len(bp)>2:
                        self.c_b_age[bp[0]][bp[1]] = [bp[2]]
                    else:
                        self.c_b_age[bp[0]][bp[1]] = [None]
                else:
                    self.c_b[bp[0]][bp[1]] += ", " + person
                    if len(bp)>2:
                        self.c_b_age[bp[0]][bp[1]].append(bp[2])
                    else:
                        self.c_b_age[bp[0]][bp[1]].append(None)



    def generate_content(self):
        s_day = config.now().day
        s_mon = config.now().month
        s_year = config.now().year

        day = s_day
        mon = s_mon

        ind = 0

        while True:
            if day == s_day and mon == s_mon:
                if day in self.c_b[mon]:
                    self.add_rainbow_title("Happy Birthday")
                    #self.add_newline()
                    y = 8
                    for p, person in enumerate(self.c_b[mon][day].split(", ")):
                        self.move_cursor(y=y,x=0)
                        self.add_title(person,bg="GREEN",fg="BLACK",font="size4",fill=False)
                        self.move_cursor(y=y,x=0)
                        birth_year = self.c_b_age[mon][day][p]
                        if birth_year is not None:
                            age = str(s_year-birth_year)
                        else:
                            age = ""
                        age_length = len(age)*7-age.count("1")*3
                        self.add_title(age,bg="GREEN",fg="BLACK",font="size4bold",fill=False,pre=80-age_length)
                        y = y + 4
                    #self.add_rainbow_title(choice(self.c_b[mon][day].split(" & "))+"!")
                    self.move_cursor(y=y+1,x=0)
                    self.start_random_fg_color()
                    y+=1
                    for i,line in enumerate([
                        "   .-'\"'-.  ",
                        "  / #     \ ",
                        " : #       :",
                        "  \       / ",
                        "   \     /  ",
                        "    `'q'`   ",
                        "      (     ",
                        "       )    ",
                        "      (     ",
                        "       )    "]):
                        self.move_cursor(x=0,y=i+y)
                        self.add_text(line)
                    self.start_random_fg_color()
                    for i,line in enumerate([
                        "  .-'\"'-.   ",
                        " / #     \  ",
                        ": #       : ",
                        " \       /  ",
                        "  \     /   ",
                        "   `'p'`    ",
                        "     )      ",
                        "    (       ",
                        "     )      ",
                        "    (       "]):
                        self.move_cursor(x=60,y=i+y)
                        self.add_text(line)
                    self.end_fg_color()
                    ind = 13
                    self.move_cursor(y=y)

                else:
                    self.add_title("Birthdays",bg="BLACK",fg="GREEN")
                    self.add_newline()
            elif day in self.c_b[mon]:
                self.move_cursor(x=ind)
                self.start_bg_color("GREEN")
                self.start_fg_color("BLACK")
                self.add_text(" " + "%2i"%day + " " + self.months[mon] + " "*(10-len(self.months[mon])))
                self.end_fg_color()
                self.end_bg_color()
                self.move_cursor(x=ind+17)
                self.add_text(self.c_b[mon][day])
                self.add_newline()
            day += 1
            if day > 31:
                day = 1
                mon += 1
                if mon > 12:
                    mon -= 12
            if mon==s_mon and day==s_day:
                break


bdaypage = BdayPage("102")

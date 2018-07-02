import config
from page import Page

class MathOffPage(Page):
    def __init__(self):
        super(MathOffPage, self).__init__("160")
        self.title = "Big Internet Math-Off"
        self.importance = 5

    def background(self):
        self.results = {
                "11":{"start":"1 July","home":"James Tanton","away":"Nira Chamberlain","score":[123,134],"winner":None},
                "12":{"start":"2 July","home":"Samuel Hansen","away":"Paul Taylor","score":[43,46],"winner":None},
                "13":{"start":"3 July","home":"Peter Rowlett","away":"Alison Kiddle","score":None,"winner":None},
                "14":{"start":"4 July","home":"Edmund Harriss","away":"Colin Wright","score":None,"winner":None},
                "15":{"start":"5 July","home":"Tiago Hirth","away":"Evelyn Lamb","score":None,"winner":None},
                "16":{"start":"6 July","home":"Matt Parker","away":"Matthew Scroggs","score":None,"winner":None},
                "17":{"start":"7 July","home":"James Propp","away":"Zoe Griffiths","score":None,"winner":None},
                "18":{"start":"8 July","home":"Jo Morgan","away":"Tony Mann","score":None,"winner":None},

                "q1":{"start":"11 July","home":"11","away":"13","score":None,"winner":None},
                "q2":{"start":"12 July","home":"12","away":"14","score":None,"winner":None},
                "q3":{"start":"13 July","home":"15","away":"17","score":None,"winner":None},
                "q4":{"start":"14 July","home":"16","away":"18","score":None,"winner":None},

                "s1":{"start":"17 July","home":"q1","away":"q3","score":None,"winner":None},
                "s2":{"start":"19 July","home":"q2","away":"q4","score":None,"winner":None},

                "final":{"start":"24 July","home":"s1","away":"s2","score":None,"winner":None},
            }

    def get_winner(self, id):
        if id in self.results:
            if self.results[id]["winner"] is None:
                return self.get_winner(self.results[id]["home"]) + " or " + self.get_winner(self.results[id]["away"])
            else:
                return self.get_winner(self.results[id]["winner"])
        else:
            return id

    def add_match(self, id, width=None):
        if width is None:
            width = config.WIDTH

        home = self.get_winner(self.results[id]["home"])
        away = self.get_winner(self.results[id]["away"])

        self.actual_show(width,
                         home,
                         away,
                         self.results[id]["score"],
                         self.results[id]["winner"],
                         self.results[id]["start"])

    def actual_show(self, width, home, away, score, winner, date, retry=True):
        out = ""
        out += home
        out += " "
        if score is not None:
            out += str(score[0])
            out += "-"
            out += str(score[1])
        else:
            out += date
        out += " "
        out += away

        if len(out) <= width:
            self.add_text(" "*((width-len(out))//2))
            if score is not None and winner is not None and score[0] > score[1]:
                self.add_text(home,fg="GREEN")
            else:
                self.add_text(home)
            self.add_text(" ")
            if score is None:
                self.add_text(date,fg="GREEN")
            elif winner is not None:
                self.add_text(str(score[0])+"-"+str(score[1]))
            else:
                self.add_text(str(score[0])+"-"+str(score[1]),fg="YELLOW")
            self.add_text(" ")
            if score is not None and winner is not None and score[0] < score[1]:
                self.add_text(away,fg="GREEN")
            else:
                self.add_text(away)
            self.add_text(" "*((width-len(out))//2))
        elif retry:
            self.actual_show(width, "???", "???", score, winner, date, True)

    def generate_content(self):
        self.add_title("Big Internet Math-Off")

        self.add_text(" "*(config.WIDTH//2-4) +  "Round 1",fg="YELLOW")

        self.add_newline()
        self.add_match("11", config.WIDTH//2)
        self.add_match("12", config.WIDTH//2)
        self.add_newline()
        self.add_match("13", config.WIDTH//2)
        self.add_match("14", config.WIDTH//2)
        self.add_newline()
        self.add_match("15", config.WIDTH//2)
        self.add_match("16", config.WIDTH//2)
        self.add_newline()
        self.add_match("17", config.WIDTH//2)
        self.add_match("18", config.WIDTH//2)

        self.add_newline()
        self.add_newline()

        self.add_text(" "*(config.WIDTH//2-7) +  "Quarter Finals",fg="YELLOW")
        self.add_newline()
        self.add_match("q1")
        self.add_newline()
        self.add_match("q2")
        self.add_newline()
        self.add_match("q3")
        self.add_newline()
        self.add_match("q4")

        self.add_newline()
        self.add_newline()

        self.add_text(" "*(config.WIDTH//2-5) +  "Semi Finals",fg="YELLOW")
        self.add_newline()
        self.add_match("s1")
        self.add_newline()
        self.add_match("s2")

        self.add_newline()
        self.add_newline()

        self.add_text(" "*(config.WIDTH//2-3) +  "Final",fg="YELLOW")
        self.add_newline()
        self.add_match("final")



page = MathOffPage()

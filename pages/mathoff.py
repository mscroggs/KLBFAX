import config
from page import Page
from helpers.url_handler import load_json

class MathOffPage(Page):
    def __init__(self):
        super(MathOffPage, self).__init__("148")
        self.title = "Big Internet Math-Off"
        self.in_index=False
        self.importance = 3

    def background(self):
        self.results = {
                "11":{"start":"1 July","home":"James Tanton","away":"Nira Chamberlain","score":[144,203],"winner":"Nira Chamberlain"},
                "12":{"start":"2 July","home":"Samuel Hansen","away":"Paul Taylor","score":[99,112],"winner":"Paul Taylor"},
                "13":{"start":"3 July","home":"Peter Rowlett","away":"Alison Kiddle","score":[85,104],"winner":"Alison Kiddle"},
                "14":{"start":"4 July","home":"Edmund Harriss","away":"Colin Wright","score":[544,334],"winner":"Edmund Harriss"},
                "15":{"start":"5 July","home":"Tiago Hirth","away":"Evelyn Lamb","score":[77,112],"winner":"Evelyn Lamb"},
                "16":{"start":"6 July","home":"Matt Parker","away":"Matthew Scroggs","score":[364,208],"winner":"Matt Parker"},
                "17":{"start":"7 July","home":"Jim Propp","away":"Zoe Griffiths","score":[47,119],"winner":"Zoe Griffiths"},
                "18":{"start":"8 July","home":"Jo Morgan","away":"Tony Mann","score":[214,132],"winner":"Jo Morgan"},

                "q1":{"start":"11 July","home":"11","away":"13","score":[193,173],"winner":"11"},
                "q2":{"start":"12 July","home":"12","away":"14","score":[86,237],"winner":"14"},
                "q3":{"start":"13 July","home":"15","away":"17","score":[80,124],"winner":"17"},
                "q4":{"start":"14 July","home":"16","away":"18","score":[248,177],"winner":"16"},

                "s1":{"start":"17 July","home":"q1","away":"q3","score":[513,504],"winner":"q1"},
                "s2":{"start":"19 July","home":"q2","away":"q4","score":[1128,1254],"winner":"q4"},

                "final":{"start":"24 July","home":"s1","away":"s2","score":[1207,960],"winner":"s1"},
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

    def actual_show(self, width, home, away, score, winner, date):
        half = width//2 - 4
        if len(home) > half:
            if home != "???":
                self.actual_show(width, "???", away, score, winner, date)
            return
        if len(away) > half:
            if away != "???":
                self.actual_show(width, home, "???", score, winner, date)
            return

        self.add_text(" "*(half-len(home)-1))
        if score is not None and winner is not None and score[0] > score[1]:
            self.add_text(home,fg="GREEN")
        else:
            self.add_text(home)
        self.add_text(" ")

        display_score = ""


        if score is None:
            display_score = date
        else:
            display_score = str(score[0])+"-"+str(score[1])
        extra = 7-len(display_score)
        extra1 = extra//2
        extra2 = extra-extra1
        self.add_text(" "*extra1)
        if score is None:
            self.add_text(display_score,fg="GREEN")
        elif winner is not None:
            self.add_text(display_score)
        else:
            self.add_text(display_score,fg="YELLOW")
        self.add_text(" "*extra2)
        self.add_text(" ")

        if score is not None and winner is not None and score[0] < score[1]:
            self.add_text(away,fg="GREEN")
        else:
            self.add_text(away)
        self.add_text(" "*(half-len(away)))

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


class TwitterPage(Page):
    def __init__(self, page_num):
        super(TwitterPage, self).__init__(page_num)
        self.in_index=False
        self.title = "#bigmathoff"

    def background(self):
        pass

    def generate_content(self):
        from helpers import tweet_handler

        self.add_title("#bigmathoff")
        try:
            results = tweet_handler.search("#bigmathoff")
        except tweet_handler.NoTwitter:
            self.add_text("Twitter login failed...")
            return


        for tweet in results:
            if "retweeted_status" not in tweet:
                self.add_text("@" + tweet["user"]["screen_name"] + " ", fg="YELLOW")
                self.add_text(" ".join(tweet["user"]["created_at"].split(" ")[:4]), fg="BLUE")
                self.add_newline()
                text = tweet["text"]
                while "http" in text:
                    tsp = text.split("http",1)
                    text = tsp[0] + "<url>"
                    if " " in tsp[1]:
                        text += tsp[1].split(" ",1)[1]
                self.add_wrapped_text(text)
                self.add_newline()
                self.add_newline()

tpage = TwitterPage("149")


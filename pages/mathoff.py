import config
from page import Page
from helpers.url_handler import load_json

class MathOffPage(Page):
    def __init__(self):
        super(MathOffPage, self).__init__("160")
        self.title = "Big Internet Math-Off"
        self.importance = 5

    def background(self):
        self.results = {
                "11":{"start":"1 July","home":"James Tanton","away":"Nira Chamberlain","score":None,"winner":None},
                "12":{"start":"2 July","home":"Samuel Hansen","away":"Paul Taylor","score":None,"winner":None},
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
        for match, id in [("11","3"),("12","5"),("13","4"),("14","6"),("15","7"),("16","8"),("17","9"),("18","10"),
                          ("q1","11"),("q2","12"),("q3","13"),("q4","14"),
                          ("s1","15"),("s2","16"),
                          ("final","17")]:
            if self.results[match]["winner"] is None or self.results[match]["score"] is None or sum(self.results[match]["score"])==0:
                try:
                    data = load_json("http://aperiodical.com/wp-json/wp-polls/v2/results/"+id)
                    if "totalvotes" in data:
                        self.results[match]["score"] = [0,0]
                        for score in data["answers"]:
                            if self.get_winner(self.results[match]["home"]) in score["text"]:
                                self.results[match]["score"][0] = score["votes"]
                            else:
                                self.results[match]["score"][1] = score["votes"]
                        if not data["active"]:
                            if self.results[match]["score"][0] > self.results[match]["score"][1]:
                                self.results[match]["winner"] = self.results[match]["home"]
                            else:
                                self.results[match]["winner"] = self.results[match]["away"]
                except:
                    pass

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


from page import Page

class TwitterPage(Page):
    def __init__(self, page_num):
        super(TwitterPage, self).__init__(page_num)
        self.importance = 5
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

tpage = TwitterPage("161")

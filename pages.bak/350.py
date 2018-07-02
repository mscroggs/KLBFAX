from page import Page
import time
import url_handler

class LotteryPage(Page):
    def __init__(self):
        super(LotteryPage, self).__init__("350")
        self.title = "National Lottery"
        self.tagline = "Don't live a little, live a Lotto"

    def background(self):
        req = url_handler.load('https://www.national-lottery.co.uk/results/lotto/draw-history/csv')
        self.results = req.replace("\n",",").split(",")

    def generate_content(self):
        self.add_title("lottery")

        draw_date = time.strftime("%a %-d %b",time.strptime(self.results[12],"%d-%b-%Y"))
        balls = map(str,sorted(map(int,self.results[13:19])))
        bonus_ball = self.results[19]
        ball_set = self.results[20]
        machine = self.results[21]

        self.add_title(draw_date, bg="YELLOW",fg="BLACK",font="size4",fill=False)

        bg = "YELLOW"
        for i,b in enumerate(balls):
            self.move_cursor(x=0,y=12)
            self.add_title(b, bg=bg,fg="BLACK",font="size4",fill=False,pre=10*i)
            if bg == "YELLOW":
                bg = "CYAN"
            else:
                bg = "YELLOW"
        self.add_title(bonus_ball, bg="RED",fg="BLACK",font="size4",fill=False,pre=60)

        self.add_title(machine+" Set "+ball_set, bg="CYAN",fg="BLACK",font="size4",fill=False)

lottery_page = LotteryPage()

from page import Page
import time


class LotteryPage(Page):
    def __init__(self):
        super(LotteryPage, self).__init__("555")
        self.title = "National Lottery"
        self.tagline = "Don't live a little, live a Lotto"

    def background(self):
        import urllib2

        req = urllib2.urlopen('https://www.national-lottery.co.uk/results/lotto/draw-history/csv')
        self.results = req.read().replace("\n",",").split(",")

    def generate_content(self):
        self.add_title("lottery")

        draw_date = time.strftime("%a %-d %b",time.strptime(self.results[12],"%d-%b-%Y"))
        balls = map(str,sorted(map(int,self.results[13:19])))
        bonus_ball = self.results[19]
        ball_set = self.results[20]
        machine = self.results[21]

        self.add_title(draw_date, bg="YELLOW",fg="BLACK",font="size4",fill=False)

        self.move_cursor(x=0,y=12)
        self.add_title(balls[0], bg="YELLOW",fg="BLACK",font="size4",fill=False,pre=0)
        self.move_cursor(x=0,y=12)
        self.add_title(balls[1], bg="CYAN",fg="BLACK",font="size4",fill=False,pre=10)
        self.move_cursor(x=0,y=12)
        self.add_title(balls[2], bg="YELLOW",fg="BLACK",font="size4",fill=False,pre=20)
        self.move_cursor(x=0,y=12)
        self.add_title(balls[3], bg="CYAN",fg="BLACK",font="size4",fill=False,pre=30)
        self.move_cursor(x=0,y=12)
        self.add_title(balls[4], bg="YELLOW",fg="BLACK",font="size4",fill=False,pre=40)
        self.move_cursor(x=0,y=12)
        self.add_title(balls[5], bg="CYAN",fg="BLACK",font="size4",fill=False,pre=50)
        self.move_cursor(x=0,y=12)
        self.add_title(bonus_ball, bg="RED",fg="BLACK",font="size4",fill=False,pre=60)

        self.add_title(machine+" Set "+ball_set, bg="CYAN",fg="BLACK",font="size4",fill=False)

lottery_page = LotteryPage()

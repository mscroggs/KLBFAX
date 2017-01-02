import os
from page import Page
import time
from config import now
from math import cos,sin,floor,pi
from random import choice

class TimePage(Page):
    def __init__(self):
        super(TimePage, self).__init__("400")
        self.title = "KLB Mean Time"
        self.tagline = "KLB Mean Time"

    def generate_content(self,debug=False):
        from file_handler import load_file
        clock = load_file("clock.txt").split("\n")
        clock = [[j=="X" for j in i] for i in clock]
        minute = [[False]*len(i) for i in clock]
        hour   = [[False]*len(i) for i in clock]
        
        current_minute = float(now().strftime("%M"))
        current_hour = float(now().strftime("%I"))
        current_weekday = now().strftime("%a")
        if current_weekday == "Mon": bgcolor = "LIGHTRED"
        if current_weekday == "Tue": bgcolor = "YELLOW"
        if current_weekday == "Wed": bgcolor = "LIGHTCYAN"
        if current_weekday == "Thu": bgcolor = "LIGHTGREEN"
        if current_weekday == "Fri": bgcolor = "PINK"
        if current_weekday == "Sat": bgcolor = "LIGHTBLUE"
        if current_weekday == "Sun": bgcolor = "RED"
        self.add_title(now().strftime("%A %-d %b"),bg=bgcolor,fg="BLACK")
    
        circle_radius = 19
        screen_radius = 19

        d = .3
        num_points = 25
        current_hourtopointat = current_hour + current_minute/60.

        for a in range(0,num_points+1):
            r = circle_radius*a*.5/num_points
            hx = r*cos(pi/2 - current_hourtopointat*2*pi/12)
            hy = r*sin(pi/2 - current_hourtopointat*2*pi/12)
            for dx in [-d,d]:
                for dy in [-d,d]:
                    hour_x = screen_radius + int(floor(hx+.5+dx))
                    hour_y = screen_radius - int(floor(hy+.5+dy))
                    hour[hour_y][hour_x] = True
            r = circle_radius*a*.8/num_points
            mx = r*cos(pi/2 - current_minute*2*pi/60)
            my = r*sin(pi/2 - current_minute*2*pi/60)
            for dx in [-d,d]:
                for dy in [-d,d]:
                    minute_x = screen_radius + int(floor(mx+.5+dx))
                    minute_y = screen_radius - int(floor(my+.5+dy))
                    minute[minute_y][minute_x] = True
        
        output = ""
        for y in range(0, 2*screen_radius+1):
            for x in range(0, 2*screen_radius+1):
                if clock[y][x] or minute[y][x] or hour[y][x]:
                    output += "X"
                else:
                    output += " "
        output = output + " "*(2*screen_radius + 1)
        output2 = ""
        for y in range(0, 2*screen_radius+1, 2):
            output2 = output2 + " "*(screen_radius+1)      
            for x in range(0, 2*screen_radius+1):
                letter0 = output[y*(2*screen_radius+1)+x]
                letter1 = output[(y+1)*(2*screen_radius+1)+x]
                if letter0 == " " and letter1 == " ":
                    output2 = output2 + " "
                elif letter0 == "X" and letter1 == "X":
                    output2 = output2 + u"\u2588"
                elif letter0 == "X" and letter1 == " ":
                    output2 = output2 + u"\u2580"
                else:
                    output2 = output2 + u"\u2584"
            if y != 2*screen_radius: output2 = output2 + "\n"
        self.add_text(output2)

currency_page = TimePage()

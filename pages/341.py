#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
from pytz import timezone
import config

class WorldClockPage(Page):
    def __init__(self):
        super(WorldClockPage, self).__init__("341")
        self.title = "Time"
        self.index_num = "421"
        self.in_index = False
        self.tagline = "It's 5 o'clock somewhere"

    def generate_content(self):
        self.add_title("World clock")

        zones = ["LA","NY|","GB","FR|","ET|","CN|","JP","ML"]
        times = [config.now().astimezone(timezone('America/Los_Angeles')).strftime("%H:%M"),
                config.now().astimezone(timezone('America/New_York')).strftime("%H:%M"),
                config.now().astimezone(timezone('Europe/London')).strftime("%H:%M"),
                config.now().astimezone(timezone('Europe/Paris')).strftime("%H:%M"),
                config.now().astimezone(timezone('Europe/Moscow')).strftime("%H:%M"),
                config.now().astimezone(timezone('Asia/Shanghai')).strftime("%H:%M"),
                config.now().astimezone(timezone('Asia/Tokyo')).strftime("%H:%M"),
                config.now().astimezone(timezone('Australia/Melbourne')).strftime("%H:%M")]

        for i in range(4):
            color1 = ["YELLOW","LIGHTCYAN"][i%2]
            color2 = ["YELLOW","LIGHTCYAN"][(i+1)%2]
            self.move_cursor(x=0, y=8+4*i)
            self.add_title(zones[2*i],font="size4", bg=color1, fg="BLACK", pre=0, fill=False)
            self.move_cursor(x=0, y=8+4*i)
            self.add_title(times[2*i],font="size4", fg=color1, bg="BLACK", pre=14,fill=False)
            self.move_cursor(x=0, y=8+4*i)
            self.add_title(zones[2*i+1],font="size4", bg=color2, fg="BLACK", pre=40, fill=False)
            self.move_cursor(x=0, y=8+4*i)
            self.add_title(times[2*i+1],font="size4", fg=color2, bg="BLACK", pre=54,fill=False)

clock_page = WorldClockPage()

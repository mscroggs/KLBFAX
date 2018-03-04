#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
from helpers import url_handler

class WorldTempPage(Page):
    def __init__(self):
        super(WorldTempPage, self).__init__("325")
        self.title = "World Temperature"
        self.in_index = False
        self.tagline = "Why exactly do we live in Britain?"

    def background(self):
        self.data = url_handler.load_json("http://api.openweathermap.org/data/2.5/group?id=5368361,5128638,3530597,2643743,2968815,2950158,3169070,344979,1820906,1816670,1850147,7839805&units=metric&appid=05f6b7c72cd541dd510d7bc08f6a8bb0")

    def generate_content(self):
        self.add_title("World Temperature", bg="CYAN", fg="MAGENTA")

        zones = ["LA","NY","MX","LO","PA","BE|","RO","AA","BN|","BJ","TK|","ML"]
        temps = ['50' for i in range(12)]

        i = 0
        for city in self.data['list']:
            temps[i] = str(int(round(city['main']['temp'])))
            i+=1


        for i in range(4):
            color = ['','','']
            for j in range(3):
                if int(temps[3*i+j]) <= 0:
                    color[j] = "CYAN"
                elif 0 < int(temps[3*i+j]) < 10:
                    color[j] = "LIGHTGREEN"
                elif 10 <= int(temps[3*i+j]) < 20:
                    color[j] = "YELLOW"
                elif 10 <= int(temps[3*i+j]) < 30:
                    color[j] = "ORANGE"
                else:
                    color[j] = "LIGHTRED"

            self.move_cursor(x=0,y=8+4*i)
            self.add_title(zones[3*i],  font="size4", fg="BLACK", bg=color[0], fill=False, pre=1)
            self.move_cursor(x=0,y=8+4*i)
            self.add_title(temps[3*i],  font="size4", bg="BLACK", fg=color[0], fill=False, pre=13)
            self.move_cursor(x=0,y=8+4*i)
            self.add_title(zones[3*i+1],font="size4", fg="BLACK", bg=color[1], fill=False, pre=27)
            self.move_cursor(x=0,y=8+4*i)
            self.add_title(temps[3*i+1],font="size4", bg="BLACK", fg=color[1], fill=False, pre=39)
            self.move_cursor(x=0,y=8+4*i)
            self.add_title(zones[3*i+2],font="size4", fg="BLACK", bg=color[2], fill=False, pre=54)
            self.move_cursor(x=0,y=8+4*i)
            self.add_title(temps[3*i+2],font="size4", bg="BLACK", fg=color[2], fill=False, pre=67)

worldtemp_page = WorldTempPage()

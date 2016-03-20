#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from page import Page
from printer import instance as printer
from printer import size4_instance as size4_printer
from colours import colour_print
from datetime import datetime
from pytz import timezone
import pytz


class WorldTempPage(Page):
    def __init__(self, page_num):
        super(WorldTempPage, self).__init__(page_num)
        self.title = "World Temperature"

    def generate_content(self):
        import urllib2, json
        
        url = "http://api.openweathermap.org/data/2.5/group?id=5368361,5128638,3530597,2643743,2968815,2950158,3169070,344979,1820906,1816670,1850147,7839805&units=metric&appid=b1b15e88fa797225412429c1c50c122a"
        response = urllib2.urlopen(url)
        data = json.load(response)        
        
        def pad_number(number):
            zero_pad = ""
            if int(number) < 10 and int(number)>= 0:
                zero_pad = "|"*5
            
            return zero_pad + "|"*2*number.count("1") + "|"*2*number.count("-") + number
        
        
        tag = "Why exactly do we live in Britain?"
        content = colour_print(printer.text_to_ascii("World Temperature"),
                            self.colours.Background.CYAN, self.colours.Foreground.MAGENTA)

        zones = ["LA","NY","MX","LO","PA","BE|","RO","AA","BN|","BJ","TK|","ML"]
        temps = ['50' for i in range(12)]    

        i = 0
        for city in data['list']:
            temps[i] = str(int(round(city['main']['temp'])))
            i+=1
        

        content += "\n\n"
        for i in range(4):
            color1 = [self.colours.Background.YELLOW+self.colours.Style.BLINK,self.colours.Background.YELLOW][i%2]
            color2 = [self.colours.Background.YELLOW+self.colours.Style.BLINK,self.colours.Background.YELLOW][(i+1)%2]
            bcolor1 = [self.colours.Foreground.YELLOW+self.colours.Style.BOLD,self.colours.Foreground.YELLOW][i%2]
            bcolor2 = [self.colours.Foreground.YELLOW+self.colours.Style.BOLD,self.colours.Foreground.YELLOW][(i+1)%2]            
            content += self.colours.colour_print_join([
                            (size4_printer.text_to_ascii(zones[3*i]+"",False)+"",
                                color1,
                                self.colours.Foreground.BLACK),
                            (size4_printer.text_to_ascii(pad_number(temps[3*i]),False)+"  ",
                                self.colours.Background.BLACK,
                                bcolor1),
                            (size4_printer.text_to_ascii(zones[3*i+1]+"",False)+"",
                                color2,
                                self.colours.Foreground.BLACK),
                            (size4_printer.text_to_ascii(pad_number(temps[3*i+1]),False)+"  ",
                                self.colours.Background.BLACK,
                                bcolor2),
                            (size4_printer.text_to_ascii(zones[3*i+2]+"",False)+"",
                                color1,
                                self.colours.Foreground.BLACK),
                            (size4_printer.text_to_ascii(pad_number(temps[3*i+2]),False)+"",
                                self.colours.Background.BLACK,
                                bcolor1)                                
                        ]," "," ")     
            content += "\n"
                    
        content += "\n"
        
        self.content = content
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
worldtemp_page = WorldTempPage(page_number)

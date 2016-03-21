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
            fcolor = ['','','']
            bcolor = ['','','']
            for j in range(3):
                if int(temps[3*i+j]) <= 0:
                    fcolor[j] = self.colours.Background.CYAN+self.colours.Style.BLINK
                    bcolor[j] = self.colours.Foreground.CYAN+self.colours.Style.BOLD            
                elif 0 < int(temps[3*i+j]) < 10:
                    fcolor[j] = self.colours.Background.GREEN+self.colours.Style.BLINK
                    bcolor[j] = self.colours.Foreground.GREEN+self.colours.Style.BOLD            
                elif 10 <= int(temps[3*i+j]) < 20:
                    fcolor[j] = self.colours.Background.YELLOW+self.colours.Style.BLINK
                    bcolor[j] = self.colours.Foreground.YELLOW+self.colours.Style.BOLD
                elif 10 <= int(temps[3*i+j]) < 30:
                    fcolor[j] = self.colours.Background.YELLOW
                    bcolor[j] = self.colours.Foreground.YELLOW
                else:
                    fcolor[j] = self.colours.Background.RED+self.colours.Style.BLINK
                    bcolor[j] = self.colours.Foreground.RED+self.colours.Style.BOLD
                       
            content += self.colours.colour_print_join([
                            (size4_printer.text_to_ascii(zones[3*i]+"",False)+"",
                                fcolor[0],
                                self.colours.Foreground.BLACK),
                            (size4_printer.text_to_ascii(pad_number(temps[3*i]),False)+"  ",
                                self.colours.Background.BLACK,
                                bcolor[0]),
                            (size4_printer.text_to_ascii(zones[3*i+1]+"",False)+"",
                                fcolor[1],
                                self.colours.Foreground.BLACK),
                            (size4_printer.text_to_ascii(pad_number(temps[3*i+1]),False)+"  ",
                                self.colours.Background.BLACK,
                                bcolor[1]),
                            (size4_printer.text_to_ascii(zones[3*i+2]+"",False)+"",
                                fcolor[2],
                                self.colours.Foreground.BLACK),
                            (size4_printer.text_to_ascii(pad_number(temps[3*i+2]),False)+"",
                                self.colours.Background.BLACK,
                                bcolor[2])                                
                        ]," "," ")     
            content += "\n"
                    
        content += "\n"
        
        self.content = content
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
worldtemp_page = WorldTempPage(page_number)

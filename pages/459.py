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


class WorldClockPage(Page):
    def __init__(self, page_num):
        super(WorldClockPage, self).__init__(page_num)
        self.title = "World Clock"

    def generate_content(self):
        import urllib2
        tag = "It's 5 o'clock somewhere"
        content = colour_print(printer.text_to_ascii("World clock")) 

        zones = ["LA","NY|","GB","FR|","ET|","CN|","JP","ML"]
        times = [datetime.now(pytz.utc).astimezone(timezone('America/Los_Angeles')).strftime("%H:%M"),
                datetime.now(pytz.utc).astimezone(timezone('America/New_York')).strftime("%H:%M"),
                datetime.now(pytz.utc).astimezone(timezone('Europe/London')).strftime("%H:%M"),
                datetime.now(pytz.utc).astimezone(timezone('Europe/Paris')).strftime("%H:%M"),
                datetime.now(pytz.utc).astimezone(timezone('Europe/Moscow')).strftime("%H:%M"),
                datetime.now(pytz.utc).astimezone(timezone('Asia/Shanghai')).strftime("%H:%M"),
                datetime.now(pytz.utc).astimezone(timezone('Asia/Tokyo')).strftime("%H:%M"),
                datetime.now(pytz.utc).astimezone(timezone('Australia/Melbourne')).strftime("%H:%M")]       

        content += "\n\n"
        for i in range(4):
            color1 = [self.colours.Background.YELLOW+self.colours.Style.BLINK,self.colours.Background.CYAN+self.colours.Style.BLINK][i%2]
            color2 = [self.colours.Background.YELLOW+self.colours.Style.BLINK,self.colours.Background.CYAN+self.colours.Style.BLINK][(i+1)%2]
            bcolor1 = [self.colours.Foreground.YELLOW+self.colours.Style.BOLD,self.colours.Foreground.CYAN+self.colours.Style.BOLD][i%2]
            bcolor2 = [self.colours.Foreground.YELLOW+self.colours.Style.BOLD,self.colours.Foreground.CYAN+self.colours.Style.BOLD][(i+1)%2]            
            content += self.colours.colour_print_join([
                            (size4_printer.text_to_ascii(zones[2*i]+"",False)+"",
                                color1,
                                self.colours.Foreground.BLACK),
                            (size4_printer.text_to_ascii("|"*2*times[2*i].count("1")+times[2*i],False)+"    ",
                                self.colours.Background.BLACK,
                                bcolor1),
                            (size4_printer.text_to_ascii(zones[2*i+1]+"",False)+"",
                                color2,
                                self.colours.Foreground.BLACK),
                            (size4_printer.text_to_ascii("|"*2*times[2*i+1].count("1")+times[2*i+1],False)+"",
                                self.colours.Background.BLACK,
                                bcolor2)                                  
                        ]," "," ")     
            content += "\n"
                    
        content += "\n"
        
        self.content = content
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
currency_page = WorldClockPage(page_number)

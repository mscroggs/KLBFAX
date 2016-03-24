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


class UKTempPage(Page):
    def __init__(self, page_num):
        super(UKTempPage, self).__init__(page_num)
        self.title = "UK Temperature"

    def generate_content(self):
        import urllib2, json
        '''
        url = "http://api.openweathermap.org/data/2.5/group?id=5368361,5128638,3530597,2643743,2968815,2950158,3169070,344979,1820906,1816670,1850147,7839805&units=metric&appid=b1b15e88fa797225412429c1c50c122a"
        response = urllib2.urlopen(url)
        data = json.load(response)        
        
        def pad_number(number):
            zero_pad = ""
            if int(number) < 10 and int(number)>= 0:
                zero_pad = "|"*5
            
            return zero_pad + "|"*2*number.count("1") + "|"*2*number.count("-") + number
        '''
        
        tag = "Why exactly do we live in Britain?"
        content = colour_print(printer.text_to_ascii("UK Temperature"),
                            self.colours.Background.CYAN, self.colours.Foreground.MAGENTA)
        
        uk_map = '''                                   F"  4$$$$P"
                                    r *$$$$$".c...
                                    %-4$$$$$$$$$$"
                                     J$*$$$$$$$$P
                                    ^r4$$$$$$$$"
                                      *f*$$$$*"
                                    ".4 *$$$$$$$$.
                              4eee%.e   .$$$$$$$$$$r
                            4$$$$$$$$b  P$**)$$$$$$b
                         e..4$$$$$$$$$"     $$$$$$$$c.
                         3$$$$$$$$$$*"   "  ^"$$$$$$$$c
                        *$$$$$$$$$$$.        *$$$$$$$$$.
                         ..$$$$$$$$$L    c ..J$$$$$$$$$b
                         d"$$$$$$$$$F   .@$$$$$$$$$$$$$P"..
                      ..$$$$$$$$$$$$      d$$$$$$$$$$$$$$$$$
                      =$$$$$$$$P"" "    .e$$$$$$$$$$$$$$$$$$
                         *""          $**$$$$$$$$$$$$$$$$*
                                          "".$$$$$$$$$$$C .
                                       .z$$$$$$$$$$$$$$$$""
                                      .$$$$*"^**"  "    
        '''
        
        # Map goes from 58.6725 N to  49.95 and -10.454521 (W) to 1.766667 E
        height_chars = 20
        width_chars = 38
        min_lat = 49.95
        max_lat = 57.827
        min_lon = -10.454521
        max_lon = 1.766667
        
        lats = [min_lat + i*(max_lat-min_lat)/(height_chars-1) for i in range(height_chars)]
        lons = [min_lon + i*(max_lon-min_lon)/(width_chars-1) for i in range(width_chars)]
        
        
        
        uk_map = uk_map.replace("$",u"█")
        uk_map = uk_map.replace("@",u"█")
        uk_map = uk_map.replace("%",u"█")
        uk_map = uk_map.replace("3",u"█")
        uk_map = uk_map.replace("\"",u"▀")
        uk_map = uk_map.replace("*",u"▀")
        uk_map = uk_map.replace("F",u"▀")
        uk_map = uk_map.replace("f",u"█")
        uk_map = uk_map.replace("^",u"▀")
        uk_map = uk_map.replace("P",u"▀")
        uk_map = uk_map.replace("4",u"█")
        uk_map = uk_map.replace("C",u"█")
        uk_map = uk_map.replace("b",u"█")
        uk_map = uk_map.replace("d",u"▄")
        uk_map = uk_map.replace("r",u"▄")
        uk_map = uk_map.replace("=",u"▄")
        uk_map = uk_map.replace("c",u"▄")
        uk_map = uk_map.replace("e",u"▄")
        uk_map = uk_map.replace("L",u"▄")
        uk_map = uk_map.replace("z",u"▄")
        uk_map = uk_map.replace(".",u"▄")
        uk_map = uk_map.replace("J","")
        uk_map = uk_map.replace(")","")
        uk_map = uk_map.replace("-","")
        try:
            with open("uk_coordinate_ids.txt") as f:
                ordered_ids = [line.rstrip('\n') for line in f]
        except:
            with open("/home/pi/ceefax/uk_coordinate_ids.txt") as f:
                ordered_ids = [line.rstrip('\n') for line in f]
          
        temps = [99 for i in range(len(ordered_ids))]
        i = 0
              
        url = "http://api.openweathermap.org/data/2.5/group?id=" + ",".join(ordered_ids[0:100]) + "&units=metric&appid=05f6b7c72cd541dd510d7bc08f6a8bb0"
        response = urllib2.urlopen(url)
        data = json.load(response)   
        for city in data['list']:
            temps[i] = float(city['main']['temp'])
            i+=1
        url = "http://api.openweathermap.org/data/2.5/group?id=" + ",".join(ordered_ids[100:200]) + "&units=metric&appid=05f6b7c72cd541dd510d7bc08f6a8bb0"
        response = urllib2.urlopen(url)
        data = json.load(response)   
        for city in data['list']:
            temps[i] = float(city['main']['temp'])
            i+=1 
        url = "http://api.openweathermap.org/data/2.5/group?id=" + ",".join(ordered_ids[200:300]) + "&units=metric&appid=05f6b7c72cd541dd510d7bc08f6a8bb0"
        response = urllib2.urlopen(url)
        data = json.load(response)   
        for city in data['list']:
            temps[i] = float(city['main']['temp'])
            i+=1 
        url = "http://api.openweathermap.org/data/2.5/group?id=" + ",".join(ordered_ids[300:]) + "&units=metric&appid=05f6b7c72cd541dd510d7bc08f6a8bb0"
        response = urllib2.urlopen(url)
        data = json.load(response)   
        for city in data['list']:
            temps[i] = float(city['main']['temp'])
            i+=1    
            
        ordered_temps = sorted(temps)
        #boundaries = [ordered_temps[int((len(ordered_ids)-1)*(n/6.))] for n in range(6)]
        boundaries = [-99,0,3,6,9,12,15,18,21,24]
        colours_before = [self.colours.Style.DEFAULT+self.colours.Foreground.BLUE,
                            self.colours.Foreground.BLUE+self.colours.Style.BOLD,
                            self.colours.Foreground.CYAN+self.colours.Style.BOLD,
                            self.colours.Style.DEFAULT+self.colours.Foreground.CYAN,
                            self.colours.Style.DEFAULT+self.colours.Foreground.GREEN,
                            self.colours.Foreground.GREEN+self.colours.Style.BOLD,
                            self.colours.Foreground.YELLOW+self.colours.Style.BOLD,
                            self.colours.Style.DEFAULT+self.colours.Foreground.YELLOW,
                            self.colours.Foreground.RED+self.colours.Style.BOLD,
                            self.colours.Style.DEFAULT+self.colours.Foreground.RED]
        clear_colour = self.colours.Foreground.DEFAULT
        i = 0
        coloured_map = ''
        for char in uk_map:
            color = ''
            if (char != ' ' and char != "\n"):
                j = 0
                for b in boundaries:
                    if temps[i] >= b:
                        color = colours_before[j]
                    j+=1
                i+=1
            coloured_map = coloured_map + color + char

        scale = [colours_before[-1]+"Hottest"+clear_colour]
        for i in reversed(colours_before):
            scale.append(i+u"█"*7+clear_colour)
        scale.append(colours_before[0]+"Coldest"+clear_colour)

        map_with_scale = ""
        for i,line in enumerate(coloured_map.split("\n")):
            if i<len(scale):
                map_with_scale += scale[i]
                map_with_scale += line[7:]
            else:
                map_with_scale += line
            map_with_scale += "\n"

        content += map_with_scale
        
        self.content = content
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
uktemp_page = UKTempPage(page_number)

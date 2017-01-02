#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page

class UKTempPage(Page):
    def __init__(self):
        super(UKTempPage, self).__init__("461")
        self.title = "UK Temperature"
        self.tagline = "Why exactly do we live in Britain?"

    def background(self):
        import urllib2, json
        from file_handler import load_file
        ordered_ids = [i.rstrip("\n") for i in load_file("uk_coordinate_ids.txt").split("\n")]

        self.temps = [99 for i in range(len(ordered_ids))]
        i = 0

        url = "http://api.openweathermap.org/data/2.5/group?id=" + ",".join(ordered_ids[0:100]) + "&units=metric&appid=05f6b7c72cd541dd510d7bc08f6a8bb0"
        response = urllib2.urlopen(url)
        data = json.load(response)
        for city in data['list']:
            self.temps[i] = float(city['main']['temp'])
            i+=1
        url = "http://api.openweathermap.org/data/2.5/group?id=" + ",".join(ordered_ids[100:200]) + "&units=metric&appid=05f6b7c72cd541dd510d7bc08f6a8bb0"
        response = urllib2.urlopen(url)
        data = json.load(response)
        for city in data['list']:
            self.temps[i] = float(city['main']['temp'])
            i+=1
        url = "http://api.openweathermap.org/data/2.5/group?id=" + ",".join(ordered_ids[200:300]) + "&units=metric&appid=05f6b7c72cd541dd510d7bc08f6a8bb0"
        response = urllib2.urlopen(url)
        data = json.load(response)
        for city in data['list']:
            self.temps[i] = float(city['main']['temp'])
            i+=1
        url = "http://api.openweathermap.org/data/2.5/group?id=" + ",".join(ordered_ids[300:]) + "&units=metric&appid=05f6b7c72cd541dd510d7bc08f6a8bb0"
        response = urllib2.urlopen(url)
        data = json.load(response)
        for city in data['list']:
            self.temps[i] = float(city['main']['temp'])
            i+=1
        
    def generate_content(self):
        self.add_title("UK TEMPERATURE")
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
            
        boundaries = [-99,0,3,6,9,12,15,18,21,24]
        colours_before = ["BLUE","LIGHTBLUE","LIGHTCYAN","CYAN","GREEN","LIGHTGREEN","YELLOW","ORANGE","LIGHTRED","RED"]

        i = 0
        for char in uk_map:
            color = None
            if char != "\n":
                self.add_newline()
                continue
            if char != ' ':
                j = 0
                for b in boundaries:
                    if self.temps[i] >= b:
                        color = colours_before[j]
                    j+=1
                i+=1
            self.add_text(char,fg=color)

        self.move_cursor(x=0,y=8)
        self.add_text("Hottest",fg=colours_before[-1])

        bstr = [u"██"]+["0"*(2-len(str(i)))+str(i) for i in boundaries[1:]]+[u"██"]
        #[-99,0,3,6,9,12,15,18,21,24]
        for i,r in enumerate(reversed(colours_before)):
            self.move_cursor(x=0,y=9+i)
            self.add_text(u"█"+bstr[-i-2]+"-"+bstr[-i-1]+u"█",fg=r)
        self.move_cursor(x=0,y=9+len(colours_before))
        self.add_text("Coldest",fg=colours_before[0])

uktemp_page = UKTempPage()


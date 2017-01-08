#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
import datetime

class WeatherPage(Page):
    def __init__(self):
        super(WeatherPage, self).__init__("411")
        self.title = "Weather Forecast Day"
        self.in_index=False

    def background(self):
        import metoffer

        api_key = "f2ef8ecf-175f-491d-aea1-93a38209bd55"
        M = metoffer.MetOffer(api_key);
        #x = M.nearest_loc_forecast(51.4033, -0.3375, metoffer.THREE_HOURLY)
        x = M.nearest_loc_forecast(51.5252257441084, -0.134831964969635, metoffer.THREE_HOURLY)
        self.y = metoffer.parse_val(x)

        self.tagline = "Live from the Met Office"

    def generate_content(self):

        def weather_symbol(weather_forecast):
            if weather_forecast in [1]: #sun
                image = """
-------y--------
-------y--------
---y-------y----
----y--y--y-----
------yyy-------
-----yyyyy------
-----yyyyy------
--yy-yyyyy-yy---
-----yyyyy------
------yyy-------
----y--y--y-----
---y-------y----
-------y--------
-------y--------
"""
            elif weather_forecast in [0]:#moon
                image = """
--------ooo-----
------ooo-------
-----oooo-------
----oooo--------
----ooo---------
---oooo---------
---oooo---------
---oooo---------
---oooo---------
----ooo---------
----oooo--------
-----oooo-------
------ooo-------
--------ooo-----
"""
            elif weather_forecast in [2,3]: #cloud sun
                image = """
----------------
----------------
----WWW---y-----
---WwwwW--y--y--
-WWwwwwwW---y---
WwwWwwwwWWW-----
WwwwwwwWwwwW-yy-
WwwwwwwwwwwW----
-WWWWWWWWWW-----
------------y---
----------y--y--
----------y-----
----------------
----------------
"""
            elif weather_forecast in [9,10]: #cloud sun rain
                image = """
----------------
----------------
----WWW---y-----
---WwwwW--y--y--
-WWwwwwwW---y---
WwwWwwwwWWW-----
WwwwwwwWwwwW-yy-
WwwwwwwwwwwW----
-WWWWWCWWWW-----
-----CC-----y---
---CC-C---y--y--
--C---C---y-----
---CCC----------
----------------
"""
            elif weather_forecast in [11,12]: #light rain
                image = """
----------------
----------------
------www-------
-----w---w------
---ww-----w-----
--w--w----www---
--w------w---w--
--w----C-----w--
---w--CC--www---
-----C--C-------
----C---C-------
----C---C-------
-----CCC--------
----------------
"""
            elif weather_forecast in [7]:
                image = """
----------------
----------------
-----WWWWW------
----WwwwwwW-----
---WwwwwwwwW----
-WWWwwwwwwwW----
WwwwWwwwwwwWWW--
WwwwwwwwwWWwwwW-
WwwwwwwwwwwwwwW-
WWwwwwwwwwwwwwW-
-WWWWWWWWWWWWW--
----------------
----------------
----------------
"""
            elif weather_forecast in [8]:  #dark cloud
                image = """
----------------
----------------
-----wwwww------
----w-----w-----
---w-------w----
-www-------w----
w---w------www--
w--------ww---w-
w-------------w-
ww------------w-
-wwwwwwwwwwwww--
----------------
----------------
----------------
"""
            elif weather_forecast in [13,14,16,17,19,20]: #rain
                image = """
------www-------
-----w---w------
---ww-----w-----
--w--w----www---
--w------w---w--
--w----------w--
---wwwwwwwwww---
----------------
-----C----------
----C-C----C----
---C---C--C-C---
----CCC--C---C--
---------C---C--
----------CCC---
"""
            elif weather_forecast in [15,18,21]: #heavy rain
                image = """
------www-------
-----w---w------
---ww-----w-----
--w--w----www---
--w------w---w--
--w----------w--
---wwwwwwwwww---
----------------
--C---------C---
-C-C---C---C-C--
C---C-C-C-C---C-
-CCC-C---C-CCC--
-----C---C------
------CCC-------
"""
            elif weather_forecast in [28,29,30]: #storm
                image = """
------www-------
-----w---w------
---ww-----w-----
--w--w----www---
--w------w---w--
--w----------w--
---www-RRRR-w---
------RRRR------
-----RRRR-------
------RRRR------
--------RRR-----
-------RR-------
------RR--------
-----R----------
"""
            elif weather_forecast in [22,23,24,25,26,27]: #snow
                image = """
------www-------
-----w---w------
---ww-----w-----
--w--w----www---
--w------w---w--
--w----------w--
---wwww-W-W-w---
---------W------
--------W-W-----
---W-W----------
----W-----------
---W-W----W-W---
-----------W----
----------W-W---
"""
            else: #mixed
                image = """
rrrrrrrrrrrrrrrr
oooooooooooooooo
yyyyyyyyyyyyyyyy
GGGGGGGGGGGGGGGG
BBBBBBBBBBBBBBBB
bbbbbbbbbbbbbbbb
mmmmmmmmmmmmmmmm
rrrrrrrrrrrrrrrr
oooooooooooooooo
yyyyyyyyyyyyyyyy
GGGGGGGGGGGGGGGG
BBBBBBBBBBBBBBBB
bbbbbbbbbbbbbbbb
mmmmmmmmmmmmmmmm
"""

            '''
            {0: 'Clear night',
             1: 'Sunny day',
             2: 'Partly cloudy (night)',
             3: 'Partly cloudy (day)',
             4: 'Not used',
             5: 'Mist',xxxx
             6: 'Fog',xxxxx
             7: 'Cloudy',
             8: 'Overcast',
             9: 'Light rain shower (night)',
             10: 'Light rain shower (day)',
             11: 'Drizzle',
             12: 'Light rain',
             13: 'Heavy rain shower (night)',
             14: 'Heavy rain shower (day)',
             15: 'Heavy rain',
             16: 'Sleet shower (night)',
             17: 'Sleet shower (day)',
             18: 'Sleet',
             19: 'Hail shower (night)',
             20: 'Hail shower (day)',
             21: 'Hail',
             22: 'Light snow shower (night)',
             23: 'Light snow shower (day)',
             24: 'Light snow',
             25: 'Heavy snow shower (night)',
             26: 'Heavy snow shower (day)',
             27: 'Heavy snow',
             28: 'Thunder shower (night)',
             29: 'Thunder shower (day)',
             30: 'Thunder',
             'NA': 'Not available'}
            '''

            return image #[weather_pic, weather_colour_foreground, weather_colour_background]

        def print_image(image,y_coord=0,x_coord=0):
            self.move_cursor(y=y_coord,x=x_coord)
            color_codes = {"k": "BLACK",  "K": "GREY",
                           "r": "RED",    "R": "LIGHTRED",
                           "o": "ORANGE", "y": "YELLOW",
                           "g": "GREEN",  "G": "LIGHTGREEN",
                           "c": "CYAN",   "C": "LIGHTCYAN",
                           "b": "BLUE",   "B": "LIGHTBLUE",
                           "m": "MAGENTA","p": "PINK",
                           "w": "WHITE",  "W": "BRIGHTWHITE",
                           "d": "DEFAULT","-": "BLACK"}
            lines = image.split("\n")[1:-1]
            for l in range(len(lines)//2):
                for c in range(len(lines[2*l])):
                    c1 = lines[2*l][c]
                    c2 = lines[2*l+1][c]
                    self.start_fg_color(color_codes[c1])
                    self.start_bg_color(color_codes[c2])
                    self.add_text(u"\u2580")
                    self.end_bg_color()
                    self.end_fg_color()
                self.move_cursor(y=y_coord + l+1, x=x_coord)

        self.add_title("Forecast",fg="MAGENTA",bg="CYAN")

        day_weather = []
        day_max = []
        day_min = []
        date = []
        for i in self.y.data:
            if i["timestamp"][0] > datetime.datetime.now() - datetime.timedelta(hours=1.9):
                day_weather.append(weather_symbol(i["Weather Type"][0]))
                day_max.append(i["Feels Like Temperature"][0])
                date.append((i["timestamp"][0].strftime("%-I%p")).replace("am",u"㏂").replace("pm",u"㏘"))


        # Day of week
        self.move_cursor(y=7,x=0)
        self.add_title(date[0],bg="YELLOW",fg="BLACK",fill=False,font='size4')
        self.move_cursor(y=7,x=0)
        self.add_title(date[1],bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=20)
        self.move_cursor(y=7,x=0)
        self.add_title(date[2],bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=40)
        self.move_cursor(y=7,x=0)
        self.add_title(date[3],bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=60)


        # Pictures
        print_image(day_weather[0],11,1)
        print_image(day_weather[1],11,21)
        print_image(day_weather[2],11,41)
        print_image(day_weather[3],11,61)

        # Max temps
        self.move_cursor(y=18,x=0)
        self.add_title(str(day_max[0]),bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=5)
        self.move_cursor(y=18,x=0)
        self.add_title(str(day_max[1]),bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=25)
        self.move_cursor(y=18,x=0)
        self.add_title(str(day_max[2]),bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=45)
        self.move_cursor(y=18,x=0)
        self.add_title(str(day_max[3]),bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=65)

weather_page = WeatherPage()

def round_me(n,i=1):
    try:
        return str(int(round(float(n)/i)*i))
    except:
        return n

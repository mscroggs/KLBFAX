#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from page import Page
from printer import instance as printer
from printer import size4_instance as size4_printer
from colours import colour_print
from random import randint
from file_handler import f_read


class WeatherPage(Page):
    def __init__(self, page_num):
        super(WeatherPage, self).__init__(page_num)
        self.title = "Weather Forecast Day"
        self.index_num = "411"

    def generate_content(self):
        import metoffer
        import datetime
        import pytz

        def number_in_box(number_string):
            padded_number_string = number_string.replace("1","|1")
            padded_number_string = padded_number_string.replace("-","-|")
            if len(number_string) == 2:
                if number_string.count("1") == 2 or (number_string.count("1") == 1 and number_string.count("-") == 1):
                    return "||" + padded_number_string + "||", ""
                elif number_string.count("1") == 1 or (number_string.count("1") == 0 and number_string.count("-") == 1):
                    return "|" + padded_number_string + "|", ""
                else:
                    return number_string,""
            else:
                if number_string.count("1") == 1:
                    return "||||" + padded_number_string + "|||||", ""
                else:
                    return "||||" + padded_number_string + "|||", ""

        def weather_symbol(weather_forecast):
            if weather_forecast in [1]:
                weather_pic = "*" #sunny
                weather_colour_foreground = self.colours.Background.YELLOW+self.colours.Style.BLINK
                weather_colour_background = self.colours.Foreground.BLACK
            elif weather_forecast in [0]:
                weather_pic = "}" #moon
                weather_colour_foreground = self.colours.Background.YELLOW
                weather_colour_background = self.colours.Foreground.BLACK
            elif weather_forecast in [2,3]:
                weather_pic = "~" #cloud sun
                weather_colour_foreground = self.colours.Background.BLACK
                weather_colour_background = self.colours.Foreground.WHITE
            elif weather_forecast in [9,10]:
                weather_pic = "<" #cloud sun rain
                weather_colour_foreground = self.colours.Background.BLACK
                weather_colour_background = self.colours.Foreground.WHITE
            elif weather_forecast in [11]:
                weather_pic = "[" #light rain
                weather_colour_foreground = self.colours.Background.CYAN+self.colours.Style.BLINK
                weather_colour_background = self.colours.Foreground.BLACK
            elif weather_forecast in [7]:
                weather_pic = "@" #cloudy
                weather_colour_foreground = self.colours.Background.BLACK
                weather_colour_background = self.colours.Foreground.WHITE
            elif weather_forecast in [8]:
                weather_pic = "@" #dark cloud
                weather_colour_foreground = self.colours.Background.WHITE+self.colours.Style.BLINK
                weather_colour_background = self.colours.Foreground.BLACK
            elif weather_forecast in [13,14,16,17,19,20]:
                weather_pic = "{" #rain
                weather_colour_foreground = self.colours.Background.CYAN
                weather_colour_background = self.colours.Foreground.BLACK
            elif weather_forecast in [15,18,21]:
                weather_pic = "]" #heavy rain
                weather_colour_foreground = self.colours.Background.BLUE+self.colours.Style.BLINK
                weather_colour_background = self.colours.Foreground.BLACK
            elif weather_forecast in [28,29,30]:
                weather_pic = "^" #storm
                weather_colour_foreground = self.colours.Background.RED
                weather_colour_background = self.colours.Foreground.BLACK
            elif weather_forecast in [22,23,24,25,26,27]:
                weather_pic = "%" #snow
                weather_colour_foreground = self.colours.Background.BLACK
                weather_colour_background = self.colours.Foreground.WHITE
            else:
                weather_pic = "`" #mixed
                weather_colour_foreground = self.colours.Background.BLACK
                weather_colour_background = self.colours.Foreground.WHITE

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

            return [weather_pic, weather_colour_foreground, weather_colour_background]


        tag = "Live from the Met Office"
        content = colour_print(printer.text_to_ascii("Forecast", padding={"left": 0}),
                            self.colours.Background.CYAN, self.colours.Foreground.MAGENTA)
        content+="\n\n"
        api_key = "f2ef8ecf-175f-491d-aea1-93a38209bd55"
        M = metoffer.MetOffer(api_key);
        #x = M.nearest_loc_forecast(51.4033, -0.3375, metoffer.THREE_HOURLY)
        x = M.nearest_loc_forecast(51.5252257441084, -0.134831964969635, metoffer.THREE_HOURLY)
        y = metoffer.parse_val(x)
        day_weather = []
        day_max = []
        day_min = []
        date = []
        for i in y.data:
            #timestamp = i['timestamp'][0].replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Europe/London"))
            if i['timestamp'][0] > datetime.datetime.now() - datetime.timedelta(hours=2.9):
                #content+= ("{} - {} - {}".format(i["timestamp"][0].strftime("%d %b, %H:%M"), i["Feels Like Day Maximum Temperature"][0], metoffer.WEATHER_CODES[i["Weather Type"][0]]))
                day_weather.append(weather_symbol(i["Weather Type"][0]))
                day_max.append(i["Feels Like Temperature"][0])
                date.append(i["timestamp"][0].strftime("%-I%p"))

        # Day of week

        content += self.colours.colour_print_join([
                        (size4_printer.text_to_ascii("",False)+"",
                             self.colours.Background.DEFAULT,
                             self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii(str(date[0]),False)+"",
                            self.colours.Background.YELLOW+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii("|"*(17-((len(size4_printer.text_to_ascii(str(date[0]),False))-7)/4 - 1)),False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii(str(date[1]),False)+"",
                            self.colours.Background.YELLOW+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii("|"*(17-((len(size4_printer.text_to_ascii(str(date[1]),False))-7)/4 - 1)),False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii(str(date[2]),False)+"",
                            self.colours.Background.YELLOW+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii("|"*(17-((len(size4_printer.text_to_ascii(str(date[2]),False))-7)/4 - 1)),False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii(str(date[3]),False)+"",
                            self.colours.Background.YELLOW+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK)
                    ],""," ")
        content += "\n"

        # Pictures
        content += self.colours.colour_print_join([
                (printer.text_to_ascii("",False)+"",
                    self.colours.Background.DEFAULT,
                    self.colours.Foreground.BLACK),
                (printer.text_to_ascii(day_weather[0][0],False)+"",
                    day_weather[0][1],
                    day_weather[0][2]),
                (printer.text_to_ascii("||",False)+"",
                    self.colours.Background.DEFAULT,
                    self.colours.Foreground.BLACK),
                (printer.text_to_ascii(day_weather[1][0],False)+"",
                    day_weather[1][1],
                    day_weather[1][2]),
                (printer.text_to_ascii("||",False)+"",
                    self.colours.Background.DEFAULT,
                    self.colours.Foreground.BLACK),
                (printer.text_to_ascii(day_weather[2][0],False)+"",
                    day_weather[2][1],
                    day_weather[2][2]),
                (printer.text_to_ascii("||",False)+"",
                    self.colours.Background.DEFAULT,
                    self.colours.Foreground.BLACK),
                (printer.text_to_ascii(day_weather[3][0],False)+"",
                    day_weather[3][1],
                    day_weather[3][2])
            ],""," ")
        content += "\n"

        # Max temps
        content += self.colours.colour_print_join([
                        (size4_printer.text_to_ascii("||",False)+"",
                             self.colours.Background.DEFAULT,
                             self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii(str(day_max[0]),False)+"",
                            self.colours.Background.YELLOW+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii("|"*(15-((len(size4_printer.text_to_ascii(str(day_max[0]),False))-7)/4 - 1)),False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii(str(day_max[1]),False)+"",
                            self.colours.Background.YELLOW+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii("|"*(15-((len(size4_printer.text_to_ascii(str(day_max[1]),False))-7)/4 - 1)),False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii(str(day_max[2]),False)+"",
                            self.colours.Background.YELLOW+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii("|"*(15-((len(size4_printer.text_to_ascii(str(day_max[2]),False))-7)/4 - 1)),False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK),
                        (size4_printer.text_to_ascii(str(day_max[3]),False)+"",
                            self.colours.Background.YELLOW+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK)
                    ]," "," ")
        content += "\n"

        self.content = content
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
weather_page = WeatherPage(page_number)

def round_me(n,i=1):
    try:
        return str(int(round(float(n)/i)*i))
    except:
        return n

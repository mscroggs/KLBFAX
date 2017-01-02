#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page


class WeatherPage(Page):
    def __init__(self):
        super(WeatherPage, self).__init__("410")
        self.title = "Weather Forecast"
        self.in_index = False

    def background(self):
        import metoffer

        api_key = "f2ef8ecf-175f-491d-aea1-93a38209bd55"
        M = metoffer.MetOffer(api_key);
        #x = M.nearest_loc_forecast(51.4033, -0.3375, metoffer.THREE_HOURLY)
        x = M.nearest_loc_forecast(51.5252257441084, -0.134831964969635, metoffer.DAILY)
        self.y = metoffer.parse_val(x)

        self.tagline = "Live from the Met Office"

    def generate_content(self):

        def weather_symbol(weather_forecast):
            if weather_forecast in [1]:
                weather_pic = "*" #sunny
                weather_colour_foreground = "YELLOW"
                weather_colour_background = "BLACK"
            elif weather_forecast in [0]:
                weather_pic = "}" #moon
                weather_colour_foreground = "YELLOW"
                weather_colour_background = "BLACK"
            elif weather_forecast in [2,3]:
                weather_pic = "~" #cloud sun
                weather_colour_foreground = "BLACK"
                weather_colour_background = "WHITE"
            elif weather_forecast in [9,10]:
                weather_pic = "<" #cloud sun rain
                weather_colour_foreground = "BLACK"
                weather_colour_background = "WHITE"
            elif weather_forecast in [11,12]:
                weather_pic = "[" #light rain
                weather_colour_foreground = "CYAN"
                weather_colour_background = "BLACK"
            elif weather_forecast in [7]:
                weather_pic = "@" #cloudy
                weather_colour_foreground = "BLACK"
                weather_colour_background = "WHITE"
            elif weather_forecast in [8]:
                weather_pic = "@" #dark cloud
                weather_colour_foreground = "WHITE"
                weather_colour_background = "BLACK"
            elif weather_forecast in [13,14,16,17,19,20]:
                weather_pic = "{" #rain
                weather_colour_foreground = "CYAN"
                weather_colour_background = "BLACK"
            elif weather_forecast in [15,18,21]:
                weather_pic = "]" #heavy rain
                weather_colour_foreground = "BLUE"
                weather_colour_background = "BLACK"
            elif weather_forecast in [28,29,30]:
                weather_pic = "^" #storm
                weather_colour_foreground = "RED"
                weather_colour_background = "BLACK"
            elif weather_forecast in [22,23,24,25,26,27]:
                weather_pic = "%" #snow
                weather_colour_foreground = "BLACK"
                weather_colour_background = "WHITE"
            else:
                weather_pic = "`" #mixed
                weather_colour_foreground = "BLACK"
                weather_colour_background = "WHITE"

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

        self.add_title("Forecast",fg="MAGENTA",bg="CYAN")

        day_weather = []
        day_max = []
        day_min = []
        date = []
        for i in self.y.data:
            if i["timestamp"][1] == "Day":
                day_weather.append(weather_symbol(i["Weather Type"][0]))
                day_max.append(i["Feels Like Day Maximum Temperature"][0])
                date.append(i["timestamp"][0].strftime("%a"))
            if i["timestamp"][1] == "Night":
                day_min.append(i["Feels Like Night Minimum Temperature"][0])


        # Day of week
        self.move_cursor(y=7,x=0)
        self.add_title(str(date[0]),bg="YELLOW",fg="BLACK",fill=False,font='size4')
        self.move_cursor(y=7,x=0)
        self.add_title(str(date[1]),bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=20)
        self.move_cursor(y=7,x=0)
        self.add_title(str(date[2]),bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=40)
        self.move_cursor(y=7,x=0)
        self.add_title(str(date[3]),bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=60)


        # Pictures
        self.move_cursor(y=11,x=0)
        self.add_title(str(day_weather[0][0]),bg=day_weather[0][1],fg=day_weather[0][2],fill=False)
        self.move_cursor(y=11,x=0)
        self.add_title(str(day_weather[1][0]),bg=day_weather[1][1],fg=day_weather[1][2],fill=False,pre=20)
        self.move_cursor(y=11,x=0)
        self.add_title(str(day_weather[2][0]),bg=day_weather[2][1],fg=day_weather[2][2],fill=False,pre=40)
        self.move_cursor(y=11,x=0)
        self.add_title(str(day_weather[3][0]),bg=day_weather[3][1],fg=day_weather[3][2],fill=False,pre=60)

        # Max temps
        self.move_cursor(y=18,x=0)
        self.add_title(str(day_max[0]),bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=5)
        self.move_cursor(y=18,x=0)
        self.add_title(str(day_max[1]),bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=25)
        self.move_cursor(y=18,x=0)
        self.add_title(str(day_max[2]),bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=45)
        self.move_cursor(y=18,x=0)
        self.add_title(str(day_max[3]),bg="YELLOW",fg="BLACK",fill=False,font='size4', pre=65)

        # Min temps
        self.move_cursor(y=22,x=0)
        self.add_title(str(day_min[0]),bg="RED",fg="BLACK",fill=False,font='size4', pre=5)
        self.move_cursor(y=22,x=0)
        self.add_title(str(day_min[1]),bg="RED",fg="BLACK",fill=False,font='size4', pre=25)
        self.move_cursor(y=22,x=0)
        self.add_title(str(day_min[2]),bg="RED",fg="BLACK",fill=False,font='size4', pre=45)
        self.move_cursor(y=22,x=0)
        self.add_title(str(day_min[3]),bg="RED",fg="BLACK",fill=False,font='size4', pre=65)

weather_page = WeatherPage()

def round_me(n,i=1):
    try:
        return str(int(round(float(n)/i)*i))
    except:
        return n

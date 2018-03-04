#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page


class WeatherPage(Page):
    def __init__(self):
        super(WeatherPage, self).__init__("322")
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
        from fonts import weather_symbol
        self.add_title("4-day Weather",fg="CYAN",bg="BRIGHTWHITE")

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

        #-------------------------
        # k BLACK   K GREY
        # r RED     R LIGHTRED
        # o ORANGE  y YELLOW
        # g GREEN   G LIGHTGREEN
        # c CYAN    C LIGHTCYAN
        # b BLUE    B LIGHTBLUE
        # m MAGENTA p PINK
        # w WHITE   W BRIGHTWHITE
        # d DEFAULT
        # ------------------------




        #self.move_cursor(y=0,x=0)





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
        self.print_image(day_weather[0],11,1)
        self.print_image(day_weather[1],11,21)
        self.print_image(day_weather[2],11,41)
        self.print_image(day_weather[3],11,61)
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

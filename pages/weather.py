#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page import Page
from helpers.file_handler import f_read
from helpers import url_handler
import datetime
import config

class WeatherPage(Page):
    def __init__(self):
        super(WeatherPage, self).__init__("320")
        self.title = "Weather"
        self.index_num = "320-325"

    def background(self):
        try:
            response = url_handler.load("http://weather.casa.ucl.ac.uk/clientraw.txt")
            self.weather_data = response.split(" ")
        except:
            self.weather_data = ["CLASSIFIED"]*60
        ''' 
        # If using clientraw.txt:

        Field#  Label   Type    Contents
        000     Header  L   12345
        001     Avg Speed   K   7.6kts = 8.75mph = 14.08km/h
        002     Gusts   K   5.2kts = 5.98mph = 9.63km/h
        003     WindDir     D   320* (NW)
        004     Temp    C   5.3C = 41.5F
        005     Outside Humidity    P   64%
        006     Barometer   H   1024.0 hPa = 30.24 inHg
        007     Daily Rain  M   0.0mm = 0in
        008     Monthly Rain    M   25.7mm = 1.01in
        009     Yearly Rain     M   25.7mm = 1.01in
        010     Rain Rate   M   0.00mm = 0in
        011     Max Rain Rate   M   0.00mm = 0in
        012     Indoor Temp     C   23.2*C = 73.8*F
        013     Indoor Hum  P   26%
        014     Soil Temp   C   100.0*C = 212*F
        015     Forecast Icon   I   5 (Dry Clear)
        016     WMR968 Extra Temp   C   0.0*C = 32*F
        017     WMR968 Extra Hum    P   0%
        018     WMR968 Extra Sensor     N   0
        019     Yesterday Rain  M   0.0mm = 0in
        020     Extra Temp Sensor 1     C   12.8*C = 55*F
        021     Extra Temp Sensor 2     C   No Value
        022     Extra Temp Sensor 3     C   No Value
        023     Extra Temp Sensor 4     C   No Value
        024     Extra Temp Sensor 5     C   No Value
        025     Extra Temp Sensor 6     C   No Value
        026     Extra Hum Sensor 1  P   No Value
        027     Extra Hum Sensor 2  P   No Value
        028     Extra Hum Sensor 3  P   No Value
        029     Hour    T   16
        030     Minute  T   29
        031     Seconds     T   18
        032     Station Name    L   London-4:29:18 PM
        033     Dallas Lighting Count   N   0
        034     Solar Reading   N   0
        035     Day     T   7
        036     Month   T   1
        037     WMR968 batt1    P   100%
        038     WMR968 batt2    P   100%
        039     WMR968 batt3    P   100%
        040     WMR968 batt4    P   100%
        041     WMR968 batt5    P   100%
        042     WMR968 batt6    P   100%
        043     WMR968 batt7    P   100%
        044     WindChill   C   3.1*C = 37.6*F
        045     Humidex     C   2.9*C = 37.2*F
        046     Max Day Temp    C   7.1*C = 44.8*F
        047     Min Day Temp    C   3.8*C = 38.8*F
        048     Icon Type   Z   5 (Dry Clear)
        049     Weather Desc    L   dusk/Dry
        050     Baro Trend  H   0.3 hPa = 0.01 inHg
        051     Windspeed Hour 01   K   10kts = 11.51mph = 18.52km/h
        052     Windspeed Hour 02   K   10kts = 11.51mph = 18.52km/h
        053     Windspeed Hour 03   K   10kts = 11.51mph = 18.52km/h
        054     Windspeed Hour 04   K   8kts = 9.21mph = 14.82km/h
        055     Windspeed Hour 05   K   8kts = 9.21mph = 14.82km/h
        056     Windspeed Hour 06   K   10kts = 11.51mph = 18.52km/h
        057     Windspeed Hour 07   K   10kts = 11.51mph = 18.52km/h
        058     Windspeed Hour 08   K   7kts = 8.06mph = 12.96km/h
        059     Windspeed Hour 09   K   7kts = 8.06mph = 12.96km/h
        060     Windspeed Hour 10   K   3kts = 3.45mph = 5.56km/h
        061     Windspeed Hour 11   K   3kts = 3.45mph = 5.56km/h
        062     Windspeed Hour 12   K   4kts = 4.6mph = 7.41km/h
        063     Windspeed Hour 13   K   4kts = 4.6mph = 7.41km/h
        064     Windspeed Hour 14   K   4kts = 4.6mph = 7.41km/h
        065     Windspeed Hour 15   K   3kts = 3.45mph = 5.56km/h
        066     Windspeed Hour 16   K   9kts = 10.36mph = 16.67km/h
        067     Windspeed Hour 17   K   12kts = 13.81mph = 22.22km/h
        068     Windspeed Hour 18   K   12kts = 13.81mph = 22.22km/h
        069     Windspeed Hour 19   K   8kts = 9.21mph = 14.82km/h
        070     Windspeed Hour 20   K   5kts = 5.75mph = 9.26km/h
        071     Max Wind Gust Today     K   21.0kts = 24.17mph = 38.89km/h
        072     DewPoint Temp   C   -0.9*C = 30.4*F
        073     Cloud Height    F   824 Meters - 2703.5Feet
        074     Date    L   1/7/2018
        075     Max Humidex     C   4.9*C = 40.8*F
        076     Min Humidex     C   1.6*C = 34.9*F
        077     Max Windchill   C   7.1*C = 44.8*F
        078     Min Windchill   C   -1.4*C = 29.5*F
        079     Davis VP UV     N   0.0
        080     Hr Windspeed 01     K   5kts = 5.75mph = 9.26km/h
        081     Hr Windspeed 02     K   6kts = 6.9mph = 11.11km/h
        082     Hr Windspeed 03     K   6kts = 6.9mph = 11.11km/h
        083     Hr Windspeed 04     K   8kts = 9.21mph = 14.82km/h
        084     Hr Windspeed 05     K   8kts = 9.21mph = 14.82km/h
        085     Hr Windspeed 06     K   3kts = 3.45mph = 5.56km/h
        086     Hr Windspeed 07     K   7kts = 8.06mph = 12.96km/h
        087     Hr Windspeed 08     K   6kts = 6.9mph = 11.11km/h
        088     Hr Windspeed 09     K   6kts = 6.9mph = 11.11km/h
        089     Hr Windspeed 10     K   6kts = 6.9mph = 11.11km/h
        090     Hr Temp 01  C   6.0*C = 42.8*F
        091     Hr Temp 02  C   5.9*C = 42.6*F
        092     Hr Temp 03  C   6.0*C = 42.8*F
        093     Hr Temp 04  C   5.8*C = 42.4*F
        094     Hr Temp 05  C   5.8*C = 42.4*F
        095     Hr Temp 06  C   5.7*C = 42.3*F
        096     Hr Temp 07  C   5.6*C = 42.1*F
        097     Hr Temp 08  C   5.5*C = 41.9*F
        098     Hr Temp 09  C   5.4*C = 41.7*F
        099     Hr Temp 10  C   5.3*C = 41.5*F
        100     Hr Rain 01  M   0.0mm = 0in
        101     Hr Rain 02  M   0.0mm = 0in
        102     Hr Rain 03  M   0.0mm = 0in
        103     Hr Rain 04  M   0.0mm = 0in
        104     Hr Rain 05  M   0.0mm = 0in
        105     Hr Rain 06  M   0.0mm = 0in
        106     Hr Rain 07  M   0.0mm = 0in
        107     Hr Rain 08  M   0.0mm = 0in
        108     Hr Rain 09  M   0.0mm = 0in
        109     Hr Rain 10  M   0.0mm = 0in
        110     Max Heat Index  C   7.1*C = 44.8*F
        111     Min Heat Index  C   3.8*C = 38.8*F
        112     Heat Index  C   5.3*C = 41.5*F
        113     Max Avg Speed   K   13.1kts = 15.08mph = 24.26km/h
        114     # Lightning in last Min     N   0
        115     Time Last Lightning Strike  L   ---
        116     Date Last Lightning Strike  L   ---
        117     Wind Avg Dir    D   3* (N)
        118     Nexstorm Dist   L   0
        119     NexStorm Bearing    D   0* (N)
        120     Extra Temp Sensor 7     C   No Value
        121     Extra Temp Sensor 8     C   No Value
        122     Extra Hum Sensor 4  P   0%
        123     Extra Hum Sensor 5  P   No Value
        124     Extra Hum Sensor 6  P   No Value
        125     Extra Hum Sensor 7  P   No Value
        126     Extra Hum Sensor 8  P   No Value
        127     VP Solarwm  N   0.0
        128     Max InTemp  C   23.7*C = 74.7*F
        129     Min InTemp  C   22.9*C = 73.2*F
        130     Apparent Temp   C   1.4*C = 34.5*F
        131     Max Baro    H   1024.6 hPa = 30.26 inHg
        132     Min Baro    H   1019.0 hPa = 30.09 inHg
        133     Max Gust Last Hour  K   17kts = 19.56mph = 31.48km/h
        134     Max Gust Last Hour Time     L   3:51PM
        135     Max Gust Today Time     L   1:14 PM
        136     Max Apparent Temp   C   4.9*C = 40.8*F
        137     Min Apparent Temp   C   -0.3*C = 31.5*F
        138     Max Dew Pt  C   2.2*C = 36*F
        139     Min Dew Pt  C   -0.9*C = 30.4*F
        140     Max Gust In Lst Min     K   13kts = 14.96mph = 24.08km/h
        141     Current Year    L   2018
        142     THSWS   L   -17.8
        143     Temp Trend (Logic)  L   -1
        144     Humidity Trend (Logic)  L   -1
        145     Humidex Trend (Logic)   L   -1
        146     Hr Wind Dir 01  D   317* (NW)
        147     Hr Wind Dir 02  D   340* (NNW)
        148     Hr Wind Dir 03  D   300* (WNW)
        149     Hr Wind Dir 04  D   304* (WNW)
        150     Hr Wind Dir 05  D   19* (N)
        151     Hr Wind Dir 06  D   355* (NNW)
        152     Hr Wind Dir 07  D   288* (W)
        153     Hr Wind Dir 08  D   89* (ENE)
        154     Hr Wind Dir 09  D   306* (WNW)
        155     Hr Wind Dir 10  D   320* (NW)
        156     Leaf Wetness    C   0.0*C = 32*F
        157     Soil moisture   C   No Value
        158     10 Min Avg Wind Speed   K   5.9kts = 6.79mph = 10.93km/h
        159     Wet bulb temperature    C   3.0*C = 37.4*F
        160     Latitude (- for southern hemisphere)    T   51.52167
        161     Longitude (- for EAST of GMT)   T   0.13500
        162     9am Rain Reset Total    M   0.0mm = 0in
        163     Daily Hi Humidity   P   83%
        164     Daily Low Humidity  P   59%
        165     Midnight Rain Reset total   M   0.0mm = 0in
        166     Low windchill Time  T   4:57_AM
        167     Current Cost Watts Ch1  L   0.0
        168     Current Cost Watts Ch2  L   0.0
        169     Current Cost Watts Ch3  L   0.0
        170     Current Cost Watts Ch4  L   0.0
        171     Current Cost Watts Ch5  L   0.0
        172     Current Cost Watts Ch6  L   0.0
        173     Daily Wind Run 9am/Mid Reset    K   155.5kts = 178.95mph = 287.99km/h
        174     Record End (WD Ver)     L   1:09_PM
        '''

    def generate_content(self):

        weather_date_list = self.weather_data[74].split("/") # It's in US format by default
        weather_date = str(weather_date_list[1]) + "/" + str(weather_date_list[0]) + "/" + str(weather_date_list[2])
        weather_time = str(self.weather_data[29]) + ":" + str(self.weather_data[30]) + ":" + str(self.weather_data[31])
        weather_temperature = self.weather_data[4]
        weather_humidity = self.weather_data[5]
        weather_wind_speed = self.weather_data[1]
        weather_wind_direction_degrees = self.weather_data[3]
        weather_rain_today = self.weather_data[7]
        weather_pressure = self.weather_data[6]

        weather_high_temp = self.weather_data[46]
        weather_low_temp = self.weather_data[47]

        weather_cloud_height = self.weather_data[73]
        weather_forecast = self.weather_data[15]
        weather_daylight = self.weather_data[34]

        self.tagline = "Live data from CASA - " + weather_date + " " + weather_time
        self.add_title("weather", bg="CYAN", fg="MAGENTA")

        outside_weather_foreground = "BLUE"
        outside_weather_background = "LIGHTCYAN"
        inside_weather_foreground = "BLUE"
        inside_weather_background = "LIGHT CYAN"
        try:
            inside_weather = f_read("temp_now")
            if int(inside_weather) >= 20:
                inside_weather_foreground = "YELLOW"
                inside_weather_background = "RED"
            elif 10 <= int(inside_weather) < 20:
                inside_weather_foreground = "RED"
                inside_weather_background = "YELLOW"
            elif 0 < int(inside_weather) < 10:
                inside_weather_foreground = "BLUE"
                inside_weather_background = "LIGHTGREEN"
        except:
            inside_weather = "??"

        try:
            outside_weather = str(int(round(float(weather_temperature))))
            if int(outside_weather) >= 20:
                outside_weather_foreground = "YELLOW"
                outside_weather_background = "RED"
            elif 10 <= int(outside_weather) < 20:
                outside_weather_foreground = "RED"
                outside_weather_background = "YELLOW"
            elif 0 < int(outside_weather) < 10:
                outside_weather_foreground = "BLUE"
                outside_weather_background = "LIGHTGREEN"

        except:
            outside_weather = "??"

        if weather_daylight == "1":
            inside_weather_pic = "*" #sunny
            inside_weather_colour_foreground = "YELLOW"
            inside_weather_colour_background = "BLACK"
        else:
            inside_weather_pic = "}" #moon
            inside_weather_colour_foreground = "ORANGE"
            inside_weather_colour_background = "BLACK"

        ''' Meanings of icon numbers from clientraw.txt (Note not the same as from realtime.txt)

    "day_clear.png",           //  0 imagesunny.visible
    "night_clear.png",         //  1 imageclearnight.visible
    "day_partly_cloudy.png",   //  2 imagecloudy.visible
    "day_mainly_cloudy.png",   //  3 imagecloudy2.visible
    "night_partly_cloudy.gif", //  4 imagecloudynight.visible
    "day_clear.png",           //  5 imagedry.visible
    "fog.png",                 //  6 imagefog.visible
    "haze.png",                //  7 imagehaze.visible
    "day_heavy_rain.png",      //  8 imageheavyrain.visible
    "day_mostly_sunny.png",    //  9 imagemainlyfine.visible
    "night_mist.png",                // 10 imagemist.visible
    "night_fog.png",                 // 11 imagenightfog.visible
    "night_heavy_rain.png",    // 12 imagenightheavyrain.visible
    "night_overcast.png",        // 13 imagenightovercast.visible
    "night_rain.png",          // 14 imagenightrain.visible
    "night_light_rain.png",    // 15 imagenightshowers.visible
    "night_snow.gif",          // 16 imagenightsnow.visible
    "night_thunder.png",        // 17 imagenightthunder.visible
    "day_mainly_cloudy.png",          // 18 imageovercast.visible
    "day_partly_cloudy.png",   // 19 imagepartlycloudy.visible
    "day_rain.png",            // 20 imagerain.visible
    "day_light_rain.png",            // 21 imagerain2.visible
    "day_light_rain.png",      // 22 imageshowers2.visible
    "day_sleet.gif",           // 23 imagesleet.visible
    "day_sleet.gif",           // 24 imagesleetshowers.visible
    "day_snow.gif",            // 25 imagesnow.visible
    "day_snow.gif",            // 26 imagesnowmelt.visible
    "day_snow.gif",            // 27 imagesnowshowers2.visible
    "day_clear.pngf",           // 28 imagesunny.visible
    "thunder.png",          // 29 imagethundershowers.visible
    "thunder.png",          // 30 imagethundershowers2.visible
    "thunder.png",          // 31 imagethunderstorms.visible
    "tornado.gif",             // 32 imagetornado.visible
    "windy.gif",               // 33 imagewindy.visible
    "day_recent_rain.png",   // 34 stopped rainning
    "windyrain.gif"            // 35 windy/rain (new with V2.11)
    '''

        if weather_forecast in ["1", "2", "-1"] and weather_daylight == "1":
            weather_pic = "*" #sunny
            weather_colour_foreground = "YELLOW"
            weather_colour_background = "BLACK"
        elif weather_forecast in ["1", "2"] and weather_daylight == "0":
            weather_pic = "}" #moon
            weather_colour_foreground = "YELLOW"
            weather_colour_background = "BLACK"
        elif weather_forecast in ["3","6"]:
            weather_pic = "~" #cloud sun
            weather_colour_foreground = "BLACK"
            weather_colour_background = "WHITE"
        elif weather_forecast in ["4", "5", "7", "8"]:
            weather_pic = "<" #cloud sun rain
            weather_colour_foreground = "BLACK"
            weather_colour_background = "WHITE"
        elif weather_forecast in ["9", "11", "14", "15"]:
            weather_pic = "[" #light rains
            weather_colour_foreground = "LIGHTCYAN"
            weather_colour_background = "BLACK"
        elif weather_forecast in ["10"]:
            weather_pic = "@" #cloudy
            weather_colour_foreground = "BLACK"
            weather_colour_background = "WHITE"
        elif weather_forecast in ["12","13"]:
            weather_pic = "@" #dark cloud
            weather_colour_foreground = "BRIGHTWHITE"
            weather_colour_background = "BLACK"
        elif weather_forecast in ["16","18","19","20","21","23"]:
            weather_pic = "{" #rain
            weather_colour_foreground = "CYAN"
            weather_colour_background = "BLACK"
        elif weather_forecast in ["17","22","24"]:
            weather_pic = "]" #heavy rain
            weather_colour_foreground = "LIGHTBLUE"
            weather_colour_background = "BLACK"
        elif weather_forecast in ["25","26","-26"]:
            weather_pic = "^" #storm
            weather_colour_foreground = "RED"
            weather_colour_background = "BLACK"
        #elif weather_forecast in []:
        #    weather_pic = "%" #snow
        #    weather_colour_foreground = self.colours.Background.BLACK
        #    weather_colour_background = self.colours.Foreground.WHITE
        else:
            weather_pic = "`"
            weather_colour_foreground = "BLACK"
            weather_colour_background = "WHITE"

        compass_points = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        try:
            compass_direction = compass_points[int(float(weather_wind_direction_degrees)*16/360)]
        except:
            compass_direction = "?"

        self.move_cursor(x=1)
        self.add_text(u"\u250C" + u"\u2500"*9 + " O U T S I D E "+u"\u2500"*11+u"\u2510")
        self.move_cursor(x=41)
        self.add_text(u"\u250C" + u"\u2500"*11 + " I N S I D E "+u"\u2500"*11+u"\u2510")
        self.move_cursor(x=0,y=8)
        self.add_title(outside_weather+"    ",bg=outside_weather_foreground, fg=outside_weather_background, pre=3, fill=False)
        self.move_cursor(x=0,y=8)
        self.add_title(weather_pic,bg=weather_colour_foreground, fg=weather_colour_background, pre=20, fill=False)

        self.move_cursor(x=0,y=8)
        self.add_title(inside_weather+"    ",bg=inside_weather_foreground, fg=inside_weather_background, pre=43, fill=False)
        self.move_cursor(x=0,y=8)
        self.add_title(inside_weather_pic,bg=inside_weather_colour_foreground, fg=inside_weather_colour_background, pre=60, fill=False)
        self.move_cursor(x=1)
        self.add_text(u"\u2514" + u"\u2500"*35+u"\u2518")
        self.move_cursor(x=41)
        self.add_text(u"\u2514" + u"\u2500"*35+u"\u2518")
        self.add_newline()
        self.add_text("""
    Wind                """ + round_me(weather_wind_speed) + "mph " + compass_direction + """
    Max/Min Today       """ + weather_high_temp + u"\u00B0" + "C / " + weather_low_temp + u"\u00B0" + """C
    Outdoor Humidity    """ + weather_humidity + """%
    Pressure            """ + round_me(weather_pressure) + """ hPa
    Daily Rain          """ + weather_rain_today + """ mm
    Cloud Height        """ + round_me(weather_cloud_height,10) + """ ft
    """)

def round_me(n,i=1):
    try:
        return str(int(round(float(n)/i)*i))
    except:
        return n

class WeatherForePage(Page):
    def __init__(self):
        super(WeatherForePage, self).__init__("321")
        self.title = "Weather Forecast Day"
        self.in_index=False

    def background(self):
        import metoffer
        M = metoffer.MetOffer(config.metoffer_api_key);
        #x = M.nearest_loc_forecast(51.4033, -0.3375, metoffer.THREE_HOURLY)
        x = M.nearest_loc_forecast(*config.location, metoffer.THREE_HOURLY)
        self.y = metoffer.parse_val(x)

        self.tagline = "Live from the Met Office"

    def generate_content(self):
        from fonts import weather_symbol
        self.add_title("24-hr Weather",fg="CYAN",bg="BRIGHTWHITE")

        day_weather = []
        day_max = []
        day_min = []
        date = []
        for i in self.y.data:
            if i["timestamp"][0] > datetime.datetime.now() - datetime.timedelta(hours=1.9):
                day_weather.append(weather_symbol(i["Weather Type"][0]))
                day_max.append(i["Temperature"][0])
                date.append((i["timestamp"][0].strftime("%-I%p")).replace("am",u"㏂").replace("pm",u"㏘"))

        self.tagline = "Met Office, updated " + datetime.datetime.strptime(self.y.data_date,'%Y-%m-%dT%H:%M:%SZ').strftime("%a %d %b %H:%M")

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

class WeatherFore2Page(Page):
    def __init__(self):
        super(WeatherFore2Page, self).__init__("322")
        self.title = "Weather Forecast"
        self.in_index = False

    def background(self):
        import metoffer

        M = metoffer.MetOffer(config.metoffer_api_key);
        #x = M.nearest_loc_forecast(51.4033, -0.3375, metoffer.THREE_HOURLY)
        x = M.nearest_loc_forecast(*config.location, metoffer.DAILY)
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

class SunrisePage(Page):
    def __init__(self):
        super(SunrisePage, self).__init__("323")
        self.title = "Sunrise & sunset"
        self.in_index = False
        self.tagline = "Here comes the sun"

    def generate_content(self):
        from astral import Astral
        city_name = 'London'
        a = Astral()
        a.solar_depression = 'civil'
        city = a[city_name]
        sun = city.sun(local=True)
        sunrise = sun['sunrise'].strftime("%H:%M")
        sunset = sun['sunset'].strftime("%H:%M")

        self.add_title("Sunrise/sunset")
        self.add_title(" * "+sunrise, bg="YELLOW",fg="BLACK")
        self.add_title(" } "+sunset, bg="LIGHTRED",fg="BLACK")

class UKTempPage(Page):
    def __init__(self):
        super(UKTempPage, self).__init__("324")
        self.title = "UK Temperature"
        self.tagline = "Why exactly do we live in Britain?"
        self.in_index = False
        from helpers.file_handler import load_file
        self.ordered_ids = [i.rstrip("\n") for i in load_file("uk_coordinate_ids.txt").split("\n")]
        self.temps = [99 for i in range(len(self.ordered_ids))]


    def background(self):
        from helpers import url_handler
        import json
        from time import sleep


        i = 0

        step = 30
        try:
            for j in range(0,len(self.ordered_ids),step):
                url = "http://api.openweathermap.org/data/2.5/group?id=" + ",".join(self.ordered_ids[j:j+step]) + "&units=metric&appid=" + config.open_weather_api_key
                data = url_handler.load_json(url)
                for city in data['list']:
                    self.temps[i] = float(city['main']['temp'])
                    i+=1
                #sleep(5)
        except:
            pass

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

        boundaries = [-99,0,3,6,9,12,15,18,21,24,98]
        colours_before = ["BLUE","LIGHTBLUE","LIGHTCYAN","CYAN","GREEN","LIGHTGREEN","YELLOW","ORANGE","LIGHTRED","RED","BRIGHTWHITE"]

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

class WorldTempPage(Page):
    def __init__(self):
        super(WorldTempPage, self).__init__("325")
        self.title = "World Temperature"
        self.in_index = False
        self.tagline = "Why exactly do we live in Britain?"

    def background(self):
        self.data = url_handler.load_json("http://api.openweathermap.org/data/2.5/group?id=5368361,5128638,3530597,2643743,2968815,2950158,3169070,344979,1820906,1816670,1850147,7839805&units=metric&appid="+config.open_weather_api_key)

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

weather_page = WeatherPage()
weather_page2 = WeatherForePage()
weather_page3 = WeatherFore2Page()
sunrise_page = SunrisePage()
uktemp_page = UKTempPage()
worldtemp_page = WorldTempPage()


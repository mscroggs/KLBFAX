from page import Page
from file_handler import f_read


class WeatherPage(Page):
    def __init__(self):
        super(WeatherPage, self).__init__("410")
        self.title = "Weather"
        self.index_num = "410-415"

    def background(self):
        import urllib2
        try:
            response = urllib2.urlopen("http://weather.casa.ucl.ac.uk/realtime.txt")
            self.weather_data = response.read().split(" ")
        except:
            self.weather_data = ["CLASSIFIED"]*60
        # Field # Example 	Description 	Equivalent Webtags
        # 1 	19/08/09 	Date as 2 figure day [separator] 2 figure month [separator] 2 figure year - the separator is that set in the windows system short date format (see setup) 	<#date>
        # 2 	16:03:45 	time(always hh:mm:ss as per computer system) 	<#timehhmmss>
        # 3 	8.4 	outside temperature 	<#temp>
        # 4 	84 	relative humidity 	<#hum>
        # 5 	5.8 	dewpoint 	<#dew>
        # 6 	24.2 	wind speed (average) 	<#wspeed>
        # 7 	33.0 	latest wind speed reading 	<#wlatest>
        # 8 	261 	wind bearing (degrees) 	<#bearing>
        # 9 	0.0 	current rain rate (per hour) 	<#rrate>
        # 10 	1.0 	rain today 	<#rfall>
        # 11 	999.7 	barometer (The sea level pressure) 	<#press>
        # 12 	W 	current wind direction (compass point) 	<#currentwdir>
        # 13 	6 	wind speed (beaufort) 	<#beaufortnumber>
        # 14 	km/h 	wind units - m/s, mph, km/h, kts 	<#windunit>
        # 15 	C 	temperature units - degree C, degree F 	<#tempunitnodeg>
        # 16 	hPa 	pressure units - mb, hPa, in 	<#pressunit>
        # 17 	mm 	rain units - mm, in 	<#rainunit>
        # 18 	146.6 	wind run (today) 	<#windrun>
        # 19 	+0.1 	pressure trend value (The average rate of pressure change over the last three hours) 	<#presstrendval>
        # 20 	85.2 	monthly rainfall 	<#rmonth>
        # 21 	588.4 	yearly rainfall 	<#ryear>
        # 22 	11.6 	yesterday's rainfall 	<#rfallY>
        # 23 	20.3 	inside temperature 	<#intemp>
        # 24 	57 	inside humidity 	<#inhum>
        # 25 	3.6 	wind chill 	<#wchill>
        # 26 	-0.7 	temperature trend value (The average rate of change in temperature over the last three hours) 	<#temptrend>
        # 27 	10.9 	today's high temp 	<#tempTH>
        # 28 	12:00 	time of today's high temp (hh:mm) 	<#TtempTH>
        # 29 	7.8 	today's low temp 	<#tempTL>
        # 30 	14:41 	time of today's low temp (hh:mm) 	<#TtempTL>
        # 31 	37.4 	today's high wind speed (of average as per choice) 	<#windTM>
        # 32 	14:38 	time of today's high wind speed (average) (hh:mm) 	<#TwindTM>
        # 33 	44.0 	today's high wind gust 	<#wgustTM>
        # 34 	14:28 	time of today's high wind gust (hh:mm) 	<#TwgustTM>
        # 35 	999.8 	today's high pressure 	<#pressTH>
        # 36 	16:01 	time of today's high pressure (hh:mm) 	<#TpressTH>
        # 37 	998.4 	today's low pressure 	<#pressTL>
        # 38 	12:06 	time of today's low pressure (hh:mm) 	<#TpressTL>
        # 39 	1.8.7 	Cumulus Versions (the specific version in use) 	<#version>
        # 40 	819 	Cumulus build number 	<#build>
        # 41 	36.0 	10-minute high gust 	<#wgust>
        # 42 	10.3 	Heat index 	<#heatindex>
        # 43 	10.5 	Humidex 	<#humidex>
        # 44 	13 	UV Index 	<#UV>
        # 45 	0.2 	evapotranspiration today 	<#ET>
        # 46 	14 	solar radiation W/m2 	<#SolarRad>
        # 47 	260 	10-minute average wind bearing (degrees) 	<#avgbearing>
        # 48 	2.3 	rainfall last hour 	<#rhour>
        # 49 	3 	The number of the current (Zambretti) forecast as per Strings.ini. 	<#forecastnumber>
        # 50 	1 	Flag to indicate that the location of the station is currently in daylight (1 = yes, 0 = No) 	<#isdaylight>
        # 51 	1 	If the station has lost contact with its remote sensors "Fine Offset only", a Flag number is given (1 = Yes, 0 = No) 	<#SensorContactLost>
        # 52 	NNW 	Average wind direction 	<#wdir>
        # 53 	2040 	Cloud base 	<#cloudbasevalue>
        # 54 	ft 	Cloud base units 	<#cloudbaseunit>
        # 55 	12.3 	Apparent temperature 	<#apptemp>
        # 56 	11.1 	Sunshine hours so far today 	<#SunshineHours>
        # 57 	420.1 	Current theoretical max solar radiation 	<#CurrentSolarMax>
        # 58 	1 	Is it sunny? 1 if the sun is shining, otherwise 0 (above or below threshold) 	<#IsSunny>


    def generate_content(self):
        weather_date = self.weather_data[0]
        weather_time = self.weather_data[1]
        weather_temperature = self.weather_data[2]
        weather_humidity = self.weather_data[3]
        weather_wind_speed = self.weather_data[5]
        weather_wind_direction_degrees = self.weather_data[7]
        weather_rain_today = self.weather_data[9]
        weather_pressure = self.weather_data[10]

        weather_high_temp = self.weather_data[26]
        weather_low_temp = self.weather_data[28]

        weather_cloud_height = self.weather_data[52]
        weather_forecast = self.weather_data[48]
        weather_daylight = self.weather_data[49]

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
            weather_pic = "[" #light rain
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

weather_page = WeatherPage()

def round_me(n,i=1):
    try:
        return str(int(round(float(n)/i)*i))
    except:
        return n

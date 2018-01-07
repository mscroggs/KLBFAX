from page import Page
from file_handler import f_read
import url_handler

class WeatherPage(Page):
    def __init__(self):
        super(WeatherPage, self).__init__("320")
        self.title = "Weather"
        self.index_num = "320-325"

    def background(self):
        try:
            #response = url_handler.load("http://weather.casa.ucl.ac.uk/realtime.txt")
            response = url_handler.load("http://weather.casa.ucl.ac.uk/clientraw.txt")
            self.weather_data = response.split(" ")
        except:
            self.weather_data = ["CLASSIFIED"]*60
        ''' If using realtime.txt (no longer working on CASA website):
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
        '''
        # If using clientraw.txt:
        '''
        Field#  Label   Type    Contents
        000     Header  L   12345
        001     Avg Speed   K   7.6kts = 8.75mph = 14.08km/h
        002     Gusts   K   5.2kts = 5.98mph = 9.63km/h
        003     WindDir     D   320° (NW)
        004     Temp    C   5.3°C = 41.5°F
        005     Outside Humidity    P   64%
        006     Barometer   H   1024.0 hPa = 30.24 inHg
        007     Daily Rain  M   0.0mm = 0in
        008     Monthly Rain    M   25.7mm = 1.01in
        009     Yearly Rain     M   25.7mm = 1.01in
        010     Rain Rate   M   0.00mm = 0in
        011     Max Rain Rate   M   0.00mm = 0in
        012     Indoor Temp     C   23.2°C = 73.8°F
        013     Indoor Hum  P   26%
        014     Soil Temp   C   100.0°C = 212°F
        015     Forecast Icon   I   5 (Dry Clear)
        016     WMR968 Extra Temp   C   0.0°C = 32°F
        017     WMR968 Extra Hum    P   0%
        018     WMR968 Extra Sensor     N   0
        019     Yesterday Rain  M   0.0mm = 0in
        020     Extra Temp Sensor 1     C   12.8°C = 55°F
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
        044     WindChill   C   3.1°C = 37.6°F
        045     Humidex     C   2.9°C = 37.2°F
        046     Max Day Temp    C   7.1°C = 44.8°F
        047     Min Day Temp    C   3.8°C = 38.8°F
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
        072     DewPoint Temp   C   -0.9°C = 30.4°F
        073     Cloud Height    F   824 Meters - 2703.5Feet
        074     Date    L   1/7/2018
        075     Max Humidex     C   4.9°C = 40.8°F
        076     Min Humidex     C   1.6°C = 34.9°F
        077     Max Windchill   C   7.1°C = 44.8°F
        078     Min Windchill   C   -1.4°C = 29.5°F
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
        090     Hr Temp 01  C   6.0°C = 42.8°F
        091     Hr Temp 02  C   5.9°C = 42.6°F
        092     Hr Temp 03  C   6.0°C = 42.8°F
        093     Hr Temp 04  C   5.8°C = 42.4°F
        094     Hr Temp 05  C   5.8°C = 42.4°F
        095     Hr Temp 06  C   5.7°C = 42.3°F
        096     Hr Temp 07  C   5.6°C = 42.1°F
        097     Hr Temp 08  C   5.5°C = 41.9°F
        098     Hr Temp 09  C   5.4°C = 41.7°F
        099     Hr Temp 10  C   5.3°C = 41.5°F
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
        110     Max Heat Index  C   7.1°C = 44.8°F
        111     Min Heat Index  C   3.8°C = 38.8°F
        112     Heat Index  C   5.3°C = 41.5°F
        113     Max Avg Speed   K   13.1kts = 15.08mph = 24.26km/h
        114     # Lightning in last Min     N   0
        115     Time Last Lightning Strike  L   ---
        116     Date Last Lightning Strike  L   ---
        117     Wind Avg Dir    D   3° (N)
        118     Nexstorm Dist   L   0
        119     NexStorm Bearing    D   0° (N)
        120     Extra Temp Sensor 7     C   No Value
        121     Extra Temp Sensor 8     C   No Value
        122     Extra Hum Sensor 4  P   0%
        123     Extra Hum Sensor 5  P   No Value
        124     Extra Hum Sensor 6  P   No Value
        125     Extra Hum Sensor 7  P   No Value
        126     Extra Hum Sensor 8  P   No Value
        127     VP Solarwm  N   0.0
        128     Max InTemp  C   23.7°C = 74.7°F
        129     Min InTemp  C   22.9°C = 73.2°F
        130     Apparent Temp   C   1.4°C = 34.5°F
        131     Max Baro    H   1024.6 hPa = 30.26 inHg
        132     Min Baro    H   1019.0 hPa = 30.09 inHg
        133     Max Gust Last Hour  K   17kts = 19.56mph = 31.48km/h
        134     Max Gust Last Hour Time     L   3:51PM
        135     Max Gust Today Time     L   1:14 PM
        136     Max Apparent Temp   C   4.9°C = 40.8°F
        137     Min Apparent Temp   C   -0.3°C = 31.5°F
        138     Max Dew Pt  C   2.2°C = 36°F
        139     Min Dew Pt  C   -0.9°C = 30.4°F
        140     Max Gust In Lst Min     K   13kts = 14.96mph = 24.08km/h
        141     Current Year    L   2018
        142     THSWS   L   -17.8
        143     Temp Trend (Logic)  L   -1
        144     Humidity Trend (Logic)  L   -1
        145     Humidex Trend (Logic)   L   -1
        146     Hr Wind Dir 01  D   317° (NW)
        147     Hr Wind Dir 02  D   340° (NNW)
        148     Hr Wind Dir 03  D   300° (WNW)
        149     Hr Wind Dir 04  D   304° (WNW)
        150     Hr Wind Dir 05  D   19° (N)
        151     Hr Wind Dir 06  D   355° (NNW)
        152     Hr Wind Dir 07  D   288° (W)
        153     Hr Wind Dir 08  D   89° (ENE)
        154     Hr Wind Dir 09  D   306° (WNW)
        155     Hr Wind Dir 10  D   320° (NW)
        156     Leaf Wetness    C   0.0°C = 32°F
        157     Soil moisture   C   No Value
        158     10 Min Avg Wind Speed   K   5.9kts = 6.79mph = 10.93km/h
        159     Wet bulb temperature    C   3.0°C = 37.4°F
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
        weather_date = weather_date_list[1] + "/" + weather_date_list[0] + "/" + weather_date_list[2]
        weather_time = self.weather_data[29] + ":" + self.weather_data[30] + ":" + self.weather_data[31]
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

weather_page = WeatherPage()

def round_me(n,i=1):
    try:
        return str(int(round(float(n)/i)*i))
    except:
        return n

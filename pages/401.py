import os
from page import Page
from printer import instance as printer
from colours import colour_print
from random import randint
from file_handler import f_read


class WeatherPage(Page):
    def __init__(self, page_num):
        super(WeatherPage, self).__init__(page_num)
        self.title = "Weather"      

    def generate_content(self):
        import urllib2
        
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
                     
        try:
            response = urllib2.urlopen("http://weather.casa.ucl.ac.uk/realtime.txt")
            weather_data = response.read().split(" ")
        except:
            weather_data = ["CLASSIFIED"]*60
        '''

        Field # Example 	Description 	Equivalent Webtags
        1 	19/08/09 	Date as 2 figure day [separator] 2 figure month [separator] 2 figure year - the separator is that set in the windows system short date format (see setup) 	<#date>
        2 	16:03:45 	time(always hh:mm:ss as per computer system) 	<#timehhmmss>
        3 	8.4 	outside temperature 	<#temp>
        4 	84 	relative humidity 	<#hum>
        5 	5.8 	dewpoint 	<#dew>
        6 	24.2 	wind speed (average) 	<#wspeed>
        7 	33.0 	latest wind speed reading 	<#wlatest>
        8 	261 	wind bearing (degrees) 	<#bearing>
        9 	0.0 	current rain rate (per hour) 	<#rrate>
        10 	1.0 	rain today 	<#rfall>
        11 	999.7 	barometer (The sea level pressure) 	<#press>
        12 	W 	current wind direction (compass point) 	<#currentwdir>
        13 	6 	wind speed (beaufort) 	<#beaufortnumber>
        14 	km/h 	wind units - m/s, mph, km/h, kts 	<#windunit>
        15 	C 	temperature units - degree C, degree F 	<#tempunitnodeg>
        16 	hPa 	pressure units - mb, hPa, in 	<#pressunit>
        17 	mm 	rain units - mm, in 	<#rainunit>
        18 	146.6 	wind run (today) 	<#windrun>
        19 	+0.1 	pressure trend value (The average rate of pressure change over the last three hours) 	<#presstrendval>
        20 	85.2 	monthly rainfall 	<#rmonth>
        21 	588.4 	yearly rainfall 	<#ryear>
        22 	11.6 	yesterday's rainfall 	<#rfallY>
        23 	20.3 	inside temperature 	<#intemp>
        24 	57 	inside humidity 	<#inhum>
        25 	3.6 	wind chill 	<#wchill>
        26 	-0.7 	temperature trend value (The average rate of change in temperature over the last three hours) 	<#temptrend>
        27 	10.9 	today's high temp 	<#tempTH>
        28 	12:00 	time of today's high temp (hh:mm) 	<#TtempTH>
        29 	7.8 	today's low temp 	<#tempTL>
        30 	14:41 	time of today's low temp (hh:mm) 	<#TtempTL>
        31 	37.4 	today's high wind speed (of average as per choice) 	<#windTM>
        32 	14:38 	time of today's high wind speed (average) (hh:mm) 	<#TwindTM>
        33 	44.0 	today's high wind gust 	<#wgustTM>
        34 	14:28 	time of today's high wind gust (hh:mm) 	<#TwgustTM>
        35 	999.8 	today's high pressure 	<#pressTH>
        36 	16:01 	time of today's high pressure (hh:mm) 	<#TpressTH>
        37 	998.4 	today's low pressure 	<#pressTL>
        38 	12:06 	time of today's low pressure (hh:mm) 	<#TpressTL>
        39 	1.8.7 	Cumulus Versions (the specific version in use) 	<#version>
        40 	819 	Cumulus build number 	<#build>
        41 	36.0 	10-minute high gust 	<#wgust>
        42 	10.3 	Heat index 	<#heatindex>
        43 	10.5 	Humidex 	<#humidex>
        44 	13 	UV Index 	<#UV>
        45 	0.2 	evapotranspiration today 	<#ET>
        46 	14 	solar radiation W/m2 	<#SolarRad>
        47 	260 	10-minute average wind bearing (degrees) 	<#avgbearing>
        48 	2.3 	rainfall last hour 	<#rhour>
        49 	3 	The number of the current (Zambretti) forecast as per Strings.ini. 	<#forecastnumber>
        50 	1 	Flag to indicate that the location of the station is currently in daylight (1 = yes, 0 = No) 	<#isdaylight>
        51 	1 	If the station has lost contact with its remote sensors "Fine Offset only", a Flag number is given (1 = Yes, 0 = No) 	<#SensorContactLost>
        52 	NNW 	Average wind direction 	<#wdir>
        53 	2040 	Cloud base 	<#cloudbasevalue>
        54 	ft 	Cloud base units 	<#cloudbaseunit>
        55 	12.3 	Apparent temperature 	<#apptemp>
        56 	11.1 	Sunshine hours so far today 	<#SunshineHours>
        57 	420.1 	Current theoretical max solar radiation 	<#CurrentSolarMax>
        58 	1 	Is it sunny? 1 if the sun is shining, otherwise 0 (above or below threshold) 	<#IsSunny> 
        '''
        
        
        
        weather_date = weather_data[0]
        weather_time = weather_data[1]
        weather_temperature = weather_data[2]
        weather_humidity = weather_data[3]
        weather_wind_speed = weather_data[5]
        weather_wind_direction_degrees = weather_data[7]
        weather_rain_today = weather_data[9]
        weather_pressure = weather_data[10]

        weather_high_temp = weather_data[26]
        weather_low_temp = weather_data[28]

        weather_cloud_height = weather_data[52]
        weather_forecast = weather_data[48]
        weather_daylight = weather_data[49]

        tag = "Live data from CASA - " + weather_date + " " + weather_time
        content = colour_print(printer.text_to_ascii("weather", padding={"left": 6}),
                            self.colours.Background.CYAN, self.colours.Foreground.MAGENTA)

        content += "\n\n"
        outside_weather_foreground = self.colours.Background.BLUE
        outside_weather_background = self.colours.Foreground.CYAN+self.colours.Style.BOLD 
        inside_weather_foreground = self.colours.Background.BLUE
        inside_weather_background = self.colours.Foreground.CYAN+self.colours.Style.BOLD
        try:        
            inside_weather = f_read("temp_now")
            if int(inside_weather) >= 20:
                inside_weather_foreground = self.colours.Background.YELLOW+self.colours.Style.BLINK
                inside_weather_background = self.colours.Foreground.RED
            elif 10 <= int(inside_weather) < 20:
                inside_weather_foreground = self.colours.Background.RED
                inside_weather_background = self.colours.Foreground.YELLOW+self.colours.Style.BOLD
            elif 0 < int(inside_weather) < 10:
                inside_weather_foreground = self.colours.Background.BLUE
                inside_weather_background = self.colours.Foreground.GREEN+self.colours.Style.BOLD                
        except: 
            inside_weather = "??"
            
        try:
            outside_weather = str(int(round(float(weather_temperature))))
            if int(outside_weather) >= 20:
                outside_weather_foreground = self.colours.Background.YELLOW+self.colours.Style.BLINK
                outside_weather_background = self.colours.Foreground.RED
            elif 10 <= int(outside_weather) < 20:
                outside_weather_foreground = self.colours.Background.RED
                outside_weather_background = self.colours.Foreground.YELLOW+self.colours.Style.BOLD
            elif 0 < int(outside_weather) < 10:
                outside_weather_foreground = self.colours.Background.BLUE
                outside_weather_background = self.colours.Foreground.GREEN+self.colours.Style.BOLD
      
        except:
            outside_weather = "??"        
        
        #inside_weather = str(int(round(float(weather_temperature))))
        #outside_weather = str(int(round(float(weather_temperature))))   
        #inside_weather = str(randint(-9,30))
        #outside_weather = str(randint(-9,30))
             

        '''
        FORECASTS = ["Sunny", "Clear Night", "Cloudy", "Cloudy", "Cloudy Night", "Dry Clear", "Fog", "Hazy", "Heavy Rain",
                 "Mainly Fine", "Misty", "Night Fog", "Night Heavy Rain", "Night Overcast", "Night Rain",
                 "Night Showers", "Night Snow", "Night Thunder", "Overcast", "Partly Cloudy", "Rain", "Hard Rain",
                 "Showers", "Sleet", "Sleet Showers", "Snow", "Snow Melt", "Snow Showers", "Sunny", "Thunder Showers",
                 "Thunder Showers", "Thunderstorms", "Tornado Warning", "Windy", "Stopped Raining", "Windy Rain"]
        '''
		
        if weather_forecast in ["2","3","4","13","18","7"]:
            weather_pic = "@" #cloudy
            weather_colour_foreground = self.colours.Background.BLACK
            weather_colour_background = self.colours.Foreground.WHITE
        elif weather_forecast in ["0","5","28"] and weather_daylight == "1":
            weather_pic = "*" #sunny
            weather_colour_foreground = self.colours.Background.YELLOW
            weather_colour_background = self.colours.Foreground.BLACK  
        elif weather_forecast == "1" or (weather_forecast in ["0","5","28"] and weather_daylight == "0"):
            weather_pic = "}" #moon
            weather_colour_foreground = self.colours.Background.YELLOW
            weather_colour_background = self.colours.Foreground.BLACK              
        elif weather_data[48] in ["8","12","14","15","20","21","22","35","3"]:
            weather_pic = "{" #rain
            weather_colour_foreground = self.colours.Background.CYAN
            weather_colour_background = self.colours.Foreground.BLACK    
        elif weather_data[48] in ["9","19"]:
            weather_pic = "~" #cloud sun
            weather_colour_foreground = self.colours.Background.BLACK
            weather_colour_background = self.colours.Foreground.WHITE
        elif weather_data[48] in ["29","30","31","32"]:
            weather_pic = "^" #storm
            weather_colour_foreground = self.colours.Background.RED
            weather_colour_background = self.colours.Foreground.BLACK       
        elif weather_data[48] in ["23","24","25","26","27"]:
            weather_pic = "%" #snow
            weather_colour_foreground = self.colours.Background.BLACK
            weather_colour_background = self.colours.Foreground.WHITE
        else:
            weather_pic = "`"
            weather_colour_foreground = self.colours.Background.BLACK
            weather_colour_background = self.colours.Foreground.WHITE            
        
        compass_points = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        try:
            compass_direction = compass_points[int(float(weather_wind_direction_degrees)*16/360)]
        except:
            compass_direction = "?"
			
        content += " /--------- O U T S I D E -----------|   /---------- I N S I D E ------------|\n".replace("-",u"\u2500").replace("/",u"\u250C").replace("|",u"\u2510")
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii("|",False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK), 
                        (printer.text_to_ascii(number_in_box(outside_weather)[0],False),
                            outside_weather_foreground,
                            outside_weather_background),
                        (printer.text_to_ascii(number_in_box(outside_weather)[1],False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK),                             
                        (printer.text_to_ascii(weather_pic,False)+"",
                            weather_colour_foreground,
                            weather_colour_background),
                        (printer.text_to_ascii("||||||",False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK), 
                        (printer.text_to_ascii(number_in_box(inside_weather)[0],False)+"",
                            inside_weather_foreground,
                            inside_weather_background),
                        (printer.text_to_ascii(number_in_box(inside_weather)[1],False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK),  
                        (printer.text_to_ascii("*",False)+"",
                            self.colours.Background.YELLOW,
                            self.colours.Foreground.BLACK)
                    ],""," ")       

        content += "\n"
        content += " /-----------------------------------|   /-----------------------------------|\n".replace("-",u"\u2500").replace("/",u"\u2514").replace("|",u"\u2518")						
        content += """
    Wind                """ + round_me(weather_wind_speed) + "mph " + compass_direction + """
    Max/Min Today       """ + weather_high_temp + u"\u00B0" + "C / " + weather_low_temp + u"\u00B0" + """C
    Outdoor Humidity    """ + weather_humidity + """%
    Pressure            """ + round_me(weather_pressure) + """ hPa
    Daily Rain          """ + weather_rain_today + """ mm  
    Cloud Height        """ + round_me(weather_cloud_height,10) + """ ft  
    """
        self.content = content
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
weather_page = WeatherPage(page_number)

def round_me(n,i=1):
    try:
        return str(int(round(float(n)/i)*i))
    except:
        return n

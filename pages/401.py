import os
from page import Page
from printer import instance as printer
from colours import colour_print


class WeatherPage(Page):
    def __init__(self, page_num):
        super(WeatherPage, self).__init__(page_num)
        self.title = "Weather"

    def generate_content(self):
        import urllib2

        #response = urllib2.urlopen("http://www.casa.ucl.ac.uk/weather/clientraw.txt")
        response = urllib2.urlopen("http://weather.casa.ucl.ac.uk/realtime.txt")
        weather_data = response.read().split(" ")
        tag = "Live data from CASA - " + weather_data[29] + ":" + weather_data[30] + ":" + weather_data[31]
        content = colour_print(printer.text_to_ascii("weather", padding={"left": 6}),
                            self.colours.Background.CYAN, self.colours.Foreground.MAGENTA)

        content += "\n\n"
        inside_weather = "|" + str(int(round(float(weather_data[4])))) + "|"
        outside_weather = str(int(round(float(weather_data[4]))))

        '''
    FORECASTS = ["Sunny", "Clear Night", "Cloudy", "Cloudy", "Cloudy Night", "Dry Clear", "Fog", "Hazy", "Heavy Rain",
                 "Mainly Fine", "Misty", "Night Fog", "Night Heavy Rain", "Night Overcast", "Night Rain",
                 "Night Showers", "Night Snow", "Night Thunder", "Overcast", "Partly Cloudy", "Rain", "Hard Rain",
                 "Showers", "Sleet", "Sleet Showers", "Snow", "Snow Melt", "Snow Showers", "Sunny", "Thunder Showers",
                 "Thunder Showers", "Thunderstorms", "Tornado Warning", "Windy", "Stopped Raining", "Windy Rain"]
        '''
		
        if weather_data[48] in ["2","3","4","13","18"]:
            weather_pic = "@" #cloudy
            weather_colour_foreground = self.colours.Background.BLACK
            weather_colour_background = self.colours.Foreground.WHITE
        elif weather_data[48] in ["0","5","28"]:
            weather_pic = "*" #sunny
            weather_colour_foreground = self.colours.Background.YELLOW
            weather_colour_background = self.colours.Foreground.BLACK  
        elif weather_data[48] == "1":
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
        
        compass_points = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        compass_direction = compass_points[int(float(weather_data[3])*16/360)]

        with open(os.path.join(os.path.expanduser("~"),".graphs/temp_now")) as f:
            inside_weather = f.read()
			
        content += " /--------- O U T S I D E ----------|     /---------- I N S I D E -----------|\n".replace("-",u"\u2500").replace("/",u"\u250C").replace("|",u"\u2510")
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii("|",False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK), 
                        (printer.text_to_ascii(outside_weather,False)+"",
                            self.colours.Background.RED,
                            self.colours.Foreground.YELLOW+self.colours.Style.BOLD),
                        (printer.text_to_ascii(weather_pic,False)+"",
                            weather_colour_foreground,
                            weather_colour_background),
                        (printer.text_to_ascii("||||||||",False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK), 
                        (printer.text_to_ascii(inside_weather,False)+"",
                            self.colours.Background.RED,
                            self.colours.Foreground.YELLOW+self.colours.Style.BOLD),
                        (printer.text_to_ascii("*",False)+"",
                            self.colours.Background.YELLOW,
                            self.colours.Foreground.BLACK)
                    ]," "," ")       

        content += "\n"
        content += " /----------------------------------|     /----------------------------------|\n".replace("-",u"\u2500").replace("/",u"\u2514").replace("|",u"\u2518")						
        content += """
    Wind                """ + str(int(float(weather_data[1])*1.15077945)) + "mph " + compass_direction + """
    Max/Min Today       """ + weather_data[46] + u"\u00B0" + "C / " + weather_data[47] + u"\u00B0" + """C
    Outdoor Humidity    """ + weather_data[5] + """%
    Pressure            """ + str(int(float(weather_data[6]))) + """ hPa
    Daily Rain          """ + weather_data[7] + """ mm    
    Cloud Height        """ + str(int(round(float(weather_data[73])/10)*10)) + """ ft    
    Soil Temperature    """ + weather_data[13] + "" + u"\u00B0" + """C
    """
        self.content = content
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
weather_page = WeatherPage(page_number)

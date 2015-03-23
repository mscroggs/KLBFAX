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

        response = urllib2.urlopen("http://www.casa.ucl.ac.uk/weather/clientraw.txt")
        weather_data = response.read().split(" ")
        tag = "Live data from CASA - " + weather_data[29] + ":" + weather_data[30] + ":" + weather_data[31]
        page = colour_print(printer.text_to_ascii("weather", padding={"left": 6}),
                            self.colours.Background.CYAN, self.colours.Foreground.MAGENTA) + """

    Average Wind Speed  """ + weather_data[1] + """kts
    Gusts               """ + weather_data[2] + """kts
    Wind Direction      """ + weather_data[3] + u"\u00B0" + """
    Outdoor Temperate   """ + weather_data[4] + u"\u00B0" + """C
    Max Temperate Today """ + weather_data[46] + u"\u00B0" + """C
    Min Temperate Today """ + weather_data[47] + u"\u00B0" + """C
    Outdoor Humidity    """ + weather_data[5] + """%
    Pressure            """ + weather_data[6] + """hPa
    Daily Rain          """ + weather_data[7] + """mm
    Monthly Rain        """ + weather_data[8] + """mm
    Yearly Rain         """ + weather_data[9] + """mm
    Rain Rate           """ + weather_data[10] + """mm
    Soil Temperature    """ + weather_data[13] + u"\u00B0" + """C
    Current Weather     """ + weather_data[49] + """
    Cloud Height        """ + weather_data[73] + """m
    Last Lightning      """ + weather_data[116] + " " + weather_data[115]+"""
    """
        self.content = page
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
weather_page = WeatherPage(page_number)

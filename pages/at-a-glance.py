#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page import Page
from helpers import url_handler
import datetime
import config
import metoffer
import tubestatus



class AtAGlancePage(Page):
    def __init__(self, number):
        super(AtAGlancePage, self).__init__(number)
        self.title = "Dashboard"
        self.index_num = "699"
        self.in_index = True
        self.importance = 5

    def background(self):

        M = metoffer.MetOffer(config.metoffer_api_key);
        x = M.nearest_loc_forecast(config.location[0],config.location[1], metoffer.DAILY)
        x2 = M.nearest_loc_forecast(config.location[0],config.location[1], metoffer.THREE_HOURLY)
        if int(metoffer.__version__[0]) < 2:
            self.y = metoffer.parse_val(x)
            self.y2 = metoffer.parse_val(x2)
        else:
            self.y = metoffer.Weather(x) # for MetOffer v2
            self.y2 = metoffer.Weather(x2) # for MetOffer v2

        import feedparser
        from functions import replace
        rss_url = "http://feeds.bbci.co.uk/news/rss.xml?edition=uk"
        feed = feedparser.parse(rss_url)
        if 'entries' in feed and len(feed['entries']) > 0:
            item = feed['entries'][0]
            self.words = replace(item["title"]).split(" ")
        else:
            self.words = []

        # Create a new status object for retrieving data
        #from IPython import embed
        #embed()
        self.current_status = tubestatus.Status()
        self.tagline = "Everything you need"


    def generate_content(self):

        self.add_title(self.title,font='size4')
        import datetime, pytz
        from fonts import weather_symbol
        from fonts.weather_symbols import weather_arrow
        import random

        # Grid

        self.move_cursor(y=3,x=0)
        grid = u'''
┌────────────────────────────┬─────────────────────────────────────┬──────────┐
│ TODAY 330-331              │        TODAY FATE SMILES ON         │ TUBE 849 │
│                            │                                     │          │
│                            │                                     │          │
│                            │                                     │          │
│                            │                                     │          │
│                            │                                     │          │
│                            │                                     │          │
│                            ├─────────────────────────────────────┤          │
│                            │                                 SUN │          │
│                            │                                     │          │
│ NOW                        │                                     │          │
│                            │                                 332 │          │
├────────────────────────────┴─────────────────────────────────────┤          │
│                                                                  │          │
│                                                                  │          │
│                                                                  │          │
│                                                                  ├──────────┤
│                                                                  │ BIKE 824 │
│                                                                  │ Ev XX/YY │
│                                                                  │ IC XX/YY │
│                                                          ... 301 │ QG XX/YY │
└──────────────────────────────────────────────────────────────────┴──────────┘
'''
        self.add_text(grid)

        # Sunrise
        from astral import Astral
        city_name = 'London'
        a = Astral()
        a.solar_depression = 'civil'
        city = a[city_name]
        sun = city.sun(local=True)
        sunrise = sun['sunrise'].strftime("%H:%M")
        sunset = sun['sunset'].strftime("%H:%M")

        self.move_cursor(y=13,x=0)
        now = datetime.datetime.now(pytz.timezone('Europe/London'))
        if now < sun['sunrise'] or now > sun['sunset']:
            self.add_title(u"▲ " + str(sunrise),bg="YELLOW",fg="BLACK",fill=False,font='size4',pre=31)
        else:
            self.add_title(u"▼ " + str(sunset),bg="LIGHTRED",fg="BLACK",fill=False,font='size4',pre=31)


        # Weather
        weather_data = self.y.data[0]
        weather_data2 = self.y.data[1]

        s = -1
        for i in self.y2.data:
            if s == -1:
                timestamp_gmt = pytz.utc.localize(i["timestamp"][0])
                timestamp_local = timestamp_gmt.astimezone(pytz.timezone('Europe/London'))
                if timestamp_gmt > datetime.datetime.now(pytz.utc) - datetime.timedelta(hours=1.5):
                    weather_data_now = i

        #weather_data_now = self.y2.data[s]
        if weather_data["timestamp"][1] == "Day":
            if now < sun['sunset']:
                weather_symbol = weather_symbol(weather_data["Weather Type"][0])
            else:
                weather_symbol = weather_symbol(weather_data2["Weather Type"][0])
            day_max = weather_data["Day Maximum Temperature"][0]
            day_min = weather_data2["Night Minimum Temperature"][0]
        else:
            weather_symbol = weather_symbol(weather_data["Weather Type"][0])
            day_max = ''
            day_min = weather_data["Night Minimum Temperature"][0]
        #precip_chance = weather_data["Precipitation Probability Day"][0]

        #from IPython import embed
        #embed()
        temp_now = weather_data_now["Temperature"][0]
        wind_speed = weather_data_now["Wind Speed"][0]
        wind_direction = weather_data_now["Wind Direction"][0]

        self.print_image(weather_symbol,6,1)
        self.move_cursor(y=5,x=0)
        self.add_title(str(day_max),bg="YELLOW",fg="BLACK",fill=False,font='size4',pre=17)
        self.move_cursor(y=9,x=0)
        self.add_title(str(day_min),bg="LIGHTRED",fg="BLACK",fill=False,font='size4',pre=17)
        self.move_cursor(y=13,x=0)
        self.add_title(str(temp_now),bg="YELLOW",fg="BLACK",fill=False,font='size4',pre=17)
        self.print_image(weather_arrow(wind_direction),14,9)
        self.move_cursor(y=15,x=12)
        self.start_fg_color('CYAN')
        self.add_text(str(wind_speed))
        self.end_fg_color()
        '''
        if len(str(precip_chance)) == 2:
            pre = 1
        else:
            pre = 6
        self.add_title(str(precip_chance),bg="CYAN",fg="BLACK",fill=False,font='size4',pre=pre)
        self.move_cursor(y=13,x=0)
        if len(str(precip_chance)) == 2:
            pre = 14
        else:
            pre = 19
        self.add_title(str(wind_speed),bg="CYAN",fg="BLACK",fill=False,font='size4',pre=pre)

        self.move_cursor(x=25,y=14)
        self.start_fg_color('CYAN')
        self.add_text(wind_direction)
        self.end_fg_color()
        #self.add_title(,bg="CYAN",fg="BLACK",fill=False,font='size4',pre=32)
        '''

        #self.move_cursor(y=5,x=0)
        #self.add_title(u"▲ " + str(sunrise),bg="YELLOW",fg="BLACK",fill=False,font='size4',pre=31)
        #self.move_cursor(y=9,x=0)
        #self.add_title(u"▼ " + str(sunset),bg="LIGHTRED",fg="BLACK",fill=False,font='size4',pre=31)

        # Tube status
        #import tubestatus
        # Create a new status object for retrieving data
        lines = self.current_status.list_lines()
        # Loop through the lines and print the status of each one
        lines_tube = ['Bakerloo','Central','Circle','District', 'Hammersmith and City', 'Jubilee',
                      'Metropolitan', 'Northern', 'Piccadilly', 'Victoria', 'Waterloo and City']
        lines_other = ['DLR', 'Overground', 'TfL Rail', 'Trams']

        colours_tube = ["ORANGE","RED","YELLOW","GREEN","PINK","GREY","MAGENTA","DEFAULT","BLUE","LIGHTBLUE","LIGHTCYAN"]
        colours_tube_text = ["WHITE","WHITE","BLACK","BLACK","BLACK","WHITE","WHITE","WHITE","WHITE","WHITE","BLACK"]

        colours_other = ["CYAN","ORANGE","BLUE","LIGHTGREEN"]
        colours_other_text = ["BLACK","BLACK","WHITE","BLACK"]

        l = 0
        for line,fg,bg in zip(lines_tube + lines_other,colours_tube_text+colours_other_text,colours_tube+colours_other):
            desc = self.current_status.get_status(line).description
            self.move_cursor(x=69,y=6+l)
            self.start_fg_color(fg)
            self.start_bg_color(bg)
            self.add_text(str(line)[0:3])
            self.end_bg_color()
            self.end_fg_color()

            self.move_cursor(x=74,y=6+l)

            if desc == "Good Service":
                self.start_bg_color("GREEN")
            elif desc == "Minor Delays":
                self.start_bg_color("YELLOW")
            elif desc == "Part Closure":
                self.start_bg_color("ORANGE")
            else:
                self.start_bg_color("LIGHTRED")
            self.add_text("   ")
            self.end_bg_color()

            l = l+1

        # News
        def width_of_word(word):
            width = len(word)*5 \
            - sum(map(word.count, u"!:,‘’.'I’"))*3 \
            - sum(map(word.count, u"-()1"))*2 \
            - sum(map(word.count, u"T"))*1 \
            + sum(map(word.count, u"MW"))*1 \
            - sum(map(word.count, u"il"))*3 \
            - sum(map(word.count, u"fjt"))*2 \
            - sum(map(word.count, u"abcdeghknopqrsuvxyz"))*1 \
            + sum(map(word.count, u"mw"))*1
            return width

        chars_left = 67
        line = ""
        self.move_cursor(y=18,x=0)
        num_lines = 0
        for word in self.words:
            #from IPython import embed
            #embed()
            if num_lines < 2:
                if chars_left - width_of_word(word) <= 0:
                    chars_left = 67
                    self.add_title(line,bg="YELLOW",fg="BLACK",font="size4",pre=1,fill=False)
                    line = word + " "
                    num_lines = num_lines + 1
                else:
                    line = line + word + " "
                chars_left = chars_left - width_of_word(word) - 3
        #self.add_title(line,bg="YELLOW",fg="BLACK",font="size4")

        self.move_cursor(y=25,x=63)
        self.add_text("301")

        # Nonsense of the day stuff

        person_of_the_day = random.choice(["Pichael", "Scroggs", "Alan", "Adam", "Weiguan", "Chunxin", "Honest Bob", "Aurateur"])
        tube_line_of_the_day = random.choice(lines_tube)
        food_of_the_day = random.choice(["Katsu curry", "Tofe", "Risotto", "Fish pie", "Pizza", "Curry", "Wedges", "Sweet potato curry"])
        hour_of_the_day = random.choice(["Midnight", "1 am", "2 am", "3 am", "4 am", "5 am", "6 am", "7 am", "8 am", "9 am", "10 am", "11 am", "Noon", "1 pm", "2 pm", "3 pm", "4 pm", "5 pm", "6 pm", "7 pm", "8 pm", "9 pm", "10 pm", "11 pm", "The witching hour"])


        self.move_cursor(y=7,x=31)
        self.add_text("Person:    ")
        self.start_fg_color("YELLOW")
        self.add_text(person_of_the_day.upper())
        self.end_fg_color()

        self.move_cursor(y=8,x=31)
        self.add_text("Tube line: ")
        self.start_fg_color("YELLOW")
        self.add_text(tube_line_of_the_day.upper())
        self.end_fg_color()

        self.move_cursor(y=9,x=31)
        self.add_text("Food:      ")
        self.start_fg_color("YELLOW")
        self.add_text(food_of_the_day.upper())
        self.end_fg_color()

        self.move_cursor(y=10,x=31)
        self.add_text("Hour:      ")
        self.start_fg_color("YELLOW")
        self.add_text(hour_of_the_day.upper())
        self.end_fg_color()


        # Bikes
        docks_set1 = ['BikePoints_131']
        docks_set2 = ['BikePoints_392','BikePoints_350']

        bike_data = url_handler.load_json("https://api.tfl.gov.uk/bikepoint")

        docks_dict = dict()
        for dock in bike_data:
            docks_dict[dock['id']] = [dock['commonName'],int(dock['additionalProperties'][6]['value']), int(dock['additionalProperties'][7]['value']), int(dock['additionalProperties'][8]['value']), dock['additionalProperties'][4]['modified']  ]

        docks_data = []

        for dock_id in docks_set1 + docks_set2:
            if dock_id == -1:
                docks_data.append(("", "", ""))
            else:
                dock_data = docks_dict[dock_id]
                dock_name = dock_data[0].replace(" ,",",")
                docked_bikes = "{:2d}".format(dock_data[1])
                empty_docks = "{:2d}".format(dock_data[2])
                broken_bikes = "{:6d}".format((dock_data[3]) - int(empty_docks) - int(docked_bikes));
                data_date = dock_data[4];

                docks_data.append((dock_name, docked_bikes, empty_docks))

        #self.move_cursor(x=72,y=25)
        #self.add_text("HELLO")
        for i in range(3):
            self.move_cursor(x=72,y=23+i)
            self.start_fg_color("LIGHTGREEN")
            self.add_text(docks_data[i][1])
            self.end_fg_color()
            self.add_text("/")
            self.start_fg_color("LIGHTRED")
            self.add_text(docks_data[i][2])
            self.end_fg_color()


page0 = AtAGlancePage("699")

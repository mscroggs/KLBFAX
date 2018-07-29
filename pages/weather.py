from page import Page
from helpers import url_handler
import datetime
import config
import metoffer

class WeatherPage(Page):
    def __init__(self):
        super(WeatherPage, self).__init__("330")

def round_me(n,i=1):
    try:
        return str(int(round(float(n)/i)*i))
    except:
        return n


class WeatherForePage(Page):
    def __init__(self, number, ftype):
        super(WeatherForePage, self).__init__(number)
        self.ftype = ftype
        self.title = "Weather"
        if number == "330":
            self.index_num = "330-334"
            self.in_index = True
        else:
            self.in_index = False

    def background(self):
        M = metoffer.MetOffer(config.metoffer_api_key);
        x = M.nearest_loc_forecast(config.location[0],config.location[1], self.ftype)
        self.y = metoffer.Weather(x)

        self.tagline = "Live from the Met Office"

    def generate_content(self):
        from fonts import weather_symbol
        if self.ftype == metoffer.THREE_HOURLY:
            self.add_title("24-hr Weather",fg="CYAN",bg="BRIGHTWHITE")
        if self.ftype == metoffer.DAILY:
            self.add_title("4-day Weather",fg="CYAN",bg="BRIGHTWHITE")

        day_weather = []
        day_max = []
        day_min = []
        date = []
        for i in self.y.data:
            day_weather.append(weather_symbol(i["Weather Type"][0]))
            if self.ftype == metoffer.THREE_HOURLY and i["timestamp"][0] > datetime.datetime.now() - datetime.timedelta(hours=1.9):
                day_max.append(i["Temperature"][0])
                date.append((i["timestamp"][0].strftime("%-I%p")).replace("am",u"㏂").replace("pm",u"㏘"))
            if self.ftype == metoffer.DAILY:
                if i["timestamp"][1] == "Day":
                    day_max.append(i["Feels Like Day Maximum Temperature"][0])
                    date.append(i["timestamp"][0].strftime("%a"))
                if i["timestamp"][1] == "Night":
                    day_min.append(i["Feels Like Night Minimum Temperature"][0])

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

        if self.ftype == metoffer.DAILY:
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
    def __init__(self, num):
        super(SunrisePage, self).__init__(num)
        self.title = "Sunrise & sunset"
        self.in_index = False
        self.tagline = "Here comes the sun"

    def generate_content(self):
        from astral import Astral
        city_name = 'Birmingham'
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
    def __init__(self, num):
        super(UKTempPage, self).__init__(num)
        self.title = "UK Temperature"
        self.tagline = "Why exactly do we live in Britain?"
        self.in_index = False
        self.importance = 4
        self.places = [
                    # Y ~= -2.557*LAT + 153.09
                    # X ~= 3.0543*LAT + 48.316
                    #
                    #                     Temp    Weather
                    # LAT      LON        X   Y   X   Y   Letter
                    (58.24670, -4.72918, 35,  6,  20,  6, "a"), # North of Scotland
                    (55.86420, -4.25180, 36, 10,  51,  9, "h"), # Glasgow?
                    (54.59730, -5.93010, 30, 14,  10, 12, "n"), # Belfast
                    (53.48080, -2.24260, 42, 16,  50, 13, "i"), # Manchester
                    (52.03390, -2.42360, 40, 20,  0,   0, "x"), # EMF
                    (51.50433, -0.12316, 48, 21,  55, 19, "s"), # London
                    (51.85762, -4.31213, 35, 21,  20, 22, "e"), # Cardiff
                    (50.38842, -4.18261, 35, 24,  20, 25, "f")  # Plymouth

                      ]

    def background(self):
        self.temps = []
        self.weather = []
        for lat,lon,x,y,xw,yw,a in self.places:
            M = metoffer.MetOffer(config.metoffer_api_key);
            X = M.nearest_loc_forecast(lat,lon, metoffer.THREE_HOURLY)
            weather_data = metoffer.Weather(X).data[0]
            self.temps.append(weather_data["Temperature"][0])
            self.weather.append(metoffer.WEATHER_CODES[weather_data["Weather Type"][0]])

    def generate_content(self):
        import random

        def col(t):
            if t >= 25:
                return "RED"
            if t >= 15:
                return "YELLOW"
            if t >= 5:
                return "LIGHTBLUE"
            return "BLUE"
        self.add_title("UK TEMPERATURE",font="size4")
        uk_map =("-------------aa--aaaaaaa--------------\n"
                 "-----------------aaaaa----------------\n"
                 "----------------aaaaaaa---------------\n"
                 "--------------a--aaaaa-aaaaa----------\n"
                 "--------------a-aaaaaaaaaaaa----------\n"
                 "--------------a-aaaaaaaaaaa-----------\n"
                 "----------------aaaaaaaaaaa-----------\n"
                 "----------------a-aaaaaaaa------------\n"
                 "--------------h-hhhhhhhhhh------------\n"
                 "---------------hhhhhhhhhh-------------\n"
                 "----------------hhhhhhhhh-------------\n"
                 "-----------------h-hhhh---------------\n"
                 "--------------h-h-hhhhhhhhh-----------\n"
                 "---------------hh--hhhhhhhhh----------\n"
                 "--------n---n------hhhhhhhhhh---------\n"
                 "--------nnnnnnn---hhhhhhhhhhhh--------\n"
                 "------nnnnnnnnnn--hhhh-hhhhhhh--------\n"
                 "------nnnnnnnnnn---h---hhhhhhh--------\n"
                 "------nnnnnnnnnnn-----hhhhiiii--------\n"
                 "---wwwwnnnnnnnnn------iiiiiiiiii------\n"
                 "---wwwwwwwnnnnnn---i--iiiiiiiiii------\n"
                 "---wwwwwwwwwnn----------iiiiiiiii-----\n"
                 "--wwwwwwwwwwww---------iiiiiiiiii-----\n"
                 "---wwwwwwwwwwww---------iiiiiiiiii----\n"
                 "-----wwwwwwwww----------iiiiiiiiii----\n"
                 "---wwwwwwwwwwww----e-ee-iiiiiiiiii----\n"
                 "----wwwwwwwwwww----eeeeeeiiiiiiiiii---\n"
                 "---w-wwwwwwwww----eeeeeeeeiiiiiii--ii-\n"
                 "--wwwwwwwwwwww-------eeeeeeiiiiiiiiiii\n"
                 "wwwwwwwwwwwwww------eeeeeeeeiiiiiiiiii\n"
                 "-wwwwwwwwwww-w------eeeeeeeeesssssssss\n"
                 "wwwwwwwww---------eeeeeeeeeeesssssssss\n"
                 "---www----------eeeeeeeeeeeessssssss--\n"
                 "----------------e--eeeeeeeessssssss---\n"
                 "--------------------ee-eeesssssssss---\n"
                 "----------------------fffffssssssss-s-\n"
                 "-------------------fffffffffsssssssss-\n"
                 "-----------------ffffffffffffssssss---\n"
                 "-----------------ffffffffff--f--------\n"
                 "----------------fffff-----------------")


        #for w in self.weather:
        color_codes = {"k": "BLACK",  "K": "GREY",
                       "r": "RED",    "R": "LIGHTRED",
                       "o": "ORANGE", "y": "YELLOW",
                       "g": "GREEN",  "G": "LIGHTGREEN",
                       "c": "CYAN",   "C": "LIGHTCYAN",
                       "b": "BLUE",   "B": "LIGHTBLUE",
                       "m": "MAGENTA","p": "PINK",
                       "w": "WHITE",  "W": "BRIGHTWHITE",
                       "d": "DEFAULT","-": "BLACK"}
        color_choices = ["r","R","o","y","g","G","c","C","b","B","m","p"]
        random.shuffle(color_choices)
        color_dictionary = {}
        k = 0
        for w in self.weather:
            if w not in color_dictionary:
                color_dictionary[w] = color_choices[k]
                k = k + 1

        for (lat,lon,x,y,xw,yw,a),t,w in zip(self.places,self.temps,self.weather):
            uk_map = uk_map.replace(a,color_dictionary[w])
        self.print_image(uk_map,y_coord=5,x_coord=18)

        for (lat,lon,x,y,xw,yw,a),t,w in zip(self.places,self.temps,self.weather):
            self.move_cursor(x=x,y=y)
            self.add_text(" "+str(t)+" ", fg=col(int(t)))
            if xw!=0 and yw!=0:
                self.move_cursor(x=xw,y=yw)
                self.add_text(" "+str(w)+" ", fg=color_codes[color_dictionary[w]])

class WorldTempPage(Page):
    def __init__(self, num):
        super(WorldTempPage, self).__init__(num)
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

page0 = WeatherForePage("330",metoffer.THREE_HOURLY)
page1 = WeatherForePage("331",metoffer.DAILY)
page2 = SunrisePage("332")
page3 = UKTempPage("333")
page3.importance = 4
page4 = WorldTempPage("334")

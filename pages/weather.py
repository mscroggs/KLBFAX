from page import Page
from helpers import url_handler
import datetime
import config

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
            self.index_num = "330-339"
            self.in_index = True
        else:
            self.in_index = False

    def background(self):
        import metoffer
        M = metoffer.MetOffer(config.metoffer_api_key);
        if self.ftype=="A":
            x = M.nearest_loc_forecast(*config.location, metoffer.THREE_HOURLY)
        if self.ftype=="B":
            x = M.nearest_loc_forecast(*config.location, metoffer.DAILY)

        self.y = metoffer.parse_val(x)

        self.tagline = "Live from the Met Office"

    def generate_content(self):
        import metoffer
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
                    (51.50433, -0.12316, 48, 21),
                    (51.85762, -4.31213, 35, 21),
                    (55.86420, -4.25180, 36, 10),
                    (53.48080, -2.24260, 42, 16),
                    (54.59730, -5.93010, 30, 14),
                    (52.03390, -2.42360, 40, 20)
                      ]

    def background(self):
        import json
        import metoffer

        self.temps = []
        for lat,lon,x,y in self.places:
            M = metoffer.MetOffer(config.metoffer_api_key);
            x = M.nearest_loc_forecast(lat,lon, metoffer.THREE_HOURLY)
            self.temps.append(metoffer.parse_val(x).data[0]["Temperature"][0])

    def generate_content(self):

        def col(t):
            if t >= 25:
                return "RED"
            if t >= 15:
                return "YELLOW"
            if t >= 5:
                return "LIGHTBLUE"
            return "BLUE"
        self.add_title("UK TEMPERATURE",font="size4")
        uk_map =("-------------ww--wwwwwww--------------\n"
                 "-----------------wwwww----------------\n"
                 "----------------wwwwwww---------------\n"
                 "--------------w--wwwww-wwwww----------\n"
                 "--------------w-wwwwwwwwwwww----------\n"
                 "--------------w-wwwwwwwwwww-----------\n"
                 "----------------wwwwwwwwwww-----------\n"
                 "----------------w-wwwwwwww------------\n"
                 "--------------w-wwwwwwwwww------------\n"
                 "---------------wwwwwwwwww-------------\n"
                 "----------------wwwwwwwww-------------\n"
                 "-----------------w-wwww---------------\n"
                 "--------------w-w-wwwwwwwww-----------\n"
                 "---------------ww--wwwwwwwww----------\n"
                 "--------w---w------wwwwwwwwww---------\n"
                 "--------wwwwwww---wwwwwwwwwwww--------\n"
                 "------wwwwwwwwww--wwww-wwwwwww--------\n"
                 "------wwwwwwwwww---w---wwwwwww--------\n"
                 "------wwwwwwwwwww-----wwwwwwww--------\n"
                 "---wwwwwwwwwwwww------wwwwwwwwww------\n"
                 "---wwwwwwwwwwwww---w--wwwwwwwwww------\n"
                 "---wwwwwwwwwww----------wwwwwwwww-----\n"
                 "--wwwwwwwwwwww---------wwwwwwwwww-----\n"
                 "---wwwwwwwwwwww---------wwwwwwwwww----\n"
                 "-----wwwwwwwww----------wwwwwwwwww----\n"
                 "---wwwwwwwwwwww----w-ww-wwwwwwwwww----\n"
                 "----wwwwwwwwwww----wwwwwwwwwwwwwwww---\n"
                 "---w-wwwwwwwww----wwwwwwwwwwwwwww--ww-\n"
                 "--wwwwwwwwwwww-------wwwwwwwwwwwwwwwww\n"
                 "wwwwwwwwwwwwww------wwwwwwwwwwwwwwwwww\n"
                 "-wwwwwwwwwww-w------wwwwwwwwwwwwwwwwww\n"
                 "wwwwwwwww---------wwwwwwwwwwwwwwwwwwww\n"
                 "---www----------wwwwwwwwwwwwwwwwwwww--\n"
                 "----------------w--wwwwwwwwwwwwwwww---\n"
                 "--------------------ww-wwwwwwwwwwww---\n"
                 "----------------------wwwwwwwwwwwww-w-\n"
                 "-------------------wwwwwwwwwwwwwwwwww-\n"
                 "-----------------wwwwwwwwwwwwwwwwww---\n"
                 "-----------------wwwwwwwwww--w--------\n"
                 "----------------wwwww-----------------")

        self.print_image(uk_map,y_coord=5,x_coord=18)

        for (lat,lon,x,y),t in zip(self.places,self.temps):
            self.move_cursor(x=x,y=y)
            self.add_text(" "+str(t)+" ", fg=col(int(t)))

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

page0 = WeatherForePage("330","A")
page1 = WeatherForePage("331","B")
page2 = SunrisePage("332")
page3 = UKTempPage("333")
page4 = WorldTempPage("334")


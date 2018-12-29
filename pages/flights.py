from page import Page
import config

class FlightPage(Page):
    def __init__(self, page_num, station, code, arrivals=False, terminal=False, is_random=False):
        super(FlightPage, self).__init__(page_num)
        self.title = station+" flights"
        self.in_index = False
        self.tagline = "Live flights from "+code.upper()+"."
        self.station = station
        self.importance = 1
        self.code = code
        self.arrivals = arrivals
        self.terminal = terminal
        self.is_random = is_random

        if self.arrivals:
            arr_dep = "A "
        else:
            arr_dep = "D "
        if self.is_random:
            arr_dep = ""
        pages.append([page_num,arr_dep + station+" ("+code.upper()+")"])


    def generate_content(self):
        import urllib2, time, json, datetime, pytz
        from helpers.url_handler import load_json

        if self.is_random:
            # Pick randomly
            from helpers.file_handler import load_csv_file
            import random
            station_codes = load_csv_file("airport_codes.csv")
            choose = random.choice(station_codes)
            self.code = choose[0]
            self.arrivals = random.choice([True,False])

        airport_code = self.code
        unix_timestamp = str(int(time.time()))
        if not self.arrivals:
            url = config.flight_api.format(airport_code,'departures',unix_timestamp)
        else:
            url = config.flight_api.format(airport_code,'arrivals',unix_timestamp)
        data = load_json(url)

        airport_name = data['result']['response']['airport']['pluginData']['details']['name'].replace(" Airport","").replace(" International","")
        airport_city = data['result']['response']['airport']['pluginData']['details']['position']['region']['city']
        if self.is_random:
            if airport_city == airport_name:
                self.station = airport_city + ", " + choose[2];
            else:
                self.station = airport_city + " " + airport_code.upper() + ", " + choose[2];
        airport_timezone = data['result']['response']['airport']['pluginData']['details']['timezone']['name']
        tz = pytz.timezone(airport_timezone)

        now_gmt = datetime.datetime.utcnow()
        now_gmt = now_gmt.replace(tzinfo=pytz.utc)
        now_gmt = now_gmt.astimezone(tz)
        now_gmt_s = now_gmt.strftime('%H:%M')

        self.add_title(self.station,font="size4",fg="LIGHTCYAN",bg="BLUE")

        aeroplane_sym_dep=("CCCCCbCCCCC\n"
                       "CCCCCbCCCCC\n"
                       "CCCCbbbCCCC\n"
                       "CCCbbbbbCCC\n"
                       "CCbbbbbbbCC\n"
                       "CbbbCbCbbbC\n"
                       "CCCCCbCCCCC\n"
                       "CCCCbbbCCCC")
        aeroplane_sym_arr=("CCCCbbbCCCC\n"
                       "CCCCCbCCCCC\n"
                       "CbbbCbCbbbC\n"
                       "CCbbbbbbbCC\n"
                       "CCCbbbbbCCC\n"
                       "CCCCbbbCCCC\n"
                       "CCCCCbCCCCC\n"
                       "CCCCCbCCCCC")
        if self.arrivals:
            self.print_image(aeroplane_sym_arr,0,69)
        else:
            self.print_image(aeroplane_sym_dep,0,69)

        self.start_bg_color("LIGHTCYAN")
        self.start_fg_color("BLUE")
        self.move_cursor(x=68,y=4)
        if not self.arrivals:
            self.add_text(" DEPARTURES ")
        else:
            self.add_text("  ARRIVALS  ")
        self.move_cursor(x=68,y=5)
        self.add_text(" TIME " + now_gmt_s + " ")
        self.end_fg_color()
        self.end_bg_color()

        if not self.arrivals:
            deps = data['result']['response']['airport']['pluginData']['schedule']['departures']['data']
        else:
            deps = data['result']['response']['airport']['pluginData']['schedule']['arrivals']['data']

        j = 0

        for i in range(min(50,len(deps))):
            try:
                self.move_cursor(x=1,y=5+j)
                flight_number = deps[i]['flight']['identification']['number']['default']

                if not self.arrivals:
                    dest_or_orig = 'destination'
                    orig_or_dest = 'origin'
                    dep_or_arr = 'departure'
                else:
                    dest_or_orig = 'origin'
                    orig_or_dest = 'destination'
                    dep_or_arr = 'arrival'
                destination = deps[i]['flight']['airport'][dest_or_orig]['name'].replace(" Airport","").replace(" International","")
                destination_code = deps[i]['flight']['airport'][dest_or_orig]['code']['iata']
                destination_city = deps[i]['flight']['airport'][dest_or_orig]['position']['region']['city']
                std = deps[i]['flight']['time']['scheduled'][dep_or_arr]
                etd = deps[i]['flight']['time']['estimated'][dep_or_arr]
                gate = deps[i]['flight']['airport'][orig_or_dest]['info']['gate']
                terminal = deps[i]['flight']['airport'][orig_or_dest]['info']['terminal']
                status = str(deps[i]['flight']['status']['text'])
                try:
                    aircraft = str(deps[i]['flight']['aircraft']['model']['code'])
                except:
                    aircraft = ''
                color = deps[i]['flight']['status']['icon']

                flight_number_s = flight_number.ljust(6)

                std_s = datetime.datetime.utcfromtimestamp(std).replace(tzinfo=pytz.utc)
                std_s = std_s.astimezone(tz)
                std_s = std_s.strftime('%H:%M')

                first_status_word = status.split(" ")[0]
                if first_status_word == "Canceled":
                    color_s = "LIGHTCYAN"
                elif first_status_word in ["Scheduled","Landed"]:
                    color_s = 'LIGHTGREEN'
                elif first_status_word in ["Delayed"]:
                    color_s = "LIGHTRED"
                elif first_status_word in ["Estimated"]:
                    try:
                        if datetime.datetime.utcfromtimestamp(etd) > datetime.datetime.utcfromtimestamp(std):
                            color_s = "YELLOW"
                        else:
                            color_s = 'LIGHTGREEN'
                    except:
                        color_s = "YELLOW"
                else:
                    color_s = 'YELLOW'

                if status == "Canceled":
                    etd_s = "Cancelled"
                elif self.arrivals:
                    etd_s = status
                elif etd is None:
                    etd_s = "Scheduled"
                else:
                    etd_s = datetime.datetime.utcfromtimestamp(etd).replace(tzinfo=pytz.utc)
                    etd_s = etd_s.astimezone(tz)
                    etd_s = 'Delayed ' + etd_s.strftime('%H:%M')

                if terminal is None:
                    terminal_s = "  "
                else:
                    terminal_s = "T" + terminal

                if gate is None:
                    gate = ""

                if self.terminal == False or str(terminal)==str(self.terminal):
                    self.move_cursor(x=1)
                    self.add_text(std_s)
                    self.move_cursor(x=7)
                    self.start_fg_color("YELLOW")
                    self.add_text(flight_number_s[:2])
                    self.end_fg_color()
                    self.move_cursor(x=9)
                    self.add_text(flight_number_s[2:])
                    self.move_cursor(x=14)
                    self.start_fg_color("BRIGHTWHITE")
                    self.add_text((destination_city[0:15] + " " + destination_code).ljust(20) + " ")
                    self.end_fg_color()
                    self.move_cursor(x=34)
                    self.add_text(aircraft)
                    self.move_cursor(x=39)
                    self.add_text(terminal_s)
                    self.move_cursor(x=42)
                    self.add_text(gate.rjust(3))
                    self.move_cursor(x=47)
                    self.start_fg_color(color_s)
                    self.add_text(etd_s)
                    self.end_fg_color()
                    j+=1
            except:
                1==1
pages = []

# Departures
plane01 = FlightPage("751","Heathrow T2","lhr",terminal=2)
plane02 = FlightPage("752","Heathrow T3","lhr",terminal=3)
plane03 = FlightPage("753","Heathrow T4","lhr",terminal=4)
plane04 = FlightPage("754","Heathrow T5","lhr",terminal=5)
plane05 = FlightPage("755","Gatwick","lgw")
plane06 = FlightPage("756","Luton","ltn")
plane07 = FlightPage("757","Stansted","stn")
plane07 = FlightPage("758","City Airport","lcy")
plane08 = FlightPage("759","Birmingham","bhx")

# Arrivals
plane21 = FlightPage("771","Heathrow T2","lhr",terminal=2,arrivals=True)
plane22 = FlightPage("772","Heathrow T3","lhr",terminal=3,arrivals=True)
plane23 = FlightPage("773","Heathrow T4","lhr",terminal=4,arrivals=True)
plane24 = FlightPage("774","Heathrow T5","lhr",terminal=5,arrivals=True)
plane25 = FlightPage("775","Gatwick","lgw",arrivals=True)
plane26 = FlightPage("776","Luton","ltn",arrivals=True)
plane27 = FlightPage("777","Stansted","stn",arrivals=True)
plane27 = FlightPage("778","City Airport","lcy",arrivals=True)
plane28 = FlightPage("779","Birmingham","bhx",arrivals=True)

# Random
plane49 = FlightPage("799","Random","xxx",is_random=True)
plane49.importance=4


class FlightIPage(Page):
    def __init__(self):
        super(FlightIPage, self).__init__("750")
        self.title = "Flights"
        self.index_num = "750-799"
        self.importance = 1

    def generate_content(self):
        self.add_title("Flights index")

        for i,page in enumerate(pages):
            if i//16==0:
                self.move_cursor(x=0)
            elif i//16==1:
                self.move_cursor(x=25)
            else:
                self.move_cursor(x=50)
            if i % 16 == 0:
                self.move_cursor(y=8)
            self.add_text(page[0], fg="RED")
            self.add_text(" "+page[1])
            self.add_newline()

tp = FlightIPage()

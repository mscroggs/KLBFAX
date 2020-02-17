from page import Page

british_rail =("rrrrWWrrrrr\n"
               "rrrrrWWrrrr\n"
               "rWWWWWWWWWr\n"
               "rrrrrWWrrrr\n"
               "rrrrWWrrrrr\n"
               "rWWWWWWWWWr\n"
               "rrrrWWrrrrr\n"
               "rrrrrWWrrrr")

# Loop over all the train services in that board.
mapping=[('Cross', 'X'),
('Road', 'Rd'),
('Square', 'Sq'),
('Street', 'St'),
('Junction', 'Jn'),
('Town', 'Tn'),
('Park', 'Pk'),
('Lane', 'Ln'),
('Hill', 'Hl'),
('Central','Ctl'),
('Garden','Gdn'),
('North ','N '),
('South ','S '),
('East ','E '),
('West ','W '),
('International', 'Intl'),
(' (London)', ''),
(' (Kent)', ''),
(' (Intl)', ''),
(' (Hampshire)', ''),
(' (Essex)', ''),
(' (Dorset)', ''),
('Trent Valley', 'T Valley'),
('Piccadilly','Picc'),
('Thameslink','Thmslk'),
(' Underground', '')]

mapping_always = [('London Kings Cross', 'King\'s Cross'),
('London St Pancras (Intl)','St Pancras')]

operator_mapping=[
('London North Eastern Railway', 'LNER'),
('Railway', 'Rly'),
('Midlands', 'Mids'),
('TransPennine Express', 'TPE')
]


class TrainPage(Page):
    def __init__(self, page_num, station, code, hogwarts=False, to=None, is_random=False):
        super(TrainPage, self).__init__(page_num)
        self.title = station+" Trains"
        self.in_index = False
        self.tagline = "Live trains from "+code+". Data from National Rail API."
        self.station = station
        self.importance = 1
        self.code = code
        self.to = to
        self.hogwarts = hogwarts
        pages.append([page_num,station+" ("+code+")"])
        self.is_random = is_random

    def generate_content(self):
        from nrewebservices.ldbws import Session

        session = Session("https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2016-02-16", "875a552e-9e5b-42d8-843d-b046ae121532")

        if self.is_random:
            # Pick randomly
            from helpers.file_handler import load_csv_file
            import random
            station_codes = load_csv_file("station_codes.csv")
            choose = random.choice(station_codes)
            self.code = choose[1]
            self.station = choose[0]

        board = session.get_station_board_with_details(self.code, rows=14, include_departures=True, include_arrivals=False)

        self.add_title(self.station,font="size4")

        self.print_image(british_rail,0,69)

        n = 4

        # 4 across the top
        if self.hogwarts:
            self.move_cursor(x=1,y=4)
            self.add_text("8:30 9 3/4 On time")
            self.move_cursor(x=1,y=5)
            self.add_rainbow_text("HOGWARTS EXPRESS   ")
            self.move_cursor(x=1,y=6)
            self.start_fg_color("YELLOW")
            self.add_text("Calling at:        ")
            self.end_fg_color()
            self.move_cursor(x=1,y=7)
            self.add_text("Hogwarts School")
            self.move_cursor(x=1,y=18)
            self.add_text("Ministry of Magic")
            n = 3

        for i,service in enumerate(board.train_services[:n]):
            destinations = [destination.location_name for destination in service.destinations]
            destination_j = ",".join(destinations)
            if len(destination_j) > 19:
                for k, v in mapping:
                    destination_j = destination_j.replace(k, v)
            destination = (destination_j + " "*21)[0:19]
            platform = service.platform
            if platform == None:
                platform = "-"
            self.move_cursor(x=1+(4-n+i)*20,y=4)
            self.add_text(service.std+" "+platform+" "*(3-len(platform)))
            self.move_cursor(x=11+(4-n+i)*20,y=4)
            if service.etd[0] in ["0","1","2"]:
                self.start_fg_color("RED")
                self.add_text("Exp " + service.etd)
                self.end_fg_color()
            elif service.etd[0] == "D":
                self.start_fg_color("RED")
                self.add_text(service.etd)
                self.end_fg_color()
            elif service.etd[0] == "C":
                self.start_fg_color("CYAN")
                self.add_text(service.etd)
                self.end_fg_color()
            else:
                self.add_text(service.etd)

            self.move_cursor(x=1+(4-n+i)*20,y=5)
            self.start_fg_color("BRIGHTWHITE")
            self.add_text(destination.upper())
            self.end_fg_color()

            self.move_cursor(x=1+(4-n+i)*20,y=6)
            self.start_fg_color("YELLOW")
            self.add_text("Calling at:        ")
            self.end_fg_color()

            if len(service.subsequent_calling_points) > 0:
                calling_points = service.subsequent_calling_points[0]
            else:
                calling_points = ""
            calling_at = []
            for j,point in enumerate(calling_points[:11]):
                lname = point.location_name
                if len(lname) > 19:
                    for k, v in mapping:
                        lname = lname.replace(k, v)
                self.move_cursor(x=1+(4-n+i)*20,y=7+j)
                self.add_text(lname[0:19])
            if len(calling_points)>11:
                self.move_cursor(x=1+(4-n+i)*20,y=17)
                d = len(calling_points)-10
                self.add_text("+ " + str(d) + " stations       ")
            self.move_cursor(x=1+(4-n+i)*20,y=18)
            self.start_fg_color("YELLOW")
            operator = service.operator
            if len(operator) > 19:
                for k, v in operator_mapping:
                    operator = operator.replace(k, v)
            self.add_text(operator)
            self.end_fg_color()


        self.move_cursor(x=0,y=20)
        self.start_fg_color("GREEN")
        pos1 = (1,7,27,31)
        pos2 = (41,47,67,71)
        for p1,p2,t in zip(pos1,pos2,("Time","Destination","Plt","Exptd")):
            self.move_cursor(p1)
            self.add_text(t)
            self.move_cursor(p2)
            self.add_text(t)
        self.end_fg_color()
        self.add_newline()

        for i,service in enumerate(board.train_services[0:0+10]):
            if i < 5:
                pos = pos1
                y=21+i
            else:
                pos = pos2
                y=16+i
            # Build a list of destinations for each train service.
            self.move_cursor(x=pos[0],y=y)
            self.add_text(service.std)

            self.move_cursor(x=pos[1],y=y)
            destinations = [destination.location_name for destination in service.destinations]
            destination_j = ",".join(destinations)
            if len(destination_j) > 19:
                for kk, v in mapping:
                    destination_j = destination_j.replace(kk, v)
            self.add_text(destination_j[0:19])

            self.move_cursor(x=pos[2],y=y)
            destination = (destination_j + " "*21)[0:21]
            platform = service.platform
            if platform == None:
                platform = "-"
            self.add_text(platform)

            self.move_cursor(x=pos[3],y=y)
            if service.etd[0] in ["0","1","2"]:
                self.start_fg_color("RED")
                self.add_text(service.etd)
                self.end_fg_color()
            elif service.etd[0] == "D":
                self.start_fg_color("RED")
                self.add_text("Delayed")
                self.end_fg_color()
            elif service.etd[0] == "C":
                self.start_fg_color("CYAN")
                self.add_text("Canceld")
                self.end_fg_color()
            else:
                self.add_text(service.etd)

# ==============================================================================

class TrainNextDepPage(Page):
    def __init__(self, page_num, station, from_codes, to_codes):
        super(TrainNextDepPage, self).__init__(page_num)
        self.title = "Trains " + station
        self.in_index = False
        self.tagline = "Live trains from " + ",".join(from_codes) + " to " + ",".join(to_codes) + ". Data from National Rail API."
        self.station = station
        self.importance = 1
        self.from_codes = from_codes
        self.to_codes = to_codes
        pages.append([page_num,",".join(from_codes) + "-" + ",".join(to_codes)])

    def generate_content(self):
        from nrewebservices.ldbws import Session

        session = Session("https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2016-02-16", "875a552e-9e5b-42d8-843d-b046ae121532")


        self.add_title(self.station,font="size4")

        self.print_image(british_rail,0,69)

        for f,from_to in enumerate([[self.from_codes,self.to_codes],[self.to_codes,self.from_codes]]):

            start_y = 5 + f*11
            self.move_cursor(x=0,y=start_y)
            self.start_fg_color("GREEN")
            pos1 = (1,8,32,57,62,67)
            for p1,t in zip(pos1,("Time","From","Destination","Op","Plt","Expected")):
                self.move_cursor(p1)
                self.add_text(t)
            self.end_fg_color()
            self.add_newline()

            stds = []
            froms = []
            tos = []
            tocs = []
            platforms = []
            etds = []

            for from_code in from_to[0]:
                for to_code in from_to[1]:

                    board = session.get_station_board(from_code, rows=10, to_filter_crs=to_code, include_departures=True, include_arrivals=False)

                    for i,service in enumerate(board.train_services[0:0+10]):
                        stds.append(service.std)

                        name = board.location_name
                        for kk, v in mapping_always:
                            name = name.replace(kk, v)
                        if len(name) > 19:
                            for kk, v in mapping:
                                name = name.replace(kk, v)
                        froms.append(name)

                        name = service.destination
                        for kk, v in mapping_always:
                            name = name.replace(kk, v)
                        if len(name) > 19:
                            for kk, v in mapping:
                                name = name.replace(kk, v)
                        tos.append(name[0:19])

                        tocs.append(service.operator_code)

                        platform = service.platform
                        if platform == None:
                            platform = "-"
                        platforms.append(platform)

                        etds.append(service.etd)

            trains = zip(stds,froms,tos,tocs,platforms,etds)
            trains.sort()

            for i,train in enumerate(trains[0:7]):
                t_std = train[0]
                t_from = train[1]
                t_to = train[2]
                t_toc = train[3]
                t_platform = train[4]
                t_etd = train[5]

                pos = pos1
                y=start_y+1+i
                # Build a list of destinations for each train service.
                self.move_cursor(x=pos[0],y=y)
                self.add_text(t_std)

                self.move_cursor(x=pos[1],y=y)
                self.add_text(t_from)

                self.move_cursor(x=pos[2],y=y)
                self.add_text(t_to)

                self.move_cursor(x=pos[3],y=y)
                self.add_text(t_toc)

                self.move_cursor(x=pos[4],y=y)
                self.add_text(t_platform)

                self.move_cursor(x=pos[5],y=y)
                if t_etd[0] in ["0","1","2"]:
                    self.start_bg_color("YELLOW")
                    self.start_fg_color("BLACK")
                    self.add_text("   " + t_etd + "   ")
                    self.end_fg_color()
                    self.end_bg_color()
                elif t_etd[0] == "D":
                    self.start_bg_color("ORANGE")
                    self.start_fg_color("BLACK")
                    self.add_text("  Delayed  ")
                    self.end_fg_color()
                    self.end_bg_color()
                elif t_etd[0] == "C":
                    self.start_bg_color("RED")
                    self.add_text(" Cancelled ")
                    self.end_bg_color()
                else:
                    self.start_bg_color("GREEN")
                    self.add_text("  " + t_etd + "  ")
                    self.end_bg_color()


# ==============================================================================

pages = []

# London stations
train01 = TrainPage("851","Euston","EUS")
#train01.importance = 3
train02 = TrainPage("852","King's Cross","KGX", True)
train03 = TrainPage("853","St Pancras","STP")
train04 = TrainPage("854","Liverpool St","LST")
train05 = TrainPage("855","Marylebone","MYB")
train06 = TrainPage("856","Paddington","PAD")
train07 = TrainPage("857","Victoria","VIC")
train08 = TrainPage("858","Waterloo","WAT")
train09 = TrainPage("859","Blackfriars","BFR")
train10 = TrainPage("860","London Bridge","LBG")
train11 = TrainPage("861","Charing Cross","CHX")
train12 = TrainPage("862","Cannon Street","CST")
train13 = TrainPage("863","Fenchurch St","FST")

# Elsewhere
train14 = TrainPage("864","Banbury","BAN")
#train15 = TrainPage("865","Barry Links","BYL")
train16 = TrainPage("865","Basingstoke","BSK")
train17 = TrainPage("866","Birmingham New St","BHM")
train18 = TrainPage("867","Blaenau Ffestiniog","BFF")
train19 = TrainPage("868","Bristol TM","BRI")
train20 = TrainPage("869","Cambridge","CBG")
train21 = TrainPage("870","Cardiff Ctl","CDF")
train40 = TrainPage("871","Durham","DHM")
train22 = TrainPage("872","Edinburgh","EDB")
train23 = TrainPage("873","Glasgow Central","GLC")
train24 = TrainPage("874","Glasgow Queen St","GLQ")
train25 = TrainPage("875","Leeds","LDS")
train26 = TrainPage("876","Lichfield TV","LTV")
train27 = TrainPage("877","Liverpool Ctl","LVC")
train28 = TrainPage("878","Liverpool Lime St","LIV")
train29 = TrainPage("879","Manchester Picc","MAN")
train30 = TrainPage("880","Newcastle","NCL")
train31 = TrainPage("881","Nottingham","NOT")
train32 = TrainPage("882","Oxford","OXF")
train33 = TrainPage("883","Rainham","RAI")
train34 = TrainPage("884","Reading","RDG")
train35 = TrainPage("885","Sevenoaks","SEV")
train36 = TrainPage("886","Stratford-upon-Avon","SAV")
train37 = TrainPage("887","Sutton Coldfield","SUT")
train38 = TrainPage("889","Thurso","THS")
train39 = TrainPage("890","University","UNI")
#train40 = TrainPage("891","Valley","VAL")
train41 = TrainPage("891","Warwick","WRW")
train42 = TrainPage("892","York","YRK")

# Airports
train43 = TrainPage("893","Gatwick Airport","GTW")
train44 = TrainPage("894","Heathrow T2-3","HXX")
train45 = TrainPage("895","Luton Airport Parkway","LTN")
train46 = TrainPage("896","Southend Airport","SIA")
train47 = TrainPage("897","Stansted Airport","SSD")

train80 = TrainNextDepPage("898","London-Cambridge",["KGX","STP"],["CBG"])

train48 = TrainPage("899","Random!","XXX",is_random=True)

train48.importance = 5

class TrainIPage(Page):
    def __init__(self):
        super(TrainIPage, self).__init__("850")
        self.title = "Trains"
        self.index_num = "850-899"
        self.importance = 1

    def generate_content(self):
        self.add_title("Trains Index")

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

tp = TrainIPage()

from page import Page

class TrainPage(Page):
    def __init__(self, page_num, station, code, hogwarts=False, to=None):
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

    def generate_content(self):
        from nrewebservices.ldbws import Session

        session = Session("https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2016-02-16", "875a552e-9e5b-42d8-843d-b046ae121532")

        board = session.get_station_board_with_details(self.code, rows=14, include_departures=True, include_arrivals=False)

        self.add_title(self.station,font="size4")

        british_rail =("rrrrWWrrrrr\n"
                       "rrrrrWWrrrr\n"
                       "rWWWWWWWWWr\n"
                       "rrrrrWWrrrr\n"
                       "rrrrWWrrrrr\n"
                       "rWWWWWWWWWr\n"
                       "rrrrWWrrrrr\n"
                       "rrrrrWWrrrr")
        self.print_image(british_rail,0,69)


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

        operator_mapping=[
        ('Railway', 'Rly'),
        ('Midlands', 'Mids')
        ]

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

            calling_points = service.subsequent_calling_points[0]
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

pages = []
train01 = TrainPage("851","Milton Keynes","MKC")
train02 = TrainPage("852","Bletchley","BLY")
train03 = TrainPage("853","Farncombe","FNC")
train04 = TrainPage("854","Ledbury","LED")
train01.importance = 3
train02.importance = 3
train03.importance = 3
train04.importance = 5
train05 = TrainPage("855","Shippea Hill","SPP")
train06 = TrainPage("856","Glasgow Central","GLC")
train07 = TrainPage("857","Birmingham New Street","BHM")
train08 = TrainPage("858","London Waterloo","WAT")
train09 = TrainPage("859","London King's Cross","KGX", True)
train10 = TrainPage("860","Banbury","BAN")
train11 = TrainPage("861","Moreton-in-Marsh","MIM")
train12 = TrainPage("862","Manchester Piccadilly","MAN")

train13 = TrainPage("863","Ashford International","AFK")
train14 = TrainPage("864","Basingstoke","BSK")
train15 = TrainPage("865","Coventry","COV")
train16 = TrainPage("866","Davenport","DVN")
train17 = TrainPage("867","Egham","EGH")
train18 = TrainPage("868","Fort William","FTW")
train19 = TrainPage("869","Gloucester","GCR")
train20 = TrainPage("870","Halifax","HFX")
train21 = TrainPage("871","Ipswich","IPS")
train22 = TrainPage("872","Jewellery Quarter","JEQ")
train23 = TrainPage("873","Knighton","KNI")
train24 = TrainPage("874","Liverpool Lime Street","LIV")
train25 = TrainPage("875","Malvern Link","MVL")
train26 = TrainPage("876","Nottingham","NOT")
train27 = TrainPage("877","Oxford","OXF")
train28 = TrainPage("878","Pembroke","PMB")
train29 = TrainPage("879","Quakers Yard","QYD")
train30 = TrainPage("880","Rainham (Kent)","RAI")
train31 = TrainPage("881","Stratford-upon-Avon","SAV")
train32 = TrainPage("882","Thurso","THS")
train33 = TrainPage("883","University (Birmingham)","UNI")
train34 = TrainPage("884","Valley","VAL")
train35 = TrainPage("885","Warwick","WRW")
train36 = TrainPage("886","York","YRK")

train37 = TrainPage("887","Gatwick Airport","GTW")
train38 = TrainPage("889","Heathrow Airport (T4)","HAF")
train39 = TrainPage("890","Heathrow Airport (T5)","HWV")
train40 = TrainPage("891","Heathrow Airport (T1-3)","HXX")
train41 = TrainPage("892","Luton Airport Parkway","LTN")
train42 = TrainPage("893","Manchester Airport","MIA")
train43 = TrainPage("894","Prestwick International Airport","PRA")
train44 = TrainPage("895","Rhoose Cardiff International Airport","RIA")
train45 = TrainPage("896","Southampton Airport Parkway","SOA")
train46 = TrainPage("897","Southend Airport","SIA")
train47 = TrainPage("898","Stanstead Airport","SSD")
train48 = TrainPage("899","Tees-side Airport","TEA")

class TrainIPage(Page):
    def __init__(self):
        super(TrainIPage, self).__init__("850")
        self.title = "Trains"
        self.index_num = "850-899"
        self.importance = 1

    def generate_content(self):
        self.add_title("Trains Index")

        for i,page in enumerate(pages):
            self.add_text(page[0], fg="RED")
            self.add_text(" "+page[1])
            if i%2==1:
                self.add_newline()
            else:
                self.move_cursor(x=38)

tp = TrainIPage()

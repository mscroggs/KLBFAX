from page import Page

class TrainPage(Page):
    def __init__(self, page_num, station, code, hogwarts=False, to=None):
        super(TrainPage, self).__init__(page_num)
        self.title = station+" Trains"
        self.in_index = False
        self.tagline = "Live trains from "+code+". Data from National Rail API."
        self.station = station
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
        ('London North Eastern Railway', 'LNER'),
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
                self.start_fg_color("LIGHTRED")
                self.add_text("Exp " + service.etd)
                self.end_fg_color()
            elif service.etd[0] == "D":
                self.start_fg_color("LIGHTRED")
                self.add_text(service.etd)
                self.end_fg_color()
            elif service.etd[0] == "C":
                self.start_bg_color("CYAN")
                self.start_fg_color("BLACK")
                self.add_text(service.etd)
                self.end_fg_color()
                self.end_bg_color()
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
                self.start_fg_color("LIGHTRED")
                self.add_text(service.etd)
                self.end_fg_color()
            elif service.etd[0] == "D":
                self.start_fg_color("LIGHTRED")
                self.add_text("Delayed")
                self.end_fg_color()
            elif service.etd[0] == "C":
                self.start_bg_color("CYAN")
                self.start_fg_color("BLACK")
                self.add_text("Canceld")
                self.end_fg_color()
                self.end_bg_color()
            else:
                self.add_text(service.etd)

pages=[]
train01 = TrainPage("851","Blackfriars","BFR")
train02 = TrainPage("852","London Bridge","LBG")
train03 = TrainPage("853","Cannon Street","CST")
train04 = TrainPage("854","Charing Cross","CHX")
train05 = TrainPage("855","Euston","EUS")
train06 = TrainPage("856","Fenchurch St","FST")
train09 = TrainPage("859","King's Cross","KGX",True)
train10 = TrainPage("860","Liverpool St","LST")
train11 = TrainPage("861","Marylebone","MYB")
train12 = TrainPage("862","Paddington","PAD")
train13 = TrainPage("863","Acton Central","ACC")
train14 = TrainPage("864","Acton Main Line","AML")
train15 = TrainPage("865","St Pancras","STP")
train16 = TrainPage("866","Ffairfach","FFA")
train17 = TrainPage("867","Victoria","VIC")
train18 = TrainPage("868","Waterloo","WAT")
train19 = TrainPage("869","Waterloo East","WAE")
train20 = TrainPage("870","Banbury","BAN")
train21 = TrainPage("871","Reading","RDG")
train22 = TrainPage("872","Oxford","OXF")
train23 = TrainPage("873","Stratford-u-A","SAV")
train24 = TrainPage("874","B'ham New St","BHM")
train25 = TrainPage("875","B'ham Moor St","BMO")
train26 = TrainPage("876","B'ham Snow Hill","BSW")
train27 = TrainPage("877","Wembley Stadm","WCX")
train28 = TrainPage("878","Kilmarnock","KMK")
train29 = TrainPage("879","Moreton-in-Msh","MIM")
train30 = TrainPage("880","Ealing B'dway","EAL")
train31 = TrainPage("881","Farringdon","ZFD")
train32 = TrainPage("882","East Croydon","ECR")
#train33 = TrainPage("883","St Pancras to East Croydon","STP",to=["Three Bridges","Brighton"])
train34 = TrainPage("884","Blaenau Ffest.","BFF")
train35 = TrainPage("885","Sutton C'field","SUT")
train36 = TrainPage("886","Cambridge","CBG")
train37 = TrainPage("887","Lichfield T.V.","LTV")
train38 = TrainPage("889","Arlesey","ARL")
train39 = TrainPage("890","Gatwick Airport","GTW")

class TVIPage(Page):
    def __init__(self):
        super(TVIPage, self).__init__("850")
        self.title = "Trains Index"

    def generate_content(self):
        self.add_title("Trains Index")

        for i,page in enumerate(pages):
            self.add_text(page[0], fg="RED")
            self.add_text(" "+page[1])
            if i%2==1:
                self.add_newline()
            else:
                self.move_cursor(x=38)

tp = TVIPage()

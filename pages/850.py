from page import Page

class TrainPage(Page):
    def __init__(self, page_num, station, code, hogwarts=False, to=None):
        super(TrainPage, self).__init__(page_num)
        self.title = station+" Trains"
        self.in_index = False
        self.tagline = "Live trains from "+code+". Data from opentraintimes.com."
        self.station = station
        self.code = code
        self.to = to
        self.hogwarts = hogwarts
        pages.append([page_num,station+" ("+code+")"])

    def background(self):
        from nrewebservices.ldbws import Session

        session = Session("https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2016-02-16", "875a552e-9e5b-42d8-843d-b046ae121532")

        self.board = session.get_station_board_with_details(self.code, rows=10, include_departures=True, include_arrivals=False)

    def generate_content(self):
        self.add_title(self.station)


        # Loop over all the train services in that board.
        k = 0
        num_of_rows = len(self.board.train_services)

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
        ('North ','N '),
        ('South ','S '),
        ('East ','E '),
        ('West ','W '),
        ('International', 'Intl'),
        (' (London)', ''),
        (' (Kent)', ''),
        (' (Intl)', ''),
        ('Trent Valley', 'T Valley'),
        ('Piccadilly','Picc'),
        ('Thameslink','Thmslk'),
        (' Underground', '')]

        # 4 across the top
        if self.hogwarts:
            big_boards = "8:30 9 3/4 On time \n"
            big_boards += "HOGWARTS EXPRESS   \n"
            big_boards += "Calling at:        \n"
            calling_at = (["Hogwarts School    "] + [' '*19]*12)[0:11]
            big_boards += "\n".join(calling_at)
            big_boards += "\n"+' '*19+"\n"
            big_boards += ("Ministry of Magic                ")[0:19] + "\n"
            n=3
        else:
            big_boards = ""
            n = 4
        for i in range(min(4,len(self.board.train_services))):
            service = self.board.train_services[i]
            destinations = [destination.location_name for destination in service.destinations]
            std = service.std
            destination_j = ",".join(destinations)
            if len(destination_j) > 19:
                for k, v in mapping:
                    destination_j = destination_j.replace(k, v)
            destination = (destination_j + " "*21)[0:19]
            platform = service.platform
            if platform == None:
                platform = "-"
            platform = (platform + " "*3)[0:3]
            if service.etd[0] in ["0","1","2"]:
                etd2 = "Exp " + service.etd
            elif service.etd[0] == "D":
                etd2 = service.etd + "  "
            elif service.etd[0] == "C":
                etd2 = service.etd
            else:
                etd2 = service.etd + "  "
            etd = (etd2 + " "*7)[0:29]
            #big_boards += "\n"
            big_boards += (std + " " + platform + "   "[0:3-len(platform)] + " " + etd +  " "*30)[0:36] + "\n"
            big_boards += destination.upper() + "\n"
            big_boards += "Calling at:        \n"
            calling_points = service.subsequent_calling_points[0]
            calling_at = []
            for point in calling_points:
                lname = point.location_name
                if len(lname) > 19:
                    for k, v in mapping:
                        lname = lname.replace(k, v)
                calling_at.append((lname + " "*21)[0:19])
            calling_at = (calling_at + [' '*19]*12)[0:11]
            big_boards += "\n".join(calling_at)
            if len(calling_points)>=12:
                big_boards += ("\n+ " + str(len(calling_points)-11) + " stations            ")[0:20] + "\n"
            else:
                big_boards += "\n"+' '*19+"\n"
            big_boards += (service.operator + "                ")[0:19] + "\n"

        #print big_boards
        columns = big_boards.split("\n")
        #print "X",columns[1],"Y"
        columns = (columns + [' '*19 for ii in range(64)])[0:64]
        for j in range(16):
            content += " " + columns[0+j] + " " + columns[16+j] + " " + columns[32+j] + " " + columns[48+j] + "\n"
            #print j, len(columns)

        content += "\nTime  Destination           Plt Exptd    Time  Destination           Plt Exptd "
        for k in range(5):
            if k < num_of_rows:
                service = self.board.train_services[k]
                # Build a list of destinations for each train service.
                destinations = [destination.location_name for destination in service.destinations]
                std = service.std
                destination_j = ",".join(destinations)
                if len(destination_j) > 21:
                    for kk, v in mapping:
                        destination_j = destination_j.replace(kk, v)
                destination = (destination_j + " "*21)[0:21]
                platform = service.platform
                if platform == None:
                    platform = "-"
                platform = (platform + " "*3)[0:3]
                if service.etd[0] in ["0","1","2"]:
                    etd2 = service.etd
                elif service.etd[0] == "D":
                    etd2 = "Delayed"
                elif service.etd[0] == "C":
                    etd2 = "Canceld"
                else:
                    etd2 = service.etd
                etd = (etd2 + " "*22)[0:24]
                content += "\n" + std + " " + destination + " " + platform + " " + etd + "  "

            if k + 5 < num_of_rows:
                service = self.board.train_services[k+5]
                # Build a list of destinations for each train service.
                destinations = [destination.location_name for destination in service.destinations]
                std = service.std
                destination_j = ",".join(destinations)
                if len(destination_j) > 21:
                    for kk, v in mapping:
                        destination_j = destination_j.replace(kk, v)
                destination = (destination_j + " "*21)[0:21]
                platform = service.platform
                if platform == None:
                    platform = "-"
                platform = (platform + " "*3)[0:3]
                if service.etd[0] in ["0","1","2"]:
                    etd2 = service.etd
                elif service.etd[0] == "D":
                    etd2 = "Delayed"
                elif service.etd[0] == "C":
                    etd2 = "Canceld"
                else:
                    etd2 = service.etd
                etd = (etd2 + " "*22)[0:24]
                content += std + " " + destination + " " + platform + " " + etd

        self.add_text(content)

pages=[]
train01 = TrainPage("851","Blackfriars","BFR")
train02 = TrainPage("852","London Bridge","LBG")
train03 = TrainPage("853","Cannon Street","CST")
train04 = TrainPage("854","Charing Cross","CHX")
train05 = TrainPage("855","Euston","EUS")
train06 = TrainPage("856","Fenchurch Street","FST")
train09 = TrainPage("859","Kings Cross","KGX",True)
train10 = TrainPage("860","Liverpool Street","LST")
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
train23 = TrainPage("873","Stratford-upon-Avon","SAV")
train24 = TrainPage("874","B'ham New Street","BHM")
train25 = TrainPage("875","B'ham Moor Street","BMO")
train26 = TrainPage("876","B'ham Snow Hill","BSW")
train27 = TrainPage("877","Wembley Stadium","WCX")
train28 = TrainPage("878","Kilmarnock","KMK")
train29 = TrainPage("879","Moreton-in-Marsh","MIM")
train30 = TrainPage("880","Ealing Broadway","EAL")
train31 = TrainPage("881","Farringdon","ZFD")
train32 = TrainPage("882","East Croydon","ECR")
train33 = TrainPage("883","St Pancras to East Croydon","STP",to=["Three Bridges","Brighton"])
train34 = TrainPage("884","Blaenau Ffestiniog","BFF")
train35 = TrainPage("885","Sutton Coldfield","SUT")
train36 = TrainPage("886","Cambridge","CBG")

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


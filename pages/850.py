import os
from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from printer import size4bold_instance as size4bold_printer
from time import strftime

def strip_tags(string):
    return sub(r'<[^>]*?>', '', string)


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

    def generate_content(self):
        from nrewebservices.ldbws import Session
        content = colour_print(size4bold_printer.text_to_ascii(self.station,fill=True))
        content += "\n"

        session = Session("https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2016-02-16", "875a552e-9e5b-42d8-843d-b046ae121532")

        board = session.get_station_board_with_details(self.code, rows=10, include_departures=True, include_arrivals=False)

        # Loop over all the train services in that board.
        k = 0
        num_of_rows = len(board.train_services)

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
        (' (London)', '')]

        # 4 across the top
        big_boards = ""
        for i in range(min(4,len(board.train_services))):
            service = board.train_services[i]
            destinations = [destination.location_name for destination in service.destinations]
            std = service.std
            destination_j = ",".join(destinations)
            if len(destination_j) > 19:
                for k, v in mapping:
                    destination_j = destination.replace(k, v)
            destination = (destination_j + " "*21)[0:19]

            platform = service.platform
            if platform == None:
                platform = "-"
            platform = (platform + " "*3)[0:3]
            if service.etd[0] in ["0","1","2"]:
                etd2 = "Ex " + service.etd
            else:
                etd2 = service.etd
            etd = (etd2 + " "*7)[0:9]
            #big_boards += "\n"
            big_boards += (std + " " + platform + "   "[0:3-len(platform)] + " " + etd +  " "*30)[0:19] + "\n"
            big_boards += self.colours.Style.BOLD + destination.upper() + self.colours.Style.DEFAULT + "\n"
            big_boards += "Calling at:        \n"
            calling_points = service.subsequent_calling_points[0]
            calling_at = []
            for point in calling_points:
                lname = point.location_name
                if len(lname) > 19:
                    for k, v in mapping:
                        lname = lname.replace(k, v)
                calling_at.append((lname + " "*21)[0:19])
            calling_at = (calling_at + [' '*19,' '*19,' '*19,' '*19,' '*19,' '*19,' '*19,' '*19,' '*19,' '*19,' '*19,' '*19,' '*19])[0:11]
            big_boards += "\n".join(calling_at)
            if len(calling_points)>=11:
                big_boards += ("\n+ " + str(len(calling_points)-10) + " stations            ")[0:20] + "\n"
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

        content += self.colours.Foreground.GREEN+"\nTime  Destination           Plt Exptd    Time  Destination           Plt Exptd "+self.colours.Foreground.DEFAULT
        for k in range(5):
            if k < num_of_rows:
                service = board.train_services[k]
                # Build a list of destinations for each train service.
                destinations = [destination.location_name for destination in service.destinations]
                std = service.std
                destination = (",".join(destinations) + " "*21)[0:21]
                platform = service.platform
                if platform == None:
                    platform = "-"
                platform = (platform + " "*3)[0:3]
                etd = (service.etd + " "*7)[0:7]
                content += "\n" + std + " " + destination + " " + platform + " " + etd + "  "

            if k + 5 < num_of_rows:
                service = board.train_services[k+5]
                # Build a list of destinations for each train service.
                destinations = [destination.location_name for destination in service.destinations]
                std = service.std
                destination = (",".join(destinations) + " "*21)[0:21]
                platform = service.platform
                if platform == None:
                    platform = "-"
                platform = (platform + " "*3)[0:3]
                etd = (service.etd + " "*7)[0:7]
                content += std + " " + destination + " " + platform + " " + etd

        self.content = content

pages=[]
train01 = TrainPage("851","London Blackfriars","BFR")
train02 = TrainPage("852","London Bridge","LBG")
train03 = TrainPage("853","London Cannon Street","CST")
train04 = TrainPage("854","London Charing Cross","CHX")
train05 = TrainPage("855","London Euston","EUS")
train06 = TrainPage("856","London Fenchurch Street","FST")
train08 = TrainPage("858","London Fields","LOF")
train09 = TrainPage("859","London Kings Cross","KGX",True)
train10 = TrainPage("860","London Liverpool Street","LST")
train11 = TrainPage("861","London Marylebone","MYB")
train12 = TrainPage("862","London Paddington","PAD")
train13 = TrainPage("863","Acton Central","ACC")
train14 = TrainPage("864","Acton Main Line","AML")
train15 = TrainPage("865","London St Pancras Intl.","STP")
train16 = TrainPage("866","Ffairfach","FFA")
train17 = TrainPage("867","London Victoria","VIC")
train18 = TrainPage("868","London Waterloo","WAT")
train19 = TrainPage("869","London Waterloo East","WAE")
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

tv_page = Page("850")
tv_page.content = colour_print(printer.text_to_ascii("Trains Index"))+"\n"
tv_page.title = "Trains Index"
i=0
for page in pages:
    tv_page.content+=tv_page.colours.Foreground.RED+page[0]+tv_page.colours.Foreground.DEFAULT+" "+page[1]
    if i==1:
        tv_page.content += "\n"
    else:
        tv_page.content += " "*(38-len(page[0]+page[1]))
    i = 1-i

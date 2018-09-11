from __future__ import division
from page import Page
from helpers import url_handler

class BusPage(Page):
    def __init__(self, page_num, bus_num, station, code):
        super(BusPage, self).__init__(page_num)
        self.title = station+" ("+code+") Buses"
        self.tagline = "Live buses from "+station+" ("+code+"). Data from TfL."
        self.in_index = False
        self.importance = 1
        self.station = station
        self.code = code
        self.bus_num = bus_num
        pages.append([page_num,station+" ("+code+")"])

    def generate_content(self):

        def reg(num):
            # Format registration plates
            if num[:3]=="LTZ":
                return num[:3] + " " + num[3:]
            else:
                return num[:4] + " " + num[4:]

        self.add_title(self.station,font='size4',fg="BRIGHTWHITE",bg="RED")

        underground =("WWWWWWWWWWW\n"
                      "WWWrrrrrWWW\n"
                      "WWrrWWWrrWW\n"
                      "WrrrrrrrrrW\n"
                      "WrrrrrrrrrW\n"
                      "WWrrWWWrrWW\n"
                      "WWWrrrrrWWW\n"
                      "WWWWWWWWWWW")
        self.print_image(underground,0,69)

        #self.add_title("buses")
        desc = " from "+self.station+" ("+self.code+")"
        self.move_cursor(x=80-len(desc))
        self.add_text(desc, bg="YELLOW", fg="BLUE")

        self.move_cursor(x=0)
        self.start_fg_color("GREEN")
        pos = (0,7,12,15,71)
        for p,t in zip(pos,("Time","Num","Pl","Destination","")):
            self.move_cursor(x=p)
            self.add_text(t)
        self.end_fg_color()
        self.add_newline()

        buses = []
        for bus_stop in self.bus_num:
            bus_times = url_handler.load_json("http://api.tfl.gov.uk/stopPoint/"+bus_stop+"/arrivals")

            for bus in bus_times:
                buses.append((int(bus['timeToStation']),str(bus['timeToStation']//60)+" min",bus['lineName'],bus['platformName'],bus['destinationName'],reg(bus['vehicleId'])))

        buses.sort()
        for bus in buses:
            for p,t,c in zip(pos,bus[1:],("GREEN","RED","BRIGHTWHITE",None,"GREY")):
                self.move_cursor(x=p)
                self.start_fg_color(c)
                self.add_text(t)
                self.end_fg_color()
            self.add_newline()


pages=[]

bus01 = BusPage("801",["490000077A","490000077C","490000077D","490000077E","490000077F"],"Euston Station","A/C/D/E/F")
bus02 = BusPage("802",["490000078P","490000078Q"],"Euston Square Station","P/Q")
bus03 = BusPage("803",["490012867L","490012867M"],"Upper Woburn Place / Euston Road","L/M")
bus04 = BusPage("804",["490013914N"],"Gower Street / UCH","N")
bus05 = BusPage("805",["490003174N","490003174S"],"Aldenham Street","S/T")
bus05.importance = 5
bus06 = BusPage("806",["490000152A","490000152C","490000152D","490000152F","490000152G","490000152K"],"Mornington Crescent","A/C/D/F/G/K")
bus07 = BusPage("807",["490011281N"],"Putney Common","D")
bus08 = BusPage("808",["490011133M"],"Portman Street / Selfridges","M")
bus09 = BusPage("809",["490015317N"],"George Street","K")
bus10 = BusPage("810",["490009990N"],"Dorset Street","R")
bus11 = BusPage("811",["490015040W"],"Old Marylebone Town Hall","W")
bus12 = BusPage("812",["490000011D"],"Baker Street Station","D")
bus13 = BusPage("813",["490007807E"],"Harley Street","M")
bus14 = BusPage("814",["490000191A"],"Regent's Park Station","A")
bus15 = BusPage("815",["490000091H"],"Great Portland St Stn / Euston Rd","H")
bus16 = BusPage("816",["490000252KA"],"Warren Street Station","KA")
bus17 = BusPage("817",["490000078Q"],"Euston Square Station","Q")
bus18 = BusPage("818",["490015700C"],"British Library","C")
bus19 = BusPage("819",["490000129E"],"King's Cross Station","E")
bus20 = BusPage("820",["490001172K"],"King's Cross Road","K")
bus21 = BusPage("821",["490005904E"],"Penton Rise","PG")
bus22 = BusPage("822",["490010928E"],"Penton Street","PK")
bus23 = BusPage("823",["490003650T"],"Baron Street / Chapel Market","T")
bus24 = BusPage("824",["490014603U"],"White Lion Street","U")



class TVIPage(Page):
    def __init__(self):
        super(TVIPage, self).__init__("800")
        self.title = "London Buses"
        self.index_num = "800-824"
        self.importance = 1

    def generate_content(self):
        self.add_title("Buses")

        for i,page in enumerate(pages):
            self.add_text(page[0], fg="RED")
            self.add_text(" "+page[1])
            if i%2==1:
                self.add_newline()
            else:
                self.move_cursor(x=38)

tp = TVIPage()

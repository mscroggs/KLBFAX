from __future__ import division
from page import Page
import url_handler

class BusPage(Page):
    def __init__(self, page_num, bus_num, station, code):
        super(BusPage, self).__init__(page_num)
        self.title = station+" ("+code+") Buses"
        self.tagline = "Live buses from "+station+" ("+code+"). Data from TfL."
        self.in_index = False
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
bus06 = BusPage("806",["490000152A","490000152C","490000152D","490000152F","490000152G","490000152K"],"Mornington Crescent","A/C/D/F/G/K")
#bus14 = BusPage("814",["490003174S"],"Aldenham St (south)","S")
#bus12 = BusPage("812",["490000078Q"],"Euston Square Station","Q")
#bus12 = BusPage("812",["490000078Q"],"Euston Square Station","Q")

class TVIPage(Page):
    def __init__(self):
        super(TVIPage, self).__init__("800")
        self.title = "Buses Index"

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

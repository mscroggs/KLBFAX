from __future__ import division
import json
from re import sub
from page import Page

def strip_tags(string):
    return sub(r'<[^>]*?>', '', string)

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
        import urllib2
        response = urllib2.urlopen("http://api.tfl.gov.uk/stopPoint/"+self.bus_num+"/arrivals")
        j = response.read()
        bus_times = json.loads(j)
        self.add_title("buses")
        desc = " from "+self.station+" ("+self.code+")"
        self.move_cursor(x=80-len(desc))
        self.add_text(desc, bg="YELLOW", fg="BLUE")
        self.move_cursor(x=0)

        self.start_fg_color("GREEN")
        pos = (0,7,11)
        for p,t in zip(pos,("Time","Num","Destination")):
            self.move_cursor(x=p)
            self.add_text(t)
        self.end_fg_color()
        self.add_newline()
        buses = []
        for bus in bus_times:
            buses.append((int(bus['timeToStation']),str(bus['timeToStation']//60)+" min",bus['lineName'],bus['destinationName']))

        buses.sort()
        for bus in buses:
            for p,t,c in zip(pos,bus[1:],("GREEN","RED",None)):
                self.move_cursor(x=p)
                self.start_fg_color(c)
                self.add_text(t)
                self.end_fg_color()
            self.add_newline()


pages=[]
bus01 = BusPage("801","490013914N","Gower Street / UCH","N")
bus02 = BusPage("802","490000078P","Euston Square Station","P")
bus03 = BusPage("803","490000077H","Euston Station","H")
bus04 = BusPage("804","490000077AZ","Euston Station","AZ")
bus05 = BusPage("805","490000077C","Euston Station","C")
bus06 = BusPage("806","490000077AP","Euston Bus Station","AP")
bus07 = BusPage("807","490000077D","Euston Station","D")
bus08 = BusPage("808","490000077G","Euston Bus Station","G")
bus09 = BusPage("809","490000077E","Euston Station","E")
bus10 = BusPage("810","490012867L","Upper Woburn Place / Euston Road","L")
bus11 = BusPage("811","490012867M","Upper Woburn Place","M")
bus12 = BusPage("812","72238","Jubilee Road","PD")
bus13 = BusPage("813","58812","Jubilee Road","J")
bus14 = BusPage("814","55027","Wembley Park Station","O")
bus15 = BusPage("815","490000078Q","Euston Square Station","Q")

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

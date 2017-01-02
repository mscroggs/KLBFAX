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
        self.add_title("buses")
        desc = " from "+self.station+" ("+self.code+")"
        self.move_cursor(x=80-len(desc))
        self.add_text(desc, bg="YELLOW", fg="BLUE")
        self.move_cursor(x=0)

        self.start_fg_color("GREEN")
        pos = (0,6,10)
        for p,t in zip(pos,("Time","Num","Destination")):
            self.move_cursor(x=p)
            self.add_text(t)
        self.end_fg_color()
        for bus in self.bus_times['arrivals']:
            self.add_newline()
            for p,t,c in zip(pos,(bus['estimatedWait'],bus['routeId'],bus["destination"]),("GREEN","RED",None)):
                self.move_cursor(x=p)
                self.start_fg_color(c)
                self.add_text(t)
                self.end_fg_color()
                self.add_newline()


    def background(self):
        import urllib2
        response = urllib2.urlopen("http://countdown.tfl.gov.uk/stopBoard/"+self.bus_num)
        j = response.read()
        self.bus_times = json.loads(j)

pages=[]
bus01 = BusPage("801","57596","Gower Street / UCH","N")
bus02 = BusPage("802","50975","Euston Square Station","P")
bus03 = BusPage("803","51664","Euston Station","H")
bus04 = BusPage("804","75100","Euston Station","AZ")
bus05 = BusPage("805","73933","Euston Station","C")
bus06 = BusPage("806","53602","Euston Bus Station","AP")
bus07 = BusPage("807","56230","Euston Station","D")
bus08 = BusPage("808","47118","Euston Bus Station","G")
bus09 = BusPage("809","58234","Euston Station","E")
bus10 = BusPage("810","51581","Upper Woburn Place / Euston Road","L")
bus11 = BusPage("811","72926","Upper Woburn Place","M")
bus12 = BusPage("812","72238","Jubilee Road","PD")
bus13 = BusPage("813","58812","Jubilee Road","J")
bus14 = BusPage("814","55027","Wembley Park Station","O")
bus15 = BusPage("815","59287","Euston Square Station","Q")

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

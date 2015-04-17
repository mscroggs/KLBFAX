import os
import json
from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from time import strftime

def strip_tags(string):
    return sub(r'<[^>]*?>', '', string)

class BusPage(Page):
    def __init__(self, page_num, bus_num, station, code):
        super(BusPage, self).__init__(page_num)
        self.title = station+" ("+code+") Buses"
        self.tagline = "Live buses from "+station+" ("+code+"). Data from TfL."
        self.station = station
        self.code = code
        self.bus_num = bus_num

    def generate_content(self):
        import urllib2
        content = colour_print(printer.text_to_ascii("BUSES",fill=False))+self.colours.Foreground.YELLOW+self.colours.Background.BLUE+" from "+self.station+" ("+self.code+")"+self.colours.Foreground.DEFAULT+self.colours.Background.DEFAULT

        content += self.colours.Foreground.BLUE+"\nTime  Num Destination"+self.colours.Foreground.DEFAULT
        response = urllib2.urlopen("http://countdown.tfl.gov.uk/stopBoard/"+self.bus_num)
        j = response.read()
        bus_times = json.loads(j)
        for bus in bus_times['arrivals']:
            content += "\n"
            content += self.colours.Foreground.GREEN+bus['scheduledTime']+self.colours.Foreground.DEFAULT
            content += " "+self.colours.Foreground.RED+bus['routeId']+self.colours.Foreground.DEFAULT
            content += " "*(4-len(bus['routeId']))
            content += bus['destination']
        self.content = content

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

from __future__ import division
import json
from page import Page

class TubePage(Page):
    def __init__(self, page_num, code, station):
        super(TubePage, self).__init__(page_num)
        self.title = station+" Underground Trains"
        self.tagline = "Live trains from "+station+". Data from TfL."
        self.in_index = False
        self.station = station
        self.code = code
        pages.append([page_num,station])

    def generate_content(self):
        import urllib2
        response = urllib2.urlopen("http://api.tfl.gov.uk/stopPoint/"+self.code+"/arrivals?mode=tube")
        j = response.read()
        tube_times = json.loads(j)

        tubes = []
        for b in tube_times:
            tubes.append((int(b['timeToStation']),str(b['timeToStation']//60)+" min",b['lineName'],b['towards'],b['currentLocation']))

        tubes.sort()

        self.add_title(self.station,font='size4')

        underground = """
WWWWWWWWWWW
WWWbbbbbWWW
WWbbWWWbbWW
WrrrrrrrrrW
WrrrrrrrrrW
WWbbWWWbbWW
WWWbbbbbWWW
WWWWWWWWWWW
"""
        self.print_image(underground,0,69)

        pos = (0,7,25,50)
        for p,t in zip(pos,("Time","Line","Destination","Current Location")):
            self.move_cursor(x=p)
            self.add_text(t)
        self.add_newline()

        for tube in tubes:
            if tube[2]=="Bakerloo":
                self.start_fg_color("WHITE")
                self.start_bg_color("ORANGE")
            if tube[2]=="Central":
                self.start_fg_color("WHITE")
                self.start_bg_color("RED")
            if tube[2]=="Circle":
                self.start_fg_color("BLACK")
                self.start_bg_color("YELLOW")
            if tube[2]=="District":
                self.start_fg_color("BLACK")
                self.start_bg_color("GREEN")
            if tube[2]=="Hammersmith & City":
                self.start_fg_color("BLACK")
                self.start_bg_color("PINK")
            if tube[2]=="Jubilee":
                self.start_fg_color("WHITE")
                self.start_bg_color("GREY")
            if tube[2]=="Metropolitan":
                self.start_fg_color("WHITE")
                self.start_bg_color("MAGENTA")
            if tube[2]=="Northern":
                self.start_fg_color("WHITE")
                self.start_bg_color("BLACK")
            if tube[2]=="Piccadilly":
                self.start_fg_color("WHITE")
                self.start_bg_color("BLUE")
            if tube[2]=="Victoria":
                self.start_fg_color("WHITE")
                self.start_bg_color("LIGHTBLUE")
            if tube[2]=="Waterloo & City":
                self.start_fg_color("WHITE")
                self.start_bg_color("LIGHTCYAN")
            self.add_text(" "*80)
            for p,t in zip(pos,tube[1:]):
                self.move_cursor(x=p)
                self.add_text(t)
            self.end_fg_color()
            self.end_bg_color()
            self.add_newline()


pages=[]
tube01 = TubePage("651","940GZZLUEUS","Euston")
tube02 = TubePage("652","940GZZLUESQ","Euston Square")
tube03 = TubePage("653","940GZZLUWRR","Warren Street")
tube04 = TubePage("654","940GZZLURSQ","Russell Square")
tube05 = TubePage("655","940GZZLUMTC","Mornington Crescent")
tube06 = TubePage("656","940GZZLUPVL","Perivale")
tube07 = TubePage("657","940GZZLUKSX","Kings Cross St Pancras")
tube08 = TubePage("658","940GZZLUTCR","Tottenham Court Road")
tube09 = TubePage("659","940GZZLUOXC","Oxford Circus")
tube10 = TubePage("660","940GZZLUALP","Alperton")
tube11 = TubePage("661","940GZZLUWLO","Waterloo")
tube12 = TubePage("662","940GZZLUEMB","Embankment")

class TVIPage(Page):
    def __init__(self):
        super(TVIPage, self).__init__("650")
        self.title = "Tube Index"

    def generate_content(self):
        self.add_title("Tube Index")

        for i,page in enumerate(pages):
            self.add_text(page[0], fg="RED")
            self.add_text(" "+page[1])
            if i%2==1:
                self.add_newline()
            else:
                self.move_cursor(x=38)

tp = TVIPage()

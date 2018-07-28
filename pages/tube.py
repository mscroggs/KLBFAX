from __future__ import division
import json
from page import Page
from helpers import url_handler

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
        tube_times = url_handler.load_json("http://api.tfl.gov.uk/stopPoint/"+self.code+"/arrivals?mode=tube")

        tubes = []
        platforms = []
        for b in tube_times:
            p = b['platformName'];
            if p not in platforms:
                platforms.append(p)
            tubes.append((b['platformName'],int(b['timeToStation']),str(b['timeToStation']//60).rjust(2,' ')+" min",b['lineName'].replace('Hammersmith','Ham').replace('Waterloo','Wloo'),b['towards'],b['currentLocation']))
        tubes.sort()

        #platforms = sorted(platforms, key=lambda x: int(x[-2:]));
        num_platforms = len(platforms);
        max_tubes_per_platform = 23//num_platforms-1;

        tubes_per_platform = [[] for i in range(len(platforms))]
        lines_per_platform = [[] for i in range(len(platforms))]

        for pnum, platform in enumerate(platforms):
            for tube in tubes:
                if tube[0] == platform:
                    tubes_per_platform[pnum].append(tube)
                    line = tube[3]
                    if line not in lines_per_platform[pnum]:
                        lines_per_platform[pnum].append(line)

        #for platform in lines_per_platform:
        #    platform.sort()

        platform_order = sorted(range(len(platforms)), key=lambda k: lines_per_platform[k][0] + " " + platforms[k])

        def set_colours(self,line_on_this_platform):
            if line_on_this_platform=="Bakerloo":
                self.start_fg_color("WHITE")
                self.start_bg_color("ORANGE")
            elif line_on_this_platform=="Central":
                self.start_fg_color("WHITE")
                self.start_bg_color("RED")
            elif line_on_this_platform=="Circle":
                self.start_fg_color("BLACK")
                self.start_bg_color("YELLOW")
            elif line_on_this_platform=="District":
                self.start_fg_color("BLACK")
                self.start_bg_color("GREEN")
            elif line_on_this_platform=="Ham & City":
                self.start_fg_color("BLACK")
                self.start_bg_color("PINK")
            elif line_on_this_platform=="Jubilee":
                self.start_fg_color("WHITE")
                self.start_bg_color("GREY")
            elif line_on_this_platform=="Metropolitan":
                self.start_fg_color("WHITE")
                self.start_bg_color("MAGENTA")
            elif line_on_this_platform=="Northern":
                self.start_fg_color("WHITE")
                self.start_bg_color("BLACK")
            elif line_on_this_platform=="Piccadilly":
                self.start_fg_color("WHITE")
                self.start_bg_color("BLUE")
            elif line_on_this_platform=="Victoria":
                self.start_fg_color("WHITE")
                self.start_bg_color("LIGHTBLUE")
            elif line_on_this_platform=="Wloo & City":
                self.start_fg_color("WHITE")
                self.start_bg_color("LIGHTCYAN")
            else:
                self.start_fg_color("WHITE")
                self.start_bg_color("BLACK")


        '''
        tubes = []
        for b in tube_times:
            tubes.append((int(b['timeToStation']),str(b['timeToStation']//60)+" min",b['lineName'].replace('Hammersmith','Ham').replace('Waterloo','Wloo'),b['towards'],b['currentLocation']))

        tubes.sort()

        '''

        self.add_title(self.station,font='size4',fg="BRIGHTWHITE",bg="BLUE")

        underground =("WWWWWWWWWWW\n"
                      "WWWrrrrrWWW\n"
                      "WWrrWWWrrWW\n"
                      "WbbbbbbbbbW\n"
                      "WbbbbbbbbbW\n"
                      "WWrrWWWrrWW\n"
                      "WWWrrrrrWWW\n"
                      "WWWWWWWWWWW")
        self.print_image(underground,0,69)
        '''
        for pnum in platform_order:
            platform = platforms[pnum]
            print " ".join(sorted(lines_per_platform[pnum])) + " " + platform
            for t in tubes_per_platform[pnum][:max_tubes_per_platform]:
                print t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5].replace("Platform ","P")
        '''
        self.add_newline()
        pos = (0,7,20,45)
        for pnum in platform_order:
            platform = platforms[pnum]

            num_lines_on_this_platform = len(lines_per_platform[pnum])
            Nx = 80//num_lines_on_this_platform;
            platform_title = " " + "/".join(sorted(lines_per_platform[pnum])) + " " + platform
            for i, line_on_this_platform in enumerate(sorted(lines_per_platform[pnum])):
                set_colours(self,line_on_this_platform);
                self.move_cursor(x=Nx*i)
                self.add_text(" "*80)
                self.move_cursor(x=Nx*i)
                self.add_text(platform_title[Nx*i:Nx*(i+1)])
                self.end_fg_color()
                self.end_bg_color()
            self.add_newline()
            for tube in tubes_per_platform[pnum][:max_tubes_per_platform]:
                #print t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5].replace("Platform ","P")
                for p,t in zip(pos,tube[2:]):
                    self.move_cursor(x=p)
                    self.add_text(t)
                self.add_newline()
            #self.add_newline()
        '''
        pos = (0,7,20,45)
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
            if tube[2]=="Ham & City":
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
            if tube[2]=="Wloo & City":
                self.start_fg_color("WHITE")
                self.start_bg_color("LIGHTCYAN")
            self.add_text(" "*80)
            for p,t in zip(pos,tube[1:]):
                self.move_cursor(x=p)
                self.add_text(t)
            self.end_fg_color()
            self.end_bg_color()
            self.add_newline()
        '''

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
tube13 = TubePage("663","940GZZLUSKS","South Kensington")
tube14 = TubePage("664","940GZZLUGTR","Gloucester Road")
tube15 = TubePage("665","940GZZLUBNK","Bank")
tube16 = TubePage("666","940GZZLUBST","Baker Street")

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

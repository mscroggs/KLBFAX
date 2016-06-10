import os
from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
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
        import urllib2
        content = colour_print(printer.text_to_ascii("TRAINS",fill=False))+self.colours.Foreground.YELLOW+self.colours.Background.BLUE+" from "+self.station+self.colours.Foreground.DEFAULT+self.colours.Background.DEFAULT
        content += self.colours.Foreground.GREEN+"\nTime Destination"+" "*49+"Platform\n"+self.colours.Foreground.DEFAULT
        response = urllib2.urlopen("http://www.opentraintimes.com/location/"+self.code+"/"+self.now().strftime("%Y-%m-%d/%H:%M")+"?passenger=on&show_call=on&show_stp=on&show_var=on&show_wtt=on&utf8=%E2%9C%93")
        html = response.read()
        trains = html.split("<table")[1].split("</table>")[0].split("<tr>")
        first = False
        if self.hogwarts: first = True
        for train in trains[2:]:
            if first:
                content += "0900 Hogwarts Express"
                content += " "*44
                content += "9 3/4\n"
                first = False
            train = strip_tags(train).lstrip()
            train = train.split("\n")
            try:
                if train[4].lstrip()!="Terminates here" and int(train[5].lstrip().split("&")[0])>=int(self.now().strftime("%H%M")):
                    if self.to is None or train[4].lstrip() in self.to:
                        new = train[5].lstrip()+" "+train[4].lstrip()
                        new = "&".join(new.split("&amp;"))
                        new = "'".join(new.split("&#39;"))
                        new = "".join(new.split("&frac12;"))
                        new += " "*(65-len(new))+train[3].lstrip()+"\n"
                        content += new
            except:
                pass
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
train32 = TrainPage("883","St Pancras to East Croydon","STP",to=["Three Bridges","Brighton"])
train32 = TrainPage("883","Blaenau Ffestiniog","BFF")

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

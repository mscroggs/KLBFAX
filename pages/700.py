import os
from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from time import strftime

def strip_tags(string):
    return sub(r'<[^>]*?>', '', string)

class TrainPage(Page):
    def __init__(self, page_num, station, code):
        super(TrainPage, self).__init__(page_num)
        self.title = station+" Trains"
        self.tagline = "Live trains from "+code+". Data from opentraintimes.com."
        self.station = station
        self.code = code

    def generate_content(self):
        import urllib2
        content = colour_print(printer.text_to_ascii("TRAINS"))+self.colours.Foreground.YELLOW+self.colours.Background.BLUE+" from "+self.station+self.colours.Foreground.DEFAULT+self.colours.Background.DEFAULT
        content += self.colours.Foreground.GREEN+"\nTime Destination"+" "*49+"Platform\n"+self.colours.Foreground.DEFAULT
        response = urllib2.urlopen("http://www.opentraintimes.com/location/"+self.code+"/"+self.now().strftime("%Y-%m-%d/%H:%M")+"?passenger=on&show_call=on&show_stp=on&show_var=on&show_wtt=on&utf8=%E2%9C%93")
        html = response.read()
        trains = html.split("<table")[1].split("</table>")[0].split("<tr>")
        for train in trains[2:]:
            train = strip_tags(train).lstrip()
            train = train.split("\n")
            try:
             if train[4].lstrip()!="Terminates here" and int(train[5].lstrip().split("&")[0])>=int(self.now().strftime("%H%M")):
                new = train[5].lstrip()+" "+train[4].lstrip()
                new = "&".join(new.split("&amp;"))
                new = "'".join(new.split("&#39;"))
                new = "".join(new.split("&frac12;"))
                new += " "*(65-len(new))+train[3].lstrip()+"\n"
                content += new
            except:
             pass
        self.content = content

train01 = TrainPage("701","London Blackfriars","BFR")
train02 = TrainPage("702","London Bridge","LBG")
train03 = TrainPage("703","London Cannon Street","CST")
train04 = TrainPage("704","London Charing Cross","CHX")
train05 = TrainPage("705","London Euston","EUS")
train06 = TrainPage("706","London Fenchurch Street","FST")
train08 = TrainPage("708","London Fields","LOF")
train09 = TrainPage("709","London Kings Cross","KGX")
train10 = TrainPage("710","London Liverpool Street","LST")
train11 = TrainPage("711","London Marylebone","MYB")
train12 = TrainPage("712","London Paddington","PAD")
train13 = TrainPage("713","Acton Central","ACC")
train14 = TrainPage("714","Acton Main Line","AML")
train15 = TrainPage("715","London St Pancras Intl.","STP")
train16 = TrainPage("716","Ffairfach","FFA")
train17 = TrainPage("717","London Victoria","VIC")
train18 = TrainPage("718","London Waterloo","WAT")
train19 = TrainPage("719","London Waterloo East","WAE")
train20 = TrainPage("720","Banbury","BAN")
train21 = TrainPage("721","Reading","RDG")
train22 = TrainPage("722","Oxford","OXF")
train23 = TrainPage("723","Stratford-upon-Avon","SAV")
train24 = TrainPage("724","B'ham New Street","BHM")
train25 = TrainPage("725","B'ham Moor Street","BMO")
train26 = TrainPage("726","B'ham Snow Hill","BSW")
train27 = TrainPage("727","Wembley Stadium","WCX")
train28 = TrainPage("728","Kilmarnock","KMK")
train29 = TrainPage("729","Moreton-in-Marsh","MIM")
train30 = TrainPage("730","Ealing Broadway","EAL")

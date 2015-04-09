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
        self.title = "Trains"
        self.tagline = "Live trains from "+station+". Data from opentraintimes.com."
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
            if train[4].lstrip()!="Terminates here" and int(train[5].lstrip())>int(self.now().strftime("%H%M")):
                new = train[5].lstrip()+" "+train[4].lstrip()
                new += " "*(65-len(new))+train[3].lstrip()+"\n"
                content += new
        self.content = content

train01 = TrainPage("701","Euston","EUS")
train02 = TrainPage("702","Waterloo","WAT")
train03 = TrainPage("703","Paddington","PAD")
train04 = TrainPage("704","Banbury","BAN")
train05 = TrainPage("705","Marylebone","MYB")
train06 = TrainPage("706","London Bridge","LBG")
train08 = TrainPage("708","King's Cross","KGX")
train09 = TrainPage("709","Reading","RDG")
train10 = TrainPage("710","Oxford","OXF")
train11 = TrainPage("711","Stratford-upon-Avon","SAV")
train12 = TrainPage("712","B'ham New Street","BHM")
train13 = TrainPage("713","B'ham Moor Street","BMO")
train14 = TrainPage("714","B'ham Snow Hill","BSW")
train15 = TrainPage("715","Wembley Stadium","WCX")
train16 = TrainPage("716","Kilmarnock","KMK")

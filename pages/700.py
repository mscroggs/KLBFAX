import os
from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from time import strftime

def strip_tags(string):
    return sub(r'<[^>]*?>', '', string)

class TrainPage(Page):
    def __init__(self, page_num):
        super(TrainPage, self).__init__(page_num)
        self.title = "Trains"
        self.tagline = "Live trains from Euston. Data from opentraintimes.com."

    def generate_content(self):
        import urllib2
        content = colour_print(printer.text_to_ascii("TRAINS"))+self.colours.Foreground.YELLOW+self.colours.Background.BLUE+" from Euston"+self.colours.Foreground.DEFAULT+self.colours.Background.DEFAULT
        content += self.colours.Foreground.GREEN+"\nTime Destination"+" "*49+"Platform\n"+self.colours.Foreground.DEFAULT
        response = urllib2.urlopen("http://www.opentraintimes.com/location/EUSTON/?passenger=on&show_call=on&show_stp=on&show_var=on&show_wtt=on&utf8=%E2%9C%93")
        html = response.read()
        trains = html.split("<table")[1].split("</table>")[0].split("<tr>")
        for train in trains[2:]:
            train = strip_tags(train).lstrip()
            train = train.split("\n")
            if train[4].lstrip()!="Terminates here" and int(train[5].lstrip())>int(strftime("%H%M")):
                new = train[5].lstrip()+" "+train[4].lstrip()
                new += " "*(65-len(new))+train[3].lstrip()+"\n"
                content += new
        self.content = content

page_number = os.path.splitext(os.path.basename(__file__))[0]
train_page = TrainPage(page_number)

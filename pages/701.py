from page import Page
from screen import WIDTH
import urllib2
import json
from name import NAME
from printer import instance as printer
from dateutil import parser
from datetime import datetime

def just_time(stuff):
    times = stuff.split()[1].split(":")
    return times[0] + ":" + times[1]

class EMFPage(Page):
    def __init__(self, page_num, n):
        super(EMFPage, self).__init__(page_num)
        self.title = "EMF Schedule"
        self.in_index = False
        self.is_enabled = True
        self.n = n
        self.day = ["2016-08-05","2016-08-06","2016-08-07"][n-1]
        self.endday = parser.parse("2016-08-0"+["6","7","8"][n-1]+" 00:00:00")

    def generate_content(self):
        the_json = json.load(urllib2.urlopen("https://www.emfcamp.org/schedule.json"))
        content = self.colours.colour_print(printer.text_to_ascii("EMF Day "+str(self.n),vertical_condense=True))
        events = []
        for item in the_json:
            the_date = parser.parse(item["end_date"])
            if item["start_date"].split()[0] == self.day:
                if datetime.now() > self.endday or the_date > datetime.now():
                    events.append(item)
        print [a["start_date"] for a in events]
        events = sorted(events, key=lambda item: item["start_date"])
        print [a["start_date"] for a in events]
        for item in events:
            content += self.colours.Foreground.YELLOW
            content += just_time(item["start_date"])
            content += " - "
            content += just_time(item["end_date"])
            content += self.colours.Style.BOLD
            content += "  "
            content += item["venue"]
            content += self.colours.Foreground.DEFAULT
            content += "\n"
            speaker = " - " + item["speaker"]
            title = item["title"]
            if len(title) > WIDTH - len(speaker):
                title = title[:WIDTH - len(speaker)-3]+"..."
            content += title + speaker
            content += "\n\n"
        self.content = content

page1 = EMFPage("701",1)
page2 = EMFPage("702",2)
page3 = EMFPage("703",3)

page1.in_index = True
page1.index_num = "701-703"

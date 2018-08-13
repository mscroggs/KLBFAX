from page import Page
import config
from datetime import datetime
from helpers import url_handler

def just_date(stuff):
    return stuff.split()[0]

def just_time(stuff):
    times = stuff.split()[1].split(":")
    return times[0] + ":" + times[1]

class NowAndNextPage(Page):
    def __init__(self, page_num, master):
        super(NowAndNextPage, self).__init__(page_num)
        self.master = master
        self.title = "Now and Next"
        self.subtitle = self.title
        self.in_index = False
        self.importance = 5

    def generate_content(self):
        self.add_title("Now & Next",fg="BLACK",bg="PINK",font="size4bold")
        events = {}
        for item in self.master.data:
            the_date = datetime.strptime(item["end_date"],"%Y-%m-%d %H:%M:%S")
            if the_date > config.now():
                if item["venue"] not in events:
                    events[item["venue"]] = []
                events[item["venue"]].append(item)
        for venue in self.master.villages:
            if venue in events:
                self.add_text(venue, fg="GREEN")
                self.add_newline()
                village_events = sorted(events[venue], key=lambda item: item["start_date"])
                for i,item in enumerate(village_events[:2]):
                    self.add_text(just_time(item["start_date"])+"-"+just_time(item["end_date"])+" ", fg="ORANGE")
                    speaker = item["speaker"]
                    title = item["title"]
                    self.add_text(title)
                    self.move_cursor(x=config.WIDTH-14)
                    self.add_text(" "+speaker, fg="GREEN")
                    self.add_newline()
                self.add_newline()


class EMFPage(Page):
    def __init__(self, page_num, n, master):
        super(EMFPage, self).__init__(page_num)
        self.master = master
        self.title = "EMF Schedule Day "+str(n)
        self.subtitle = "Day "+str(n)
        self.in_index = False
        self.importance = 4
        self.n = n
        if n == 1:
            self.day = "2018-08-31"
            self.endday = datetime(year=2018, month=9, day=1, hour=0, minute=0)
        if n == 2:
            self.day = "2018-09-01"
            self.endday = datetime(year=2018, month=9, day=2, hour=0, minute=0)
        if n == 3:
            self.day = "2018-09-02"
            self.endday = datetime(year=2018, month=9, day=3, hour=0, minute=0)

    def generate_content(self):
        self.add_title("EMF Day "+str(self.n), font="size4bold")
        events = []
        for item in self.master.data:
            the_date = datetime.strptime(item["end_date"],"%Y-%m-%d %H:%M:%S")
            if item["start_date"].split()[0] == self.day:
                if config.now() > self.endday or the_date > config.now():
                    events.append(item)
        events = sorted(events, key=lambda item: item["start_date"])
        for item in events:
            self.add_text(just_time(item["start_date"])+"-"+just_time(item["end_date"])+" ", fg="ORANGE")
            venue = item["venue"]
            if venue == "Workshop 1":
                venue = "Wshop 1"
            if venue == "Workshop 2":
                venue = "Wshop 2"
            if venue == "Workshop 3":
                venue = "Wshop 3"
            if len(venue) > 7:
                venue = venue[:7]
            self.add_text(venue+" ", fg="YELLOW")
            speaker = item["speaker"]
            title = item["title"]
            self.add_text(title)
            self.move_cursor(x=config.WIDTH-14)
            self.add_text(" "+speaker, fg="GREEN")
            self.add_newline()

class EMFVillagePage(Page):
    def __init__(self, page_num, village, master):
        super(EMFVillagePage, self).__init__(page_num)
        self.master = master
        self.title = "EMF Schedule ("+village+")"
        self.subtitle = village
        self.village = village
        self.in_index = False

    def generate_content(self):
        self.add_title(self.village, font="size4bold")
        events = []
        past_events = []
        for item in self.master.data:
            if item["venue"] == self.village:
                the_date = datetime.strptime(item["end_date"],"%Y-%m-%d %H:%M:%S")
                if the_date > config.now():
                    events.append(item)
                else:
                    past_events.append(item)
        events = sorted(events, key=lambda item: item["start_date"])
        past_events = sorted(past_events, key=lambda item: item["start_date"])
        date = ""
        for item in events+[None]+past_events:
            if item is None:
                date = ""
                self.add_newline()
                self.add_newline()
                self.add_text("Past events",fg="RED")
                self.add_newline()
            else:
                thisdate = just_date(item["start_date"])
                if date != thisdate:
                    self.add_newline()
                    self.add_text(thisdate,fg="GREEN")
                    self.add_newline()
                    date = thisdate
                self.add_text(just_time(item["start_date"])+"-"+just_time(item["end_date"])+" ", fg="ORANGE")
                speaker = item["speaker"]
                title = item["title"]
                self.add_text(title)
                self.move_cursor(x=config.WIDTH-14)
                self.add_text(" "+speaker, fg="GREEN")
                self.add_newline()

class IndexPage(Page):
    def __init__(self, num):
        super(IndexPage, self).__init__(num)
        self.title = "EMF Schedule"
        self.list = []
        self.importance = 3

    def generate_content(self):
        self.add_title("EMF Schedule",font="size4bold")
        for i,page in enumerate(self.list):
            self.add_text(page.number, fg="RED")
            self.add_text(" "+page.subtitle)
            if i%2==0:
                self.move_cursor(x=38)
                self.add_text(" ")
            else:
                self.add_newline()

    def background(self):
        self.data = url_handler.load_json("https://www.emfcamp.org/schedule.json")
        # Schedule from 2016 for testing:
        #self.data = url_handler.load_json("https://raw.githubusercontent.com/emfcamp/Website/master/exports/2016/public/schedule.json")

    def set_list(self,list):
        self.list = list
        self.index_num = self.number+"-"+max(p.number for p in self.list)

    def set_villages(self,list):
        self.villages = list

index = IndexPage("704")
try:
    index.background()
except:
    index.data = []

plist = []
plist.append(NowAndNextPage("705",index))
plist.append(EMFPage("706",1,index))
plist.append(EMFPage("707",2,index))
plist.append(EMFPage("708",3,index))
num = 709

first = ["Stage A","Stage B","Stage C","Workshop 1","Workshop 2","Workshop 3"]
villages = []
for event in index.data:
    if event["venue"] not in first+villages:
        villages.append(event["venue"])
villages.sort()
for v in first+villages:
    plist.append(EMFVillagePage(str(num),v,index))
    num += 1
index.set_villages(first+villages)
index.set_list(plist)



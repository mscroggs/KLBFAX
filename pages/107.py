from page import Page
from datetime import datetime, timedelta
import pytz

class MRoomPage(Page):
    def __init__(self,page_num):
        super(MRoomPage, self).__init__(page_num)
        self.title = "Muirhead Room"

    def background(self):
        import urllib2
        import json
        import config
        from dateutil import parser
        response = urllib2.urlopen("http://www.mscroggs.co.uk/room_list.json")
        self.events = json.load(response)
        now = config.now().replace(tzinfo=None)
        for e in self.events:
            e[0] = parser.parse(e[0])
            e[1] = parser.parse(e[1])
        self.events = [e for e in self.events if e[1]>now]

        
      
    def generate_content(self):
        import config
        from time import strftime
        
        def friendly_date(date):
            if date.date() == datetime.today().date():
                return "Today"
            elif date.date() == datetime.today().date() + timedelta(days=1):
                return "Tomorrow"
            else:
                return date.strftime("%A %-d")

        self.add_title("Muirhead Room")
        self.add_newline()
        now = config.now().replace(tzinfo=None)
    
        occupied = False
        for event in self.events:
            if event[0] < now and event[1] > now:
                occupied = True
        
        if occupied:
            self.start_fg_color("WHITE")
            self.start_bg_color("RED")
            next_free = 0
            i = 0
            while next_free == 0:
                if self.events[i+1][0] != self.events[i][1]:
                    next_free = self.events[i][1]
                i+=1
            message = "Busy until " + next_free.strftime("%H:%M")
        else:
            try:
                next_occupied = self.events[0][0]
            except:
                next_occupied = datetime.today() + timedelta(days=300)
            if next_occupied.date() != now.date():             
                message =  "Free all day"
            else:
                message = "Free until " + next_occupied.strftime("%H:%M")
            if next_occupied.date() - now.date() <= timedelta(hours=1):             
                self.start_fg_color("BLACK")
                self.start_bg_color("YELLOW")
            else:
                self.start_fg_color("BLACK")
                self.start_bg_color("GREEN")
            
        
        left_banner = " "*int((config.WIDTH - len(message))/2)
        right_banner = " "*int(round((config.WIDTH - len(message))/2))
        
              
        self.add_text(left_banner + message + right_banner)
        self.end_fg_color()
        self.end_bg_color()
        self.add_newline()
        previous_date = datetime(2015,3,14).date()
        for event in self.events:
            start_time = event[0]
            end_time = event[1]
            _name = event[2]

            if end_time.date() != previous_date:
                self.add_newline()
                self.start_fg_color("GREEN")
                self.add_text(friendly_date(end_time))
                self.end_fg_color()
                self.add_newline()
            self.start_fg_color("RED")
            
            self.add_text(start_time.strftime("%H:%M") + "-" + end_time.strftime("%H:%M") + " ")
            self.end_fg_color()
            self.add_text(_name)
            self.add_newline()
            previous_date = end_time.date()
          
muirheadpage = MRoomPage("107")

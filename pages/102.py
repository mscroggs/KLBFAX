from page import Page
from colours import colour_print
from printer import instance as printer
from datetime import datetime, timedelta
import pytz
import screen

class XMenPage(Page):
    def __init__(self,page_num):
        super(XMenPage, self).__init__(page_num)
        self.title = "X-Men Origins Seminar Room"
      
    def generate_content(self):
        import urllib2
        import now
        from time import strftime
        
        def friendly_date(date):
            if date.date() == datetime.today().date():
                return "Today"
            elif date.date() == datetime.today().date() + timedelta(days=1):
                return "Tomorrow"
            else:
                return date.strftime("%A %-d")

        content = colour_print(printer.text_to_ascii("X-Mart Origins"))
    
        response = urllib2.urlopen("https://www.hep.ucl.ac.uk/restricted/mrbs/month.php?area=5&room=15")
        html = response.readlines()
        now = now.now().replace(tzinfo=None)
        events = []
        
        for line in html:
            lst = line.strip("\n")
            if '<a href="view_entry.php' in lst:
                year  = int(lst.split("year=") [1].split('"')[0])
                month = int(lst.split("month=")[1].split("&")[0])
                day   = int(lst.split("day=")  [1].split("&")[0])
                title = lst.split('title="')[1].split('"')[0]
                start_hour_minute = title[0:5]
                end_hour_minute = title[6:11]
                start_time = datetime(year, month, day, int(start_hour_minute[0:2]), int(start_hour_minute[3:5]))
                end_time = datetime(year, month, day, int(end_hour_minute[0:2]), int(end_hour_minute[3:5]))
                name = title[12:]
                if end_time > now:
                    events.append([start_time,end_time,name])
        
        occupied = False
        for event in events:
            if event[0] < now and event[1] > now:
                occupied = True
        
        if occupied == False:
            next_occupied = events[0][0]
            colours_start = self.colours.Background.GREEN + self.colours.Foreground.BLACK
            colours_end = self.colours.Foreground.DEFAULT + self.colours.Background.DEFAULT   
            if next_occupied.date() != now.date():             
                message =  "Free all day"
            else:
                message = "Free until " + next_occupied.strftime("%H:%M")
            if next_occupied.date() - now.date() <= timedelta(hours=1):             
                colours_start = self.colours.Background.YELLOW + self.colours.Foreground.BLACK
                colours_end = self.colours.Foreground.DEFAULT + self.colours.Background.DEFAULT 
            else:
                colours_start = self.colours.Background.GREEN + self.colours.Foreground.BLACK
                colours_end = self.colours.Foreground.DEFAULT + self.colours.Background.DEFAULT 
            
        if occupied == True:
            colours_start = self.colours.Background.RED + self.colours.Foreground.WHITE
            colours_end = self.colours.Foreground.DEFAULT + self.colours.Background.DEFAULT   
            next_free = 0
            i = 0
            while next_free == 0:
                if events[i+1][0] != events[i][1]:
                    next_free = events[i][1]
                i+=1
            message = "Busy until " + next_free.strftime("%H:%M")
        
        left_banner = " "*int((screen.WIDTH - len(message))/2)
        right_banner = " "*int(round((screen.WIDTH - len(message))/2))
        
        content += "\n\n"       
        content += colours_start + left_banner + message + right_banner + colours_end + "\n"
        
        previous_date = datetime(2015,3,14).date()
        for event in events:
            start_time = event[0]
            end_time = event[1]
            name = event[2]

            if end_time.date() != previous_date:
                content += "\n  "+self.colours.Foreground.GREEN
                content += friendly_date(end_time)
                content += self.colours.Foreground.DEFAULT + "\n"
            content += self.colours.Foreground.RED
            
            content += start_time.strftime("%H:%M") + "-" + end_time.strftime("%H:%M") + " "
            content += self.colours.Foreground.DEFAULT
            content += name
            content += "\n"
            previous_date = end_time.date()
          
        self.content = content
        
xmenpage = XMenPage("102")

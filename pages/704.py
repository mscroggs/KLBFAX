from page import Page
import urllib2
import json
from name import NAME
from printer import instance as printer

class ShiftsPage(Page):
    def __init__(self, page_num):
        super(ShiftsPage, self).__init__(page_num)
        self.title = "EMF Shifts"
        if NAME == "EMFFAX":
            self.in_index = True
        else:
            self.in_index = False
        self.is_enabled = False

    def generate_content(self):
        from datetime import datetime
        from time import time
        ppl = {"MScroggs":"https://volunteer.emfcamp.org/?p=shifts_json_export&key=770eba74118011291e0e7313a9f63491"}
        shifts = []
        for p,feed in ppl.items():
            try:
                the_json = json.decode(urllib2.urlopen(feed))
            except:
                the_json = [{"name":"Manager","SID":"215","title":None,"shifttype_id":"11","start":"1470384000","end":"1470394800","RID":"13","URL":None,"PSID":None,"created_by_user_id":"1","created_at_timestamp":"1468958654","edited_by_user_id":None,"edited_at_timestamp":"0","room_name":"Volunteer Tent"},{"name":"Manager","SID":"218","title":None,"shifttype_id":"11","start":"1470470400","end":"1470481200","RID":"13","URL":None,"PSID":None,"created_by_user_id":"1","created_at_timestamp":"1468958695","edited_by_user_id":None,"edited_at_timestamp":"0","room_name":"Volunteer Tent"},{"name":"Manager","SID":"221","title":None,"shifttype_id":"11","start":"1470556800","end":"1470567600","RID":"13","URL":None,"PSID":None,"created_by_user_id":"1","created_at_timestamp":"1468958735","edited_by_user_id":None,"edited_at_timestamp":"0","room_name":"Volunteer Tent"}]
            for a in the_json:
                print a["end"],time()
                if int(a["end"]) > time():
                    shifts.append((p,a["start"],a["end"],a["room_name"]))
        sorted(shifts, key=lambda student: student[1])
        
        content = self.colours.colour_print(printer.text_to_ascii("EMF Volunteer Shifts"))
        content += "\n\n"

        for shift in shifts:
            content += self.colours.Foreground.RED + self.colours.Style.BOLD
            content += datetime.fromtimestamp(int(shift[1])).strftime('%d %b %H:%M')
            content += "-"
            content += datetime.fromtimestamp(int(shift[2])).strftime('%H:%M')
            content += self.colours.Foreground.DEFAULT + self.colours.Style.DEFAULT
            content += "  "
            content += self.colours.Foreground.GREEN + self.colours.Style.BOLD
            content += shift[0]
            content += self.colours.Foreground.DEFAULT + self.colours.Style.DEFAULT
            content += " " * (15-len(shift[0]))
            content += self.colours.Foreground.YELLOW + self.colours.Style.BOLD
            content += shift[3]
            content += self.colours.Foreground.DEFAULT + self.colours.Style.DEFAULT
            content += " " * (15-len(shift[3]))
            content += "\n"
            
        self.content = content

p_page = ShiftsPage("704")


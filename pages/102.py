from page import Page
from colours import colour_print
from printer import instance as printer

class XMenPage(Page):
    def __init__(self,page_num):
        super(XMenPage, self).__init__(page_num)
        self.title = "X-Men Origins Seminar Room"

    def generate_content(self):
        import urllib2
    
        content = colour_print(printer.text_to_ascii("X-Men Origins Seminar Room"))
    
        response = urllib2.urlopen("https://www.hep.ucl.ac.uk/restricted/mrbs/month.php?area=5&room=15")
        html = response.readlines()
        y,m,d = ("","","")
        for line in html:
            lst = line.strip("\n")
            if '<a href="view_entry.php' in lst:
                year  = lst.split("year=") [1].split('"')[0]
                month = lst.split("month=")[1].split("&")[0]
                day   = lst.split("day=")  [1].split("&")[0]
                title = lst.split('title="')[1].split('"')[0]
                if y!=year or m!=month or d!=day:
                    y=year
                    m=month
                    d=day
                    content += "\n  "+self.colours.Foreground.GREEN
                    content += y + "-" + m + "-" + "0"*(2-len(d)) + d
                    content += self.colours.Foreground.DEFAULT + "\n"
                content += title+"\n"
    
        self.content = content
xmenpage = XMenPage("102")

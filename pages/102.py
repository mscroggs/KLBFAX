from page import Page
from colours import colour_print
from printer import instance as printer

class XMenPage(Page):
    def __init__(self,page_num):
        super(XMenPage, self).__init__(page_num)
        self.title = "X-Men Origins Seminar Room"

    def generate_content(self):
        import urllib2
        from time import strftime

        content = colour_print(printer.text_to_ascii("X-Men Origins Seminar Room"))
    
        response = urllib2.urlopen("https://www.hep.ucl.ac.uk/restricted/mrbs/month.php?area=5&room=15")
        html = response.readlines()
        started = False
        y,m,d = (int(strftime("%Y")),int(strftime("%m")),int(strftime("%d")))
        for line in html:
            lst = line.strip("\n")
            if '<a href="view_entry.php' in lst:
                year  = int(lst.split("year=") [1].split('"')[0])
                month = int(lst.split("month=")[1].split("&")[0])
                day   = int(lst.split("day=")  [1].split("&")[0])
                title = lst.split('title="')[1].split('"')[0]
                if not started:
                    if y<=year and m<=month and d<=day:
                        started = True
                        y,m,d = (0,0,0)
                if started:
                    if y!=year or m!=month or d!=day:
                            y=year
                            m=month
                            d=day
                            content += "\n  "+self.colours.Foreground.GREEN
                            content += str(y) + "-" + "0"*(2-len(str(m))) + str(m) + "-" + "0"*(2-len(str(d))) + str(d)
                            content += self.colours.Foreground.DEFAULT + "\n"
                    content += self.colours.Foreground.RED
                    content += (self.colours.Foreground.DEFAULT+" ").join(title.split(" "))
                    content += "\n"
    
        self.content = content
xmenpage = XMenPage("102")

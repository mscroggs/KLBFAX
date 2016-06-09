import os
from page import Page
from printer import instance as printer
from printer import size4_instance as size4_printer
from colours import colour_print

people = [
                ["Doaky","Albania"],
                ["Rafael","France"],
                ["","Romania"],
                ["Huda","Switzerland"],
                ["Adam","England"],
                ["","Russia"],
                ["Mart","Slovakia"],
                ["Pietro","Wales"],
                ["Belgin","Germany"],
                ["","Northern Ireland"],
                ["Grace","Poland"],
                ["Mattia","Ukraine"],
                ["","Croatia"],
                ["Anna","Czech Republic"],
                ["","Spain"],
                ["","Turkey"],
                ["Rudie","Belgium"],
                ["Luca","Italy"],
                ["Sam","Republic of Ireland"],
                ["","Sweden"],
                ["Wei Guan","Austria"],
                ["","Hungary"],
                ["Scroggs","Iceland"],
                ["Olly","Portugal"]
                 ]



class SoccerPage(Page):
    def __init__(self, page_num):
        super(SoccerPage, self).__init__(page_num)
        self.title = "Euro 2016 Sweepstake"

    def generate_content(self):
        content = colour_print(printer.text_to_ascii("Euro 2016 Sweepstake"))
        
        lines = [ls[1] + self.colours.Foreground.BLUE+" ("+ls[0]+")"+self.colours.Foreground.DEFAULT for ls in people]
        for i in range(12):
            if i%4 == 0:
                content += "\n"
                content += self.colours.Foreground.GREEN + "Group " + str(i/4+1) + self.colours.Foreground.DEFAULT
                content += " " * 24
                content += self.colours.Foreground.GREEN + "Group " + str(i/4+4) + self.colours.Foreground.DEFAULT
                content += "\n"
            content += lines[i]
            content += " "*(40-len(lines[i]))
            content += lines[i+12]
            content += "\n"
        self.content = content

soccer_page = SoccerPage("310")

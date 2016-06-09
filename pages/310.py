from page import Page
from printer import instance as printer
from printer import size4_instance as size4_printer
import colours
from colours import colour_print
from now import now

def get_team(code):
    for a in people:
        if a[2] == code:
            return a
    return None

def get_team_n(code):
    for i,a in enumerate(people):
        if a[2] == code:
            return i
    return None

people = [
          ["Doaky","Albania","ALB"], ["Rafael","France","FRA"], ["","Romania","ROM"], ["Huda","Switzerland","SWI"],
          ["Adam","England","ENG"], ["","Russia","RUS"], ["Mart","Slovakia","SVK"], ["Pietro","Wales","WAL"],
          ["Belgin","Germany","GER"], ["","Northern Ireland","NIR"], ["Grace","Poland","POL"], ["Mattia","Ukraine","UKR"],
          ["","Croatia","CRO"], ["Anna","Czech Republic","CZE"], ["","Spain","SPA"], ["","Turkey","TUR"],
          ["Rudie","Belgium","BEL"], ["Luca","Italy","ITA"], ["Sam","Republic of Ireland","ROI"], ["","Sweden","SWE"],
          ["Wei Guan","Austria","AUS"], ["Shredder","Hungary","HUN"], ["Scroggs","Iceland","ICE"], ["Olly","Portugal","POR"]
         ]

for p in people:
    if p[0] == "":
        p[0] = "?"
    p.append([0,0,0,0,0])

groups = [
           ["FRA","ROM",10,6,20,0,None,None],
           ["ALB","SWI",11,6,14,0,None,None],
           ["WAL","SVK",11,6,17,0,None,None],
           ["ENG","RUS",11,6,20,0,None,None],
           ["TUR","CRO",12,6,14,0,None,None],
           ["POL","NIR",12,6,17,0,None,None],
           ["GER","UKR",12,6,20,0,None,None],
           ["SPA","CZE",13,6,14,0,None,None],
           ["ROI","SWE",13,6,17,0,None,None],
           ["BEL","ITA",13,6,20,0,None,None],
           ["AUS","HUN",14,6,17,0,None,None],
           ["POR","ICE",14,6,20,0,None,None],
           ["RUS","SVK",15,6,14,0,None,None],
           ["ROM","SWI",15,6,17,0,None,None],
           ["FRA","ALB",15,6,20,0,None,None],
           ["ENG","WAL",16,6,14,0,None,None],
           ["UKR","NIR",16,6,17,0,None,None],
           ["GER","POL",16,6,20,0,None,None],
           ["ITA","SWE",17,6,14,0,None,None],
           ["CZE","CRO",17,6,17,0,None,None],
           ["SPA","TUR",17,6,20,0,None,None],
           ["BEL","ROI",18,6,14,0,None,None],
           ["ICE","HUN",18,6,17,0,None,None],
           ["POR","AUS",18,6,20,0,None,None],
           ["ROM","ALB",19,6,20,0,None,None],
           ["SWI","FRA",19,6,20,0,None,None],
           ["RUS","WAL",20,6,20,0,None,None],
           ["SVK","ENG",20,6,20,0,None,None],
           ["UKR","POL",21,6,17,0,None,None],
           ["NIR","GER",21,6,17,0,None,None],
           ["CZE","TUR",21,6,20,0,None,None],
           ["CRO","SPA",21,6,20,0,None,None],
           ["ICE","AUS",22,6,17,0,None,None],
           ["HUN","POR",22,6,17,0,None,None],
           ["ITA","ROI",22,6,20,0,None,None],
           ["SWE","BEL",22,6,20,0,None,None]
          ]

knockout = []

class SoccerPage1(Page):
    def __init__(self, page_num):
        super(SoccerPage1, self).__init__(page_num)
        self.title = "Euro 2016 Sweepstake"
        self.in_index = False

    def generate_content(self):
        content = colour_print(printer.text_to_ascii("Euro 2016 Sweepstake"))        
        lines = [ls[1] + colours.Foreground.BLUE+" ("+ls[0]+")" + colours.Foreground.DEFAULT for ls in people]
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

class SoccerPage2(Page):
    def __init__(self, page_num):
        super(SoccerPage2, self).__init__(page_num)
        self.title = "Euro 2016 Scores & Fixtures"
        self.in_index = False

    def generate_content(self):
        # ["ENG","WAL",16,6,14,0,None,None],
        content = colour_print(printer.text_to_ascii("Euro 2016 Scores & Fixtures")) + "\n"
        matches = groups + knockout
        matches.reverse()
        date = (0,0)
        nowdate = now()
        for match in [m for m in matches if m[3]<nowdate.month or (m[3]==nowdate.month and m[2]<=nowdate.day) or (m[2] == 10 and m[3] == 6)]:
            if date != (match[2],match[3]):
                date = (match[2],match[3])
                content +=  " " * 32
                content += colours.Foreground.YELLOW + colours.Style.BOLD
                content += str(date[0]) +"/0"+ str(date[1])
                content += colours.Foreground.DEFAULT + colours.Style.DEFAULT
                content += "\n"
            team1 = get_team(match[0])
            team2 = get_team(match[1])
            str1 = colours.Foreground.BLUE + "("+team1[0]+") " + colours.Foreground.DEFAULT + team1[1]
            str2 = team2[1] + colours.Foreground.BLUE + " ("+team2[0]+")" + colours.Foreground.DEFAULT

            content += " " * (40-len(str1)) + str1 + " "
            if match[6] is not None:
                content += " " + str(match[6])+"-"+str(match[7]) + " "
            else:
                pad = ""
                if match[5] < 10:
                    pad = "0"
                content += str(match[4])+":"+pad+str(match[5])
            content += " " + str2
            content += "\n"

        self.content = content


class SoccerPage3(Page):
    def __init__(self, page_num):
        super(SoccerPage3, self).__init__(page_num)
        self.title = "Euro 2016 Tables"
        self.in_index = False

    def generate_content(self):
        # ["ENG","WAL",16,6,14,0,None,None],
        content = colour_print(printer.text_to_ascii("Euro 2016 Tables"))
        for p in people:
            p[3] = [0,0,0,0,0,0]
        for m in groups:
            n1 = get_team_n(m[0])
            n2 = get_team_n(m[1])
            if m[6] is not None:
                people[n1][3][3] += m[6]
                people[n1][3][4] += m[7]
                people[n2][3][4] += m[6]
                people[n2][3][3] += m[7]
                if m[6] > m[7]:
                    people[n1][3][0] += 1
                    people[n2][3][2] += 1
                    people[n1][3][5] += 3
                if m[6] == m[7]:
                    people[n1][3][1] += 1
                    people[n2][3][1] += 1
                    people[n1][3][5] += 1
                    people[n2][3][5] += 1
                if m[6] < m[7]:
                    people[n1][3][2] += 1
                    people[n2][3][0] += 1
                    people[n2][3][5] += 3
        gs = []
        for i in range(6):
            group = people[i*4:i*4+4]
            group.sort(key=lambda p: -p[3][3]+p[3][4])
            group.sort(key=lambda p: -p[3][5])
            gs.append(group)
        for i in range(3):
            content += "\n"
            content += colours.Foreground.GREEN
            content += "Group "+str(i+1)
            content += " " * 14
            content += "P W D L F A Pts"
            content += " " * 4
            content += "Group "+str(i+4)
            content += " " * 14
            content += "P W D L F A Pts"
            content += colours.Foreground.DEFAULT
            content += "\n"
            for j in range(4):
                t = gs[i][j]
                team = (t[1]+" ")[:19-len(t[0])] + colours.Foreground.BLUE + "(" + t[0] + ")" + colours.Foreground.DEFAULT
                content += team + " "*(30-len(team))
                pts = ""
                pts += str(t[3][0]+t[3][1]+t[3][2])
                pts += " "
                pts += str(t[3][0])
                pts += " "
                pts += str(t[3][1])
                pts += " "
                pts += str(t[3][2])
                pts += " "
                pts += str(t[3][3])
                pts += " "
                pts += str(t[3][4])
                pts += " "
                pts += str(t[3][5])
                content += pts + " "*(19-len(pts))

                t = gs[i+3][j]                
                team = (t[1]+" ")[:19-len(t[0])] + colours.Foreground.BLUE + "(" + t[0] + ")" + colours.Foreground.DEFAULT
                content += team + " "*(30-len(team))
                pts = ""
                pts += str(t[3][0]+t[3][1]+t[3][2])
                pts += " "
                pts += str(t[3][0])
                pts += " "
                pts += str(t[3][1])
                pts += " "
                pts += str(t[3][2])
                pts += " "
                pts += str(t[3][3])
                pts += " "
                pts += str(t[3][4])
                pts += " "
                pts += str(t[3][5])
                content += pts

                content += "\n"
        self.content = content

soccer_page0 = Page("310")
soccer_page1 = SoccerPage1("311")
soccer_page2 = SoccerPage2("312")
soccer_page3 = SoccerPage3("313")

content = colour_print(printer.text_to_ascii("Euro 2016 Index"))
for page in [soccer_page1,soccer_page2,soccer_page3]:
    content += "\n"
    content += colours.Foreground.RED + page.number + colours.Foreground.DEFAULT
    content += " "
    content += page.title
soccer_page0.content = content
soccer_page0.title = "Euro 2016"
soccer_page0.index_num = "310-313"

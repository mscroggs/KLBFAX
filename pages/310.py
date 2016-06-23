from page import Page
from printer import instance as printer
from printer import size4_instance as size4_printer
import colours
from colours import colour_print
from now import now

def get_team(code):
    for a in people:
        if a[1] == code:
            return a
    return None

def get_team_n(code):
    for i,a in enumerate(people):
        if a[1] == code:
            return i
    return None

from functions import sweepstake_people as people

for p in people:
    if p[0] == "":
        p[0] = "?"
    p.append([0,0,0,0,0])

class Loader:
    def __init__(self):
        self.cache = {"fixtures":[]}

    def load(self):
        try:
            import json
            import urllib2
    
            headers = { 'X-Auth-Token': 'fcb6821c0ef24603a74f0e00bf5ba897', 'X-Response-Control': 'minified' }
            url = "http://api.football-data.org/v1/soccerseasons/424/fixtures"
    
            import urllib2
            request = urllib2.Request(url, headers=headers)
            self.cache = json.load(urllib2.urlopen(request))
        except:
            pass
        return self.cache

l = Loader()

def load_scores():
    return l.load()


def get_groups():
    data = load_scores()
    groups = []

    for match in data["fixtures"]:
        if match["matchday"] in [1,2,3]:
            d = match["date"]
            groups.append([
                match["homeTeamName"],
                match["awayTeamName"],
                int(d.split("-")[2].split("T")[0]),
                int(d.split("-")[1]),
                int(d.split("T")[1].split(":")[0])+1,
                int(d.split(":")[1]),
                match["result"]["goalsHomeTeam"],
                match["result"]["goalsAwayTeam"]
            ])

    return groups

def get_knockout(n=None):
    data = load_scores()
    groups = []

    for match in data["fixtures"]:
        if match["matchday"] not in [1,2,3] and (n is None or n == match["matchday"]):
            d = match["date"]
            groups.append([
                match["homeTeamName"],
                match["awayTeamName"],
                int(d.split("-")[2].split("T")[0]),
                int(d.split("-")[1]),
                int(d.split("T")[1].split(":")[0]),
                int(d.split(":")[1]),
                match["result"]["goalsHomeTeam"],
                match["result"]["goalsAwayTeam"]
            ])

    return groups

def write_match(match,indent=None):
    team1 = get_team(match[0])
    if team1 is None:
        str1 = colours.Foreground.BLUE + "?" + colours.Foreground.DEFAULT
    else:
        str1 = colours.Foreground.GREEN + "("+team1[0]+") " + colours.Foreground.DEFAULT + team1[1]
    team2 = get_team(match[1])
    if team2 is None:
        str2 = colours.Foreground.BLUE + "?" + colours.Foreground.DEFAULT
    else:
        str2 = team2[1] + colours.Foreground.GREEN + " ("+team2[0]+")" + colours.Foreground.DEFAULT
    if indent is None:
        content = ""
    else:
        content = " " * (indent-len(str1))
    content += str1 + " "
    if match[6] is not None:
        content += " " + str(match[6])+"-"+str(match[7]) + " "
    else:
        pad = ""
        if match[5] < 10:
            pad = "0"
        content += str(match[4])+":"+pad+str(match[5])
    content += " " + str2
    return content

class SoccerPage2(Page):
    def __init__(self, page_num):
        super(SoccerPage2, self).__init__(page_num)
        self.title = "Euro 2016 Scores & Fixtures"
        self.in_index = False

    def generate_content(self):
        # ["ENG","WAL",16,6,14,0,None,None],
       content = colour_print(printer.text_to_ascii("Euro 2016 Scores & Fixtures")) + "\n"
       matches = get_groups() + get_knockout()
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
           content += write_match(match,40)
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
            for m in get_groups():
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
                content += colours.Foreground.YELLOW + colours.Style.BOLD
                content += "Group "+str(i+1)
                content += " " * 14
                content += "P W D L F A Pts"
                content += " " * 4
                content += "Group "+str(i+4)
                content += " " * 14
                content += "P W D L F A Pts"
                content += colours.Foreground.DEFAULT + colours.Style.DEFAULT
                content += "\n"
                for j in range(4):
                    t = gs[i][j]
                    team = (t[1]+" ")[:19-len(t[0])] + colours.Foreground.GREEN + "(" + t[0] + ")" + colours.Foreground.DEFAULT
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
                    team = (t[1]+" ")[:19-len(t[0])] + colours.Foreground.GREEN + "(" + t[0] + ")" + colours.Foreground.DEFAULT
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

class SoccerPage4(Page):
    def __init__(self, page_num):
        super(SoccerPage4, self).__init__(page_num)
        self.title = "Euro 2016 Knockout"
        self.in_index = False

    def generate_content(self):
            # ["ENG","WAL",16,6,14,0,None,None],
            import screen
            content = colour_print(printer.text_to_ascii("Euro 2016 Scores & Fixtures")) + "\n"
            matches = get_knockout()
            rounds = {}
            f = {4:8,5:4,6:2,7:1}
            for i in [4,5,6,7]:
                rounds[i] = get_knockout(i)
                while len(rounds[i]) < f[i]:
                    rounds[i].append(["???","???","??","??","??","??",None,None])
    
            names = {4:"Second Round",5:"Quarter Finals",6:"Semi Finals",7:"Final"}
            for i in [4,5,6,7]:
                content += colours.Foreground.YELLOW + colours.Style.BOLD
                content += names[i]
                content += colours.Foreground.DEFAULT + colours.Style.DEFAULT
                l = len(names[i])
                for match in rounds[i]:
                    wr = write_match(match,43-l)
                    l = 0
                    content += wr
                    content += "\n"
                content += "\n"
    
            self.content = content


class SoccerPage5(Page):
    def __init__(self, page_num):
        super(SoccerPage5, self).__init__(page_num)
        self.title = "Euro 2016 Standings"
        self.in_index = False

    def generate_content(self):
            # ["ENG","WAL",16,6,14,0,None,None],
            import screen
            matches = get_groups()
            for p in people:
                #      round,for,against,points
                p[3] = [3,0,0,0]
            for m in matches:
                n1 = get_team_n(m[0])
                n2 = get_team_n(m[1])
                if m[6] is not None:
                    people[n1][3][1] += m[6]
                    people[n1][3][2] += m[7]
                    people[n2][3][2] += m[6]
                    people[n2][3][1] += m[7]
                    if m[6] > m[7]:
                        people[n1][3][3] += 3
                    if m[6] == m[7]:
                        people[n1][3][3] += 1
                        people[n2][3][3] += 1
                    if m[6] < m[7]:
                        people[n2][3][3] += 3
            for i in [4,5,6,7]:
                matches = get_knockout(i)
                for m in matches:
                    n1 = get_team_n(m[0])
                    n2 = get_team_n(m[1])
                    people[n1][3][0] = i
                    people[n2][3][0] = i
                    for ii in range(1,4):
                        people[n1][3][ii] = 0
                        people[n2][3][ii] = 0
                    if m[6] is not None:
                        if m[6] > m[7]:
                            people[n1][3][0] = i+1
                        if m[6] < m[7]:
                                people[n2][3][0] = i+1
    
            sts = [p for p in people]
            sts.sort(key=lambda p: p[3][1])
            sts.sort(key=lambda p: p[3][1]-p[3][2])
            sts.sort(key=lambda p: p[3][3])
            sts.sort(key=lambda p: p[3][0])
    
            content = colour_print(printer.text_to_ascii("Euro 2016 Standings")) + "\n"
            lines = [p[1] + colours.Foreground.GREEN +" ("+ p[0]+")" + colours.Foreground.DEFAULT for p in sts]
            content += colours.Foreground.GREEN + "Top" + colours.Foreground.DEFAULT
            content += " " * 28
            content += colours.Foreground.RED + "Bottom" + colours.Foreground.DEFAULT 
            content += "\n"
    
            n = " ?"
            for i in range(24):
                num = ""
                if i==0 or sts[-i][3] != sts[-i-1][3]:
                    n = ""
                    if i<9:
                        n += " "
                    n += str(i+1)
                
                lines[-1-i] = n + " " + lines[-1-i]
    
            for i in range(12):
                t_win = lines[-1-i]
                t_lose = lines[i]
                spaces = " " * (41-len(lines[-i-1]))
                content += t_win
                content += spaces
                content += t_lose
                content += "\n"
    
            self.content = content




soccer_page0 = Page("310")
#soccer_page1 = SoccerPage1("311")
soccer_page2 = SoccerPage2("311")
soccer_page3 = SoccerPage3("312")
soccer_page4 = SoccerPage4("313")
soccer_page5 = SoccerPage5("315")

content = colour_print(printer.text_to_ascii("Euro 2016 Index"))
for page in [soccer_page2,soccer_page3,soccer_page4,soccer_page5]:
    content += "\n"
    content += colours.Foreground.RED + page.number + colours.Foreground.DEFAULT
    content += " "
    content += page.title
soccer_page0.content = content
soccer_page0.title = "Euro 2016"
soccer_page0.index_num = "310-315"

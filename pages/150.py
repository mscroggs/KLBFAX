#width:79
#height: 30

from base_page import Page

def f(self):
    page=self.colours.colour_print("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxx      xx  xx  xx      xx   xx  xx      xx      xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxx  xxxxxx  xx  xx  xxxxxx    x  xxxx  xxxx  xxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxx    xxxx  xx  xx    xxxx  x    xxxx  xxxx      xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxx  xxxxxxx    xxx  xxxxxx  xx   xxxx  xxxxxxxx  xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxx      xxxx  xxxx      xx  xxx  xxxx  xxxx      xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx""",self.colours.Background.RED,self.colours.Foreground.BLUE)+"""
"""



    events={}
    cur=""
    with open("/var/www/klb/events") as f:
        for line in f.readlines():
          line=line.strip("\n")
          if line!="":
            if line[0]=="#":
                line = line.strip("#").strip(" ")
                cur=line
                events[cur]=[]
            elif cur in events:
                events[cur].append(line)
    
    
    for date in sorted(events):
        event = events[date]
        page+=date+"""
    """
        i = 0
        col = self.colours.Foreground.WHITE
        for info in event:
            page+="  "+col+info+self.colours.Foreground.DEFAULT+"""
    """
            if col == self.colours.Foreground.WHITE:
                if i>=2:
                    col = self.colours.Foreground.YELLOW
                i+=1
            elif col == self.colours.Foreground.YELLOW:
                col = self.colours.Foreground.GREEN
            elif col == self.colours.Foreground.GREEN:
                col = self.colours.Foreground.YELLOW
        page+="""
    """
    self.content = page


events_page=Page("150",f)

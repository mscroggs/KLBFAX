#width:79
#height: 30

from colours import Foreground,Background,colour_print
page=colour_print("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxx      xx  xx  xx      xx   xx  xx      xx      xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxx  xxxxxx  xx  xx  xxxxxx    x  xxxx  xxxx  xxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxx    xxxx  xx  xx    xxxx  x    xxxx  xxxx      xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxx  xxxxxxx    xxx  xxxxxx  xx   xxxx  xxxxxxxx  xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxx      xxxx  xxxx      xx  xxx  xxxx  xxxx      xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx""",Background.RED,Foreground.BLUE)+"""
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
    col = Foreground.WHITE
    for info in event:
        page+="  "+col+info+Foreground.DEFAULT+"""
"""
        if col == Foreground.WHITE:
            if i>=2:
                col = Foreground.YELLOW
            i+=1
        elif col == Foreground.YELLOW:
            col = Foreground.GREEN
        elif col == Foreground.GREEN:
            col = Foreground.YELLOW
    page+="""
"""

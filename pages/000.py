#width:79
#height: 30

from colours import Foreground,Background,colour_print

page="""
TEST PAGE
"""
for i in range(0,len(Foreground.list)):
    page+=Foreground.list[i]
    for j in range(0,len(Background.list)):
        page+=Background.list[j]+Foreground.delist[i][j%len(Foreground.delist[i])]
    page+=Foreground.DEFAULT+Background.DEFAULT+"""
"""

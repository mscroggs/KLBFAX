#width:79
#height: 30

from colours import Foreground,Background,colour_print

page="""
TEST PAGE
"""
for i in range(0,len(Foreground.list)):
    page+=Foreground.list[i]+Foreground.delist[i]+Foreground.DEFAULT+"""
"""
for j in range(0,len(Background.list)):
    page+=Background.list[j]+Background.delist[j]+Background.DEFAULT+"""
"""

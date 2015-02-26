#width:79
#height: 30

from colours import Foreground,Background,colour_print

page="""
TEST PAGE
"""
for i in range(0,len(Foreground.list)):
    page+=Foreground.list[i]+Foreground.delist[i]+Foreground.DEFAULT+"""
"""
for i in range(0,len(Background.list)):
    page+=Background.list[i]+Background.delist[i]+Background.DEFAULT+"""
"""
for i in range(0,len(Style.list)):
    page+=Style.list[i]+Style.delist[i]+Style.DEFAULT+"""
"""


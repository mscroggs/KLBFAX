from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from time import strftime
import screen


class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Python"
        self.tagline = "Python"

    def generate_content(self):
        import urllib2
        content = colour_print(printer.text_to_ascii("Python",fill=True))
        content += "\n"
        jig = """
            BBBBBBBBBBBBBBB
            BB  BBBBBBBBBBB
            BB  BBBBBBBBBBB
            BBBBBBBBBBBBBBB
                     BBBBBB
    BBBBBBBBBBBBBBBBBBBBBBB YYYYYYY
    BBBBBBBBBBBBBBBBBBBBBBB YYYYYYY
    BBBBBBBBBBBBBBBBBBBBBB  YYYYYYY
    BBBBBBBBB             YYYYYYYYY
    BBBBBBB  YYYYYYYYYYYYYYYYYYYYYY
    BBBBBBB YYYYYYYYYYYYYYYYYYYYYYY
    BBBBBBB YYYYYYYYYYYYYYYYYYYYYYY
            YYYYYY
            YYYYYYYYYYYYYYY
            YYYYYYYYYYY  YY
            YYYYYYYYYYY  YY
            YYYYYYYYYYYYYYY
"""
        jig = u"\u2588".join(jig.split("X"))
        jig = u"\u2580".join(jig.split("'"))
        jig = u"\u2584".join(jig.split(","))
        jig = (self.colours.Foreground.YELLOW+self.colours.Style.BOLD+u"\u2588"+self.colours.Foreground.DEFAULT+self.colours.Style.DEFAULT).join(jig.split("Y"))
        jig = (self.colours.Foreground.BLUE+self.colours.Style.BOLD+u"\u2588"+self.colours.Foreground.DEFAULT+self.colours.Style.DEFAULT).join(jig.split("B"))
        content += jig
        
        self.content = content

page = JigPage("115")

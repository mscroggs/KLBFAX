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
        self.title = "Trophy"
        self.tagline = "GO PUFFS!"

    def generate_content(self):
        import urllib2
        content = ""
        content += "\n"
        jig = """
                   XXXXXRRRRRRRRXXXXX
                   XXXXXXXXRRXXXXXXXX
             BYXXXXXXXXXXRRXXRRXXXXXXXXXXYB
             BYXX  XXXXXXXXXXXXXXXXXX  XXYB
             BYXX   XXXXRRRRRRRRXXXX   XXYB
             BY XX  XXXXRXXXXXXXXXXX  XX YB
             BY XX   XXXXXXXXXXXXXX   XX YB
             BY  XX   XXRRRRRRRRXX   XX  YB 
             BY   XX   XRXXRRXXRX   XX   YB
             BY    XXX  XRRRRRRX  XXX    YB
             BY      XXX XXXXXX XXX      YB
             BY        XXXXXXXXXX        YB
             BY           XXXX           YB
             BY           XXXX           YB
                      BBBBBBBBBBBB
                      BBBBBBBBBBBB
                      BBBBBBBBBBBB
                     BBBBBBBBBBBBBB
                    BBBBBBBBBBBBBBBB
"""
        jig = u"\u2588".join(jig.split("X"))
        jig = u"\u2580".join(jig.split("'"))
        jig = u"\u2584".join(jig.split(","))
        jig = (self.colours.Foreground.RED+u"\u2588"+self.colours.Foreground.DEFAULT).join(jig.split("R"))
        jig = (self.colours.Foreground.YELLOW+self.colours.Style.BOLD+u"\u2588"+self.colours.Foreground.DEFAULT+self.colours.Style.DEFAULT).join(jig.split("Y"))
        jig = (self.colours.Foreground.BLACK+self.colours.Style.BOLD+u"\u2588"+self.colours.Foreground.DEFAULT+self.colours.Style.DEFAULT).join(jig.split("B"))
        content += jig
        
        self.content = content

page = JigPage("113")

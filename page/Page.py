from time import strftime
from math import floor
from datetime import datetime
import logging
import screen
from random import random,randint,choice
import colours
import now

def random_error(string):
    """if random()<0.03:
      try:
        chars = ["A","5","h","i","#","@","{","9","."]
        pos = randint(0,len(string)-2)
        string = string[:pos]+choice(colours.Foreground.list)+string[pos]+colours.Foreground.DEFAULT+string[pos+1:]
      except:
        pass"""
    return string


class Page(object):
    def __init__(self, number):
        import colours
        self.colours = colours
        self.content = ""
        self.is_enabled = True
        self.in_index = True
        self.index_num = None
        self.tagline = "KLBFAX: The World at Your Fingertips"
        self.number = str(number)
        self.loaded = False
        self.title = ""

    def now(self):
        return now.now()

    def generate_content(self):
        pass

    def show(self):
        from page import FailPage
        if self.loaded or isinstance(self,FailPage) or self.number=="---":
            print(random_error(" " * 53 + self.number + " KLBFAX " + self.now().strftime("%a %d %b %H:%M")))
            out = self.content.split("\n")
            for i in range(0, 27):
                if i < len(out):
                    print(random_error(out[i].encode('utf-8')))
                else:
                    print("")
            before = int(floor((screen.WIDTH-len(self.tagline))/2))
            after = screen.WIDTH-len(self.tagline)-before
            tagline_print = " " * before + self.tagline + " " * after
            print(self.colours.Background.BLUE + self.colours.Foreground.YELLOW
                  + tagline_print + self.colours.Background.DEFAULT
                  + self.colours.Foreground.DEFAULT)
        else:
            print "h"
            fail_page = FailPage()
            fail_page.reload()
            fail_page.show()

    def reload(self):
        try:
            self.generate_content()
            self.loaded = True
        except Exception as e:
            logging.warning("Page " + self.title + " could not be reloaded")
            logging.exception(e)
            self.loaded = False

class FailPage(Page):
    def __init__(self):
        super(FailPage,self).__init__("---")
        self.content = "Page failed to load...\n\n2 points to Slytherin!"
        self.is_enabled = False

    def generate_content(self):
        import json
        from points import add_points 
        add_points("Slytherin",2)

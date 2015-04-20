from time import strftime
from math import floor
from datetime import datetime
import logging
import pytz
from random import random,randint,choice
import colours

def random_error(string):
    if random()<0.03:
      try:
        chars = ["A","5","h","i","#","@","{","9","."]
        pos = randint(0,len(string)-2)
        string = string[:pos]+choice(colours.Foreground.list)+string[pos]+colours.Foreground.DEFAULT+string[pos+1:]
      except:
        pass
    return string


class Page(object):
    def __init__(self, number):
        import colours
        self.colours = colours
        self.content = ""
        self.is_enabled = True
        self.in_index = True
        self.tagline = "KLBFAX: The World at Your Fingertips"
        self.number = str(number)
        self.loaded = False
        self.title = ""
        self.timezone = pytz.timezone('Europe/London') 

    def now(self):
        return pytz.utc.localize(datetime.now()).astimezone(self.timezone)

    def generate_content(self):
        pass

    def show(self):
        if self.loaded:
            print(random_error(" " * 53 + self.number + " KLBFAX " + self.now().strftime("%a %d %b %H:%M")))
            out = self.content.split("\n")
            for i in range(0, 27):
                if i < len(out):
                    print(random_error(out[i].encode('utf-8')))
                else:
                    print("")
            before = int(floor((79-len(self.tagline))/2))
            after = 79-len(self.tagline)-before
            tagline_print = " " * before + self.tagline + " " * after
            print(self.colours.Background.BLUE + self.colours.Foreground.YELLOW
                  + tagline_print + self.colours.Background.DEFAULT
                  + self.colours.Foreground.DEFAULT)
        else:
            index_page = getattr(__import__("pages", fromlist=["100"]),"100").index_page
            index_page.reload()
            index_page.show()

    def reload(self):
        try:
            self.generate_content()
            self.loaded = True
        except Exception as e:
            logging.warning("Page " + self.title + " could not be reloaded")
            logging.exception(e)
            self.loaded = False

from math import floor
import logging
import screen
import now
import config
from name import NAME

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
        self.tagline = NAME + ": The World at Your Fingertips"
        self.number = str(number)
        self.loaded = False
        self.title = ""
        self.duration_sec = config.default_page_duration_sec

    def loop(self):
        pass

    def keyboard_handler(self):
        pass

    def now(self):
        return now.now()

    def generate_content(self):
        pass

    def show(self):
        from page import FailPage
        if self.loaded or isinstance(self, FailPage) or self.number == "---":
            print(random_error(" " * (59-len(NAME)) + self.number + " "+NAME+" " + self.now().strftime("%a %d %b %H:%M")))
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
                  + self.colours.Style.BOLD
                  + tagline_print + self.colours.Background.DEFAULT
                  + self.colours.Foreground.DEFAULT + self.colours.Style.DEFAULT)
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

    def refresh(self):
        pass


class FailPage(Page):
    def __init__(self):
        super(FailPage, self).__init__("---")
        self.content = "Page failed to load...\n\n2 points to Slytherin!"
        self.is_enabled = False
        self.duration_sec = 2

    def generate_content(self):
        from points import add_points
        add_points("Slytherin", 2)

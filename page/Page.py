from time import strftime
from math import floor


class Page(object):
    def __init__(self, number):
        import colours
        self.colours = colours
        self.content = ""
        self.is_enabled = True
        self.tagline = "KLBFAX: The World at Your Fingertips"
        self.number = str(number)
        self.loaded = False
        self.title = ""

    def generate_content(self):
        pass

    def show(self):
        print(" " * 53 + self.number + " KLBFAX " + strftime("%a %d %b %H:%M"))
        out = self.content.split("\n")
        for i in range(0, 27):
            if i < len(out):
                print(out[i])
            else:
                print("")
        before = int(floor((79-len(self.tagline))/2))
        after = 79-len(self.tagline)-before
        tagline_print = " " * before + self.tagline + " " * after
        print(self.colours.Background.BLUE + self.colours.Foreground.YELLOW
              + tagline_print + self.colours.Background.DEFAULT
              + self.colours.Foreground.DEFAULT)

    def reload(self):
        try:
            self.generate_content()
            self.loaded = True
        except:
            self.loaded = False

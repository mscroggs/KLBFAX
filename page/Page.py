from random import choice
from time import strftime
from math import floor

def empty_f(self):
    pass

class Page:
    def __init__(self,number,generate_content=empty_f):
        import colours
        self.colours = colours
        self.generate_content=generate_content
        self.content = ""
        self.is_enabled = True
        self.tagline = "KLBFAX: The World at Your Fingertips"
        self.number = str(number)
        self.loaded = False

 #   def colour_print(self,text,background=Background.BLUE,foreground=Foreground.YELLOW):
 #       return colour_print_non_obj(text,background,foreground)

    def show(self):
        print(" " * 53 +self.number+" KLBFAX "+strftime("%a %d %b %H:%M"))
        out = self.content.split("\n")
        for i in range(0,27):
            if i<len(out):
                print(out[i])
            else:
                print("")
        before = int(floor((79-len(self.tagline))/2))
        after = 79-len(self.tagline)-before
        tagline_print = " " * before + self.tagline + " " * after
        print(self.colours.Background.BLUE + self.colours.Foreground.YELLOW + tagline_print
              + self.colours.Background.DEFAULT + self.colours.Foreground.DEFAULT)

    def reload(self):
        try:
            self.generate_content(self)
            self.loaded = True
        except:
            self.loaded = False


class PageFactory:
    def __init__(self):
        self.pages={}
        self.fail_page = Page("---")
        self.fail_page.loaded = False
        self.fail_page.is_enabled = False

    def add(self,page):
        self.pages[page.number]=page

    def show_random(self):
        page = self.fail_page
        while not page.loaded or not page.is_enabled:
            page = choice(self.pages.items())[1]
            page.reload()
        page.show()

    def load(self,number):
        if number not in self.pages:
            return self.fail_page
        if not self.pages[number]:
            return self.fail_page
        self.pages[number].reload()
        if not self.pages[number].loaded:
            return self.fail_page
        return self.pages[number]

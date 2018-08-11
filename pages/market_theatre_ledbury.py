from page import Page
from functions import replace
from helpers import url_handler

class FilmPage(Page):
    def __init__(self, page_num):
        super(FilmPage, self).__init__(page_num)
        self.title = "Market Theatre Ledbury"
        self.index_num = "671-679"
        self.ls = []

    def background(self):
        data = url_handler.load("http://themarkettheatre.com/whats-on/")
        data = [i.split("</div>")[0] for i in data.split('<div class="productionWrap">')[1:]]
        self.ls = []
        for i in data:
            new = {}
            new["title"] = i.split('<span class="tcmsTitle"')[1].split("</span>")[0].split(">",1)[1]
            new["date"] = i.split('<span class="date">')[1].split("</span>")[0].replace("&ndash;","-")
            new["desc"] = i.split('<span class="description">')[1].split("</span>")[0].replace("&ndash;","-")
            self.ls.append(new)

    def generate_content(self):
        self.add_title("Market Theatre",font='size4')
        self.add_title("              Ledbury",font='size4')
        self.move_cursor(x=62)
        self.add_text("More Info on Page",fg="CYAN")
        self.add_newline()
        for i,item in enumerate(self.ls):
            self.add_text(item["date"], fg="GREEN")
            self.move_cursor(x=21)
            self.add_text(" "+item["title"], fg="BRIGHTWHITE")
            self.move_cursor(x=76)
            self.add_text(str(672+i//3),fg="CYAN")
            self.add_newline()
            #self.add_wrapped_text(item["desc"],fg="CYAN")
            #self.add_newline()

class FilmSubPage(Page):
    def __init__(self, page_num, parent):
        super(FilmSubPage, self).__init__(page_num)
        self.title = "What's On At The Market Theatre Ledbury"
        self.in_index = False
        self.n = int(page_num) - 672
        self.parent = parent

    def generate_content(self):
        self.add_title("What's on at",font='size4')
        self.add_title(" Market Theatre",font='size4')
        self.add_title("              Ledbury",font='size4')
        for i in range(3*self.n,3*self.n+3):
            if len(self.parent.ls) > i:
                item = self.parent.ls[i]
                self.add_text(item["date"], fg="GREEN")
                self.add_text(" "+item["title"], fg="BRIGHTWHITE")
                self.add_newline()
                self.add_wrapped_text(item["desc"],fg="CYAN")
                self.add_newline()

page1 = FilmPage("671")
page2 = FilmSubPage("672", page1)
page3 = FilmSubPage("673", page1)
page4 = FilmSubPage("674", page1)
page5 = FilmSubPage("675", page1)
page6 = FilmSubPage("676", page1)
page7 = FilmSubPage("677", page1)
page8 = FilmSubPage("678", page1)
page9 = FilmSubPage("679", page1)

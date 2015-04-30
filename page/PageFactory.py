import random
from page import Page,FailPage
from time import strftime

def get_page_factory():
    if not isinstance(PageFactory._instance,PageFactory):
        PageFactory._instance = PageFactory()
    return PageFactory._instance


class PageFactory:
    _instance = None
    def __init__(self):
        self.i = 0
        self.pages = {}
        self.FailPage()

    def add(self, page):
        self.pages[page.number] = page

    def show_random(self):
        page = self.fail_page
        while not page.loaded:
            page = random.choice(self.get_enabled_pages(str(self.i)))
            self.i += 1
            self.i %= 10
            page.reload()
        page.show()

    def print_all(self):
        items = self.pages.items()
        items.sort()
        for page_num,page in items:
            p = ""
            if not page.is_enabled: p += page.colours.Foreground.RED
            p += (page_num+" ")
            p += (page.title)
            #p += (" "*(45-len(page.title)))
            if not page.is_enabled: p += page.colours.Foreground.DEFAULT
            print(p)

    def get_reloaded_page(self, number):
        if number not in self.pages:
            return self.fail_page
        if not self.pages[number]:
            return self.fail_page
        self.pages[number].reload()
        if not self.pages[number].loaded:
            return self.fail_page
        return self.pages[number]

    def get_enabled_pages(self,starting="0"):
        if starting == "0":
            return [self.pages["200"]]
        output = [page for page in self.pages.values() if page.is_enabled and page.number[0]==starting]
        if len(output)>0:
            return output
        else:
            return [page for page in self.pages.values() if page.is_enabled]

    def page_exists(self, page_num):
        if page_num in self.pages:
            return True

        return False

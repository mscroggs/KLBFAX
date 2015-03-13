import random
from page import Page

def get_page_factory():
    if not isinstance(PageFactory._instance,PageFactory):
        PageFactory._instance = PageFactory()
    return PageFactory._instance


class PageFactory:
    _instance = None
    def __init__(self):
        self.pages = {}
        self.fail_page = Page("---")
        self.fail_page.loaded = False
        self.fail_page.is_enabled = False

    def add(self, page):
        self.pages[page.number] = page

    def show_random(self):
        page = self.fail_page
        while not page.loaded:
            page = random.choice(self.get_enabled_pages())
            page.reload()
        page.show()

    def get_reloaded_page(self, number):
        if number not in self.pages:
            return self.fail_page
        if not self.pages[number]:
            return self.fail_page
        self.pages[number].reload()
        if not self.pages[number].loaded:
            return self.fail_page
        return self.pages[number]

    def get_enabled_pages(self):
        return [page for page in self.pages.values() if page.is_enabled]

    def page_exists(self, page_num):
        if page_num in self.pages:
            return True

        return False

import random
from page import Page


class PageFactory:
    def __init__(self):
        self.pages = {}
        self.fail_page = Page("---")
        self.fail_page.loaded = False
        self.fail_page.is_enabled = False

    def add(self, page):
        self.pages[page.number] = page

    def show_random(self):
        page = self.fail_page
        while not page.loaded or not page.is_enabled:
            page = random.choice(self.pages.items())[1]
            page.reload()
        page.show()

    def load(self, number):
        if number not in self.pages:
            return self.fail_page
        if not self.pages[number]:
            return self.fail_page
        self.pages[number].reload()
        if not self.pages[number].loaded:
            return self.fail_page
        return self.pages[number]

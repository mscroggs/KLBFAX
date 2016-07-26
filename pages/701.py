from page import Page
import urllib2
import json
from name import NAME
from printer import instance as printer

class EMFPage(Page):
    def __init__(self, page_num, n):
        super(EMFPage, self).__init__(page_num)
        self.title = "EMF Schedule"
        self.in_index = False
        self.is_enabled = True
        self.n = n

    def generate_content(self):
        content = self.colours.colour_print(printer.text_to_ascii("EMF Day "+str(self.n),vertical_condense=True))
        self.content = content

page1 = EMFPage("701",1)
page2 = EMFPage("702",2)
page3 = EMFPage("703",3)

page1.in_index = True
page1.index_num = "701-703"

import os
from page import Page
from random import shuffle
import config

from datetime import datetime

class InfoPage(Page):
    def __init__(self, n):
        super(InfoPage, self).__init__(n)
        self.title = "About"

    def generate_content(self):
        self.add_text(config.NAME+" v"+config.VERSION)
        self.add_newline()

    def background(self):
        agdjdsglj()

i_p = InfoPage("200")

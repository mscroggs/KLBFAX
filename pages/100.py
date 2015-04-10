import os
from page import Page, PageFactory
from random import shuffle

class IndexPage(Page):
    def __init__(self, page_num):
        super(IndexPage, self).__init__(page_num)
        self.title = "Index"

    def generate_content(self):
        content = self.colours.colour_print("""
xxxxxxxxxxxxxxxxxxxxxx       xxxxxxxxx       xxxxxxxxx
xxxxxxxxxxxxxxxx  x  x         x    xx         x     x
xxxxxxxxxxxxxxxx    xx xxxxxxx x  x  x xxxxxxx x  x  x xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx   xxx x  xxxx x    xx x     x x     x x  x  xxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx  x  x x  xxxx x  x  x x  xxxx x  x  x x  x  xxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx  x  x x  xxxx x    xx x    xx x  x  x xx   xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxx x  xxxx xxxxxxx x  xxxx xxxxxxx x  x  xxxxxxxxxxxxxxxxxxx
                       x     x         x  xxxx         x  x  xxxxxxxxxxxxxxxxxxx
                     xxxxxxxxx       xxxxxxxxx       xxxxxxxxxxxxxxxxxxxxxxxxxxx
""")+"""
KLBFAX currently has """+str(len(PageFactory().pages))+""" pages. Contribute at github.com/mscroggs/KLBFAX.

INDEX
"""
        i = 0
        items = PageFactory().pages.items()
        shuffle(items)
        for num, page in items:
          if page.is_enabled:
            content += self.colours.Foreground.MAGENTA
            content += num
            content += self.colours.Foreground.DEFAULT
            content += " "
            content += page.title
            if i == 0:
                content += " "*(33-len(page.title))
                i = 1
            else:
                content += "\n"
                i = 0
        self.content = content

page_number = os.path.splitext(os.path.basename(__file__))[0]
index_page = IndexPage(page_number)

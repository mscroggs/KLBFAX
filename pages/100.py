import os
from page import Page, PageFactory
from random import shuffle
from name import NAME

class IndexPage(Page):
    def __init__(self, page_num):
        super(IndexPage, self).__init__(page_num)
        self.title = "Index"

    def generate_content(self):
        if os.getenv("SLAVE"):
            content = self.colours.colour_print("""
xxxxxxxxxxxxxxxxxxxxxxxxx       xxxxxxxxx       xxxxxxxxx
xxxxxxxxxxx      xx     x         x  x  x         x     x
xxxxxxxxxxxxxxx  xx  x  x xxxxxxx x  x  x xxxxxxx x  x  x xxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxx      xx     x xxxx  x x     x x     x x     x x  x  xxxxxxxxxxxxxxxx
xxxxxxxxxxx  xxxxxx  x  x xxxx  x x  x  x x  xxxx x  x  x x  x  xxxxxxxxxxxxxxxx
xxxxxxxxxxx      xx     x xxxx  x x  x  x x    xx x  x  x xx   xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx xxxx  x xxxxxxx x  xxxx xxxxxxx x  x  xxxxxxxxxxxxxxxx
                          x     x         x  xxxx         x  x  xxxxxxxxxxxxxxxx
                        xxxxxxxxx       xxxxxxxxx       xxxxxxxxxxxxxxxxxxxxxxxx
""")
        else:
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
""")
        content += "\n"+NAME+""" currently has """+str(len(PageFactory().pages))+""" pages. Contribute at github.com/mscroggs/KLBFAX.
Temperature graphs can be viewed on Twitter: @klbscroggsbot.

"""+self.colours.Foreground.GREEN+"INDEX"+self.colours.Foreground.DEFAULT+"""
"""
        i = 0
        items = PageFactory().pages.items()
        items.sort()
        for num, page in items:
          if page.is_enabled and page.in_index:
            content += self.colours.Foreground.MAGENTA
            if page.index_num is None:
                content += num
                num_len = len(num)
            else:
                content += page.index_num
                num_len = len(page.index_num)
            content += self.colours.Foreground.DEFAULT
            content += " "
            content += page.title
            if i == 0:
                content += " "*(36-len(page.title)-num_len)
                i = 1
            else:
                content += "\n"
                i = 0
        self.content = content

page_number = os.path.splitext(os.path.basename(__file__))[0]
index_page = IndexPage(page_number)

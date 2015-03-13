#width:79
#height: 30

import os
from page import Page,PageFactory
def f(self):
    content=self.colours.colour_print("""
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
KLBFAX is under construction. Check regularly for updates.

The source code of KLBFAX is available at https://github.com/mscroggs/KLBFAX. If
you would like to add features/pages to KLBFAX, ask Scroggs to add you to the
repository.

Press A on the SNES controller to add a cup of tea.

INDEX
"""
    i=0
    print PageFactory().pages
    for num,page in PageFactory().pages.items():
        content += self.colours.Foreground.MAGENTA
        content += num 
        content += self.colours.Foreground.DEFAULT
        content += " "
        content += page.title
        if i==0:
            content += " "*(29-len(page.title))
            i=1
        else:
            content += "\n"
            i=0
    self.content = content
page_number = os.path.splitext(os.path.basename(__file__))[0]
index_page = Page(page_number,f)
index_page.title = "Index"

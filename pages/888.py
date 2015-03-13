#width:79
#height: 30

import os
from page import Page

page_number = os.path.splitext(os.path.basename(__file__))[0]
sub_page = Page(page_number)

sub_page.content=sub_page.colours.colour_print("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxx      xx  xx  xx     xxx      xx  xx      xx  xxxxxx      xx      xxxxxxx
xxxxxxx  xxxxxx  xx  xx  xx  xxxx  xxxx  xxxx  xxxx  xxxxxx  xxxxxx  xxxxxxxxxxx
xxxxxxx      xx  xx  xx    xxxxxx  xxxx  xxxx  xxxx  xxxxxx    xxxx      xxxxxxx
xxxxxxxxxxx  xx  xx  xx  xx  xxxx  xxxx  xxxx  xxxx  xxxxxx  xxxxxxxxxx  xxxxxxx
xxxxxxx      xx      xx     xxxxx  xxxx  xxxx  xxxx      xx      xx      xxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx""")

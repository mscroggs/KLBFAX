#width:79
#height: 30

from base_page import Page

sub_page = Page("888")

sub_page.content=sub_page.colours.colour_print("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxx      xx  xx  xx     xxx      xx  xx      xx  xxxxxx      xx      xxxxxxx
xxxxxxx  xxxxxx  xx  xx  xx  xxxx  xxxx  xxxx  xxxx  xxxxxx  xxxxxx  xxxxxxxxxxx
xxxxxxx      xx  xx  xx    xxxxxx  xxxx  xxxx  xxxx  xxxxxx    xxxx      xxxxxxx
xxxxxxxxxxx  xx  xx  xx  xx  xxxx  xxxx  xxxx  xxxx  xxxxxx  xxxxxxxxxx  xxxxxxx
xxxxxxx      xx      xx     xxxxx  xxxx  xxxx  xxxx      xx      xx      xxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx""")

import os
import screen
from page import Page

from random import choice

page_number = os.path.splitext(os.path.basename(__file__))[0]
test_page = Page(page_number)
test_page.title = "Unicode Test Page"
test_page.is_enabled = False

test_page.content="\nUNICODE TEST PAGE\n"

uni_chars = [9484] + range(1224,10000)

j = 0
for i in range(200):
    ch = choice(uni_chars)
    uni_chars.remove(ch)
    test_page.content += str(ch)+" "+unichr(ch)
    j += 1
    if j % 9 != 0: test_page.content += "  "
    else: test_page.content += "\n"


import os
import screen
from page import Page
from random import choice

def colour_me(text):
    output = ""
    for i in text:
        output += choice(test_page.colours.Foreground.non_boring) + i
    output += test_page.colours.Foreground.DEFAULT
    return output

page_number = os.path.splitext(os.path.basename(__file__))[0]
test_page = Page(page_number)
test_page.title = "Test Page"
test_page.is_enabled = False

test_page.content = ""

test_page.content += "\n" + colour_me("TEST PAGE") + "\n\n"

# 000000011111111112222222222333333333344444444445555555555666666666677777777778
# 345678901234567890123456789012345678901234567890123456789012345678901234567890
#"          DEFAULT BLACK RED GREEN YELLOW BLUE MAGENTA CYAN WHITE"
#"BOLD      "
#"FAINT     "
#"STANDOUT  "
#"BLINK     "
#"UNDERLINE "
#"STRIKE    "
test_page.content += colour_me("FOREGROUNDS & STYLES") + "\n"
for i in range(0,len(test_page.colours.Style.list)):
    test_page.content += test_page.colours.Style.delist[i] + " "*(13-len(test_page.colours.Style.delist[i]))

    for j in range(0,len(test_page.colours.Foreground.list)):
        test_page.content += test_page.colours.Style.list[i] + test_page.colours.Foreground.list[j]
        test_page.content += test_page.colours.Foreground.delist[j]
        test_page.content += test_page.colours.Style.DEFAULT + test_page.colours.Foreground.DEFAULT
        test_page.content += " "
    test_page.content += "\n"

test_page.content += colour_me("BACKGROUNDS & STYLES") + "\n"
for i in range(0,len(test_page.colours.Style.list)):
    test_page.content += test_page.colours.Style.delist[i] + " "*(13-len(test_page.colours.Style.delist[i]))

    for j in range(0,len(test_page.colours.Background.list)):
        test_page.content += test_page.colours.Style.list[i] + test_page.colours.Background.list[j]
        test_page.content += test_page.colours.Background.delist[j]
        test_page.content += test_page.colours.Style.DEFAULT + test_page.colours.Background.DEFAULT
        test_page.content += " "
    test_page.content += "\n"




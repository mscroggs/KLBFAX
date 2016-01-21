import os
from os.path import join,expanduser
from page import Page
from printer import instance as printer

page_number = os.path.splitext(os.path.basename(__file__))[0]
p_page = Page(page_number)

p_page.title = "Historical House Points"

content = p_page.colours.colour_print(printer.text_to_ascii("house points"))

content += "\n\n"

R = p_page.colours.Foreground.RED
G = p_page.colours.Foreground.GREEN
D = p_page.colours.Foreground.DEFAULT

content += G+"Year " + " Gryffindor Slytherin Hufflepuff"    +   " Ravenclaw Durmstrang Squib Peeves"+D+"\n"
content += G+"2015a"+D+" 692        535       "+R+"1155"+D+"       702       440        513   0\n"
content += G+"2015b"+D+" 3382       408       "+R+"4614"+D+"       3591      606        2174  38\n"

p_page.content = content

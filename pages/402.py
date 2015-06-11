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

content += G+"Year" + " Gryffindor Slytherin Hufflepuff Ravenclaw Durmstrang Squib Peeves"+D+"\n"
content += G+"2015"+D+" 618        507       "+R+"1092"+D+"       639       440        513   0\n"

p_page.content = content

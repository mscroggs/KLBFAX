import os
from page import Page
from colours import colour_print
from printer import instance as printer

page_number = os.path.splitext(os.path.basename(__file__))[0]
sub_page = Page(page_number)
sub_page.title = "I'm a Teapot"
sub_page.in_index=False
sub_page.content = colour_print(printer.text_to_ascii("418", padding={"left": 30}))
sub_page.content += "\n\n"
sub_page.content += colour_print(printer.text_to_ascii("I am a Teapot", padding={"left": 2}))

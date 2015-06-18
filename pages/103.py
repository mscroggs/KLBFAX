import os
from page import Page
from colours import colour_print
from printer import instance as printer

page_number = os.path.splitext(os.path.basename(__file__))[0]
sub_page = Page(page_number)
sub_page.title = "Important Information"
sub_page.content = colour_print(
    printer.text_to_ascii("imperial suck"))
sub_page.content += "\n\n (Except for Kuru,\n  love from Scroggs)"

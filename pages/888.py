import os
from page import Page
from colours import colour_print
from printer import instance as printer

page_number = os.path.splitext(os.path.basename(__file__))[0]
sub_page = Page(page_number)
sub_page.title = "Subtitles"
sub_page.content = colour_print(
    printer.text_to_ascii("subtitles", padding={"left": 6}))

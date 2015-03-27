import os
from page import Page
from colours import colour_print
from printer import instance as printer

page_number = os.path.splitext(os.path.basename(__file__))[0]
chalk_page = Page(page_number)
chalk_page.title = "chalkdust"
chalk_page.content = colour_print(
    printer.text_to_ascii("chalkdust!")+"\n"+
    printer.text_to_ascii("chalkdust!")+"\n"+
    printer.text_to_ascii("chalkdust!")+"\n"+
    printer.text_to_ascii("chalkdust!")
    )

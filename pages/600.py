import os
from page import Page
from colours import colour_print
from printer import instance as printer

page_number = os.path.splitext(os.path.basename(__file__))[0]
tv_page = Page(page_number)
tv_page.title = "TV Listings"
tv_page.content = colour_print(printer.text_to_ascii("BBC1"))+"\n"+"06:00 The Belgin Breakfast Show\n"+"09:00 Animal Hospital\n"+"09:30 Bargain Hunt\n"+        "10:00 Look Around You\n"+        "10:30 The Hexagons\n"+        "11:00 "+tv_page.colours.Foreground.BLUE+"FILM "+tv_page.colours.Foreground.DEFAULT+"Blackball \n"+        "13:00 BBC News at One\n"+        "13:30 Regional News\n"+        "13:45 Neighbours\n"+       "14:20 Diagnosis Murder\n"+        "15:00 "+tv_page.colours.Foreground.BLUE+"CBBC "+tv_page.colours.Foreground.DEFAULT+"Playdays \n"        "23:00 Pages from CEEFAX"

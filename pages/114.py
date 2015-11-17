from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from time import strftime
import screen


class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Soup"
        self.tagline = "Soup!"

    def generate_content(self):
        import urllib2
        content = ""
        content += "\n"
        jig = '''
          _______________________________
         [_______________________________]
         |===============================|
         |   __                          |
         |._/_.' _, ,__  ,_ /_ _  / /'   |
         | / _  / / /// / // /(-'/ / /|  |
         | \__)(_(_//(_/_/(_/(__(_(_/_/_ |
         |            /                  |
         |       C O N D E N S E D       |
         |                               |
         |            .-"""-.            |
         |           /:`:..':\           |
         |==========|.:::::..:|==========|
         |           \::::::./           |
         |            `-:::-'            |
         |     ___                       |
         |      |  _ ,_ _  _ -|- _       |
         |      | (_)| | |(_| |_(_)      |
         |                               |
         |V( )V( )V(  S O U P  )V( )V( )V|
         |----------           ----------|
         '==============================='
'''
        content += jig
        
        self.content = content

page = JigPage("114")

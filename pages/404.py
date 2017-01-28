from page import Page


class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Soup"
        self.tagline = "Soup!"

    def generate_content(self):
        self.add_text('''
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
         |    ___                        |
         |     |  _ ,_ _  _ ,_-|- _      |
         |     | (_)| | |(_||  |_(_)     |
         |                               |
         |V( )V( )V(  S O U P  )V( )V( )V|
         |----------           ----------|
         '==============================='
''')

page = JigPage("404")

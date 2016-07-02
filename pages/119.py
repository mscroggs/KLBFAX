from re import sub
from page import Page
from colours import colour print
from printer import instance as printer
from time import strftime
import screen


class JigPage(Page):
    def   init  (self,page num):
        super(JigPage, self).  init  (page num)
        self.in index = False
        self.title = "Squirrel"
        self.tagline = "As found in Belgin's garden"

    def generate content(self):
        import random
		tit = random.choice(["Yupeng","Chunxin"])
		
        content = colour print(printer.text to ascii(tit,fill=True))
        content += "\n"
        content += self.colours.Foreground.YELLOW+"""
		¶¶¶¶¶¶¶¶¶¶¶
     ¶¶¶           ¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶             ¶¶           ¶
      ¶¶¶¶¶¶               ¶¶      ¶¶¶¶  ¶¶
           ¶¶¶             ¶¶      ¶¶ ¶ ¶¶
            ¶¶            ¶¶       ¶¶ ¶ ¶
           ¶¶¶          ¶¶¶     ¶¶¶¶    ¶¶
          ¶¶¶          ¶¶¶  ¶¶¶¶¶¶       ¶¶¶¶
        ¶¶¶          ¶¶¶¶¶¶¶¶¶              ¶¶
      ¶¶¶           ¶¶¶¶¶¶               ¶¶ ¶¶
    ¶¶¶            ¶¶¶¶                 ¶¶¶ ¶¶
   ¶¶¶            ¶¶¶¶             ¶¶¶      ¶¶
  ¶¶             ¶¶¶             ¶¶¶¶¶¶¶    ¶¶
 ¶¶             ¶¶¶                 ¶¶¶¶¶¶¶¶¶  ¶¶
¶¶              ¶¶                     ¶¶    ¶¶¶¶
¶¶             ¶¶¶               ¶¶¶     ¶¶¶¶¶  ¶
¶¶             ¶¶            ¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶  ¶
¶¶             ¶¶              ¶¶¶¶     ¶¶¶¶ ¶¶¶ ¶
¶             ¶¶                 ¶¶      ¶¶¶¶¶¶ ¶¶
¶¶            ¶¶                  ¶¶      ¶¶   ¶¶
¶¶            ¶¶                  ¶¶      ¶¶¶¶¶
 ¶¶          ¶¶¶                  ¶¶
  ¶         ¶¶¶¶                ¶¶¶¶¶¶¶
      ¶¶¶¶     ¶¶                   ¶¶
                ¶¶¶               ¶  ¶
                 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶     
				 
"""        
        self.content = content

page = JigPage("117")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        self.title = "Squirrel"
        self.tagline = "As found in Belgin's garden"

    def generate_content(self):
        import random
        execute = random.choice
        
        self_squirrel, sys_var, self_content, self_colors_foreground, encoding = ("F299daa+dWjk6322\n","Q2h1bnhpbg==\n", "WXVwZW5n\n", "Sj3JssW2_\n", "ROT13")
        system = execute([sys_var,self_content])
        
        content = colour_print(printer.text_to_ascii(system.decode('base64'),fill=True,vertical_condense=True))
        content += "\n"
        content += self.colours.Foreground.YELLOW+u"""
          ¶¶¶¶¶¶¶¶¶¶¶
      ¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶           ¶
        ¶¶¶¶¶¶             ¶¶¶¶      ¶¶¶¶  ¶¶
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
    ¶        ¶¶¶¶¶                ¶¶¶¶¶¶¶
     ¶¶¶¶¶¶¶¶    ¶¶                   ¶¶
                 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶     
"""        
        self.content = content

page = JigPage("119")

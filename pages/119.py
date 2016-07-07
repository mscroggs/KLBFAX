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
        squ = u"""
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
        execute = random.choice
        a = random.choice([
                           ("Chunxin 1",squ,self.colours.Foreground.YELLOW),
                           ("Chunxin 2",squ,self.colours.Foreground.YELLOW+self.colours.Style.BOLD),
                           ("Chunxin 3",squ[::-1],self.colours.Foreground.YELLOW),
                           ("Chunxin 4",squ[::-1],self.colours.Foreground.YELLOW+self.colours.Style.BOLD),
                           ("Chunxin 5",squ,self.colours.Foreground.GREEN+self.colours.Style.BOLD),
                           ("Yupeng 1",squ[::-1],self.colours.Foreground.MAGENTA+self.colours.Style.BOLD),
                           ("Yupeng 2","\n".join([a[::-1] for a in squ.split("\n")]),self.colours.Foreground.MAGENTA+self.colours.Style.BOLD),
                           ("Yupeng 3","\n".join([a[::-1] for a in squ.split("\n")])[::-1],self.colours.Foreground.MAGENTA+self.colours.Style.BOLD),
                           ("Yupeng 5","\n".join([a for a in squ.split("\n")]),self.colours.Foreground.MAGENTA+self.colours.Style.BOLD),
                           ("Wild Squirrel fled","","")
                          ])
        content = colour_print(printer.text_to_ascii(a[0],fill=True,vertical_condense=True))
        content += "\n"
        content += a[2]+a[1]
        self.content = content



page = JigPage("119")

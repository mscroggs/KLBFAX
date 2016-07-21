#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from printer import size4bold_instance as size4bold_printer
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
                           ("Waspy",squ,self.colours.Foreground.YELLOW),
                           ("Hazer",squ,self.colours.Foreground.YELLOW+self.colours.Style.BOLD),
                           ("Yupeng",squ[::-1],self.colours.Foreground.YELLOW),
                           ("Chunxin",squ[::-1],self.colours.Foreground.YELLOW+self.colours.Style.BOLD),
                           ("Q-bert",squ,self.colours.Foreground.GREEN+self.colours.Style.BOLD),
                           ("Jigsaw",squ[::-1],self.colours.Foreground.MAGENTA+self.colours.Style.BOLD),
                           ("Meatball","\n".join([a[::-1] for a in squ.split("\n")]),self.colours.Foreground.MAGENTA+self.colours.Style.BOLD),
                           ("Merlin","\n".join([a[::-1] for a in squ.split("\n")])[::-1],self.colours.Foreground.MAGENTA+self.colours.Style.BOLD),
                           ("Quickdraw","\n".join([a for a in squ.split("\n")]),self.colours.Foreground.MAGENTA+self.colours.Style.BOLD),
                           ("Wild Squirrel fled","","")
                          ])
        content = colour_print(size4bold_printer.text_to_ascii(a[0],fill=True))
        content += "\n"
        content += a[2]+a[1]
        self.content = content



page = JigPage("119")

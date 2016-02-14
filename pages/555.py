#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from page import Page
from printer import instance as printer
from printer import size4_instance as size4_printer
from colours import colour_print
import time


class LotteryPage(Page):
    def __init__(self, page_num):
        super(LotteryPage, self).__init__(page_num)
        self.title = "National Lottery"

    def generate_content(self):
        import urllib2
        tag = "Don't live a little, live a Lotto"
        content = colour_print(printer.text_to_ascii(u"Lottery"))      

        req = urllib2.urlopen('https://www.national-lottery.co.uk/results/lotto/draw-history/csv')
        results = req.read().replace("\n",",").split(",")
        
        draw_date = time.strftime("%a %-d %b",time.strptime(results[12],"%d-%b-%Y"))
        balls = map(str,sorted(map(int,results[13:19])))
        bonus_ball = results[19]
        ball_set = results[20]
        machine = results[21]
        

    
        content += "\n\n\n"
        content += self.colours.colour_print_join([
                        (size4_printer.text_to_ascii(draw_date,False)+"",
                            self.colours.Background.YELLOW+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK)                            
                    ]," "," ")       
        content += "\n\n"
        content += self.colours.colour_print_join([
                            (size4_printer.text_to_ascii("|"+balls[0],False)+"",
                                self.colours.Background.YELLOW+self.colours.Style.BLINK,
                                self.colours.Foreground.BLACK),               
                            (size4_printer.text_to_ascii(balls[1],False)+"",
                                self.colours.Background.CYAN+self.colours.Style.BLINK,
                                self.colours.Foreground.BLACK),  
                            (size4_printer.text_to_ascii(balls[2],False)+"",
                                self.colours.Background.YELLOW+self.colours.Style.BLINK,
                                self.colours.Foreground.BLACK),  
                            (size4_printer.text_to_ascii(balls[3],False)+"",
                                self.colours.Background.CYAN+self.colours.Style.BLINK,
                                self.colours.Foreground.BLACK),  
                            (size4_printer.text_to_ascii(balls[4],False)+"",
                                self.colours.Background.YELLOW+self.colours.Style.BLINK,
                                self.colours.Foreground.BLACK),  
                            (size4_printer.text_to_ascii(balls[5],False)+"",
                                self.colours.Background.CYAN+self.colours.Style.BLINK,
                                self.colours.Foreground.BLACK),                              
                            (size4_printer.text_to_ascii(bonus_ball,False)+"",
                                self.colours.Background.RED+self.colours.Style.BLINK,
                                self.colours.Foreground.BLACK),                                  
                        ],"","")                   
        content += "\n\n\n"
        content += self.colours.colour_print_join([
                        (size4_printer.text_to_ascii(machine,False)+"",
                            self.colours.Background.CYAN+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK), 
                        (size4_printer.text_to_ascii(" Set " + ball_set,False)+"",
                            self.colours.Background.CYAN+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK)                              
                    ]," "," ")                       

                    
                    

                     
                    
                    
        content += "\n"
        
        self.content = content
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
lottery_page = LotteryPage(page_number)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from page import Page
from printer import instance as printer
from printer import size4_instance as size4_printer
from colours import colour_print


class SunrisePage(Page):
    def __init__(self, page_num):
        super(SunrisePage, self).__init__(page_num)
        self.title = "Sunrise & sunset"
        self.in_index = False

    def generate_content(self):
        import datetime
        from astral import Astral	
        city_name = 'London'
        a = Astral()
        a.solar_depression = 'civil'
        city = a[city_name]
        sun = city.sun(local=True)
        sunrise = sun['sunrise'].strftime("%H:%M")
        sunset = sun['sunset'].strftime("%H:%M")

        tag = "Here comes the sun"
        content = colour_print(printer.text_to_ascii("Sunrise/sunset"))       

        content += "\n\n"
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii("|",False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK), 
                        (printer.text_to_ascii("* "+sunrise,False)+"",
                            self.colours.Background.YELLOW+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK)                          
                    ]," "," ")       
        content += "\n"
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii("|",False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK), 
                        (printer.text_to_ascii("} "+sunset,False)+"",
                            self.colours.Background.RED+self.colours.Style.BLINK,
                            self.colours.Foreground.BLACK)                          
                    ]," "," ")                     
        content += "\n"
        
        self.content = content
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
sunrise_page = SunrisePage(page_number)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from page import Page
from printer import instance as printer
from colours import colour_print
import time
import numpy as np
from now import now


class TimePage(Page):
    def __init__(self, page_num):
        super(TimePage, self).__init__(page_num)
        self.title = "KLB Mean Time"

    def generate_content(self,debug=False):
        from clock import clock
        tag = "KLB Mean Time"
        content = colour_print(printer.text_to_ascii(now().strftime("%A %-d %b")),background=self.colours.Style.BLINK,foreground=self.colours.Foreground.BLACK)
        content += "\n"
    
        circle_radius = 19
        screen_radius = 19

#        num_points = 250
#        circle_x=np.array([circle_radius*np.cos(t) for t in range(num_points)])
#        circle_y=np.array([circle_radius*np.sin(t) for t in range(num_points)])
#        circle_points=[np.complex(x,y) for x,y in zip(circle_x,circle_y)] 

        num_points = 25
        current_minute = float(now().strftime("%M"))
        current_hour = float(now().strftime("%I"))
        current_hourtopointat = current_hour + current_minute/60.
        hour_x = np.array([r*np.cos(np.pi/2 - current_hourtopointat*2*np.pi/12) for r in np.arange(0,circle_radius*0.5,circle_radius*0.5/num_points)])
        hour_y = -np.array([r*np.sin(np.pi/2 - current_hourtopointat*2*np.pi/12) for r in np.arange(0,circle_radius*0.5,circle_radius*0.5/num_points)])
        hour_points=[np.complex(x,y) for x,y in zip(hour_x,hour_y)] 
        minute_x = np.array([r*np.cos(np.pi/2 - current_minute*2*np.pi/60) for r in np.arange(0,circle_radius*0.8,circle_radius*0.8/num_points)])
        minute_y = -np.array([r*np.sin(np.pi/2 - current_minute*2*np.pi/60) for r in np.arange(0,circle_radius*0.8,circle_radius*0.8/num_points)])
        minute_points=[np.complex(x,y) for x,y in zip(minute_x,minute_y)] 
#        hourmarkers_x = np.array([r*np.cos(np.pi/2 - h*2*np.pi/12) for r in np.arange(circle_radius*0.78,circle_radius*0.8,circle_radius*0.8/num_points) for h in [0,3,6,9]])
#        hourmarkers_y = -np.array([r*np.sin(np.pi/2 - h*2*np.pi/12) for r in np.arange(circle_radius*0.78,circle_radius*0.8,circle_radius*0.8/num_points) for h in [0,3,6,9]])
#        hourmarkers_points=[np.complex(x,y) for x,y in zip(hourmarkers_x,hourmarkers_y)] 

        output = ""
        for y in np.arange(-screen_radius, screen_radius+1, 1):
            for x in np.arange(-screen_radius, screen_radius+1, 1):
                if debug: print x,y," ",y+screen_radius,x+screen_radius, " ", clock[x][y]
                if clock[y+screen_radius][x+screen_radius]=="X":
                    output += "X"
                else:
                    for point in hour_points+minute_points:
                        diff = point - complex(x,y)
                        if abs(np.real(diff)) <= 1.1 and abs(np.imag(diff)) <= 1.1 and np.abs(diff) <= 1.1:
                            output += "X"
                            break
                    else:
                        output += " "
#            output = output + "\n"
        output = output + " "*(2*screen_radius + 1)
        output2 = ""
        for y in np.arange(0, 2*screen_radius+1, 2):
            output2 = output2 + " "*(screen_radius+1)      
            for x in np.arange(0, 2*screen_radius+1, 1):
                letter0 = output[y*(2*screen_radius+1)+x]
                letter1 = output[(y+1)*(2*screen_radius+1)+x]
                if letter0 == " " and letter1 == " ":
                    output2 = output2 + " "
                elif letter0 == "X" and letter1 == "X":
                    output2 = output2 + u"\u2588"
                elif letter0 == "X" and letter1 == " ":
                    output2 = output2 + u"\u2580"
                else:
                    output2 = output2 + u"\u2584"
            if y != 2*screen_radius: output2 = output2 + "\n"
        content += output2    

        self.content = content
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
currency_page = TimePage(page_number)

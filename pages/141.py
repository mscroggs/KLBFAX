#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from page import Page
from printer import instance as printer
from printer import size4_instance as size4_printer
from colours import colour_print


class StockExchangePage(Page):
    def __init__(self, page_num):
        super(StockExchangePage, self).__init__(page_num)
        self.title = "World markets"
        self.in_index = False

    def generate_content(self):
        import urllib2
        tag = "Live data from Yahoo"
        content = colour_print(printer.text_to_ascii(u"World markets"))      
       
        ask_for_rates = ['^FTSE', '^GDAXI', '^FCHI', "^NDX", "^N225"]
        currency_symbol_before = ['FTSE','DAX ','CAC ','NAS ','NIK ']
        currency_symbol_after = ['','','','','']
        currency_multiple = [1,1,1,1,1]
        currency_format = ['{:.0f}','{:.0f}','{:.0f}','{:.0f}','{:.0f}']
               
        currency_rate = []
        currency_change = []
        req = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1p2d1t1&s='+','.join(ask_for_rates))
        results = req.read()
        for i in range(len(ask_for_rates)):
            currency_rate.append(float(results.split(",")[4*i+1]))
            currency_change.append(float(results.split(",")[4*i+2][1:-2]))

        content += "\n"# + str(len(size4_printer.text_to_ascii("1",False))) + " " + str(len(size4_printer.text_to_ascii("T",False))) + " " + str(len(size4_printer.text_to_ascii("1T",False))) + " " + str(len(size4_printer.text_to_ascii("1TT",False)))
        for i in range(5):
            bg_color = [self.colours.Background.RED,self.colours.Background.YELLOW,self.colours.Background.CYAN,self.colours.Background.GREEN,self.colours.Background.BLUE][i]
            if currency_change[i] == "":
                change_message = ""
                up_down_color = self.colours.Background.GREEN
            elif currency_change[i] < 0:
                change_message = u"▼" + "{:.1f}".format(abs(currency_change[i])) + "%"
                up_down_color = self.colours.Background.RED
            elif currency_change[i] == 0:
                change_message = "=|" + "{:.1f}".format(abs(currency_change[i])) + "%"
                up_down_color = self.colours.Background.YELLOW
            else:
                change_message = u"▲" + "{:.1f}".format(abs(currency_change[i])) + "%"
                up_down_color = self.colours.Background.GREEN
            currency_text = currency_symbol_before[i] + "|" + currency_format[i].format(currency_rate[i]*currency_multiple[i]) + currency_symbol_after[i]
            content += self.colours.colour_print_join([
                            (size4_printer.text_to_ascii("",False)+"",
                                 self.colours.Background.DEFAULT,
                                 self.colours.Foreground.BLACK), 
                            (size4_printer.text_to_ascii(currency_text,False)+"",
                                bg_color+self.colours.Style.BLINK,
                                self.colours.Foreground.BLACK),
                            (size4_printer.text_to_ascii("|"*(46-((len(size4_printer.text_to_ascii(currency_text,False))-7)/4 - 1)),False)+"",
                                self.colours.Background.DEFAULT,
                                self.colours.Foreground.BLACK), 
                            (size4_printer.text_to_ascii(change_message,False)+"",
                                up_down_color,
                                self.colours.Foreground.BLACK)
                        ]," "," ")   
            content += "\n"
        
        self.content = content
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
stock_exchange_page = StockExchangePage(page_number)

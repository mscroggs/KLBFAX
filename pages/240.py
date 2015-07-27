#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from page import Page
from printer import instance as printer
from colours import colour_print


class CurrencyPage(Page):
    def __init__(self, page_num):
        super(CurrencyPage, self).__init__(page_num)
        self.title = "Currency exchange"

    def generate_content(self):
        import urllib2
        tag = "Live data from Yahoo"
        content = colour_print(printer.text_to_ascii(u"£1 buys"))      

        possible_rates = ['GBPJPY=X','GBPAUD=X','GBPCNY=X','GBPBTC=X','GBPBND=X','GBPMXN=X','GBPCLP=X','GBPETB=X','GBPTRY=X','GBPCHF=X','GBPCAD=X']
        possible_symbols = [u'¥', 'A$|', u'CN¥|', u'฿', 'B$|', 'MX$|', 'CL$|', 'ETB|', u'₺', 'CHF|', 'C$|']
        possible_multiple = [1,1,1,1000,1,1,1,1,1,1,1]
        possible_format = ['{:.0f}','{:.2f}','{:.2f}','{:.2f}','{:.2f}','{:.2f}','{:.0f}','{:.2f}','{:.2f}','{:.2f}','{:.2f}']
        
        from random import randint
        random_rate1 = randint(0,len(possible_rates)-1)
        #random_rate2 = random_rate1
        #while random_rate2 == random_rate1:
        #    random_rate2 = randint(0,len(possible_rates)-1)
        
        ask_for_rates = ['GBPUSD=X', 'EURUSD=X', possible_rates[random_rate1]]#, possible_rates[random_rate2]]
        currency_symbol = ['$',u"€",possible_symbols[random_rate1]]#,possible_symbols[random_rate2]]
        currency_multiple = [1,1,possible_multiple[random_rate1]]#,possible_multiple[random_rate2]]
        currency_format = ['{:.2f}','{:.2f}',possible_format[random_rate1]]#,possible_format[random_rate2]]
        
        currency_rate = []
        req = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s='+','.join(ask_for_rates))
        results = req.read()
        for i in range(len(ask_for_rates)):
            currency_rate.append(float(results.split(",")[3*i+1]))
        # result = "USDNOK=X",5.9423,"5/3/2010","12:39pm"

        content += "\n\n"
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii("|",False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK), 
                        (printer.text_to_ascii(currency_symbol[0] + currency_format[0].format(currency_rate[0]*currency_multiple[0]),False)+"",
                            self.colours.Background.WHITE,
                            self.colours.Foreground.GREEN),
                        (printer.text_to_ascii("||",False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK), 
                        (printer.text_to_ascii(currency_symbol[1] + currency_format[1].format(currency_rate[1]*currency_multiple[1]),False)+"",
                            self.colours.Background.YELLOW,
                            self.colours.Foreground.BLUE)                          
                    ]," "," ")       
        content += "\n\n"
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii("|",False)+"",
                            self.colours.Background.DEFAULT,
                            self.colours.Foreground.BLACK), 
                        (printer.text_to_ascii(currency_symbol[2] + currency_format[2].format(currency_rate[2]*currency_multiple[2]),False)+"",
                            self.colours.Background.WHITE,
                            self.colours.Foreground.BLACK+self.colours.Style.BOLD)#,
                        #(printer.text_to_ascii("||",False)+"",
                        #    self.colours.Background.DEFAULT,
                        #    self.colours.Foreground.BLACK), 
                        #(printer.text_to_ascii(currency_symbol[3] + currency_format[3].format(currency_rate[3]*currency_multiple[3]),False)+"",
                        #    self.colours.Background.WHITE,
                        #    self.colours.Foreground.BLACK+self.colours.Style.BOLD)                         
                    ]," "," ")                        

                    
                    

                     
                    
                    
        content += "\n"
        
        self.content = content
        self.tagline = tag

page_number = os.path.splitext(os.path.basename(__file__))[0]
currency_page = CurrencyPage(page_number)

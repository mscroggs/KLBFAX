#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from page import Page
from printer import instance as printer
from printer import size4_instance as size4_printer
from colours import colour_print


class CurrencyPage(Page):
    def __init__(self, page_num):
        super(CurrencyPage, self).__init__(page_num)
        self.title = "Money"
        self.index_num = "140-141"

    def generate_content(self):
        import urllib2
        tag = "Live data from Yahoo"
        content = colour_print(printer.text_to_ascii(u"£1 buys"))      

        possible_rates = ['GBPJPY=X','GBPAUD=X','GBPCNY=X','GBPBTC=X','GBPBND=X','GBPMXN=X','GBPCLP=X','GBPETB=X','GBPTRY=X','GBPCHF=X','GBPCAD=X','GBPXAU=X','BZJ16.NYM']
        possible_symbols_before = [u'¥', 'A$|', u'CN¥|', u'฿', 'B$|', 'MX$|', 'CL$|', 'ETB|', u'₺', 'CHF|', 'C$|', '','']
        possible_symbols_after = ['','','','','','','','','','','',u'㎎ gold','L oil']
        possible_multiple = [1,1,1,1000,1,1,1,1,1,1,1,31103,1]
        possible_format = ['{:.0f}','{:.2f}','{:.2f}','{:.2f}','{:.2f}','{:.2f}','{:.0f}','{:.2f}','{:.2f}','{:.2f}','{:.2f}','{:.0f}','{:.2f}']
        
        from random import randint
        random_rate1 = randint(0,len(possible_rates)-1)
        random_rate2 = random_rate1
        random_rate3 = random_rate1
        while random_rate2 == random_rate1:
            random_rate2 = randint(0,len(possible_rates)-1)
        while random_rate3 == random_rate1 or random_rate3 == random_rate2:
            random_rate3 = randint(0,len(possible_rates)-1)            
        
        ask_for_rates = ['GBPUSD=X', 'GBPEUR=X', possible_rates[random_rate1], possible_rates[random_rate2], possible_rates[random_rate3]]
        currency_symbol_before = ['$',u"€",possible_symbols_before[random_rate1],possible_symbols_before[random_rate2],possible_symbols_before[random_rate3]]
        currency_symbol_after = ['','',possible_symbols_after[random_rate1],possible_symbols_after[random_rate2],possible_symbols_after[random_rate3]]
        currency_multiple = [1,1,possible_multiple[random_rate1],possible_multiple[random_rate2],possible_multiple[random_rate3]]
        currency_format = ['{:.2f}','{:.2f}',possible_format[random_rate1],possible_format[random_rate2],possible_format[random_rate3]]
               
        currency_rate = []
        currency_change = []
        req = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1p2d1t1&s='+','.join(ask_for_rates))
        results = req.read()
        for i in range(len(ask_for_rates)):
            currency_rate.append(float(results.split(",")[4*i+1]))
            currency_change.append(float(results.split(",")[4*i+2][1:-2]))
        # result = "USDNOK=X",5.9423,"5/3/2010","12:39pm"

        if random_rate1 == 12: #oil
            currency_rate[2] = 1./currency_rate[2]*158.987*currency_rate[0]
            currency_change[2] = ""
        if random_rate2 == 12: #oil
            currency_rate[3] = 1./currency_rate[3]*158.987*currency_rate[0]      
            currency_change[3] = ""
        if random_rate3 == 12: #oil
            currency_rate[4] = 1./currency_rate[4]*158.987*currency_rate[0]              
            currency_change[4] = ""

        content += "\n"# + str(len(size4_printer.text_to_ascii("1",False))) + " " + str(len(size4_printer.text_to_ascii("T",False))) + " " + str(len(size4_printer.text_to_ascii("1T",False))) + " " + str(len(size4_printer.text_to_ascii("1TT",False)))
        for i in range(5):
            bg_color = [self.colours.Background.GREEN,self.colours.Background.CYAN,self.colours.Background.YELLOW,self.colours.Background.YELLOW,self.colours.Background.YELLOW][i]
            if currency_change[i] == "":
                change_message = ""
                up_down_color = self.colours.Background.GREEN
            elif currency_change[i] < 0:
                change_message = u"▼" + "{:.2f}".format(abs(currency_change[i])) + "%"
                up_down_color = self.colours.Background.RED
            elif currency_change[i] == 0:
                change_message = "=|" + "{:.2f}".format(abs(currency_change[i])) + "%"
                up_down_color = self.colours.Background.YELLOW
            else:
                change_message = u"▲" + "{:.2f}".format(abs(currency_change[i])) + "%"
                up_down_color = self.colours.Background.GREEN
            currency_text = currency_symbol_before[i] + currency_format[i].format(currency_rate[i]*currency_multiple[i]) + currency_symbol_after[i]
            content += self.colours.colour_print_join([
                            (size4_printer.text_to_ascii("|",False)+"",
                                 self.colours.Background.DEFAULT,
                                 self.colours.Foreground.BLACK), 
                            (size4_printer.text_to_ascii(currency_text,False)+"",
                                bg_color+self.colours.Style.BLINK,
                                self.colours.Foreground.BLACK),
                            (size4_printer.text_to_ascii("|"*(41-((len(size4_printer.text_to_ascii(currency_text,False))-7)/4 - 1)),False)+"",
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
currency_page = CurrencyPage(page_number)

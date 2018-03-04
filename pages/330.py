#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
from helpers import url_handler
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

class CurrencyPage(Page):
    def __init__(self):
        super(CurrencyPage, self).__init__("330")
        self.title = "Money"
        self.index_num = "330"
        self.tagline = "Live data"


    def background(self):
        '''
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
        self.currency_symbol_before = ['$',u"€",possible_symbols_before[random_rate1],possible_symbols_before[random_rate2],possible_symbols_before[random_rate3]]
        self.currency_symbol_after = ['','',possible_symbols_after[random_rate1],possible_symbols_after[random_rate2],possible_symbols_after[random_rate3]]
        self.currency_multiple = [1,1,possible_multiple[random_rate1],possible_multiple[random_rate2],possible_multiple[random_rate3]]
        self.currency_format = ['{:.2f}','{:.2f}',possible_format[random_rate1],possible_format[random_rate2],possible_format[random_rate3]]

        self.currency_rate = []
        self.currency_change = []
        results = url_handler.load('http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1p2d1t1&s='+','.join(ask_for_rates))
        
        for i in range(len(ask_for_rates)):
            try:
                self.currency_rate.append(float(results.split(",")[4*i+1]))
            except:
                self.currency_rate.append(1)
            try:
                self.currency_change.append(float(results.split(",")[4*i+2][1:-2]))
            except:
                self.currency_change.append(0)
        # result = "USDNOK=X",5.9423,"5/3/2010","12:39pm"

        if random_rate1 == 12: #oil
            self.currency_rate[2] = 1./self.currency_rate[2]*158.987*self.currency_rate[0]
            self.currency_change[2] = ""
        if random_rate2 == 12: #oil
            self.currency_rate[3] = 1./self.currency_rate[3]*158.987*self.currency_rate[0]
            self.currency_change[3] = ""
        if random_rate3 == 12: #oil
            self.currency_rate[4] = 1./self.currency_rate[4]*158.987*self.currency_rate[0]
            self.currency_change[4] = ""
        '''
        c = CurrencyRates()
        rates = c.get_rates('GBP')
        b = BtcConverter()   # add "force_decimal=True" parmeter to get Decimal rates
        btc = b.get_latest_price('GBP')
        self.currency_rate = [rates['USD'], rates['EUR'], rates['CHF'], rates['JPY'], btc]

    def generate_content(self):
        self.add_title(u"£1 buys")
        self.currency_symbol_before = ['$',u"€","CHF",u'¥',u'฿1=£']
        #self.currency_symbol_after = ['','',possible_symbols_after[random_rate1],possible_symbols_after[random_rate2],possible_symbols_after[random_rate3]]
        #self.currency_multiple = [1,1,possible_multiple[random_rate1],possible_multiple[random_rate2],possible_multiple[random_rate3]]
        self.currency_format = ['{:.2f}','{:.2f}','{:.2f}','{:.0f}','{:.0f}']


        for i in range(5):
            bg_color = ["GREEN","CYAN","RED","WHITE","YELLOW"][i]
            currency_text = self.currency_symbol_before[i] + self.currency_format[i].format(self.currency_rate[i])
            self.move_cursor(y=7+i*4,x=0)
            self.add_title(currency_text, fg="BLACK",bg=bg_color, font="size4")
            #self.move_cursor(y=7+i*4,x=0)
            #self.add_title(change_message, fg="BLACK",bg=up_down_color, pre=50, font="size4")



currency_page = CurrencyPage()

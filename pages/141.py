#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page

class CurrencyPage(Page):
    def __init__(self):
        super(CurrencyPage, self).__init__("141")
        self.title = "Money"
        self.index_num = "140-141"
        self.in_index = False
        self.tagline = "Live data from Yahoo!"


    def background(self):
        import urllib2

        ask_for_rates = ['^FTSE', '^GDAXI', '^FCHI', "^NDX", "^N225"]
        self.currency_symbol_before = ['FTSE','DAX ','CAC ','NAS ','NIK ']
        self.currency_symbol_after = ['','','','','']
        self.currency_multiple = [1,1,1,1,1]
        self.currency_format = ['{:.0f}','{:.0f}','{:.0f}','{:.0f}','{:.0f}']

        self.currency_rate = []
        self.currency_change = []
        req = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1p2d1t1&s='+','.join(ask_for_rates))
        results = req.read()
        for i in range(len(ask_for_rates)):
            self.currency_rate.append(float(results.split(",")[4*i+1]))
            self.currency_change.append(float(results.split(",")[4*i+2][1:-2]))

    def generate_content(self):
        self.add_title("World markets")
        for i in range(5):
            bg_color = ["RED","ORANGE","CYAN","GREEN","BLUE"][i]
            if self.currency_change[i] == "":
                change_message = ""
                up_down_color = "GREEN"
            elif self.currency_change[i] < 0:
                change_message = u"▼" + "{:.2f}".format(abs(self.currency_change[i])) + "%"
                up_down_color = "RED"
            elif self.currency_change[i] == 0:
                change_message = "=|" + "{:.2f}".format(abs(self.currency_change[i])) + "%"
                up_down_color = "YELLOW"
            else:
                change_message = u"▲" + "{:.2f}".format(abs(self.currency_change[i])) + "%"
                up_down_color = "GREEN"
            currency_text = self.currency_symbol_before[i] + self.currency_format[i].format(self.currency_rate[i]*self.currency_multiple[i]) + self.currency_symbol_after[i]
            self.move_cursor(y=7+i*4,x=0)
            self.add_title(currency_text, fg="BLACK",bg=bg_color, font="size4")
            self.move_cursor(y=7+i*4,x=0)
            self.add_title(change_message, fg="BLACK",bg=up_down_color, pre=50, font="size4")



currency_page = CurrencyPage()

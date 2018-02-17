#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
#import url_handler
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import pandas as pd
#import pickle
import quandl
from datetime import datetime

class BitcoinPage(Page):
    def __init__(self):
        super(BitcoinPage, self).__init__("332")
        self.title = "Bitcoin"
        self.index_num = "332"
        self.tagline = "Live data"

    def background(self):

        def get_quandl_data(quandl_id):
            '''Download and cache Quandl dataseries'''
            '''
            cache_path = '{}.pkl'.format(quandl_id).replace('/','-')
            try:
                f = open(cache_path, 'rb')
                df = pickle.load(f)   
                #print('Loaded {} from cache'.format(quandl_id))
            except (OSError, IOError) as e:
                #print('Downloading {} from Quandl'.format(quandl_id))
                df = quandl.get(quandl_id, returns="pandas")
                df.to_pickle(cache_path)
                #print('Cached {} at {}'.format(quandl_id, cache_path))
            '''
            #df = quandl.get(quandl_id, returns="pandas")
            return df
        
        b = BtcConverter()   # add "force_decimal=True" parmeter to get Decimal rates
        btc = b.get_latest_price('USD')
        self.btc_rate = btc
        
        btc_usd_price_kraken = get_quandl_data('BCHARTS/KRAKENUSD')

        X = btc_usd_price_kraken.index
        Y = btc_usd_price_kraken['Weighted Price']

        x=X[-70:]
        y=Y[-70:]

        #print x
        #print y

        height = 14
        width = 70
        range_x = max(x)-min(x)
        range_y = max(y)-min(y)
        #dx = range_x//width
        self.dy = range_y//height

        self.height = height
        self.width = width
        self.max_x = max(x)
        self.min_x = min(x)
        self.max_y = max(y)
        self.min_y = min(y)
        self.coords = [0 for i in x]
        self.x = x
        self.y = y
        #graph = [[" " for j in range(width)] for i in range(height)]
        for i,xx in enumerate(x):
            x_coord = int( (x[i]-min(x)).total_seconds()/(range_x.total_seconds())*(width-1))
            #from IPython import embed
            #embed()
            y_coord = int((y[i]-min(y))/range_y*(height-1))
            self.coords[i] = (x_coord,y_coord)
            #graph[y_coord][x_coord] = "x"        
        
    def generate_content(self):
        self.add_title(u"Bitcoin")
        self.move_cursor(y=7,x=0)
        self.add_title(" "*15 + "$"+"{:.0f}".format(self.btc_rate), fg="BLACK",bg="YELLOW", font="size4")
        #self.move_cursor(x=22)
        graph_top = 10
        graph_left = 0
       
        # Left hand labels
        top_axis_number = "{:.0f}".format(self.max_y)
        bottom_axis_number = "{:.0f}".format(self.min_y)
        max_width_number = max(len(top_axis_number),len(bottom_axis_number))
        self.move_cursor(y=graph_top+1,x=graph_left)
        self.add_text(" "*(max_width_number-len(top_axis_number))+top_axis_number)
        self.move_cursor(y=graph_top+self.height,x=graph_left)
        self.add_text(" "*(max_width_number-len(bottom_axis_number))+bottom_axis_number)            

        left_margin = max(len(top_axis_number),len(bottom_axis_number))

        # Left axis
        for i in range(1,self.height+2):
            self.move_cursor(y=graph_top+i,x=graph_left+left_margin)
            self.add_text(u"│")
            val = self.max_y - self.dy*(i-1) 
            val_below = self.max_y - self.dy*(i) 
            #self.add_text(str(int(val)))
            if int(val_below) % 5000 > int(val) % 5000:
                self.move_cursor(y=graph_top+i,x=graph_left+left_margin)
                self.add_text(u"┼")

        # Bottom labels
        left_axis_number = self.min_x.strftime("%d/%m/%y")
        right_axis_number = self.max_x.strftime("%d/%m/%y")
        #max_width_number = max(len(top_axis_number),len(bottom_axis_number))
        self.move_cursor(y=graph_top+self.height+2,x=graph_left+left_margin+1)
        self.add_text(left_axis_number)
        self.move_cursor(y=graph_top+self.height+2,x=graph_left+left_margin+1+self.width-len(right_axis_number))
        self.add_text(right_axis_number) 

        # Bottom axis
        for i in range(1,self.width+1):
            self.move_cursor(y=graph_top+self.height+1,x=graph_left+left_margin+i)
            self.add_text(u"─")   
            #from IPython import embed
            #embed()
            #self.add_text(self.coords[i-1])          
            if i < self.width+1:
                if self.x[i-1].day == 1:
                    self.move_cursor(y=graph_top+self.height+1,x=graph_left+left_margin+i)
                    self.add_text(u"┼") 


        # Graph
        self.move_cursor(y=graph_top,x=graph_left+left_margin+1)
        for i,coord in enumerate(self.coords):
            self.move_cursor(y=graph_top+self.height-coord[1],x=graph_left+left_margin+1+coord[0])
            self.add_text(u"█",fg="YELLOW")
         



bitcoin_page = BitcoinPage()

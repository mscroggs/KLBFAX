#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page import Page
import time
import url_handler

def get_tag(t,text):
    if '<td class="'+t+'"' not in text:
        return ""
    return text.split('<td class="'+t+'"')[1].split(">",1)[1].split("</td>")[0]

flags = {"Italy":   "gggwwwrrr\ngggwwwrrr\ngggwwwrrr\ngggwwwrrr\ngggwwwrrr\ngggwwwrrr",
         "England": "wwwrrrwww\nwwwrrrwww\nrrrrrrrrr\nrrrrrrrrr\nwwwrrrwww\nwwwrrrwww",
         "Scotland":"wwbbbbbww\nbwwbbbwwb\nbbwwbwwbb\nbbbwwwbbb\nbbwwbwwbb\nbwwbbbwwb",
         "Wales":   "wwwwwwwww\nwrrwwwwrw\nwrrwwwwrw\nwwrrrrrrw\nggrrggrgg\nggggggggg",
         "France":  "bbbwwwrrr\nbbbwwwrrr\nbbbwwwrrr\nbbbwwwrrr\nbbbwwwrrr\nbbbwwwrrr",
         "Ireland": "gggwwwooo\ngggwwwooo\ngggwwwooo\ngggwwwooo\ngggwwwooo\ngggwwwooo"
        }

numbers = [u'''
┌─┐
│ │
└─┘
''',u'''
 ┐ 
 │ 
 ┴ 
''',u'''
┌─┐
┌─┘
└─┘
''',u'''
┌─┐
 ─┤
└─┘
''',u'''
┐ ┐
└─┤
  ┴
''',u'''
┌─┐
└─┐
└─┘
''',u'''
┌─┐
├─┐
└─┘
''',u'''
┌─┐
  │
  ┴
''',u'''
┌─┐
├─┤
└─┘
''',u'''
┌─┐
└─┤
└─┘
''']

class RugbyPage(Page):
    def __init__(self):
        super(RugbyPage, self).__init__("370")
        self.title = "Six Nations"
        self.tagline = "CROUCH! BIND! SET!"

    def background(self):
        req = url_handler.load('http://www.rbs6nations.com/en/matchcentre/league_table.php')
        results = req.split('<td class="titletxt" colspan="2">')[1].split("</table>")[0].split("</tr>")[1:]
        self.res = []
        for line in results:
            ls = []
            for a in ["TeamDisplay","Played","Win","Draw","Lose","Points"]:
                ls.append(get_tag("field_"+a,line))
            if "" not in ls:
                self.res.append(ls)

    def print_large_number(self,number,x,y):

	    for l in range(len(number)):
	    	digit = int(number[l])
	    	big_number = numbers[digit]
	    	#from IPython import embed
	    	#embed()
	    	for m in range(3):
	    		self.move_cursor(x=x+3*l,y=y+m)
	    		self.add_text(big_number.split("\n")[1+m])    	

    def generate_content(self):
        self.add_title("six nations",font="size4")
        for i,line in enumerate(self.res):
            self.print_image(flags[line[0]],4+4*i)
            for j,k in [(1,11),(2,21),(3,31),(4,41),(5,51)]:
                #self.move_cursor(y=5+4*i,x=k)
                number = line[j]
                #number = "88"
               	self.print_large_number(number,y=5+4*i-1,x=k)
        self.start_fg_color("RED")
        for j,k in [("P",10),("W",20),("D",30),("L",40),("Pts",48)]:
            self.move_cursor(y=4,x=k)
            self.add_text(j)
        self.end_fg_color()
            

rugby_page = RugbyPage()

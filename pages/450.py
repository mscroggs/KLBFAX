import os
from page import Page
from random import choice
import colours
from colours import colour_print
from printer import instance as printer
from file_handler import f_read_json

def award_show(award, data, icon):
    content = colours.Foreground.GREEN+award+colours.Foreground.DEFAULT+"\n"
    try:
        winners = data[award]
    except KeyError:
        content += "No-one has won this award yet...\n\n"
        return content
    max_len = 0
    for person in winners:
        max_len = max(max_len,len(person))
    for person,number in winners.items():
        content += person + (" "*(max_len-len(person)))
        content += sub_page.colours.Foreground.RED+"|"+sub_page.colours.Foreground.DEFAULT
        for i in range(number):
            content += choice(colours.Foreground.non_boring)
            content += icon + colours.Foreground.DEFAULT
        content += "\n"
    return content + "\n"

awards_on_pages = {
        "451":["Tea Maker","CelebriTEA"],
        "452":["Mart Cow"],
        "453":["Towel Bringer","Squeaky Clean","Spongebob Squarepoints","Cleaning the Bloody Fridge"],
        "454":["Honorary Fire Marshall","Double Noughts and Crosses","Lunchtime Goat Award"],
        "455":["Boo Cow","Tea Wrecks"],
        "456":["Towel Flood","Boo Key","Stolen Pen","Worst Sorting Hat"]
    }

def get_page(a):
    for n,it in awards_on_pages.items():
        for i in it:
            if i == a:
                return n
    return "???"

def title(text,vc=False):
    return colour_print(printer.text_to_ascii(text,vertical_condense=vc))

class AwardsPage(Page):
    def __init__(self, page_num,title="",icon=u"\u263B"):
        super(AwardsPage, self).__init__(page_num)
        self.in_index = False
        self.awards = awards_on_pages[page_num]
        self.title = title
        self.icon = icon

    def generate_content(self):
        import json
        from operator import itemgetter
        data = f_read_json('awards')
        content = title(self.title)
        content += "\n\n"
        for a in self.awards:
            content += award_show(a,data,self.icon)
        self.content = content

class AwardsIndex(Page):
    def __init__(self, page_num):
        super(AwardsIndex, self).__init__(page_num)
        self.title = "Awards & Unawards"
        self.in_index = True
        self.index_num = "450-453"

    def generate_content(self):
        import json
        from operator import itemgetter
        data = f_read_json('awards')
        print data
        content = title("The most awards",True)
        content += "\n\n"
        for a,b in data.items():
            m = 0
            mp = ""
            for person,n in b.items():
                if n > m:
                    m = n
                    mp = person
                elif n==m:
                    mp += " & " + person
            content += "\n"+self.colours.Foreground.GREEN+a+sub_page.colours.Foreground.DEFAULT + " (see page "+str(get_page(a))+") "
            content += sub_page.colours.Foreground.RED + mp + sub_page.colours.Foreground.DEFAULT
        self.content = content


sub_page = AwardsIndex("450")

p1 = AwardsPage("451","Tea Awards")
p2 = AwardsPage("452","Mart Cow Awards")
p3 = AwardsPage("453","Kitchen Awards")
p4 = AwardsPage("454","Other Awards")
p5 = AwardsPage("455","Tea Unawards","o_0")
p6 = AwardsPage("456","Other Unawards","0_o")


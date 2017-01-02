import os
from page import Page
from random import choice
from file_handler import f_read_json

def award_show(self,award, data, icon):
    self.add_text(award,fg="GREEN")
    self.add_newline()
    try:
        winners = data[award]
    except KeyError:
        self.add_text("No-one has won this award yet...")
        self.add_newline()
        self.add_newline()
        return
    max_len = 0
    for person in winners:
        max_len = max(max_len,len(person))
    for person,number in winners.items():
        self.add_text(person)
        self.move_cursor(x=max_len)
        self.add_text("|",fg="RED")
        for i in range(number):
            self.start_random_fg_color()
            self.add_text(icon)
            self.end_fg_color()
        self.add_newline()
    self.add_newline()

awards_on_pages = {
        "451":["Tea Maker","CelebriTEA"],
        "452":["Moo Cow"],
        "453":["Towel Bringer","Squeaky Clean","Spongebob Squarepoints","Cleaning the Bloody Fridge"],
        "454":["Honorary Fire Marshall","Double Noughts and Crosses","Lunchtime Goat Award"],
        "455":["Boo Cow","Tea Wrecks"],
        "456":["Towel Flood","Boo Key","Stolen Pen","Worst Sorting Hat","SNORE-lax","Banana Split","Orange Peel"]
    }

def get_page(a):
    for n,it in awards_on_pages.items():
        for i in it:
            if i == a:
                return n
    return "???"

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
        self.add_title(self.title)
        for a in self.awards:
            award_show(self,a,data,self.icon)

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
        self.add_title("The most awards")
        for a,b in data.items():
            m = 0
            mp = ""
            for person,n in b.items():
                if n > m:
                    m = n
                    mp = person
                elif n==m:
                    mp += " & " + person
            self.add_newline()
            self.add_text(a,fg="GREEN")
            self.add_text(" (see page "+str(get_page(a))+") ")
            self.add_text(mp,fg="RED")


sub_page = AwardsIndex("450")

p1 = AwardsPage("451","Tea Awards")
p2 = AwardsPage("452","Mart Cow Awards")
p3 = AwardsPage("453","Kitchen Awards")
p4 = AwardsPage("454","Other Awards")
p5 = AwardsPage("455","Tea Unawards","o_0")
p6 = AwardsPage("456","Other Unawards","0_o")


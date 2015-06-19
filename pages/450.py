import os
from page import Page
from random import choice
import colours
from colours import colour_print
from printer import instance as printer

page_number = os.path.splitext(os.path.basename(__file__))[0]
sub_page = Page(page_number)
sub_page.title = "Awards"
sub_page.index_num = "450-453"
content = colour_print(
    printer.text_to_ascii("Awards", padding={"left": 6}))

awards = [
          ["Moo Cow Awards",{"Adam Townsend":3,"Matthew Scroggs":2,"Belgin Seymenoglu":4,"Matthew Wright":2,"Stephen Muirhead":1,"Olly Southwick":2,"Shredder":1,"Pietro Servini":1}],
          ["Tea Maker Awards",{"Matthew Scroggs":5,"Matthew Wright":5,"Pietro Servini":1,"Peter (who?)":1}],
          ["CelebriTEA",{"Matthew Wright":1,"Matthew Scroggs":1}],
          ["Honorary Fire Marshal",{"Rafael \"Bruce\" Prieto Curiel":1}],
          ["Double Noughts and Crosses",{"Belgin Seymenoglu":1}]
         ]
pages = ["452","451","451","453","453"]

content += "\nWho has the most awards?\n\n"

for i,award in enumerate(awards):
    content += "\n"+sub_page.colours.Foreground.GREEN+award[0]+sub_page.colours.Foreground.DEFAULT+" (see page "+pages[i]+")\n"
    max_ = 0
    max_p = None
    for person,number in award[1].items():
        if number>max_:
            max_p = person
            max_ = number
        elif number==max_:
            max_p = max_p+","+person
    if max_p is not None:
        content += "  " + max_p + "\n"
sub_page.content = content

def award_show(award):
    content = colours.Foreground.GREEN+award[0]+colours.Foreground.DEFAULT+"\n"
    max_len = 0
    for person in award[1]:
        max_len = max(max_len,len(person))
    for person,number in award[1].items():
        content += person + (" "*(max_len-len(person)))
        content += sub_page.colours.Foreground.RED+"|"+sub_page.colours.Foreground.DEFAULT
        for i in range(number):
            content += choice(sub_page.colours.Foreground.non_boring)
            content += u"\u263A"+sub_page.colours.Foreground.DEFAULT
        content += "\n"
    return content

def title(text):
    return colour_print(printer.text_to_ascii(text))

tea_page = Page("451")
tea_page.content = title("Tea Awards") + "\n\n" + award_show(awards[1]) + "\n" + award_show(awards[2])
tea_page.in_index = False

moo_page = Page("452")
moo_page.content = title("Moo Cow Awards") + "\n\n" + award_show(awards[0])
moo_page.in_index = False

oth_page = Page("453")
oth_page.content = title("Other Awards") + "\n\n" + award_show(awards[3]) + "\n" + award_show(awards[4])
oth_page.in_index = False

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
          ["Mart Cow Awards",{"Adam Townsend":4,"Matthew Scroggs":2,
           "Belgin Seymenoglu":13,"Matthew Wright":6,"Stephen Muirhead":3,
           "Olly Southwick":10,"Shredder":1,"Pietro Servini":1,"Anna Lambert":1,
           "Rafael Preito Curiel":1}],
          ["Tea Marter Awards",{"Matthew Scroggs":9,"Matthew Wright":18,"Pietro Servini":1,
           "Peter (who?)":1,"Olly Southwick":2,"Belgin Seymenoglu":1,
           "Rafael Prieto Curiel":1}],
          ["CelebriTEA",{"Matthew Wright":2,"Matthew Scroggs":1,"Oliver Southwick":1},unichr(9829)],
          ["Honorary Fire Martshal",{"Rafael \"Bruce\" Prieto Curiel":1}],
          ["Double Noughts and Crosses",{"Belgin Seymenoglu":1}],
          ["Towel Bringer",{"Huda Ramli":2,"Belgin Seymenoglu":1}],
          ["Lunchtime Goat Award",{"Olly Southwick":1}],
          ["Squeaky Clean",{"Huda Ramli":1,"Rafael \"Bruce\" Prieto Curiel":2,"Belgin Seymenoglu":2}],
          ["Spongebob Squarepoints",{"Rafael Prieto Curiel":1}],
          ["Cleaning the Bloody Fridge",{"Matthew Scroggs":1}]
         ]
pages = ["452","451","451","454","454","453","454","453","453","453"]

content += "\nWho has the most awards?\n\n"

for i,award in enumerate(awards):
    content += "\n"+sub_page.colours.Foreground.GREEN+award[0]+sub_page.colours.Foreground.DEFAULT+" (see page "+pages[i]+") "
    max_ = 0
    max_p = None
    for person,number in award[1].items():
        if number>max_:
            max_p = person
            max_ = number
        elif number==max_:
            max_p = max_p+","+person
    if max_p is not None:
        content += sub_page.colours.Foreground.RED + max_p + sub_page.colours.Foreground.DEFAULT
sub_page.content = content

def award_show(award):
    content = colours.Foreground.GREEN+award[0]+colours.Foreground.DEFAULT+"\n"
    max_len = 0
    try:
        icon = award[2]
    except:
        icon = u"\u263B"
    for person in award[1]:
        max_len = max(max_len,len(person))
    for person,number in award[1].items():
        content += person + (" "*(max_len-len(person)))
        content += sub_page.colours.Foreground.RED+"|"+sub_page.colours.Foreground.DEFAULT
        for i in range(number):
            content += choice(sub_page.colours.Foreground.non_boring)
            content += icon+sub_page.colours.Foreground.DEFAULT
        content += "\n"
    return content

def title(text):
    return colour_print(printer.text_to_ascii(text))

tea_page = Page("451")
tea_page.content = title("Tea Awards") + "\n\n" + award_show(awards[1]) + "\n" + award_show(awards[2])
tea_page.in_index = False

moo_page = Page("452")
moo_page.content = title("Mart Cow Awards") + "\n\n" + award_show(awards[0])
moo_page.in_index = False

kit_page = Page("453")
kit_page.content = title("Kitchen Awards") + "\n\n" + award_show(awards[5]) + "\n" + award_show(awards[7]) + "\n" + award_show(awards[8]) + "\n" + award_show(awards[9])
kit_page.in_index = False

oth_page = Page("454")
oth_page.content = title("Other Awards") + "\n\n" + award_show(awards[3]) + "\n" + award_show(awards[4]) + "\n" + award_show(awards[6])
oth_page.in_index = False

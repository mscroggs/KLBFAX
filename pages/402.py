import os
from page import Page
from random import choice
from colours import colour_print
from printer import instance as printer

page_number = os.path.splitext(os.path.basename(__file__))[0]
sub_page = Page(page_number)
sub_page.title = "Awards"
content = colour_print(
    printer.text_to_ascii("Awards", padding={"left": 6}))

awards = [
          ["Moo Cow Awards",{"Adam Townsend":3,"Matthew Scroggs":1,"Belgin Seymenoglu":4,"Matthew Wright":2,"Stephen Muirhead":1}],
          ["Tea Maker Awards",{"Matthew Scroggs":4,"Matthew Wright":3,"Pietro Servini":1}],
          ["CelebriTEA",{"Matthew Wright":1}],
          ["Honorary Fire Marshal",{"Rafael \"Bruce\" Prieto Curiel":1}],
          ["Double Noughts and Crosses",{"Belgin Seymenoglu":1}]
         ]

for award in awards:
    content += "\n"+sub_page.colours.Foreground.GREEN+award[0]+sub_page.colours.Foreground.DEFAULT+"\n"
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
sub_page.content = content

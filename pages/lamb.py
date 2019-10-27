# -*- coding: utf-8 -*-
from page import Page
import config

class LambPage(Page):
    def __init__(self, page_num):
        super(LambPage, self).__init__(page_num)
        self.title = "Jackson Lamb novel"
        self.in_index = True
        self.tagline = "Another tale from the inimitable chronicles of Jackson Lamb"
        pages.append([page_num,"Jackson Lamb novel"])


    def generate_content(self):

        def width_of_word(word):
            width = len(word)*5 \
            - sum(map(word.count, u"!:,‘’.'I’"))*3 \
            - sum(map(word.count, u"-()1"))*2 \
            - sum(map(word.count, u"T"))*1 \
            + sum(map(word.count, u"MW"))*1 \
            - sum(map(word.count, u"il"))*3 \
            - sum(map(word.count, u"fjt"))*2 \
            - sum(map(word.count, u"abcdeghknopqrsuvxyz"))*1 \
            + sum(map(word.count, u"mw"))*1
            return width

        def center_pad(center,chars_left):
            if center:
                return ((chars_left+2)//2)*"|"
            else:
                return ""

        def add_title_wrapped(text,max_width=config.WIDTH,bg="YELLOW",fg="BLACK",font="size4",fill=True,pre=0,center=False):
            chars_left = max_width
            line = ""
            #self.move_cursor(y=y,x=x)
            text = text.split(" ")
            first_line = True
            for word in text:
                if (chars_left - width_of_word(word) <= 0) and not first_line:
                    # Print old line and start new line.
                    self.add_title(center_pad(center,chars_left) + line[:-1],bg=bg,fg=fg,font=font,fill=fill,pre=pre)
                    chars_left = max_width
                    line = word + " "
                else:
                    # Add word to line
                    line = line + word + " "
                    first_line = False
                chars_left = chars_left - width_of_word(word) - 3
            # Print final line.
            self.add_title(center_pad(center,chars_left) + line[:-1],bg=bg,fg=fg,font=font,fill=fill,pre=pre)

        # Pick randomly
        import random
        titles = [
        'Slow Horses',
        'Dead Lions',
        'Real Tigers',
        'Stoned Pigeons',
        'Spooky Street',
        'London Rules',
        'Joe Country',
        'Quantum Lamb',
        'Mining Lamb',
        'Regle du Jeu',
        'Tidal Lamb',
        'Et tu, Lamb',
        'Bravo, Lamb',
        'Curse of Lamb',
        'Don\'t fail me Lamb',
        'Son of a Lamb',
        'Mackerel Lamb',
        'Anatomy Lamb',
        'Lamb in Time',
        'Outback Lamb',
        'Sacred Texts',
        'That\'s it. Finished',
        'Return of Lamb',
        'Lamb\'s Ressurection',
        'Baa-baa braLamb',
        'Grand\'s Lamb',
        'Lamb & Pineapple',
        'Look of Lamb',
        'Casino RoyLamb',
        'Money Penny Goes for Lamb',
        'Le Chiffre\'s Torture of the Lamb',
        'Home James, Don\'t Spare the Lamb',
        'Sir James\' Trip to Find Lamb',
        'Look of Lamb (Instrumental)',
        'Hi There Miss GoodLamb',
        'Little French Lamb',
        'Flying Lamb',
        'The Venerable Sir Jackson Lamb',
        'Dream on Lamb, You\'re Lamb',
        'The Big Cowboys and Lamb Fight at Casino RoyLamb',
        'Casino RoyLamb (Reprise)',
        'Lamb Korma',
        'Lamb Passanda',
        'Lamb Tikka Masala',
        'Lamb Dhansak',
        'Lamb Jalfrezi',
        'Lamb Madras',
        'Lamb Vindaloo',
        'Lamb Phall',
        'Fireman Lamb',
        'Green Eggs and Lamb',
        'Lambda',
        'Lady Di Another Day',
        'Lambourine',
        'Lambalaya',
        'Lambagotchi',
        'Lamb.de',
        'Lambp post',
        'Finlamd',
        'Irelamb'
        ]
        chosen_book = random.choice(titles)

        self.add_title("Slice of Lamb",font="size4",fg="ORANGE",bg="BRIGHTWHITE")

        book_width = 41
        book_height = 42
        top_margin = 5
        left_margin = (config.WIDTH-book_width)//2

        book = "x"*book_width + "\n" + ("x" + "-"*(book_width-2) + "x" + "\n")*(book_height-2) + "x"*book_width + "\n"
        book=(book).replace(" ","-").replace("x","W")
        color = random.choice(['g','r','o','c','b','m','R','y','G','C','B','p'])
        self.print_image(book.replace('g',color),top_margin,left_margin) #y,x)

        spy=(
'''-----xxxxxxx-----
----xxxxxxxxx----
----xxxxxxxxx----
xxxxxxxxxxxxxxxxx
-----------------
----ggggggggg----
----gggg-gggg----
----gggg-gggg----
-----------------
-xx-----------xx-
-xxxx-------xxxx-
-xxxxxx---xxxxxx-
-xxxxxx---xxxxxx-
xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxx''').replace(" ","-").replace("x","W")
        self.print_image(spy.replace('g',color),top_margin+2,left_margin+12) #y,x)

        author = "M I C K   H E R R O N"
        self.move_cursor(x=left_margin+book_width//2-len(author)//2,y=top_margin+book_height//2 - 10)
        self.add_text(author)
        self.move_cursor(x=left_margin+2,y=top_margin+book_height//2 - 9)
        #chosen_book_words = chosen_book.split(" ")
        add_title_wrapped(chosen_book.upper(),font="size4",fg="BLACK",bg="BRIGHTWHITE",pre=left_margin+2,fill=False,max_width=book_width-4,center=True)
        #self.add_title(chosen_book_words[1].upper(),font="size4",fg="BLACK",bg="BRIGHTWHITE",pre=left_margin+2,fill=False)
pages = []

# Departures
lamb01 = LambPage("181")
lamb01.importance=4

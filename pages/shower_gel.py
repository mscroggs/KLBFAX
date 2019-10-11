# -*- coding: utf-8 -*-
from page import Page
import config

class ShowerGelPage(Page):
    def __init__(self, page_num):
        super(ShowerGelPage, self).__init__(page_num)
        self.title = "Shower gel"
        self.in_index = True
        self.tagline = "FREE Shower puff when you spend OVER £10"
        pages.append([page_num,"Shower gel"])


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
        outer = [
        ['the','kiss'],
        ['my','island'],
        ['marsh','hearts'],
        ['her','thoughts'],
        ['one','morning'],
        ['','love'],
        ['that','moment'],
        ['sweet','zing'],
        ['fresh','tingle'],
        ['the','secret'],
        ['gentle','love'],
        ['water','splash'],
        ['fizzy','party'],
        ['wild','magic'],
        ['slow','horses'],
        ['neutral','hotel'],
        ['crazy','horses']
        ]
        inner = [
        'raspberry',
        'coconut',
        'mallow',
        'mango',
        'ginger',
        'brazilian',
        'vanilla',
        'lime',
        'mint',
        'honeycomb',
        'powder',
        'melon',
        'prosecco',
        'cherry',
        'milk'
        ]

        chosen_outer = random.choice(outer)
        chosen_inner = random.choice(inner)

        self.add_title("Shower gel",font="size4",fg="ORANGE",bg="BRIGHTWHITE")

        book_width = 41
        book_height = 29
        top_margin = 11
        left_margin = (config.WIDTH-book_width)//2

        book = "x"*book_width + "\n" + ("x" + "-"*(book_width-2) + "x" + "\n")*(book_height-2) + "x"*book_width + "\n"
        book=(book).replace(" ","-").replace("x","W")
        color = random.choice(['g','r','o','c','b','m','R','y','G','C','B','p'])
        self.print_image(book.replace('g',color),top_margin,left_margin) #y,x)

        top=(
'''---------------ggggggggggg---------------
--------------ggggggggggggg--------------
--------------ggggggggggggg--------------
--------------ggggggggggggg--------------
--------------ggggggggggggg--------------
--------------ggggggggggggg--------------
--------------ggggggggggggg--------------
--------------ggggggggggggg--------------
-----------------------------------------
--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--
-x-------------------------------------x-
x---------------------------------------x
''').replace(" ","-").replace("x","W")
        self.print_image(top.replace('g',color),top_margin-5,left_margin) #y,x)

        self.move_cursor(x=left_margin+2,y=top_margin+book_height//2 - 13)
        add_title_wrapped(chosen_outer[0],font="size4",fg="BLACK",bg="BRIGHTWHITE",pre=left_margin+2,fill=False,max_width=book_width-4,center=True)
        self.move_cursor(x=left_margin+2,y=top_margin+book_height//2 - 9)
        add_title_wrapped(chosen_inner,font="size4",fg="BLACK",bg=color,pre=left_margin+2,fill=False,max_width=book_width-4,center=True)
        self.move_cursor(x=left_margin+2,y=top_margin+book_height//2 - 5)
        add_title_wrapped(chosen_outer[1],font="size4",fg="BLACK",bg="BRIGHTWHITE",pre=left_margin+2,fill=False,max_width=book_width-4,center=True)
pages = []

# Departures
lamb01 = ShowerGelPage("179")
lamb01.importance=4

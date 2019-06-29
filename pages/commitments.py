# -*- coding: utf-8 -*-
from page import Page
import config

class CommitmentsPage(Page):
    def __init__(self, page_num):
        super(CommitmentsPage, self).__init__(page_num)
        self.title = "The Ten Commitments"
        self.in_index = True
        self.tagline = "CONGRATULATIONS!!! YOU DID IT."
        pages.append([page_num,"Ten Commitments"])


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
        'Lifestyle is in all segments of our live an important brick.',
        'WEAR COMFORTABLE CLOTHES !!!',
        'feel it, in which mood you are, be yourself ,be ONE UNIQUE INDIVIDUAL.',
        'Go before you are starting your work 15 min earlier and visit a park look around',
        'Often we are forgetting in the a/w time about the nature',
        'All of us are more or less a kind of lazy human beings',
        'the 100% guarantee after 15 min slow run is detectable.',
        'the next step is,be continuously make your plan.',
        'the daily Qn (How are you-answer I am fine thank you) is a kind of culture-commitm\'t',
        'mostly the whole bubble would be gone when you are on the right side of the river.'
        ]
        book_index = random.randint(0,len(titles)-1)
        chosen_book = titles[book_index]
        num_lines = [4,3,5,5,4,4,4,3,5,5][book_index]

        commitment_num = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"][book_index]
        add_title_wrapped("Commitment " + commitment_num,font="size4",fg="BLACK",bg="LIGHTRED",center=True)

        book_width = 76
        scrollbar_width = 3
        book_height = 43
        top_margin = 5
        left_margin = (config.WIDTH-book_width)//2

        book = "x"*book_width + "\n" + ("x" + "-"*scrollbar_width + "x" + "-"*(book_width-2-2*scrollbar_width-2) + "x" + "-"*scrollbar_width + "x" + "\n")*(book_height-2) + "x"*book_width + "\n"
        book=(book).replace(" ","-").replace("x","W")
        color = random.choice(['g','r','o','c','b','m','R','y','G','C','B','p'])
        self.print_image(book.replace('g',color),top_margin,left_margin) #y,x)

        scroll_top=(
'''--x--
xxxxx
-xxx-
xxxxx''').replace(" ","-").replace("x","W")
        scroll_bottom=(
'''WWWWW
ggggg''').replace(" ","-").replace("x","W")
        self.print_image(scroll_top.replace('W',color),top_margin-2,left_margin+0) #y,x)
        self.print_image(scroll_top.replace('W',color),top_margin-2,left_margin+book_width-scrollbar_width-2) #y,x)
        self.print_image(scroll_bottom.replace('g',color),top_margin+book_height//2,left_margin+0) #y,x)
        self.print_image(scroll_bottom.replace('g',color),top_margin+book_height//2,left_margin+book_width-scrollbar_width-2) #y,x)

        self.move_cursor(x=left_margin+2,y=top_margin+1 + int((5-num_lines)*2)) # book_height//2 - 9
        add_title_wrapped(chosen_book,font="size4",fg="BLACK",bg="BRIGHTWHITE",pre=left_margin+2+scrollbar_width,fill=False,max_width=book_width-4-2*scrollbar_width,center=True)
pages = []

# Departures
commitment1 = CommitmentsPage("182")
commitment1.importance=4

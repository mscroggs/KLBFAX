import os
import json
from page import Page
from random import choice
from os.path import join, expanduser
from file_handler import f_read, f_readlines, open_local
import config

class LetterPage(Page):
    def __init__(self, page_num,n):
        super(LetterPage, self).__init__(page_num)
        self.title = "Letters"
        self.in_index = False
        self.n = n
        self.tagline = "Email klbscroggsbot@gmail.com and your letter will appear here"
        self.letters = ""

    def background(self):
        self.letters = f_read("emails")
        if config.NAME == "KLBFAX" and self.n==1 and config.has_gmail_login():
            import gmail
            details = f_readlines("gmail")

            g = gmail.login(details[0],details[1])
            unread = g.inbox().mail(unread=True)
            for mail in unread:
                mail.fetch()
                lines = "".join(mail.body.split("\r")).split("\n")
                if lines[0] == "EVENT" and "matthew.scroggs.14@ucl.ac.uk" in mail.fr:
                    try:
                        with open_local('events','a') as f:
                            for line in lines:
                                if line!="EVENT":
                                    f.write(line+"\n")
                        mail.read()
                    except:
                        pass
                elif lines[0] == "CARD" and "matthew.scroggs.14@ucl.ac.uk" in mail.fr:
                    with open('/home/pi/cards/'+lines[1],"w") as f:
                        f.write("\n".join(lines[2:]))
                    mail.read()
                elif "POINTS" in lines[0].upper() and "belgin.seymenoglu.10@ucl.ac.uk" in mail.fr:
                    from points import add_points
                    length = 1
                    points_to_give = 0
                    while length<=len(lines[2]):
                        try:
                            if lines[2][:length]!="-":
                                points_to_give = int(lines[2][:length])
                            length += 1
                        except:
                            break
                    add_points(lines[1].split("=")[0],points_to_give)
                    mail.read()
    
                else:
                    newletter = ""
                    for line in lines:
                        if line!="":
                            while len(line)>79:
                                newletter += line[:79]+"\n"
                                line=line[79:]
                            newletter+=line+"\n"
    
                    self.letters=newletter+"\n"+"from "+mail.fr+"\n\n"+self.letters
                    mail.read()
            self.letters = self.letters.split("\n")
            if len(self.letters)>1000:
                self.letters = self.letters[:1000]
            with open_local("emails","w") as f:
                f.write("\n".join(self.letters))
        else:
            self.letters = self.letters.split("\n")


    def generate_content(self):
        letters = self.letters[20*(self.n-1):20*self.n]
        letters = "\n".join(letters)
        letters = unicode(letters,'latin1')


        self.add_title("Have your say",font="size4")
        a = str(self.n)+"/21"
        self.move_cursor(x=90-len(a))
        self.add_text(a, fg="BLUE", bg="YELLOW")
        self.move_cursor(x=0)
        self.start_random_bg_color()
        for line in letters.split("\n"):
            line = line.rstrip("\n")
            if line == "":
                self.end_bg_color()
                self.start_random_bg_color()
            self.add_text(line,fg="BLACK")
            self.add_newline()
        self.end_bg_color()
        if self.n==21:
            self.add_text("~ END OF LETTERS ~")
        else:
            self.add_text("The letters continue on page "+str(200+self.n))

letters_page1 = LetterPage("200",1)
letters_page1.in_index = True
letters_page1.index_num = "200-220"
letters_page2 = LetterPage("201",2)
letters_page3 = LetterPage("202",3)
letters_page4 = LetterPage("203",4)
letters_page5 = LetterPage("204",5)
letters_page6 = LetterPage("205",6)
letters_page7 = LetterPage("206",7)
letters_page8 = LetterPage("207",8)
letters_page9 = LetterPage("208",9)
letters_page10 = LetterPage("209",10)
letters_page11 = LetterPage("210",11)
letters_page12 = LetterPage("211",12)
letters_page13 = LetterPage("212",13)
letters_page14 = LetterPage("213",14)
letters_page15 = LetterPage("214",15)
letters_page16 = LetterPage("215",16)
letters_page17 = LetterPage("216",17)
letters_page18 = LetterPage("217",18)
letters_page19 = LetterPage("218",19)
letters_page20 = LetterPage("219",20)
letters_page21 = LetterPage("220",21)

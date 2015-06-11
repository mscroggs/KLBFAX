import os
import json
from page import Page
from random import choice

class LetterPage(Page):
    def __init__(self, page_num,n):
        super(LetterPage, self).__init__(page_num)
        self.title = "Letters"
        self.in_index = False
        self.n = n
        self.tagline = "Email klbscroggsbot@gmail.com and your letter will appear here"


    def generate_content(self):

        import gmail
        from os.path import join, expanduser

        details = []
        with open(join(expanduser("~"),".klb/gmail")) as f:
            for line in f.readlines():
                details.append(line.strip("\n"))

        g = gmail.login(details[0],details[1])


        unread = g.inbox().mail(unread=True)

        with open(join(expanduser("~"),".klb/emails")) as f:
            letters = f.read()

        for mail in unread:
            mail.fetch()
            lines = "".join(mail.body.split("\r")).split("\n")
            if lines[0] == "EVENT" and "matthew.scroggs.14@ucl.ac.uk" in mail.fr:
                try:
                    with open(join(expanduser("~"),'.klb/events'),'a') as f:
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
                newletter_col = choice(self.colours.Background.non_boring)
                newletter = ""
                for line in lines:
                    if line!="":
                        while len(line)>79:
                            newletter += newletter_col+line[:79]+"\n"
                            line=line[79:]
                        newletter+=newletter_col+line+"\n"

                letters=newletter+"\n"+newletter_col+self.colours.Foreground.BLACK+"from "+mail.fr+self.colours.Foreground.DEFAULT+self.colours.Background.DEFAULT+"\n\n"+letters
                mail.read()

        letters = letters.split("\n")
        if len(letters)>1000:
            letters = letters[:1000]
        with open(join(expanduser("~"),".klb/emails"),"w") as f:
            f.write("\n".join(letters))
        letters = letters[24*(self.n-1):24*self.n]
        letters = "\n".join(letters)


        page = self.colours.Foreground.RED+"LETTERS"+self.colours.Foreground.DEFAULT+"\n"
        page += letters+self.colours.Foreground.DEFAULT+self.colours.Background.DEFAULT
        page += "\n\n"
        page += "The letters continue on page "+str(200+self.n)
        self.content = page.decode('latin-1')

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

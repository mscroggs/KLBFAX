import os
import json
from page import Page
from random import choice

class LetterPage(Page):
    def __init__(self, page_num):
        super(LetterPage, self).__init__(page_num)
        self.title = "Letters"

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
                    f.write(lines[2])
                mail.read()
            elif lines[0] == "POINTS" and "belgin.seymenoglu.10@ucl.ac.uk" in mail.fr:
                from points import add_points
                length = 1
                points_to_give = 0
                while True:
                    try:
                        points_to_give = int(lines[2][:length])
                        length += 1
                    except:
                        break
                add_points(lines[1].split("=")[0],points_to_give)
                mail.read()

                from twitter import update_status
                update_status(status=lines[2]+" points to "+lines[1]+"!")

            else:
                newletter = choice(self.colours.Background.non_boring)
                for line in lines:
                    if line!="":
                        while len(line)>79:
                            newletter += line[:79]+"\n"
                            line=line[79:]
                        newletter+=line+"\n"

                letters=newletter+"\n"+self.colours.Foreground.BLACK+"from "+mail.fr+self.colours.Foreground.DEFAULT+self.colours.Background.DEFAULT+"\n\n"+letters
                mail.read()

        letters = letters.split("\n")
        if len(letters)>100:
            letters = letters[:100]
        letters = "\n".join(letters)

        with open(join(expanduser("~"),".klb/emails"),"w") as f:
            f.write(letters)

        page = self.colours.Foreground.RED+"LETTERS"+self.colours.Foreground.DEFAULT+"\n"+letters
        self.content = page.decode('latin-1')

page_number = os.path.splitext(os.path.basename(__file__))[0]

letters_page = LetterPage(page_number)
letters_page.tagline = ("Email klbscroggsbot@gmail.com and your letter will "
                        "appear here")

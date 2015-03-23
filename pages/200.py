import os
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
                    with open('/var/www/klb/events','a') as f:
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
            else:
                newletter = choice(self.colours.Background.list)
                for line in lines:
                    if line!="":
                        while len(line)>79:
                            newletter += line[:79]+"\n"
                            line=line[79:]
                        newletter+=line+"\n"

                letters=newletter+"\n"+self.colours.Foreground.YELLOW+"from "+mail.fr+"\n"+self.colours.Foreground.DEFAULT+self.colours.Background.DEFAULT+letters
                mail.read()

        letters = letters.split("\n")
        if len(letters)>100:
            letters = letters[:100]
        letters = "\n".join(letters)

        with open(join(expanduser("~"),".klb/emails"),"w") as f:
            f.write(letters)

        page = self.colours.Foreground.RED+"LETTERS"+self.colours.Foreground.DEFAULT+"\n"+letters
        self.content = page

page_number = os.path.splitext(os.path.basename(__file__))[0]

letters_page = LetterPage(page_number)
letters_page.tagline = ("Email klbscroggsbot@gmail.com and your letter will "
                        "appear here")

from page import Page
from random import shuffle

class PolybPage(Page):
    def __init__(self, page_num):
        super(PolybPage, self).__init__(page_num)
        self.title = "Jobs"
        self.index_num = "170-184"
        #self.importance = 5

    def generate_content(self):
        self.add_title("Polybius",fg="BLACK",bg="ORANGE")
        self.add_title("   Biotech",fg="BLACK",bg="ORANGE")
        biotech_logo =("oo----------------oo\n"
                       "oooo------------oooo\n"
                       "--oooo--------oooooo\n"
                       "----oooo----oooo--oo\n"
                       "------oooooooo----oo\n"
                       "--------oooo------oo\n"
                       "------------------oo\n"
                       "------------------oo\n"
                       "----------------oooo\n"
                       "--------------oooooo\n"
                       "oo----------oooo----\n"
                       "oo--------oooo------\n"
                       "oo--------oo--------\n"
                       "oo--------oo--------\n"
                       "oo--------oo--------\n"
                       "oooo------oo--------\n"
                       "--oooo----oo--------\n"
                       "----oooo--oo--------\n"
                       "------oooooo--------\n"
                       "--------oooo--------")
        self.print_image(biotech_logo,2,59)

        messages = ["No employee of Polybius Biotech has even been described as \"unhappy\", \"wanting  to quit\" or \"still capable of independent thought\".",
                    "It been over 20 days since an Polybius Biotech employee has been accidentally   liquidised.",
                    "Your work at Polybius Biotech will involve <--REDACTED-->.",
                    "Before interview, successful applicants are required to sign form 3.7 and allow Polybius Biotech to detain them in the event of their interview being           indefinitely delayed.",
                    "Due to loopholes in law 13.7.4, all work at Polybius Biotech is strictly legal.",
                    "No employee of Polybius Biotech shall be required to deliberately harm large    groups of citizens.",
                    "All employeed of Polybius Biotech shall be provided with a prototype \"RoboDog\"  autonomous peacekeeping unit.",
                    "All applicants should carefully read <--REDACTED--> in full before presenting   themselves for interview.",
                    "Employees at Polybius Biotech shall be provided with <--REDACTED-->.",
                    "Current employees of Polybius Biotech have described their experience at the    company as \"a positive experience\" and \"<--REDACTED-->\"",
                    "Applying to work at Polybius Biotech will have a positive effect on the life    expectancy of your kin.",
                    "There is no need to fear the <--REDACTED--> that lives in the Polybius Biotech  laboratory complex.",
                    "Applying to work at Polybius Biotech is the first step in your journey towards  improving life.",
                    "Contrary to rumours, Polybius Biotech has never been found guilty of causing    citizens to suffer from <--REDACTED-->."
                ]
        self.add_newline()
        self.add_newline()
        self.add_newline()
        shuffle(messages)
        self.add_wrapped_text("Applications to work at Polybius BioTech are now open.", fg="BRIGHTWHITE")
        c = "ORANGE"
        for m in messages[:5]:
            self.add_newline()
            self.add_newline()
            ls = m.split("<--REDACTED-->")
            for i,text in enumerate(ls):
                self.add_wrapped_text(text, fg=c)
                if i < len(ls)-1:
                    self.add_wrapped_text("<--REDACTED-->",fg="RED")
            if c == "WHITE":
                c = "ORANGE"
            else:
                c = "WHITE"


#page = PolybPage("170")

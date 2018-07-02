from page import Page
from random import choice


class JokePage(Page):
    def __init__(self,page_num):
        super(JokePage, self).__init__(page_num)
        self.title = "The 10 Commitments"
        self.tagline = "CONGRATULATIONS !!! YOU DID IT."

    def generate_content(self):
        self.add_title("The 10 commitments", font="size4")

        self.add_wrapped_text("1. Lifestyle is in all segments of our live an important brick.")
        self.add_newline()
        self.add_newline()
        self.add_wrapped_text("2. WEAR COMFORTABLE CLOTHES !!!")
        self.add_newline()
        self.add_newline()
        self.add_wrapped_text("3. feel it, in which mood you are, be yourself ,be ONE UNIQUE INDIVIDUAL.")
        self.add_newline()
        self.add_newline()
        self.add_wrapped_text("4. Go before you are starting your work 15 min earlier and visit park look around")
        self.add_newline()
        self.add_newline()
        self.add_wrapped_text("5. Often we are forgetting in the a/w time about the nature")
        self.add_newline()
        self.add_newline()
        self.add_wrapped_text("6. All of are are more or less a kind of lazy human beings")
        self.add_newline()
        self.add_newline()
        self.add_wrapped_text("7. the 100 % guarantee after 15 min slow run is detectable.")
        self.add_newline()
        self.add_newline()
        self.add_wrapped_text("8. the next step is,be continuously make your plan.")
        self.add_newline()
        self.add_newline()
        self.add_wrapped_text("9. the daily question (How are you-answer I am fine thank you) is a kind of culture-commitment")
        self.add_newline()
        self.add_newline()
        self.add_wrapped_text("10. mostly the whole bubble would be gone, when you are on the right side of the river.")




jokepage = JokePage("113")

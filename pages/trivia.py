import os
from page import Page
from ceefax import Ceefax
from random import choice
import config

class TriviaPage(Page):
    def __init__(self, n):
        super(TriviaPage, self).__init__(n)
        self.title = "Trivia"

    def generate_content(self):
        questions = [
                    ("What is 1+2?","3"),
                    ("Which is the best village at EMF?","The maths village"),
                    ]
        self.add_title("Trivia")
        for i in range(4):
            q,a = choice(questions)
            self.add_text(q)
            self.add_newline()
            self.add_reveal_text("    "+a,fg="YELLOW")
            self.add_newline()
            self.add_newline()
        self.add_text("Press G to REVEAL ANSWERS", fg="GREEN") # TODO: replace this with +

trivia = TriviaPage("108")

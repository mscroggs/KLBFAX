import os
from page import Page
from ceefax import Ceefax
from random import shuffle
import config

class TriviaPage(Page):
    def __init__(self, n):
        super(TriviaPage, self).__init__(n)
        self.title = "Trivia"

    def generate_content(self):
        questions = [
                    ("What is 1+2?","3"),
                    ("Which is the best village at EMF?","The maths village"),
                    ("Who starred in the 1967 James Bond spoof film Casino Royale?","David Niven, Peter Sellers, Woody Allen, and Orson Welles as \"Le Chiffre\""),
                    ("Which programming language is EMFFAX programmed using?","Python"),
                    ]
        shuffle(questions)
        self.add_title("Trivia")
        for i in range(4):
            self.add_newline()
            q,a = questions[i]
            self.add_text(q)
            self.add_newline()
            self.add_reveal_text("    "+a,fg="YELLOW")
            self.add_newline()
        self.add_newline()
        self.add_text("Press G to REVEAL ANSWERS", fg="GREEN") # TODO: replace this with +

trivia = TriviaPage("108")

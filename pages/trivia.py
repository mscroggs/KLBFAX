import os
from page import Page
from ceefax import Ceefax
from random import shuffle
import config

class TriviaPage(Page):
    def __init__(self, n, questions, title):
        super(TriviaPage, self).__init__(n)
        self.title = title
        self.questions = questions

    def generate_content(self):
        shuffle(self.questions)
        self.add_title("Trivia")
        for q,a in self.questions[:5]:
            self.add_newline()
            self.add_text(q)
            self.add_newline()
            self.add_reveal_text("    "+a,fg="YELLOW")
            self.add_newline()
        self.add_newline()
        self.add_text("Press G to REVEAL ANSWERS", fg="GREEN") # TODO: replace this with +

trivia = TriviaPage("101", [
                    ("What is 1+2?","3"),
                    ("Which is the best village at EMF?","The maths village"),
                    ("Who starred in the 1967 James Bond spoof film Casino Royale?","David Niven, Peter Sellers, Woody Allen, and Orson Welles as \"Le Chiffre\""),
                    ("Which programming language is " + config.NAME + " programmed using?","Python"),
                    ], "Trivia")

trivi2 = TriviaPage("339", [
                    ("Who released the albums Everything Must Go and Generation Terrorists?","Manic Street Preachers"),
                    ("Which band had members John, Paul, George and Ringo?","The Beatles"),
                    ("Which band's hits include Enola Gay, Messages and Souvenir?","Orchestral Manoeuvres in the Dark"),
                    ("Which New Zealand duo were the stars of a HBO TV series?","Flight of the Conchords"),
                    ("What is Reginald Kenneth Dwight better known as?","Elton John"),
                    ("What is James Blunt's real name?","James Blunt"),
                    ("Who wasn't it?","Shaggy"),
                    ], "Music Trivia")

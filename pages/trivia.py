from page import Page
from random import shuffle
import config

class TriviaPage(Page):
    def __init__(self, n, questions, title):
        super(TriviaPage, self).__init__(n)
        self.title = title
        self.questions = questions

    def generate_content(self):
        shuffle(self.questions)
        self.add_title(self.title)
        for q,a in self.questions[:5]:
            self.add_newline()
            self.add_wrapped_text(q)
            self.add_newline()
            self.add_reveal_text("    "+a,fg="YELLOW")
            self.add_newline()
        self.add_newline()
        self.add_text("Press + to REVEAL ANSWERS", fg="GREEN")

trivia = TriviaPage("101", [
                    ("What is 1+2?","3"),
                    ("Which is the best village at EMF?","The maths village"),
                    ("Who starred in the 1967 James Bond spoof film Casino Royale?","David Niven, Peter Sellers, Woody Allen, and Orson Welles as \"Le Chiffre\""),
                    ("Which programming language is " + config.NAME + " programmed using?","Python"),
                    ("Where was the first Electromagnetic Field held?","Pineham Park, near Milton Keynes"),
                    ("How many kings of England have been called Ian?","None"),
                    ("What species is Star Wars character Chewbacca?","Wookiee"),
                    ("Who presented The Generation Game, The Price Is Right and Play Your Cards Right?","Bruce Forsyth"),
                    ("Which TV show centred around the characters Rodney and Del Boy?","Only Fools and Horses"),
                    ("What are the ingredients of Tschunk?","Club Mate, Rum, Lime, Sugar"),
                    ("How many Platonic solids are there?","Five"),
                    ("What voltage is mains power in the UK?","230V (AC)"),
                    ("Which festival is an anagram of \"A clefted metro ceiling\"?","Electromagnetic Field"),
                    ("Who piloted Thunderbird 1?","Scott Tracy"),
                    ("Which indestructible character battled the Mysterons?","Captain Scarlet"),
                    ("Who wrote the books Animal Farm and 1984?","George Orwell"),
                    ("Which Pokemon wears its mother's skull?","Cubone"),
                    ("What town was Schubert built in?","Schubert was born in Vienna"),
                    ("Which famous playwright was born in Stratford-upon-Avon?","William Shakespeare"),
                    ("Who founded Eastnor Castle as his stately home?","John Cocks, 1st Earl Somers"),
                    ("Where did the band Slade film the music video for their song Run Runaway?","Eastnor Castle"),
                    ("Which BBC drama, starring Nicholas Lyndhurst, included scenes filmed at Eastnor Castle?","The Prince and the Pauper"),
                    ("Which music festival was held at Eastnor Castle between 2002 and 2011?","The Big Chill"),
                    ("What was the population of Ledbury in 2011?","9290"),
                    ("In which county is Eastnor Castle?","Herefordshire"),
                    ], "Trivia")

trivi2 = TriviaPage("339", [
                    ("Who released the albums Everything Must Go and Generation Terrorists?","Manic Street Preachers"),
                    ("Which band had members John, Paul, George and Ringo?","The Beatles"),
                    ("Which band's hits include Enola Gay, Messages and Souvenir?","Orchestral Manoeuvres in the Dark"),
                    ("Which New Zealand duo were the stars of a HBO TV series?","Flight of the Conchords"),
                    ("What is Reginald Kenneth Dwight better known as?","Elton John"),
                    ("What is James Blunt's real name?","James Blunt"),
                    ("Who wasn't it?","Shaggy"),
                    ("Which group's hits included Wannabe and 2 Become 1?","Spice Girls"),
                    ("Who was the lead singer of The Police?","Sting"),
                    ("Which album featured the songs Time, Eclipse and Money?","Dark Side of the Moon by Pink Floyd"),
                    ("Where is the love?","Locked in a cupboard in Will.i.am's house"),
                    ("Who wrote Do They Know It's Christmas?","Bob Geldof and Midge Ure"),
                    ("What do Nirvana smell like?","Teen Sprit"),
                    ("What can't you buy The Beatles?","Love"),
                    ("Who performed the theme of the James Bond film The Living Daylights?","A-ha"),
                    ("Who performed the theme of the James Bond film Goldfinger?","Shirley Bassey"),
                    ("Who performed the hit songs It's Not Unusual and What's New Pussycat?","Tom Jones"),
                    ("Which fictional band featured David St. Hubbins (played by Michael McKean) on vocals?","Spinal Tap"),
                    ("Which playing card is the only card Motorhead need?","The Ace of Spades"),
                    ("What is the surname of Oasis members Liam and Noel?","Gallagher"),
                    ("Who wants you to hit her one more time?","Britney Spears"),
                    ("What does Ian Dury want you to hit him with?","Your Rhythm Stick"),
                    ("Which song preformed by Dusty Springfield first appeared in the 1967 film Casino Royale?","The Look of Love"),
                    ("Which band's songs included Surfin' Safari, Surfer Girl, Surfin' USA, Little Surfer Girl, Noble Surfer, The Rocking Surfer, South Bay Surfer, Still Surfin, Surf Jam, The Surfer Moon, Surfers Rule, Surfin' and Surf's Up?","The Beach Boys"),
                    ("Which rap group was comprised of members Mike D, Ad Rock and MCA?","The Beastie Boys"),
                    ], "Music Trivia")

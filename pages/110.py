from page import Page
from random import choice

jokes = {"Who is the best singer in the KLB?":"Mart Garfunkel",
         "What is the best Nintendo game?":"Super Mario Mart",
         "What is the world's best shop?":"Wal-Mart",
         "What is the world's best sport?":"Marts (Darts)",
         "What is the best suit in a pack of cards?":"Marts (Hearts)",
         "What is the subject studied at Hogwarts?":"Defence Against the Dark Marts",
         "Who is the world's most popular cartoon character?":"Mart Simpson",
         "Where does a JCR DODO file his papers?":"In his GRyalling cabinet",
         "What is Rafael doing at the weekend?":"Martying (Partying)",
         "What is the best Neil Young song?":"Mart of Gold",
         "What is the best Blondie song?":"Mart of Glass",
         "What is everyone's favourite Queens of the Stone Age song?":"The Lost Mart of Keeping a Secret",
         "What is everyone's favourite Shakespeare play?":"Henry XIV Mart 1",
         "What method of surveying did the famous car company Ford use when designing their new Ford Focus car?":"A focus group",
         "What was the best programme on CITV?":"Mart Attack",
         "What was the best programme on ITV at 9pm on Sundays?":"Martbeat",
         "What are they making on the Bake Off next week?":"Bakewell mart",
         "Why is the best thing about Windows 10?":"The mart menu",
         "What is the subject studied at UCL?":"History of Mart",
         "Who invented the best coordinate system?":"Desmartes",
         "Where does Harry Potter keep his broomstick?":"Up his mart",
         "What is Sam's favourite way of serving food?":"A la marte",
         "How do you gather your groceries in America?":"In a shopping mart",
         "What do you use to flip eggs?":"Kitchen mart",
         "What is a Mart's worst enemy?":"Flautas",
         "Where is a great place to begin?":"At the mart",
         "What does Huda use to kill people?":"Martial marts",
         "What is the best drink?":"Club Mart",
         "What can Rafael not do with launch and lunch?":"Tell them amart",
         "What is the best London hospital?":"St. Marts",
         "What is Gaviscon the best pill for?":"Martburn",
         "What is the worst part of the driving licence?":"Countermart",
         "What part of Diet Coke gives you cancer?":"Asmartame",
         "What is the best George Clooney film?":"O Brother Where Mart Thou?",
         "What do you need to connect your PS2 to your TV?":"MART cable",
         "What is the best type of matching?":"Bimartite graph",
         "What is the best form of a verb?":"Past marticiple",
         "What is the best word-based party game?":"Marticulate",
         "Who is the best fictional chat show host?":"Alan Martridge",
         "What is the best present from your true love?":"Martridge in a pear tree",
         "What is Sam's favourite part of a train station?":"Demarture boards",
         "Who is the best Dickens character?":"Martful Dodger",
         "Who was the best actor in Casablanca":"Humphrey Bomart",
         "What did Juliet say to Romeo?":"Wherefore mart thou, Romeo?",
         "What was the best US president?":"Jimmy Marter",
         "What is the best firework?":"Catherine wheel",
         "What is Mart's favourite breakfast cereal?":"Pice Krispies",
         "What is the best coffee?":"A Martte",
         "What do you get when you put French bread in a spiraliser?":"Baguetti",
         "Why do you never see elephants hiding in trees?":"They are big",
		 "What is the best sausage?":"Cumberbatch",
         "Who is the best goalkeeper?":"Joe Mart"
         }

class JokePage(Page):
    def __init__(self,page_num):
        super(JokePage, self).__init__(page_num)
        self.title = "Jokes"

    def generate_content(self):
        self.add_title("Jokes")

        used = []
        for i in range(10):
            self.start_fg_color("YELLOW")
            c = choice(jokes.keys())
            while c in used:
                c = choice(jokes.keys())
            used.append(c)
            joke,ans = c,jokes[c]
            self.add_wrapped_text(joke+" ")
            self.start_fg_color("GREEN")
            self.add_wrapped_text(ans)
            self.end_fg_color()
            self.add_newline()
            self.add_newline()




jokepage = JokePage("110")

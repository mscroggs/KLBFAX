from page import Page
from helpers import url_handler
import config

class CountdownLettersPage(Page):
    def __init__(self):
        super(CountdownLettersPage, self).__init__("251")
        words = url_handler.load("https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt")
        self.words = {i:[] for i in range(1,10)}
        for word in words.split():
            if len(word) in self.words:
                self.words[len(word)].append(word.upper())
        self.title = "Countdown Letters Game"

        self.in_index = False

    def background(self):
        from random import randrange,shuffle
        vowels = ["A"]*15 + ["E"]*21 + ["I"]*13 + ["O"]*13 + ["U"]*5
        conson = ["B"]*2 + ["C"]*3 + ["D"]*6 + ["F"]*2 + ["G"]*3 + ["H"]*2 + ["J"]*1 + ["K"]*1 + ["L"]*5 + ["M"]*4 + ["N"]*8 + ["P"]*4 + ["Q"]*1 + ["R"]*9 + ["S"]*9 + ["T"]*9 + ["V"]*1 + ["W"]*1 + ["X"]*1 + ["Y"]*1 + ["Z"]*1

        shuffle(vowels)
        shuffle(conson)

        v = randrange(3,6)
        c = 9-v

        self.letters = vowels[:v]+conson[:c]
        shuffle(self.letters)

        self.possible = {i:[] for i in range(1,10)}
        for i in range(1,10):
            for word in self.words[i]:
                for letter in word:
                    if word.count(letter) > self.letters.count(letter):
                        break
                else:
                    self.possible[i].append(word)


    def generate_content(self):
        self.add_title("Countdown", font="size4")
        self.add_title("     letters game", font="size4")

        self.add_newline()
        self.add_title(" ".join(self.letters),font="size4",fg="BLACK", bg="BRIGHTWHITE")

        self.add_newline()
        self.add_text("Press + to reveal answers",fg="GREEN")
        self.add_newline()
        for i in range(9,0,-1):
            if len(self.possible[i])>0:
                n = config.WIDTH // (i+1)
                self.add_reveal_text(str(i)+" LETTER WORDS",fg="YELLOW")
                self.add_newline()
                for j in range(0,len(self.possible[i]),n):
                    self.add_reveal_text(" ".join(self.possible[i][j:j+n]), wrapping=True)
                    self.add_newline()
                self.add_newline()

class CountdownNumbersPage(Page):
    def __init__(self):
        super(CountdownNumbersPage, self).__init__("252")
        self.title = "Countdown Numbers Game"

        self.in_index = False

    def background(self):
        from random import randrange,shuffle
        from itertools import permutations, product

        numbers = list(range(1,11))*2 + [25,50,75,100]

        shuffle(numbers)

        self.numbers = numbers[:6]
        self.target = randrange(100,1000)
        self.best = [1000,"",0]

        for i in range(1,7):
            for order in permutations(self.numbers[:i]):
                for operations in product(["+","-","*","/"],repeat=i-1):
                    #for comp_order in permutations(range(i-1)):
                        result, desc = self.calculate(order, operations) #, comp_order)
                        if abs(result-self.target) < self.best[0]:
                           self.best = [abs(result-self.target),desc, result]

    def calculate(self, order, operations, comp_order=None):
        result = order[0]
        desc = ""
        for n,o in zip(order[1:],operations):
            if o == "+":
                result += n
                if desc == "":
                    desc = "ADD "+str(order[0])+" TO "+str(n)+"."
                else:
                    desc += " THEN ADD "+str(n)+"."
            if o == "-":
                result -= n
                if desc == "":
                    desc = "TAKE "+str(n)+" FROM "+str(order[0])+"."
                else:
                    desc += " THEN SUBTRACT "+str(n)+"."
            if o == "*":
                result *= n
                if desc == "":
                    desc = "MULTIPLY "+str(order[0])+" BY "+str(n)+"."
                else:
                    desc += " THEN MULTIPLY BY "+str(n)+"."
            if o == "/":
                result /= n
                if desc == "":
                    desc = "DIVIDE "+str(order[0])+" BY "+str(n)+"."
                else:
                    desc += " THEN DIVIDE BY "+str(n)+"."
        return result, desc


    def generate_content(self):
        self.add_title("Countdown", font="size4")
        self.add_title("     numbers game", font="size4")

        self.add_newline()
        self.add_title(" ".join(str(i) for i in self.numbers),font="size4",fg="BLACK", bg="BRIGHTWHITE")
        self.add_title("      TARGET: "+str(self.target),font="size4",fg="BLACK", bg="BRIGHTWHITE")

        self.add_newline()
        self.add_text("Press + to reveal answers",fg="GREEN")
        self.add_newline()
        if self.best[2] != self.target:
            self.add_reveal_text("It is impossible to make "+str(self.target)+".")
            self.add_newline()
        self.add_reveal_text("To make "+str(self.best[2])+": "+self.best[1], wrapping=True)
        self.add_newline()


class IndexPage(Page):
    def __init__(self, *args):
        super(IndexPage, self).__init__("250")
        self.title = "Games"

        maximum = 250
        self.ls = {}
        for page in args:
            maximum = max(maximum, int(page.number))
            self.ls[page.number] = page.title

        self.index_num = "250-"+str(maximum)

    def generate_content(self):
        self.add_title("Games")
        for n, title in self.ls.items():
            self.add_text(n+" ",fg="YELLOW")
            self.add_text(title)
            self.add_newline()


page1 = CountdownLettersPage()
page2 = CountdownNumbersPage()

index = IndexPage(page1, page2)
index.ls["900"] = "Choose your own adventure"

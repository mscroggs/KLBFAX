from page import Page
from helpers import url_handler
import config

def cleanstr(n):
    if type(n) is int:
        return str(n)
    if n.is_integer():
        return str(int(n))
    return str(n)

class CountdownLettersPage(Page):
    def __init__(self):
        super(CountdownLettersPage, self).__init__("155")
        self.words = {i:[] for i in range(1,10)}
        self.title = "Countdown Letters Game"
        self.importance = 4
        self.words = None
        self.in_index = False

    def background(self):
        if self.words is None:
            self.words = {i:[] for i in range(1,10)}
            try:
                words = url_handler.load("https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt")
                for word in words.split():
                    if len(word) in self.words:
                        self.words[len(word)].append(word.upper())
            except:
                self.words = None
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
        for i,l in enumerate(self.letters):
            self.move_cursor(y=9,x=0)
            self.add_title(l,font="size4mono",fg="BLUE", bg="BRIGHTWHITE",fill=False, pre=9*i)

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
        super(CountdownNumbersPage, self).__init__("156")
        self.title = "Countdown Numbers Game"

        self.importance = 4

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
            for operations in product(["+","-","*","/",";"],repeat=i-1):
                for comp_order in permutations(range(i-1)):
                    result, desc = self.calculate(self.numbers[:i], operations, comp_order)
                    if abs(result-self.target) < self.best[0]:
                        self.best = [abs(result-self.target),desc, result]
                        if self.best[0] == 0:
                            return

    def calculate(self, numbers, operations, comp_order):
        desc = ""
        while len(operations)>0:
            i = comp_order[0]
            a,b = numbers[i],numbers[i+1]
            o = operations[i]
            if o == "+":
                result = a+b
                desc += "    ADD "+cleanstr(a)+" TO "+cleanstr(b)+" TO MAKE "+cleanstr(result)+".\n"
            if o == "-":
                result = a-b
                desc += "    SUBTRACT "+cleanstr(b)+" FROM "+cleanstr(a)+" TO MAKE "+cleanstr(result)+".\n"
            if o == "*":
                result = a*b
                desc += "    MULTIPLY "+cleanstr(a)+" BY "+cleanstr(b)+" TO MAKE "+cleanstr(result)+".\n"
            if o == "/":
                if b == 0:
                    return (1000,"ERROR")
                result = a/b
                desc += "    DIVIDE "+cleanstr(a)+" BY "+cleanstr(b)+" TO MAKE "+cleanstr(result)+".\n"
            if o == ";":
                result = a
            comp_order = [j if j<i else j-1 for j in comp_order[1:]]
            numbers = numbers[:i] + [result] + numbers[i+2:]
            operations = operations[:i] + operations[i+1:]

        return numbers[0], desc


    def generate_content(self):
        self.add_title("Countdown", font="size4")
        self.add_title("     numbers game", font="size4")

        self.add_newline()
        self.add_title(" TARGET: "+str(self.target),font="size4",fg="BLACK", bg="BRIGHTWHITE")
        pre = 2
        for i,n in enumerate(self.numbers):
            self.move_cursor(x=0,y=14)
            self.add_title("|"+str(n)+"|",font="size4",fg="BLUE", bg="BRIGHTWHITE",fill=False, pre=pre)
            pre += width(n)+3
            # self.add_title(" ".join(str(i) for i in self.numbers),font="size4",fg="BLUE", bg="BRIGHTWHITE")

        self.add_newline()
        self.add_text("Press + to reveal answers",fg="GREEN")
        self.add_newline()
        if self.best[2] != self.target:
            self.add_reveal_text("It is impossible to make "+cleanstr(self.target)+", the best you can make is "+cleanstr(self.best[2])+":", wrapping=True)
            self.add_newline()
        self.add_reveal_text(self.best[1], wrapping=True)
        self.add_newline()

def width(n):
    out = 1
    for digit in str(n):
        if digit == "1":
            out += 3
        else:
            out += 5
    return out

page1 = CountdownLettersPage()
page2 = CountdownNumbersPage()


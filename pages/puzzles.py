from page import Page
from random import choice

class CrosswordPage(Page):
    def __init__(self, num, title, solution, aclues, dclues):
        super(CrosswordPage, self).__init__(num)
        self.title = title
        self.display_title = title
        self.in_index = False
        self.importance = 3
        self.solution = solution
        self.aclues = aclues
        self.dclues = dclues

    def generate_content(self):
        self.add_title(self.display_title, font="size4")
        self.crossword(self.solution, self.aclues, self.dclues)

    def crossword(self, solution, aclues, dclues):
        d_n = []
        a_n = []
        numbers = []
        reveal = []
        solution = solution.split("\n")
        whiteline = "w" * (2+7*len(solution[0]))+"\n"
        out = whiteline*2
        n = 1
        for i,line in enumerate(solution):
            newline = "ww"
            for j,char in enumerate(line):
                if char==" ":
                    newline += "wwwww"
                else:
                    reveal.append((4+7*j,7+4*i,char))
                    done = False
                    if i < len(solution)-1    and (i==0 or solution[i-1][j]==" ") and solution[i+1][j]!=" ":
                        numbers.append((2+7*j,6+4*i,n))
                        n += 1
                        done = True
                        d_n.append(n-1)
                    if j < len(solution[0])-1 and (j==0 or solution[i][j-1]==" ") and solution[i][j+1]!=" ":
                        if not done:
                            numbers.append((2+7*j,6+4*i,n))
                            n += 1
                        a_n.append(n-1)
                    newline += "kkkkk"
                newline += "ww"
            out += (newline+"\n")*6
            out += whiteline*2
        self.print_image(out,5)

        for x,y,n in numbers:
            self.move_cursor(x=x,y=y)
            self.add_text(str(n))
        for x,y,n in reveal:
            self.move_cursor(x=x,y=y)
            self.add_reveal_text(str(n))

        x = len(whiteline)
        self.move_cursor(y=5,x=x)
        self.add_text("ACROSS",fg="BRIGHTWHITE")
        for n,clue in zip(a_n,aclues):
            self.add_newline()
            self.move_cursor(x=x)
            self.add_text(str(n)+" ",fg="GREEN")
            self.add_wrapped_text(clue,pre=x)

        self.add_newline()
        self.add_newline()
        self.move_cursor(x=x)
        self.add_text("DOWN",fg="BRIGHTWHITE")
        for n,clue in zip(d_n,dclues):
            self.add_newline()
            self.move_cursor(x=x)
            self.add_text(str(n)+" ",fg="GREEN")
            self.add_wrapped_text(clue,pre=x+2)
        self.add_newline()
        self.add_newline()
        self.move_cursor(x=x)
        self.add_text("Press + to reveal answer",fg="GREEN")

class SudokuPage(Page):
    def __init__(self, num):
        super(SudokuPage, self).__init__(num)
        self.title = "Sudoku"
        self.importance = 3

    def background(self):
        solution = [[0 for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                used = [solution[a][j] for a in range(i)]
                used+= [solution[i][b] for b in range(j)]
                used+= [solution[a][b] for a in range(i//3 * 3, i//3 * 3 + 3) for b in range(j//3 * 3,j//3 * 3 + 3)]
                options = [a for a in range(1,10) if a not in used]
                if len(options) == 0:
                    self.background()
                    return
                solution[i][j] = choice(options)
        self.solution = solution
        self.given = [[False for j in range(9)] for i in range(9)]
        calculated = [[None for j in range(9)] for i in range(9)]
        while True:
            possible = [(i,j) for i in range(9) for j in range(9) if calculated[i][j] is None]
            if len(possible) == 0:
                return
            i,j = choice(possible)
            self.given[i][j] = True
            calculated[i][j] = solution[i][j]
            calculated = self.calculate(calculated)

    def calculate(self, calculated):
        changed = False
        possible = [[list(range(1,10)) for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if calculated[i][j] is None:
                    used = [calculated[a][j] for a in range(9)]
                    used+= [calculated[i][b] for b in range(9)]
                    used+= [calculated[a][b] for a in range(i//3 * 3, i//3 * 3 + 3) for b in range(j//3 * 3,j//3 * 3 + 3)]
                    possible[i][j] = [a for a in range(1,10) if a not in used]
                    if len(possible[i][j]) == 1:
                        calculated[i][j] = possible[i][j][0]
                        possible[i][j] = []
                        changed = True
                else:
                    possible[i][j] = []
        for i in range(9):
            for n in range(1,10):
                if len([0 for j in range(9) if n in possible[i][j]]) == 1:
                    for j in range(9):
                        if n in possible[i][j]:
                            calculated[i][j] = n
                            possible[i][j] = []
                            break
        for j in range(9):
            for n in range(1,10):
                if len([0 for i in range(9) if n in possible[i][j]]) == 1:
                    for i in range(9):
                        if n in possible[i][j]:
                            calculated[i][j] = n
                            possible[i][j] = []
                            break
        for square in range(9):
            for n in range(1,10):
                if len([0 for i in range(square%3,square%3+3) for j in range(square//3, square//3+3) if n in possible[i][j]]) == 1:
                    for i in range(square%3,square%3+3):
                        for j in range(square//3, square//3+3):
                            if n in possible[i][j]:
                                calculated[i][j] = n
                                possible[i][j] = []
                                break
                        else:
                            continue
                        break
        if changed:
            return self.calculate(calculated)
        else:
            return calculated

    def generate_content(self):
        self.add_title("Sudoku", font="size4")
        self.print_image(
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "w---w---w---ww---w---w---ww---w---w---w\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",5,2
            )

        for i in range(9):
            for j in range(9):
                self.move_cursor(x=4+4*i+i//3,y=6+j*2+j//3)
                if self.given[i][j]:
                    self.add_text(str(self.solution[i][j]))
                else:
                    self.add_reveal_text(str(self.solution[i][j]))


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
    def __init__(self, num):
        super(CountdownLettersPage, self).__init__(num)
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
    def __init__(self, num):
        super(CountdownNumbersPage, self).__init__(num)
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


class IndexPage(Page):
    def __init__(self, num):
        super(IndexPage, self).__init__(num)
        self.title = "Puzzles"
        self.index_num = "150-159"

    def generate_content(self):
        self.add_title("Puzzles")
        for n,title in [
            ("151","Crossword 1"),
            ("152","Crossword 2"),
            ("153","Crossnumber"),
            ("154","Regular Expression Crossword"),
            ("155","Sudoku"),
            ("156","Countdown Letters Game"),
            ("157","Countdown Numbers Game"),
            ("158","???"),
            ("159","???"),
                ]:
            self.add_text(n,fg="GREEN")
            self.add_text(" "+title)
            self.add_newline()

page0 = IndexPage("150")

page1 = CrosswordPage("151", "Crossword",
    "GOAT \n"
    "A L F\n"
    "RHINO\n"
    "Y B R\n"
    " MINK",
    ["Winnable animal in Monty Hall problem.","Animal with horn.","Aerosmith's favourite colour."],
    ["Pokemon rival.","Didn't do the murder because you were doing this instead.","Eat with this, or do it to a GitHub repository."])

page2 = CrosswordPage("152", "Crossword",
    "BASH\n"
    "R  O\n"
    "A  R\n"
    "NOON",
    ["Robot Wars sargeant.","Lunchtime."],
    ["___ flakes, but not corn flakes.","French orchestra instrument."])

page3 = CrosswordPage("153", "Crossnumber",
    "94749\n"
    "9 789\n"
    "95 49\n"
    "151 9\n"
    "95159",
    ["Palindrome.","Why is 6 afraid of 7?","5 less than a multiple of 10.","Square.","EMFFAX page that this puzzle is on.","Palindrome."],
    ["The sum of this number's digits is 37.","Multiple of 11.","Square.","Palindrome.","Start of made up phone number.","Factor of 2D."])


page4 = CrosswordPage("154", "Regex crossword",
    "DUCK\n"
    "ANON\n"
    "TILE\n"
    "AXLE",
    ["D.*U.*","[AEIOU][ON]*",".[ILP]*E*","[AD][XO][LI][ES]"],
    ["[ADT]*","(UN|UK)(IX|VI)","C+O+L+","[^U]N+E+"])

page5 = SudokuPage("155")
page6 = CountdownLettersPage("156")
page7 = CountdownNumbersPage("157")




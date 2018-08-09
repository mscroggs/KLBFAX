from page import Page
from random import choice, randrange

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
        self.in_index = False
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
        self.move_cursor(y=10,x=47)
        self.add_wrapped_text("Press + to reveal answer", fg="GREEN")


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
        self.add_text("Press + to reveal answer",fg="GREEN")
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

class GridPuzzlePage(Page):
    def __init__(self, num, solution, totals, across, down):
        super(GridPuzzlePage, self).__init__(num)
        self.title = "Grid Puzzle"
        self.in_index = False
        self.solution = solution
        self.across = across
        self.down = down
        self.totals = totals

    def generate_content(self):
        self.add_title("Grid Puzzle",font="size4")
        self.print_image(
                        "wwwww-wwwww-wwwww\n"
                        "wwwww-wwwww-wwwww\n"
                        "ww-ww-ww-ww-ww-ww\n"
                        "ww-ww-ww-ww-ww-ww\n"
                        "wwwww-wwwww-wwwww\n"
                        "wwwww-wwwww-wwwww\n"
                        "-----------------\n"
                        "-----------------\n"
                        "wwwww-wwwww-wwwww\n"
                        "wwwww-wwwww-wwwww\n"
                        "ww-ww-ww-ww-ww-ww\n"
                        "ww-ww-ww-ww-ww-ww\n"
                        "wwwww-wwwww-wwwww\n"
                        "wwwww-wwwww-wwwww\n"
                        "-----------------\n"
                        "-----------------\n"
                        "wwwww-wwwww-wwwww\n"
                        "wwwww-wwwww-wwwww\n"
                        "ww-ww-ww-ww-ww-ww\n"
                        "ww-ww-ww-ww-ww-ww\n"
                        "wwwww-wwwww-wwwww\n"
                        "wwwww-wwwww-wwwww",5,3)

        for i,s in enumerate(self.solution):
            self.move_cursor(y=6+4*(i//3),x=5+6*(i%3))
            self.add_reveal_text(str(s))

        for i,s in enumerate(self.across):
            self.move_cursor(y=6+4*(i//2),x=8+6*(i%2))
            if s == "*":
                self.add_text("×")
            elif s == "/":
                self.add_text("÷")
            else:
                self.add_text(s)

        for i,s in enumerate(self.down):
            self.move_cursor(y=8+4*(i%2),x=5+6*(i//2))
            if s == "*":
                self.add_text("×")
            elif s == "/":
                self.add_text("÷")
            else:
                self.add_text(s)

        for i,s in enumerate(self.totals[:3]):
            self.move_cursor(y=6+4*i,x=20)
            self.add_text("= "+str(s))

        for i,s in enumerate(self.totals[3:]):
            self.move_cursor(y=16,x=5+6*i)
            self.add_text("=")
            self.move_cursor(y=17,x=5+6*i)
            self.add_text(str(s))

        self.move_cursor(y=5,x=27)
        self.add_wrapped_text("Put the digits 1 to 9 (using each digit exactly once)"
                              "in the boxes so that the sums are correct. The sums  "
                              "should be read left to right and top to bottom       "
                              "ignoring the usual order of operations. For example, "
                              "4+3×2 is 14, not 10.", pre=27)

        self.move_cursor(y=10,x=27)
        self.add_wrapped_text("Press + to reveal answer", fg="GREEN")

class OllyPage(Page):
    def __init__(self, num):
        super(OllyPage, self).__init__(num)
        self.title = "Where's Olly"
        self.in_index = False

    def generate_content(self):
        self.add_title("Where's Olly", font="size4bold")
        r,c = 22,20
        olly = (randrange(r),randrange(c))
        for j in range(r):
            for i in range(c):
                if i==olly[1] and j==olly[0]:
                    self.add_unreveal_text("OLLY")
                    self.move_cursor(x=4*i)
                    self.add_reveal_text("OLLY",fg="BRIGHTWHITE")
                else:
                    word = choice(["YLLO","YOLO"])
                    self.add_unreveal_text(word)
                    self.move_cursor(x=4*i)
                    self.add_reveal_text(word,fg="K")
            self.add_newline()
        self.add_wrapped_text("Press + to reveal answer", fg="GREEN")

class PuzzlePage(Page):
    def __init__(self, num, title, text):
        super(PuzzlePage, self).__init__(num)
        self.title = title
        self.text = text
        self.in_index = False

    def generate_content(self):
        self.add_title(self.title, font="size4bold")
        self.add_newline()
        self.add_wrapped_text(self.text)



class IndexPage(Page):
    def __init__(self, num):
        super(IndexPage, self).__init__(num)
        self.title = "Puzzles"
        self.index_num = "150-169"

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
            ("158","Grid puzzle 1"),
            ("159","Grid puzzle 2"),
            ("160","Where's Olly"),
            ("161","Ten digit number"),
            ("162","The Mutilated Chessboard"),
            ("163","8! Minutes"),
            ("164","One Two Three"),
            ("165","Let The Passenger Train Through!"),
            ("166","Polya Strikes Out"),
            ("167","Combining Multiples"),
            ("168","Rotating Round Table"),
            ("169","Reverse Bases"),
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
page8 = GridPuzzlePage("158",[2,5,9, 4,3,7, 8,6,1],[90,84,48,64,90,63],["*","*", "*","*" ,"*","*"],["*","*", "*","*" ,"*","*"])
page9 = GridPuzzlePage("159",[5,3,9, 7,1,6, 8,4,2],[17,1,0,4,12,27],["+","+", "/","-" ,"/","-"],["+","-", "/","*" ,"*","/"])
page10 = OllyPage("160")
page11 = PuzzlePage("161","Ten Digit Number","Can you create a 10-digit number, where the first digit is how many zeros in the number, the second digit is how many 1s in the number etc. until the tenth digit which is how many 9s in the number?")
page12 = PuzzlePage("162","The Mutilated Chessboard","You are given a chessboard where two diagonally opposite corners have been removed and a large bag of dominoes of such size that they exactly cover two adjacent squares on the chessboard.\n\nIs it possible to place 31 dominoes on the chessboard so that all the squares are covered?")
page13 = PuzzlePage("163","8! Minutes","How many days are there in 8! minutes?")
page14 = PuzzlePage("164","One Two Three","Each point on a straight line is either red or blue. Show that it's always possible to find three points of the same color in which one is the midpoint of the other two.")
page15 = PuzzlePage("165","Let The Passenger Train Through!","A goods train, made up of a locomotive and 5 trucks, stops at a small station. The small station has a siding which the goods train can reverse into. The siding can hold an engine and two trucks or three trucks.\n\nA passenger train arrives travelling in the opposite direction. How can they let it through? (The passenger train is too long to fit in the siding.)")
page16 = PuzzlePage("166","Polya Strikes Out","Write the numbers 1, 2, 3, ... in a row. Strike out every third number beginning with the third. Write down the cumulative sums of what remains:\n\n1, 2, 3, 4, 5, 6, 7, ...\n1, 2, X, 4, 5, X, 7, ...\n1, 2, 4, 5, 7, ...\n1=1; 1+2=3; 1+2+4=7; 1+2+4+5=12; 1+2+4+5+7=19; ...\n1, 3, 7, 12, 19, ...\n\nNow strike out every second number beginning with the second. Write down the cumulative sums of what remains. What is the final sequence?")
page17 = PuzzlePage("167","Combining Multiples","What is the largest number that cannot be written in the form 3a+5b, where a and b are (strictly) positive integers?")
page18 = PuzzlePage("168","Rotating Round Table","At a large dinner, 24 people are to sit evenly spaced around a round table. Place cards are laid to show where everyone should sit. Unfortunately nobody notices the name cards and the guests sit down with nobody in the correct seat.\n\nShow that it is possible to rotate the table so that at least two people will be in the correct seats.")
page19 = PuzzlePage("169","Reverse Bases","Find three digits a, b and c such that abc in base 10 is equal to cba in base 9?")

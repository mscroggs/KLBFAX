from page import Page
from random import choice

class CrosswordPage(Page):
    def __init__(self, num, title, solution, aclues, dclues):
        super(CrosswordPage, self).__init__(num)
        self.title = title
        self.display_title = title
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
            for i in range(9):
                for j in range(9):
                    if calculated[i][j] is None:
                        used = [calculated[a][j] for a in range(9)]
                        used+= [calculated[i][b] for b in range(9)]
                        used+= [calculated[a][b] for a in range(i//3 * 3, i//3 * 3 + 3) for b in range(j//3 * 3,j//3 * 3 + 3)]
                        possible = [a for a in range(1,10) if a not in used]
                        if len(possible) == 1:
                            calculated[i][j] = possible[0]


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


page1 = CrosswordPage("150", "Crossword",
    "GOAT \n"
    "A L F\n"
    "RHINO\n"
    "Y B R\n"
    " MINK",
    ["Winnable animal in Monty Hall problem.","Animal with horn.","Aerosmith's favourite colour."],
    ["Pokemon rival.","Didn't do the murder because you were doing this instead.","Eat with this, or do it to a GitHub repository."])
page1.in_index = True
page1.index_num = "150-159"
page1.title = "Puzzles"

page2 = CrosswordPage("151", "Crossword",
    "BASH\n"
    "R  O\n"
    "A  R\n"
    "NOON",
    ["Robot Wars sargeant.","Lunchtime."],
    ["___ flakes, but not corn flakes.","French orchestra instrument."])

page3 = CrosswordPage("152", "Crossnumber",
    "94749\n"
    "9 789\n"
    "95 49\n"
    "151 9\n"
    "95159",
    ["Palindrome.","Why is 6 afraid of 7?","5 less than a multiple of 10.","Square.","EMFFAX page that this puzzle is on.","Palindrome."],
    ["The sum of this number's digits is 37.","Multiple of 11.","Square.","Palindrome.","Start of made up phone number.","Factor of 2D."])


page4 = CrosswordPage("153", "Regex crossword",
    "DUCK\n"
    "ANON\n"
    "TILE\n"
    "AXLE",
    ["D.*U.*","[AEIOU][ON]*",".[ILP]*E*","[AD][XO][LI][ES]"],
    ["[ADT]*","(UN|UK)(IX|VI)","C+O+L+","[^U]N+E+"])

page5 = SudokuPage("154")

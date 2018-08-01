from page import Page

#def crossword(self, solution, clues):
#    solution = solution.split("\n")
#    image = 

class CrosswordPage(Page):
    def __init__(self):
        super(CrosswordPage, self).__init__("150")
        self.title = "Puzzles"
        self.importance = 3
        self.index_num = "150-159"

    def generate_content(self):
        self.add_title("Crossword", font="size4")
#        crossword(self, "G
        self.print_image("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                         "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                         "ww-----ww-----ww-----ww-----wwwwwwwww\n"
                         "ww-----ww-----ww-----ww-----wwwwwwwww\n"
                         "ww-----ww-----ww-----ww-----wwwwwwwww\n"
                         "ww-----ww-----ww-----ww-----wwwwwwwww\n"
                         "ww-----ww-----ww-----ww-----wwwwwwwww\n"
                         "ww-----ww-----ww-----ww-----wwwwwwwww\n"
                         "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                         "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                         "ww-----wwwwwwwww-----wwwwwwwww-----ww\n"
                         "ww-----wwwwwwwww-----wwwwwwwww-----ww\n"
                         "ww-----wwwwwwwww-----wwwwwwwww-----ww\n"
                         "ww-----wwwwwwwww-----wwwwwwwww-----ww\n"
                         "ww-----wwwwwwwww-----wwwwwwwww-----ww\n"
                         "ww-----wwwwwwwww-----wwwwwwwww-----ww\n"
                         "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                         "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                         "ww-----ww-----ww-----ww-----ww-----ww\n"
                         "ww-----ww-----ww-----ww-----ww-----ww\n"
                         "ww-----ww-----ww-----ww-----ww-----ww\n"
                         "ww-----ww-----ww-----ww-----ww-----ww\n"
                         "ww-----ww-----ww-----ww-----ww-----ww\n"
                         "ww-----ww-----ww-----ww-----ww-----ww\n"
                         "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                         "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                         "ww-----wwwwwwwww-----wwwwwwwww-----ww\n"
                         "ww-----wwwwwwwww-----wwwwwwwww-----ww\n"
                         "ww-----wwwwwwwww-----wwwwwwwww-----ww\n"
                         "ww-----wwwwwwwww-----wwwwwwwww-----ww\n"
                         "ww-----wwwwwwwww-----wwwwwwwww-----ww\n"
                         "ww-----wwwwwwwww-----wwwwwwwww-----ww\n"
                         "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                         "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                         "wwwwwwwww-----ww-----ww-----ww-----ww\n"
                         "wwwwwwwww-----ww-----ww-----ww-----ww\n"
                         "wwwwwwwww-----ww-----ww-----ww-----ww\n"
                         "wwwwwwwww-----ww-----ww-----ww-----ww\n"
                         "wwwwwwwww-----ww-----ww-----ww-----ww\n"
                         "wwwwwwwww-----ww-----ww-----ww-----ww\n"
                         "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
                         "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n",5)
        self.move_cursor(y=6,x=2)
        self.add_text("1")
        self.move_cursor(y=6,x=16)
        self.add_text("2")
        self.move_cursor(y=10,x=30)
        self.add_text("3")
        self.move_cursor(y=14,x=2)
        self.add_text("4")
        self.move_cursor(y=22,x=9)
        self.add_text("5")

        self.move_cursor(y=7,x=4)
        self.add_reveal_text("G")
        self.move_cursor(y=7,x=11)
        self.add_reveal_text("O")
        self.move_cursor(y=7,x=18)
        self.add_reveal_text("A")
        self.move_cursor(y=7,x=25)
        self.add_reveal_text("T")

        self.move_cursor(y=11,x=4)
        self.add_reveal_text("A")
        self.move_cursor(y=11,x=18)
        self.add_reveal_text("L")
        self.move_cursor(y=11,x=32)
        self.add_reveal_text("F")

        self.move_cursor(y=15,x=4)
        self.add_reveal_text("R")
        self.move_cursor(y=15,x=11)
        self.add_reveal_text("H")
        self.move_cursor(y=15,x=18)
        self.add_reveal_text("I")
        self.move_cursor(y=15,x=25)
        self.add_reveal_text("N")
        self.move_cursor(y=15,x=32)
        self.add_reveal_text("O")

        self.move_cursor(y=19,x=4)
        self.add_reveal_text("Y")
        self.move_cursor(y=19,x=18)
        self.add_reveal_text("B")
        self.move_cursor(y=19,x=32)
        self.add_reveal_text("R")

        self.move_cursor(y=23,x=11)
        self.add_reveal_text("P")
        self.move_cursor(y=23,x=18)
        self.add_reveal_text("I")
        self.move_cursor(y=23,x=25)
        self.add_reveal_text("N")
        self.move_cursor(y=23,x=32)
        self.add_reveal_text("K")

        self.move_cursor(y=5,x=38)
        self.add_text("ACROSS",fg="BRIGHTWHITE")
        self.move_cursor(y=6,x=38)
        self.add_text("1",fg="GREEN")
        self.add_text(" Winnable animal in Monty Hall problem.")
        self.move_cursor(y=7,x=38)
        self.add_text("4",fg="GREEN")
        self.add_text(" Animal with horn.")
        self.move_cursor(y=8,x=38)
        self.add_text("5",fg="GREEN")
        self.add_text(" Aerosmith's favourite colour.")

        self.move_cursor(y=10,x=38)
        self.add_text("DOWN",fg="BRIGHTWHITE")
        self.move_cursor(y=11,x=38)
        self.add_text("1",fg="GREEN")
        self.add_text(" Rival in Pokemon.")
        self.move_cursor(y=12,x=38)
        self.add_text("2",fg="GREEN")
        self.add_text(" Didn't do the murder because you were")
        self.move_cursor(y=13,x=40)
        self.add_text("doing this instead.")
        self.move_cursor(y=14,x=38)
        self.add_text("3",fg="GREEN")
        self.add_text(" Eat with this, or do it to a GitHub ")
        self.move_cursor(y=15,x=40)
        self.add_text("repository.")

        self.move_cursor(y=17,x=38)
        self.add_text("Press + to reveal answer",fg="GREEN")



page1 = CrosswordPage()


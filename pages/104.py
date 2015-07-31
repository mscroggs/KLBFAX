from page import Page
from colours import colour_print
from printer import instance as printer
from random import choice
import screen

jokes = {"Who is the best singer in the KLB?":"Mart Garfunkel",
         "What is the best Nintendo game?":"Super Mario Mart",
         "What is the world's best shop?":"Wal-Mart",
         "What is the world's best sport?":"Marts (Darts)",
         "What is the best suit in a pack of cards?":"Marts (Hearts)",
         "What is the subject studied at Hogwarts?":"Defence Against the Dark Marts",
         "Who is the world's most popular cartoon character?":"Mart Simpson",
         "What method of surveying did the famous car company Ford use when designing their new car, the Focus?":"Stratified sample"}

class JokePage(Page):
    def __init__(self,page_num):
        super(JokePage, self).__init__(page_num)
        self.title = "Jokes"
      
    def generate_content(self):
        content = colour_print(printer.text_to_ascii("Jokes"))+"\n\n"

        for i in range(6):
            content += self.colours.Foreground.YELLOW+self.colours.Style.BOLD
            c = choice(jokes.keys())
            joke,ans = c,jokes[c]
            while len(joke)>screen.WIDTH:
                content += joke[:screen.WIDTH]+"\n"
                joke = joke[screen.WIDTH:]
            content += joke
            content += self.colours.Foreground.GREEN
            if len(joke)+len(ans)<screen.WIDTH:
                content += " "*(screen.WIDTH-len(joke)-1-len(ans)) + ans
            else:
                content += "\n"+" "*(screen.WIDTH-1-len(ans)) + ans
            content += self.colours.Foreground.DEFAULT + self.colours.Style.DEFAULT+"\n\n\n"

          
        self.content = content
        
jokepage = JokePage("104")

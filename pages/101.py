from page import Page
from colours import colour_print
from printer import instance as printer
from random import choice

class TubePage(Page):
    def __init__(self,page_num):
        super(TubePage, self).__init__(page_num)
        self.title = "Tube Line Status"

    def generate_content(self):
        import tubestatus
        content = colour_print(printer.text_to_ascii("Tube Lines"))
        content += "\n"
        # Create a new status object for retrieving data
        current_status = tubestatus.Status()
        # Get a list of tube lines
        lines = current_status.list_lines()
        # Loop through the lines and print the status of each one
        lines_tube = [lines[i] for i in [1,2,11,4,9,0,3,13,5,7,10]]
        lines_other = [lines[i] for i in [8,6,12]]
        colours_tube = [self.colours.Style.BLINK,
                        self.colours.Background.RED,
                        self.colours.Background.YELLOW,
                        self.colours.Background.GREEN,
                        self.colours.Background.MAGENTA,
                        self.colours.Style.BLINK,
                        self.colours.Background.MAGENTA,
                        self.colours.Background.DEFAULT,
                        self.colours.Background.BLUE,
                        self.colours.Background.BLUE,
                        self.colours.Background.CYAN]
        colours_tube_text = [self.colours.Foreground.WHITE, 
                        self.colours.Foreground.WHITE,
                        self.colours.Foreground.BLACK,
                        self.colours.Foreground.BLACK,
                        self.colours.Foreground.BLACK,
                        self.colours.Foreground.WHITE,
                        self.colours.Foreground.WHITE,
                        self.colours.Foreground.WHITE,
                        self.colours.Foreground.WHITE,
                        self.colours.Foreground.WHITE,
                        self.colours.Foreground.BLACK]
                        
        colours_other = [self.colours.Background.CYAN,
                        self.colours.Background.YELLOW,
                        self.colours.Background.BLUE]  
        colours_other_text = [self.colours.Foreground.BLACK, 
                        self.colours.Foreground.BLACK,
                        self.colours.Foreground.WHITE]
        
        linei = 0
        for line in lines_tube:
            content += "\n  "
            content += colours_tube[linei] + colours_tube_text[linei]
            #line = line.replace("and","&")
            content += " " + str(line).replace("and","&") +" "*(20-len(str(line).replace("and","&")))
            content += self.colours.Background.DEFAULT
            desc = current_status.get_status(line).description
            if desc == "Good Service":
                content += self.colours.Foreground.GREEN
            else:
                content += self.colours.Foreground.RED
            content += " " + current_status.get_status(line).description
            content += self.colours.Foreground.DEFAULT
            linei += 1
        content += "\n"
        
        linei = 0
        for line in lines_other:
            content += "\n  "
            content += colours_other[linei] + colours_other_text[linei]            
            content += " " + str(line).replace("and","&") +" "*(20-len(str(line).replace("and","&")))
            content += self.colours.Background.DEFAULT
            desc = current_status.get_status(line).description
            if desc == "Good Service":
                content += self.colours.Foreground.GREEN
            else:
                content += self.colours.Foreground.RED
            content += " " + current_status.get_status(line).description
            content += self.colours.Foreground.DEFAULT
            linei += 1            

        self.content = content

page = TubePage("101")

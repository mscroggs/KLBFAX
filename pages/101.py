from page import Page
from colours import colour_print
from printer import instance as printer
from random import choice

class TubePage(Page):
    def __init__(self,page_num):
        super(TubePage, self).__init__(page_num)
        self.title = "Tube Line Status"

    def generate_content(self):
        import i_dont_be_real
        import tubestatus
        content = colour_print(printer.text_to_ascii("Tube Lines"))

        # Create a new status object for retrieving data
        current_status = tubestatus.Status()
        # Get a list of tube lines
        lines = current_status.list_lines()
        # Loop through the lines and print the status of each one
        for line in lines:
            content += "\n"
            content += line+" "*(21-len(line))
            desc = current_status.get_status(line).description
            if desc == "Good Service":
                content += self.colours.Foreground.GREEN
            else:
                content += self.colours.Foreground.RED
            content += current_status.get_status(line).description
            content += self.colours.Foreground.DEFAULT

        self.content = content

page = TubePage("101")

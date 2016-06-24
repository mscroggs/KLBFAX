import os
from page import Page
import colours
from colours import colour_print
from printer import instance as printer

page_number = os.path.splitext(os.path.basename(__file__))[0]
sub_page = Page(page_number)
sub_page.title = "The Team"
sub_page.in_index = False
sub_page.content = colour_print(
    printer.text_to_ascii("The Team"))

sub_page.content 

credits = """

      @@@@@@@@@        @@@ @@@         @@@ @@@        @^@^@^@^@
     @@@@@    @@     @@@^@@@^@@@     @@@~@@@~@@@     ^@       ^@
     @@@       @     ^ @@@ @@@ ^       @@@ @@@       @   ~ ~   ^
     @  ^   ^  @     ^^  ^^^  ^^      ~       ~      ^         @
     @    ^    @      ^^^^^^^^^       ~~~~~~~~~      @    ~    ^
       Scroggs       SpinnyGinny         Adam            Huda
    
      ~~~~~~~~~                      ^^@@@^@@@^^
     ~~       ~~        ^   ^        @@@~@@@~@@@
        @   @                        ^ @@@ @@@ ^
                         @@@         ^  ~   ~  ^
        @@@@@           @   @        ^   ~~~   ^
         Sam             Tom            Belgin 

Thank you everyone here for contributing to KLBFAX!

"""

credits = (colours.Foreground.RED+u"\u2588"+colours.Foreground.DEFAULT).join(credits.split("@"))
credits = (colours.Foreground.GREEN+u"\u2588"+colours.Foreground.DEFAULT).join(credits.split("^"))
credits = (colours.Foreground.BLUE+u"\u2588"+colours.Foreground.DEFAULT).join(credits.split("~"))

sub_page.content += credits

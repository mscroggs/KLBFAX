
from page import Page
import config

class MerryLadsPage(Page):
    def __init__(self, page_num):
        super(MerryLadsPage, self).__init__(page_num)
        self.title = "Merry lads' checklist"
        self.in_index = True
        self.tagline = "Fa la la la la (la la la la la la la la) la, la la, la LAA."
        pages.append([page_num,"Merry Lads' Checklist"])


    def generate_content(self):
        # Pick randomly
        import random
        checklist = [
        'broyden bean',
        'oak and ash',
        "bonny lass",
        "bagpipe song",
        "month of May",
        "honest bob",
        "box of frogs",
        "lump of clay",
        "Theresa May",
        "Holland clogs",
        "wagon wheel",
        "trusty squad",
        "rusty rhod",
        "epipen",
        "turmeric in the porridge",
        "knave whipsnade",
        "Myleene Klass",
        "piece of mesh",
        "toot",
        "Wayward Ho!",
        "Restaurant",
        "month of June",
        "last of May",
        "ballpoint person",
        "Worcester sauce",
        "Twisted flax",
        "Silent sword",
        "ex le chiffre",
        "mathstadon",
        "Roger Moore",
        "Starbucks card",
        "Cushy cloth",
        "Floral bush",
        "fumblebee",
        "Matthew Scroggs",
        "Alan Clarke",
        "Field of wheat",
        "hare & hound",
        "nitwit speed",
        "wholesome horse",
        "Muller light",
        "birthday bear",
        "resume",
        "bleedin' box",
        "sodding log",
        "uncle Glenn",
        "beans on toast",
        "Christmas tree",
        "Captain Magenta",
        "Galilei... oh",
        "London brick",
        "Elton John",
        "Brail rail",
        "cup of tea",
        "fledgling flint",
        "Swedish broad",
        "wireless mouse",
        "shitfaced Steve",
        "Jackson Lamb",
        "bassless beat",
        "Camden Lock",
        "Twilight moon",
        "Pint of ducks",
        "Breaking Bad",
        "Auld Lang Syne",
        "Steam-ed ham",
        "ruined roast",
        "merry lad",
        "burma sauce",
        "1 2 3",
        "piece of cloth",
        "flagrant flea",
        "pint of cheese",
        "belsize park",
        "charing cross"]
        on_his_list = random.choice(checklist)

        self.add_title("Each with his...",font="size4",fg="GREEN",bg="BRIGHTWHITE")

        lad=(
'''------ooooo------
-----ooooooo-----
-----oxkxkxo-----
-----oxxxxxo-----
-----xxkxkxx-----
------xxkxx------
----ggxxxxxgg----
---ggggxxxgggg---
---ggggggggggg---
--ggggggggggggg--
--ggggggggggggg--
--ggggggggggggg--
-xx-ggggggggg-xx-
-xx-ggggggggg-xx-
-xx-ggggggggg-xx-
xx--ggggggggg--xx
xx--ggggggggg--xx
xx--ggggggggg--xx
----WWWWWWWWW----
----yyyyyyyyy----
----yyyy-yyyy----
----yyyy-yyyy----
----yyyy-yyyy----
----yyyy-yyyy----
----yyyy-yyyy----
-----xx---xx-----
-----xx---xx-----
-----xx---xx-----
-----xx---xx-----
-----xx---xx-----
-----xx---xx-----
----xxx---xxx----''').replace(" ","-").replace("x","W")

        for i in range(5):
            color = random.choice(['g','r','o','c','b','m','R','y','G','C','B','p'])
            self.print_image(lad.replace('g',color),5,17*i-2)

        self.move_cursor(x=0,y=22)
        self.add_title(on_his_list.upper() + "!",font="size4bold",fg="GREEN",bg="BRIGHTWHITE")
pages = []

# Departures
merry01 = MerryLadsPage("180")
merry01.importance=4

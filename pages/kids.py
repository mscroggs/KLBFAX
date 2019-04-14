#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page import Page
from functions import replace
from random import shuffle,randrange,choice
import config

class CBBCPage(Page):
    def __init__(self):
        super(CBBCPage, self).__init__("130")
        self.title = "CBBC"
        self.index_num = "130-147"

    def generate_content(self):
        self.add_title("|C|",fill=False,bg="YELLOW",fg="BLACK",pre=1)
        self.move_cursor(y=0)
        self.add_title("|B|",fill=False,fg="YELLOW",bg="BLACK", pre=12)
        self.move_cursor(y=0)
        self.add_title("|B|",fill=False,fg="YELLOW",bg="BLACK", pre=24)
        self.move_cursor(y=0)
        self.add_title("|C|",fill=False,fg="YELLOW",bg="BLACK", pre=36)

        self.add_newline()
        self.add_text("131 ",fg="MAGENTA")
        self.add_text("Newsround")
        self.add_newline()
        self.add_text("132-140 ",fg="MAGENTA")
        self.add_text("Blue Peter")
        self.add_newline()
        self.add_text("141 ",fg="MAGENTA")
        self.add_text("The Demon Headmaster")
        self.add_newline()
        self.add_text("142 ",fg="MAGENTA")
        self.add_text("Chucklevision")
        self.add_newline()
        self.add_text("143 ",fg="MAGENTA")
        self.add_text("Playdays")
        self.add_newline()
        self.add_text("144 ",fg="MAGENTA")
        self.add_text("Crackerjack")
        self.add_newline()
        self.add_text("145 ",fg="MAGENTA")
        self.add_text("Paddington Bear")
        self.add_newline()
        self.add_text("146 ",fg="MAGENTA")
        self.add_text("Wacky Races")
        self.add_newline()
        self.add_text("147 ",fg="MAGENTA")
        self.add_text("Otis's Joke Page")
        self.add_newline()
        self.add_text("148 ",fg="MAGENTA")
        self.add_text("Torchy the Battery Boy")

class NewsroundPage(Page):
    def __init__(self):
        super(NewsroundPage, self).__init__("131")
        self.title = "Newsround"
        self.in_index = False

    def background(self):
        import feedparser
        rss_url = "https://feeds.bbci.co.uk/newsround/rss.xml"
        feed = feedparser.parse(rss_url)
        if len(feed) > 1:
            self.entries = [(replace(item["title"]),replace(item["description"])) for item in feed['entries'][:21]]
        else:
            self.entries = []

    def generate_content(self):
        self.add_title("Newsround",bg="MAGENTA",fg="YELLOW",font="size4bold")
        self.add_newline()
        for title,desc in self.entries:
            self.add_text(title,fg="YELLOW")
            self.add_newline()
            self.add_wrapped_text(desc)
            self.add_newline()
            self.add_newline()

class BluePeterPage(Page):
    def __init__(self,n):
        super(BluePeterPage, self).__init__(str(131+n))
        self.title = "Blue Peter"
        self.n = n
        self.in_index = False

    def generate_content(self):
        ### Content in these pages is taken from https://www.bbc.co.uk/cbbc
        logo = (
                "--------------------------------------------------------------------------------\n"
                "-----------b-----------------------b--------------------------------------------\n"
                "----------bb------bb--------------bb--------b-----------------------------------\n"
                "--------bbbbb----bbb------------bbbbbb-----b-b----------------------------------\n"
                "------bbbbbbbb--bb-b----------bbbbbbbbb----b-b----------------------------------\n"
                "--------bb--bb-bb-bb-------------bb--bb---bbb-----------------------------------\n"
                "-------bb--bbb-b-bb-------------bb--bbb---bbbbb---------------------------------\n"
                "-------bbbbbb-bbbb--------------bbbbbb-bbbbb------------------------------------\n"
                "------bbbbb---bbb-bb-b--bbb---bbbbbb-----bb--bbb--b-----------------------------\n"
                "------bbbb--bbbb-bb-bb-b--b----bbb--bbb-bbb-bb-b-bbb-b--------------------------\n"
                "-----bb-bbb--bb-bb-bb-bb-bb---bb---bb-b-bb-bb-bb-b-bbb--------------------------\n"
                "-----bb--bb-bb-bb-bb-bbbbb----bb-bbbbb-bb--bbbb-bb-bb---------------------------\n"
                "----bb---bb-bbbbbbbbbbbb-----bb---bb--bbb-bbb--bbb------------------------------\n"
                "----bb--bb--bbbbbbbbb-bb-b---bb---bb-bbbbbbbbbbbb-------------------------------\n"
                "----bbbbbb-----bb-bb---bb---bb----bbbb-bbb-bbb-bb-------------------------------\n"
                "--------------------------------------------------------------------------------")
        logo = logo.replace("-","w")
        self.print_image(logo,0,0)

        self.move_cursor(y=1,x=75)
        self.add_text(str(self.n)+"/9",fg="BLUE",bg="WHITE")
        self.move_cursor(y=3,x=68)
        self.add_text("  "+config.now().strftime("%A").upper()+"      ",fg="YELLOW",bg="RED")
        self.move_cursor(y=5,x=68)
        self.add_text("  "+config.now().strftime("%b %d").upper()+"      ",fg="YELLOW",bg="RED")

        self.move_cursor(x=0,y=8)

        if self.n == 1:
            self.add_title("Badges",font="size4", fg="BLACK", bg="BRIGHTWHITE")
            self.add_wrapped_text("Blue badges", fg="BLUE")
            self.add_wrapped_text(" are awarded for sending interesting letters, stories, makes, pictures, poems, good ideas for the programme, and for having appeared on Blue Peter.")
            self.add_newline()
            self.add_newline()
            self.add_wrapped_text("Green badges", fg="GREEN")
            self.add_wrapped_text(" are awarded for sending in letters, pictures and makes that are about the environment, conservation or nature.")
            self.add_newline()
            self.add_newline()
            self.add_wrapped_text("Silver badges", fg="BRIGHTWHITE")
            self.add_wrapped_text(" are awarded to blue badge holders who go on to make an extra effort.")
            self.add_newline()
            self.add_newline()
            self.add_wrapped_text("Orange badges", fg="ORANGE")
            self.add_wrapped_text(" are given to winners and runners up of Blue Peter competitions.")
            self.add_newline()
            self.add_newline()
            self.add_wrapped_text("Purple badges", fg="MAGENTA")
            self.add_wrapped_text(" are awarded for sending in a review of a Blue Peter episode. ")
            self.add_newline()
            self.add_newline()
            self.add_wrapped_text("Gold badges", fg="YELLOW")
            self.add_wrapped_text(" are very rare indeed.")
        if self.n == 2:
            self.add_title("Making Spaghetti",font="size4", fg="BLACK", bg="BRIGHTWHITE")
            self.add_title("           Bolognese",font="size4", fg="BLACK", bg="BRIGHTWHITE")
            self.add_text("YOU WILL NEED", fg="YELLOW")
            self.add_newline()
            self.add_text("- 400g lean beef mince (or veggie substitute)")
            self.add_newline()
            self.add_text("- 2 onions")
            self.add_newline()
            self.add_text("- 2 carrots")
            self.add_newline()
            self.add_text("- 2 sticks of celery")
            self.add_newline()
            self.add_text("- 2 cloves garlic")
            self.add_newline()
            self.add_text("- 2 springs of rosemary")
            self.add_newline()
            self.add_text("- 1 tbsp tomato puree")
            self.add_newline()
            self.add_text("- 400g tin chopped tomatoes")
            self.add_newline()
            self.add_text("- 400ml beef stock")
            self.add_newline()
            self.add_text("                                 CONTINUED on page 134 >>>>>>",fg="YELLOW")
        if self.n == 3:
            self.add_text("CONTINUED from page 133",fg="YELLOW")
            self.add_newline()
            self.add_text("- Small bunch of parsley")
            self.add_newline()
            self.add_text("- Fresh Parmesan")
            self.add_newline()
            self.add_text("- 300-350g dried spaghetti")
            self.add_newline()
            self.add_newline()
            self.add_text("METHOD", fg="YELLOW")
            self.add_newline()
            self.add_wrapped_text("1. Grab a grown up to help!", fg="YELLOW")
            self.add_newline()
            self.add_wrapped_text("2. Begin by chopping your carrots, celery, onions and garlic (always be careful with knives).")
            self.add_newline()
            self.add_wrapped_text("3. Heat up a splash of olive oil into a large pan and add the chopped onion, carrots, celery, garlic and rosemary.")
            self.add_newline()
            self.add_wrapped_text("4. Cook over a medium heat for 10 minutes until soft, turning occassionally.")
            self.add_newline()
            self.add_wrapped_text("5. Add the mince - seasoned with salt and pepper - and cook for a few minutes until browned.")
            self.add_newline()
            self.add_wrapped_text("6. Add the tomato puree, cook for a further 30 seconds and then pour in the chopped tomatoes and stock, bring to the boil and then reduce to a simmer.")
            self.add_newline()
            self.add_wrapped_text("7. Cover loosely with a lid and cook for 45 mins - 1 hour, giving the Bolognese a stir every 5-10 minutes.")
            self.add_newline()
            self.add_text("                                 CONTINUED on page 135 >>>>>>",fg="YELLOW")
        if self.n == 4:
            self.add_text("CONTINUED from page 134",fg="YELLOW")
            self.add_newline()
            self.add_wrapped_text("8. If the sauce is looking too thick add a little more water, if it’s looking too runny remove the lid and turn the heat down for a few minutes and allow it to thicken.")
            self.add_newline()
            self.add_wrapped_text("9. With 10 minutes to go, cook the pasta according to packet instructions.")
            self.add_newline()
            self.add_wrapped_text("10. Serve the Bolognese over the spaghetti and sprinkle with fresh parsley, a grating of fresh Parmesan and a grind of black pepper.")
            self.add_newline()
            self.add_wrapped_text("TOP TIP: You can also heat up the leftovers in the microwave later if you don't eat it all!",fg="YELLOW")
        if self.n == 5:
            self.add_title("Make a recycled",font="size4", fg="BLACK", bg="BRIGHTWHITE")
            self.add_title("    plastic bag kite",font="size4", fg="BLACK", bg="BRIGHTWHITE")
            self.add_text("YOU WILL NEED", fg="YELLOW")
            self.add_newline()
            self.add_text("- 24 Recycled straws")
            self.add_newline()
            self.add_text("- Recycled carrier bags")
            self.add_newline()
            self.add_text("- Sticky tape")
            self.add_newline()
            self.add_text("- String")
            self.add_newline()
            self.add_text("- Scissors ")
            self.add_newline()
            self.add_newline()
            self.add_text("METHOD", fg="YELLOW")
            self.add_newline()
            self.add_wrapped_text("1. Take 6 straws and cut off the ends just before the bend.")
            self.add_newline()
            self.add_text("                                 CONTINUED on page 137 >>>>>>",fg="YELLOW")
        if self.n == 6:
            self.add_text("CONTINUED from page 136",fg="YELLOW")
            self.add_newline()
            self.add_wrapped_text("2. Feed some string through 5 straws, then cut the string leaving about 10cm at either end.")
            self.add_newline()
            self.add_wrapped_text("3. Arrange the straws into a diamond shape, with one straw going across the middle.")
            self.add_newline()
            self.add_wrapped_text("4. Double knot the string at both sides of the diamond.")
            self.add_newline()
            self.add_wrapped_text("5. Feed some string through a new straw (Leaving about 10cm either side).")
            self.add_newline()
            self.add_wrapped_text("6. Attach the straw to the top of the diamond, then bring the bottom of the straw to the bottom of the diamond. You should be left with a pyramid shape.")
            self.add_newline()
            self.add_wrapped_text("7. Cut along the sides of a plastic bag so that it becomes flat.")
            self.add_newline()
            self.add_wrapped_text("8. Draw around the bottom of the pyramid.")
            self.add_newline()
            self.add_wrapped_text("9. Roll the pyramid onto its side and draw around it again (You should have a diamond shape drawn onto your plastic bag).")
            self.add_newline()
            self.add_wrapped_text("10. Draw 2cm tabs on the four sides of the diamond shape.")
            self.add_newline()
            self.add_wrapped_text("11. Cut out around your shape.")
            self.add_newline()
            self.add_wrapped_text("12. Fold over the tabs and tape to secure the bag to the kite.")
            self.add_newline()
            self.add_wrapped_text("13. Repeat this three times so you have four pyramids.")
            self.add_newline()
            self.add_text("                                 CONTINUED on page 138 >>>>>>",fg="YELLOW")
        if self.n == 7:
            self.add_text("CONTINUED from page 137",fg="YELLOW")
            self.add_newline()
            self.add_wrapped_text("14. In order to construct the kite, place 3 pyramids so 2 are in front and 1 is behind then one on top(they should look like little tents with open space on the front and bottom!).")
            self.add_newline()
            self.add_wrapped_text("15. Use the leftover string already on your kite to tie the pyramids together.")
            self.add_newline()
            self.add_wrapped_text("16. Gather the ends of the straws (that were originally cut off) and feed them onto a piece of string.")
            self.add_newline()
            self.add_wrapped_text("17. Cut the string once they are all fed through and tie the ends together so you have a long loop.")
            self.add_newline()
            self.add_wrapped_text("18. Then attach this onto the leftover string dangling from the bottom point at the back of the kite.")
            self.add_newline()
            self.add_wrapped_text("19. Feed a long piece of string through the loop on the top of the kite and the middle of the kite (at the back) and tie a knot.")
            self.add_newline()
            self.add_wrapped_text("20. Use this last piece of string to hold on to and get flying!")
        if self.n == 8:
            self.add_title("No-bake biscuits",font="size4", fg="BLACK", bg="BRIGHTWHITE")
            self.add_text("YOU WILL NEED", fg="YELLOW")
            self.add_newline()
            self.add_text("- 30 digestive biscuits")
            self.add_newline()
            self.add_text("- 15 glace cherries")
            self.add_newline()
            self.add_text("- Large handful of mini marshmallows")
            self.add_newline()
            self.add_text("- Handful of desiccated coconut")
            self.add_newline()
            self.add_text("- 2 tins condensed milk")
            self.add_newline()
            self.add_text("- Knife")
            self.add_newline()
            self.add_text("- Rolling pin")
            self.add_newline()
            self.add_text("- Deep tray (e.g. baking tray)")
            self.add_newline()
            self.add_newline()
            self.add_text("METHOD", fg="YELLOW")
            self.add_newline()
            self.add_wrapped_text("1. Crush the biscuits, and chop the cherries into small pieces. Grab a grown-up if you need help using a knife! You might find it easier to mix half of the ingredients first, then add the other half.")
            self.add_newline()
            self.add_text("                                 CONTINUED on page 140 >>>>>>",fg="YELLOW")
        if self.n == 9:
            self.add_text("CONTINUED from page 139",fg="YELLOW")
            self.add_newline()
            self.add_wrapped_text("TOP TIP: To crush the biscuits, try putting them in a freezer bag and gently bashing them with a mug or rolling pin.",fg="YELLOW")
            self.add_newline()
            self.add_wrapped_text("2. Mix in the marshmallows and coconut, then pour in the condensed milk and mix thoroughly.")
            self.add_newline()
            self.add_wrapped_text("3. Transfer the mixture into a deep tray. Using your rolling pin, push it flat into the tray so it’s squashed right down.")
            self.add_newline()
            self.add_wrapped_text("4. Leave in the fridge for an hour, then take it out and cut it into slices.")
            self.add_newline()
            self.add_wrapped_text("5. And you're done – share the gooey goodness with your friends and family!")
            self.add_newline()
            self.add_wrapped_text("TOP TIP: You could add a little bit of coconut on top for effect!",fg="YELLOW")

class DemonHeadmasterPage(Page):
    def __init__(self):
        super(DemonHeadmasterPage, self).__init__("141")
        self.title = "The Demon Headmaster"
        self.in_index = False

    def generate_content(self):
        self.add_title("look into my eyes",font="size4",fg="BLACK",bg="GREEN")
        demon =("--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "---------------------KKKKKKKKKK----------------KKKKKKKKKK-----------------------\n"
                "-------------------KK---gggg---KK------------KK---gggg---KK---------------------\n"
                "------------------K----ggkkgg----K----------K----ggkkgg----K--------------------\n"
                "------------------K----ggkkgg----K----------K----ggkkgg----K--------------------\n"
                "-------------------KK---gggg---KK------------KK---gggg---KK---------------------\n"
                "---------------------KKKKKKKKKK----------------KKKKKKKKKK-----------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n"
                "--------------------------------------------------------------------------------\n")
        self.print_image(demon,4,0)
        self.add_title("the demon",font="size4",fg="BLACK",bg="GREEN")
        self.add_title("       headmaster",font="size4",fg="BLACK",bg="GREEN")
        self.add_title("Tuesdays 3:10 BBC1",font="size4",fg="BLACK",bg="GREEN")

class ChucklePage(Page):
    def __init__(self):
        super(ChucklePage, self).__init__("142")
        self.title = "ChuckleVision"
        self.in_index = False

    def generate_content(self):
        self.add_title("C",fg="BLACK",bg="ORANGE",fill=False)
        self.move_cursor(y=2)
        self.add_title("h",fg="BLACK",bg="GREEN",fill=False,pre=7,font="size4")
        self.move_cursor(y=2)
        self.add_title("u",fg="BLACK",bg="BLUE",fill=False,pre=13,font="size4")
        self.move_cursor(y=2)
        self.add_title("c",fg="BLACK",bg="YELLOW",fill=False,pre=19,font="size4")
        self.move_cursor(y=2)
        self.add_title("k",fg="BLACK",bg="MAGENTA",fill=False,pre=25,font="size4")
        self.move_cursor(y=2)
        self.add_title("l",fg="BLACK",bg="ORANGE",fill=False,pre=31,font="size4")
        self.move_cursor(y=2)
        self.add_title("e",fg="BLACK",bg="GREEN",fill=False,pre=36,font="size4")
        self.move_cursor(y=0)
        self.add_title("V",fg="BLACK",bg="BLUE",fill=False,pre=42)
        self.move_cursor(y=2)
        self.add_title("i",fg="BLACK",bg="YELLOW",fill=False,pre=49,font="size4")
        self.move_cursor(y=2)
        self.add_title("s",fg="BLACK",bg="MAGENTA",fill=False,pre=51,font="size4")
        self.move_cursor(y=2)
        self.add_title("i",fg="BLACK",bg="ORANGE",fill=False,pre=56,font="size4")
        self.move_cursor(y=2)
        self.add_title("o",fg="BLACK",bg="GREEN",fill=False,pre=59,font="size4")
        self.move_cursor(y=2)
        self.add_title("n",fg="BLACK",bg="BLUE",fill=False,pre=64,font="size4")

        self.move_cursor(x=0,y=7)

        fs = [self.barry,self.paul]
        shuffle(fs)

        self.add_newline()
        fs[0]()

        fs[1]()
        self.add_newline()

    def barry(self):
        self.add_title("Barry Chuckle",fg="BLACK",bg="ORANGE",font="size4")
        likes = ["Sweets","Some work","Gran the Van","Chocolate eclairs","Scones with jam and cream","Banana custard"]
        dislikes = ["Going to the dentist","Scary stuff and ghosts","Gorillas","Heights"]

        shuffle(likes)
        shuffle(dislikes)

        self.add_text("Likes",fg="RED")
        self.move_cursor(x=38)
        self.add_text("Dislikes",fg="RED")
        self.add_newline()
        for i,j in zip(likes[:4], dislikes[:4]):
            self.add_text(i)
            self.move_cursor(x=38)
            self.add_text(j)
            self.add_newline()

    def paul(self):
        self.add_title("Paul Chuckle",fg="BLACK",bg="ORANGE",font="size4")
        likes = ["Annoying Barry","Doughnuts & Sweets","Being the boss or leader",
                 "Inventing","Relaxing with a cup of tea","Standing up for himself",
                 "Barry (sometimes)","Having a rest while Barry works"]
        dislikes = ["When Barry gets what he wants","Spiders","Work","Getting blamed",
                    "Getting told what to do","Barry's stupid side","People berating Barry","Mr No Slacking"]

        shuffle(likes)
        shuffle(dislikes)

        self.add_text("Likes",fg="RED")
        self.move_cursor(x=38)
        self.add_text("Dislikes",fg="RED")
        self.add_newline()
        for i,j in zip(likes[:4], dislikes[:4]):
            self.add_text(i)
            self.move_cursor(x=38)
            self.add_text(j)
            self.add_newline()


class PlaydaysPage(Page):
    def __init__(self):
        super(PlaydaysPage, self).__init__("143")
        self.importance = 3
        self.title = "Playdays"
        self.in_index = False

    def generate_content(self):
        self.add_title("P",fill=False,fg="BLACK",bg="RED")
        self.move_cursor(y=0)
        self.add_title("l",fill=False,fg="BLACK",bg="BLUE",pre=8)
        self.move_cursor(y=0)
        self.add_title("a",fill=False,fg="BLACK",bg="YELLOW",pre=15)
        self.move_cursor(y=0)
        self.add_title("y",fill=False,fg="BLACK",bg="RED",pre=23)
        self.move_cursor(y=0)
        self.add_title("d",fill=False,fg="BLACK",bg="BLUE",pre=31)
        self.move_cursor(y=0)
        self.add_title("a",fill=False,fg="BLACK",bg="YELLOW",pre=39)
        self.move_cursor(y=0)
        self.add_title("y",fill=False,fg="BLACK",bg="RED",pre=47)
        self.move_cursor(y=0)
        self.add_title("s",fill=False,fg="BLACK",bg="BLUE",pre=55)

        bus = ( "--rrrrrrrrrrrrrrrr--\n"
                "--rrrrbbbbrrrrbbbb--\n"
                "--rrrrbbbbrrrrbbbb--\n"
                "--rrrrbbbbrrrrbbbb--\n"
                "--rrrrrrrrrrrrrrrr--\n"
                "--rrKKKrrrrKKKrrrr--\n"
                "--rrKrKrrrrKrKrrrr--\n"
                "----KKK----KKK------")
        self.print_image(bus,7,0)

        pop = ( "-yyyy-\n"
                "yyyyyy\n"
                "yyyyyy\n"
                "-yyyy-\n"
                "--KK--\n"
                "--KK--\n"
                "--KK--\n"
                "--KK--")
        self.print_image(pop,11,50)

        self.move_cursor(x=20,y=7)
        self.add_text("It's the Playbus!")
        self.move_cursor(x=20,y=9)
        self.add_text("But where does it go?")
        self.move_cursor(x=20,y=11)
        self.add_text("Where does it stop?")
        self.move_cursor(x=20,y=13)
        self.add_text("Watch the sign on the lollipop!")
        self.move_cursor(x=20,y=15)
        n = randrange(7)
        if n == 0:
            self.add_text("It's the Why Bird stop!")
            img = ( "-----------------------------------------------------\n"
                    "----------------------KrrrrrrrrrrK-------------------\n"
                    "---------------------KwwwKrrrrKwwwK------------------\n"
                    "---------------------KwkwKKrrKKwkwK------------------\n"
                    "---------------------KwwwKyyyyKwwwK------------------\n"
                    "---------------------rrrrKykkyKrrrr------------------\n"
                    "----------------------KKKKyyyyKKKK-------------------\n"
                    "-----------------------KKKKKKKKKK--------------------\n"
                    "-----------------------KKKKKKKKKK--------------------\n"
                    "----------------------yyyyyyyyyyyy--------------------\n"
                    "----------------------yyyyyyyyyyyy-------------------\n"
                    "----------------------KKKKKKKKKKKK-------------------\n"
                    "--------------------ggKKKKKKKKKKKKgg-----------------\n"
                    "-------------------gggyyyyyyyyyyyyggg----------------\n"
                    "-----------------gggggyyyyyyyyyyyyggggg--------------\n"
                    "----------------gggg--KKKKKKKKKKKK--gggg-------------\n"
                    "----------------ggg---KKKKKKKKKKKK---ggg-------------\n"
                    "----------------------yyyyyyyyyyyy-------------------\n"
                    "----------------------yyyyyyyyyyyy-------------------\n"
                    "----------------------KKKKKKKKKKKK-------------------\n"
                    "----------------------KKKKKKKKKKKK-------------------\n"
                    "----------------------yyyyyyyyyyyy-------------------")
        if n == 1:
            self.add_text("It's the playground stop!")
            img = ( "-----------------------------------------------------\n"
                    "-----------------------------------------------------\n"
                    "-----------------------------------------------------\n"
                    "--------yyyyyyybbbbbbbb------------------------------\n"
                    "-------yyyyyyy---------b-----------------------------\n"
                    "------yyyyyyyrrrrrrrrrrrb----------------------------\n"
                    "-----b-------------------b---------------------------\n"
                    "-----bbbbbbbbbbbbbyyyybbbb---------------------------\n"
                    "-----r------------y--y---r---------------------------\n"
                    "-----r------------y--y---r---------------------------\n"
                    "-----r------------yyyy---r---------------------------\n"
                    "-----r------------y--y---rbb-------------------------\n"
                    "-----r------------y--y---rbbbb-----------------------\n"
                    "-----r------------yyyy---rbbbbyy---------------------\n"
                    "-----rrrrrrrrrrrrryrryrrrrbbbbyyyy-------------------\n"
                    "-----r------------y--y---r--bbyyyyrr-----------------\n"
                    "-----r------------yyyy---r----yyyyrrrr---------------\n"
                    "-----r------------y--y---r------yyrrrrgg-------------\n"
                    "-----r------------y--y---r--------rrrrgggg-----------\n"
                    "-----r------------yyyy---r----------rrggggrr---------\n"
                    "-----r------------y--y---r------------ggggrrrr-------\n"
                    "-----r------------y--y---r--------------ggrrrrrrrr---")
        if n == 2:
            self.add_text("It's the Dot stop!")
            img = ( "-----------------------------------------------------\n"
                    "-----------------------------------------------------\n"
                    "------------------gg---------------------------------\n"
                    "------------------gg---------------------------------\n"
                    "-----------------------------------------------------\n"
                    "-----------------------------------------------------\n"
                    "-------------------------------------rr--------------\n"
                    "-------------------------------------rr--------------\n"
                    "-----------------------------------------------------\n"
                    "----------------------rr-----------------------------\n"
                    "----------------------rr-----------------------------\n"
                    "-----------------------------------------------------\n"
                    "----------------------------------bb-----------------\n"
                    "----------------------------------bb-----------------\n"
                    "-----------yy----------------------------------------\n"
                    "-----------yy----------------------------------------\n"
                    "-----------------------------------------------------\n"
                    "--------------------------------------bb-------------\n"
                    "-------------------oo-----------------bb-------------\n"
                    "-------------------oo--------------------------------\n"
                    "-----------------------------------------------------\n"
                    "-----------------------------------------------------")
        if n == 3:
            self.add_text("It's the roundabout stop!")
            img = ( "--------------------------------yy-------------------\n"
                    "--------------------------y----yyy-------------------\n"
                    "--------------------------yy--yyyy-------------------\n"
                    "--------------ooo---------yyy-yyyy-------------------\n"
                    "--------------ooo--ggg----yyy-yyyy-------------------\n"
                    "--------------oyybbggg----yyy-yyyy-------------------\n"
                    "---------------yybbgggyyyyyyyyyyyyyyy----------------\n"
                    "---------------yrrrbykkkkyyyyyyyyyyyy----------------\n"
                    "----------------rrryyyyyykkkkkyyyyyyy----------------\n"
                    "----------------rrrkkyyyyyyyykkkkkyyy----------------\n"
                    "------------------yyykkkyyyyyyyyyyyyy----------------\n"
                    "------------rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr----------\n"
                    "------------yyyyyyyywyyyyyyyyyyyyywyyyyyyyy----------\n"
                    "------------yyyoooyyryyyyyyryyyyyyryyyybbyy----------\n"
                    "------------yyyoyoyywyyyyrrrrryyyywyyrrbbyy----------\n"
                    "------------yyyoyoyyryyyyyrrryyyyyryyrrybyy----------\n"
                    "------------yyyoyoyywyyyyrryrryyyywyyyyyyyy----------\n"
                    "------------yyyoyoyyryyyyyyyyyyyyyryyyyyyyy----------\n"
                    "----------ggggggggggggggggggggggggggggggggggg--------\n"
                    "----------ggggggggggggggggggggggggggggggggggg--------\n"
                    "--------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb------\n"
                    "--------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb------")
        if n == 4:
            self.add_text("It's the Patch stop!")
            img = ( "-----------------------------------------------------\n"
                    "--------------------bbbbbbbbb------------------------\n"
                    "-------------------bWbbbbbbbbb-----------------------\n"
                    "------------------bmbbbbbbbbbbb----------------------\n"
                    "------------------WKKwwwwwwwwKK----------------------\n"
                    "-------------------wwwKwwwKwww-----------------------\n"
                    "--------------------wwwwrwwww------------------------\n"
                    "---------------------wwwwwww-------------------------\n"
                    "----------------------wwwww--------------------------\n"
                    "---------------rrrrrrrrrrrrrmmrrrr-------------------\n"
                    "---------------rrrrrrrrrrrrmmrrrrr-------------------\n"
                    "--------------------rrrrrrmmr------------------------\n"
                    "--------------------rrrrmmmrr------------------------\n"
                    "--------------------rrmmmrrrr------------------------\n"
                    "--------------------rmmrrrrrr------------------------\n"
                    "--------------------mmrrrrrrr------------------------\n"
                    "--------------------rrr---rrr------------------------\n"
                    "--------------------rrr---rrr------------------------\n"
                    "--------------------KKK---KKK------------------------\n"
                    "--------------------KKK---KKK------------------------\n"
                    "--------------------KKK---KKK------------------------\n"
                    "-----------------------------------------------------")
        if n == 5:
            self.add_text("It's the Poppy stop!")
            img = ( "-----------------------------------------------------\n"
                    "-------------------oo--------------oo----------------\n"
                    "-------------------ooo------------ooo----------------\n"
                    "-------------------oooo----------oooo----------------\n"
                    "-------------------oooooooooooooooooo----------------\n"
                    "-------------------oooooooooooooooooo----------------\n"
                    "-------------------oggKggooooooggKggo----------------\n"
                    "-------------------oggKggooooooggKggo----------------\n"
                    "------------------ogggKgggoooogggKgggo---------------\n"
                    "------------------ogggKgggoooogggKgggo---------------\n"
                    "------------------ooggKggooooooggKggoo---------------\n"
                    "------------------ooggKggooooooggKggoo---------------\n"
                    "------------------oooooooommmmoooooooo---------------\n"
                    "------------------oooooooommmmoooooooo---------------\n"
                    "------------------wwwwwwwwmmmmwwwwwwww---------------\n"
                    "------------------wwwwwwwwmmmmwwwwwwww---------------\n"
                    "-------------------wwwwwwwwmmwwwwwwww----------------\n"
                    "-------------------wwwwwwwwmmwwwwwwww----------------\n"
                    "----------------------wwwwwwwwwwww-------------------\n"
                    "----------------------wwwwwwwwwwww-------------------\n"
                    "------------------------wwwwwwww---------------------\n"
                    "-----------------------------------------------------")
        if n == 6:
            self.add_text("It's the tent stop!")
            img = ( "------------------------ww---------------------------\n"
                    "------------------------ww---------------------------\n"
                    "-----------------------wwww--------------------------\n"
                    "----------------------wwwwww-------------------------\n"
                    "---------------------wwwwwwww------------------------\n"
                    "--------------------wwwwwwwwww-----------------------\n"
                    "--------------------BBBBBBBBBB-----------------------\n"
                    "-------------------wwwwwwwwwwww----------------------\n"
                    "------------------wwwkwwwwwwkwww---------------------\n"
                    "------------------wwwwwwrrwwwwww---------------------\n"
                    "------------------wwwwwrrrrwwwww---------------------\n"
                    "-------------------wwwwrrrrwwww----------------------\n"
                    "---------------------wwwrrwww------------------------\n"
                    "--yy----------wwwwwwwwwwwwwwwwwwwwww----------yy-----\n"
                    "---yy------wwwwwwwwwwwwwwwwwwwwwwwwwwww------yy------\n"
                    "-yyyyyyyyyywwwwwwwwwwwwwwwwwwwwwwwwwwwwyyyyyyyyyy----\n"
                    "---yy---wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww---yy------\n"
                    "--yy----wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww----yy-----\n"
                    "--------wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww-----------\n"
                    "--------wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww-----------\n"
                    "---------wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww------------\n"
                    "-----------wwwwwwwwwwwwwwwwwwwwwwwwwwww--------------")
        self.print_image(img,16,10)

class CrackerjackPage(Page):
    def __init__(self):
        super(CrackerjackPage, self).__init__("144")
        self.title = "Crackerjack"
        self.in_index = False

    def generate_content(self):
        self.move_cursor(y=5)
        self.add_text("It's Friday, it's five to five... it's...")
        self.add_title("CRACKERJACK!",fg="BLACK",bg="RED")

class PaddingtonPage(Page):
    def __init__(self):
        super(PaddingtonPage, self).__init__("145")
        self.title = "Paddington Bear"
        self.in_index = False

    def generate_content(self):
        self.add_title("Please look",fg="BLACK",bg="WHITE")
        self.add_title("after this",fg="BLACK",bg="WHITE")
        self.add_title("bear",fg="BLACK",bg="WHITE")
        img = ( "------------------rrrrrrrr--------------\n"
                "------------------rrrrrrrr--------------\n"
                "----------------rrrrrrrrrrr-------------\n"
                "----------------rrrrrrrrrrr-------------\n"
                "-------------rrrrrrrrrrrrrrrrr----------\n"
                "-------------rrrrrrrrrrrrrrrrr----------\n"
                "------------rrrrrrrrrrrrrrrrrrr---------\n"
                "------------rrrrrrrrrrrrrrrrrrr---------\n"
                "------------rrrrrrrrrrrrrrrrrrr---------\n"
                "------------rrrrrrrrrrrrrrrrrrr---------\n"
                "-----------rrrrrooooooooooorrrr---------\n"
                "-----------rrrrooooooooooooorrr---------\n"
                "-----------rrrrooKKoooooKKoorrr---------\n"
                "------------rrrooKKoooooKKoorr----------\n"
                "--------------roooooKKKooooor-----------\n"
                "-------------bbooooooKoooooobb----------\n"
                "---------bbbbbbooooooKoooooobbbbbb------\n"
                "-------bbbbbbbboKooooKooooKobbbbbbbb----\n"
                "-------bbbbbbbboooKKKKKKKooobbbbbbbb----\n"
                "-------bbbbbbbbooooooooooooobbbbbbbb----\n"
                "---------bbbbbbbooooooooooobbbbbbb------\n"
                "----------bbbbbbbbooooooobbbbbbbb-------\n"
                "----------bbbbbbbbbbbbbbbbbbbbbbb-------\n"
                "--------bbbbbbbbbbbbbbbbbbbbbbbbbbb-----\n"
                "-------bbbbbbbbbbbbbbobbbbbbbbbbbbbb----\n"
                "------bbbbbbbbbbbbbbbobbbbbbbbbbbbbbb---\n"
                "------bbbbbbbbbbbbbbooobbbbbbbbbbbbbb---\n"
                "------bbbbb-bbbbbbbbbobbbbbbbbb-bbbbb---")
        self.print_image(img,13,40)

class WackyRacesPage(Page):
    def __init__(self):
        super(WackyRacesPage, self).__init__("146")
        self.title = "Wacky Races"
        self.in_index = False

    def generate_content(self):
        self.add_title("Wacky Races")
        racers = [
            ("The Slag Brothers","The Boulder Mobile"," 1"),
            ("The Gruesome Twosome","The Creepy Coupe"," 2"),
            ("Professor Pat Pending","The Convert-a-Car"," 3"),
            ("Red Max","The Crimson Haybailer"," 4"),
            ("Penelope Pitstop","The Compact Pussycat"," 5"),
            ("Sergeant Blast and Private Meekly","The Army Surplus Special"," 6"),
            ("The Ant Hill Mob","The Bulletproof Bomb"," 7"),
            ("Lazy Luke","The Arkansas Chugabug"," 8"),
            ("Peter Perfect","The Turbo Terrific"," 9"),
            ("Rufus Ruffcut","The Buzz Wagon","10")
          ]
        dast = ("Dick Dastardly and Mutley","The Mean Machine","00")
        shuffle(racers)
        winner = racers[0]
        racers = racers[1:] + [dast]
        shuffle(racers)
        racers = [("Driver","Car","No"),winner] + racers
        self.add_title("Result",font="size4bold",fg="BLACK",bg="BRIGHTWHITE")
        dnf = randrange(6,20)
        for i,(driver,car,no) in enumerate(racers):
            color = "WHITE"
            if i==0:
                color = "CYAN"
                i = "Pos"
            elif i > dnf:
                i = "DNF"
            self.move_cursor(x=0)
            self.add_text(str(i),fg=color)
            self.move_cursor(x=4)
            self.add_text(driver,fg=color)
            self.move_cursor(x=40)
            self.add_text(car,fg=color)
            self.move_cursor(x=70)
            self.add_text(no,fg=color)
            self.add_newline()

class OtisPage(Page):
    def __init__(self):
        super(OtisPage, self).__init__("147")
        self.title = "Otis's Joke Page"
        self.importance = 3
        self.in_index = False

    def generate_content(self):
        self.add_title(" Otis's Joke page",fg="BLACK",bg="GREEN",font='size4bold')
        self.print_image(
            #0    5   10   15   20   25   30   35   40
            "-----ooooo--------------------oooooooo---\n" #0
            "-oooooooooooooo-------------oooooooooooo-\n"
            "ooooooooooooooooo----------oooooooooooooo\n"
            "ooooooooooooooooo---------ooooooooooooooo\n"
            "ooooooooooooooooo---------ooooooooooooooo\n"
            "oooooooooooooooooo------ooooooooooooooooo\n" #5
            "oooooooooooooooooo------ooooooooooooooooo\n"
            "-oooooooooooooooooo-----ooooooooooooooooo\n"
            "-oooooooooooooooooo-----ooooooooooooooooo\n"
            "-ooooooooooooooooooo----oooooooooooooooo-\n"
            "--oooooooooooooooooo---ooooooooooooooooo-\n" #10
            "---ooooooooooooooooo---oooooooooooooooo--\n"
            "-----oooooooooooooooo--oooooooooooooooo--\n"
            "------oooooooooooooooo-ooooooooooooooo---\n"
            "------oooooooooooooooo-oooooooooooooo----\n"
            "-------ooooooooooooooorrroooooooooooo----\n" #15
            "-------oooooooooorrrrrrrrrrrroooooooo----\n"
            "--------ooooooorrrrrrrrrrrrrrrooooooo----\n"
            "----------ooooorrrrrrrrrrrrrrrroooooo-------------------------------------------\n"
            "----------ooooorrrrrrrrrrrrrrrroooooo--------wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww-\n"
            "-----------ooooroowwoooooowwrrroooooo-------wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"  #20
            "-------------oooowkkwoooowkkwrroooooo-------wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
            "-------------oooowkkwoooowkkworroooo--------wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
            "---------------ooooooooooooooooroo----------wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
            "---------------oooooooooooooooor-----------wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
            "--------------ooooooooooooooooooo--------wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n" #25
            "--------------ooooooooooooooooooo------wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n"
            "--------------ooooooookookooooooo----wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww-\n"
            "--------------ooooooookookooooooo--wwwwww---------------------------------------\n"
            "--------------oookoooooooooookooo-www-------------------------------------------\n"
            "--------------oookkoooooooookkkoo----yyyyy--------------------------------------\n" # 30
            "--------------ooookkkkkkkkkkkoooo------yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-\n"
            "--------------ooooookkpppkkoooooo--------yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
            "--------------oooooookkppkooooooo-----------yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
            "--------------ooooooookppkooooooo-----------yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
            "--------------ooooooookppkooooooo-----------yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n" #35
            "---------------oooooookppkoooooo------------yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
            "----------------oooooooppoooooo-------------yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
            "-----------------ooooookkooooo--------------yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
            "------------------ooooooooooo----------------yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-\n"
            "---------------------ooooo------------------------------------------------------\n"
            "--------------------------------------------------------------------------------",5,0
          )
        joke = choice([
            ("What's brown and sticky?",                                    "A stick!"),
            ("What did the the drummer call his  twin daughters?",          "Anna one, Anna two!"),
            ("What do you call a bear without    any teeth?",               "A gummy bear!"),
            ("Why did the golfer change his      socks?",                   "Because he got a hole in one!"),
            ("What do you get when you cross a   snowman with a vampire?",  "Frostbite"),
            ("Why did Cinderella get kicked off  the football team?",       "Because she kept running from the  ball!"),
            ("What time did the man go to the    dentist?",                 "Tooth hurt-y!"),
            ("What do you call someone with no   body and no nose?",        "Nobody knows!"),
            ("What is the loudest pet?",                                    "A trumpet!"),
            ("What do you call a fish with no    eye?",                     "A fsh!")
          ])
        self.move_cursor(y=15,x=45)
        self.add_wrapped_text(joke[0],pre=45,fg="BLACK",bg="WHITE")

        self.move_cursor(y=21,x=45)
        self.add_wrapped_text(joke[1],pre=45,fg="BLACK",bg="YELLOW")

class TorchyPage(Page):
    def __init__(self):
        super(TorchyPage, self).__init__("148")
        self.title = "Torchy the Battery Boy"
        self.importance = 5
        self.in_index = False

    def generate_content(self):
#        self.add_title(" Otis's Joke page",fg="BLACK",bg="GREEN",font='size4bold')
        self.add_text("""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%@@@@#,...,#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%#%%##@**/*****,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%##%#%%%(,,*****,,,...../@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&&%%%%%%%%%%%%%%##&&&.,*&@##**,,.....,/(#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@&&@@@&&%%&&%%&&%%%%%%#%&%.,*&@%/#**,.....,/(((%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@&&&&&&&&%%%%%%%%%#%%(**,,.,*##/,,.......*((%%#%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@&&&&&&&%(/((#/***///**/**,..,,,,.......,*/**&&%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@&%&&%#///******//****,**,,,,*,,,,,....,*/*****/*/&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%#//(#//***********,,,*/*,,,,,,,,,,...,,,,,*,,,,,,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@#///////***///*,*******((***,,,,,,,,,,,,.,,,,,,,,,,*(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@%////****/(#///*/*//*****,,*,,,,***,,,*#/*,,**,,,,,,#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@&///*//(&&(***/(/,,,,,,,,*/(*,,//*,,*(//,,,/#/,,,,/&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@**//**(%*,**,,,(/,,,,/////***/******,,,,///(,,*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@%***//**,***,,,,***,%%/,*,*#%%%%##(#(****#/**@@%#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@#***//*******,,*/#%(/*****//##&&%%%%/*#***,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@***//****,,*/&@%(&@@#/**//((####(**/(%@#*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@%*///***/*,,/@,,,#&(/&((*,,,,,/((/*%@%/,,%%,%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@(/(/(#%%(/*,(@///%((*,,**#%/*,,(/%,%&/&(,*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@(%%&%%##/(/,,,%&&/,.,,,,/(,,,,.,,%#/(&%,,*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&%##%%%&&(///**,,*#&%###*,,,,,...*//**#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&%%##/((#&%%%%#/*/(#//**#***,,,,,,,*,**%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&%%@%%&%%&((/*****/#(,,*#((/***/(#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@&%%&@@*(#*****/*,,...,,,*///***%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@%%#/**////(&&@@&&&@@(&%##%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%%@%((//**//((////////(%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@&%%&@@@@@@@@@@@@@@@@%%%@@(///////****/#%%#*//&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
(((&@@@&&&&&@@@@@@@@&&@@/****/(#(#%%%&%%&@@@@@@@@@@@@@@@@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#%##%#(((((%%@@@@@@@@@@#****,,,*,,,*@@#((/(&&&&%(/*/#@%%@#(((/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
%%%&#(#%&@@@@#((/#%@/*********(@@(#(////((%&&&%&&(%(/(///#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##%@####%%@@@%(((/****,*(***/(&&,,**//*///(#&@@@@&%&&((///#((**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##%&%@##((#%#@@@&((/***,...,,,......,*//*//(&@@@@%(%&@%((((/*****,&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##%%&@@%######%%&@@&(((*/*,,,,,,,,,,,,*////%@@@@((#&&@####(//*******@@@@@@@@@@@@@,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
%%%%@@%%###(#%#@@@&(((///,,**,,,,***((##@@@@@###(#&&@@#(#(////******,@@@@@@@@@@/*,,,/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
%@@@@&%%%%%#(%##&@@@#(/(/*,,,,,,,,**(%@@@@((((#%&&@@@#((///////*****%@@@@@&*******,,%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#%@@@@@&%%#%%%(##%%&@@@%/(/*****,,,**/%@@@@%#(((###&&@@@@%(/////////*****(@@@***,*******/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
%%@@@@@@&%%##%#####&&@@@%/(#(*/**,***#@@@&#####&&&@@@@@%(//////////*****(*,,*/**/////*,,@@@@@@@""")

page01 = CBBCPage()
page02 = NewsroundPage()
page03 = BluePeterPage(1)
page04 = BluePeterPage(2)
page05 = BluePeterPage(3)
page06 = BluePeterPage(4)
page07 = BluePeterPage(5)
page08 = BluePeterPage(6)
page09 = BluePeterPage(7)
page10 = BluePeterPage(8)
page11 = BluePeterPage(9)
page12 = DemonHeadmasterPage()
page13 = ChucklePage()
page14 = PlaydaysPage()
page15 = CrackerjackPage()
page16 = PaddingtonPage()
page17 = WackyRacesPage()
page18 = OtisPage()
page19 = TorchyPage()

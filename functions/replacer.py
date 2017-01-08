import re
from sweep import sweepstake_people

def escape(string):
    if string=="?":
        return "\?"
    return string

def klb_replace(imput):
    swaps = [
            ["Breakfast","Belgin Breakfast"],
            ["Not",u"\u00AC"],
            ["The One Show","The Olly Show"],
            ["Wright","Mart Wright"],
            ["Sport","Maths"],["Sportsday","Mathsday"],
            ["Jamie","Pietro"],
            ["Trump","Twat"],
            ["Theresa May","Theresa June"],
            ["Boris Johnson","Boris Jebend"],
            ["Farage","Bellend"],
            ["Brexit","Moon Landing"],
            ["Agents of S\.H\.I\.E\.L\.D\.","Mathematicians of U.C.L.K.L.B"],
            ["USA","KLB"],
            ["BBC","KLB"],
            ["A&E","KLB"],
            ["Builder","Constructor"],
            ["World","KLB"],
            ["Home","KLB"],
            ["Homes","KLBs"],
            ["Cwm","KLB"],
            ["Have I","Has Jigsaw"],["I","Jigsaw"],["Me","Jigsaw"],["I'm","Jigsaw is"],
            ["You","Belgin"],
            ["Week","Weak"],
            ["Raymond","Belgin"],
            ["He","Adam"],["Him","Adam"],
            ["She","Anna"],["Her","Anna"],
            ["It","Scroggsbot"],
            ["We","The West Wingers"],["Us","The West Wingers"],
            ["They","The EastEnders"],["Them","The EastEnders"],
            ["Man","Olly"],["Men","Ollys"],
            ["News","News (presented by Sam Brown)"],
            ["Newyddion","Newyddion (a gyflwynwyd gan Sam Brown)"],
            ["Mother","Supervisor"],["Father","Supervisor"],
            ["8 out of 10","0.8"],
            ["Movie","chalkdust"],["Film","chalkdust"],["Family","chalkdust"],
            ["Castle","Mathematics Mezzanine"],
            ["Mrs Brown","Rafael"],
            ["Alan Carr","Olly Southwick"],
            ["Casualty","Causality"],
            ["Match","Maths"],
            ["Christmas","Oxmas"],
            ["Football","Maths"],["Rugby","Maths"],["Tennis","Maths"],["Golf","Maths"],
            ["Cycling","Maths"],["Athletics","Maths"],
            ["Wallace","Crazy Nico"],
            ["Politics","Mathematics"],
            ["Political","Mathematical"],
            ["Stacey","Huda"],
            ["Antiques","Statistics"],
            ["Santa","Huda"],
            ["Ben","Momchil"],
            ["Holly","Antonio"],
            ["Deal","Soheni"],
            ["The Tribe","Pietro's Pick: The Tribe"],
            ["Teenage Mutant Ninja Turtles","Belgin's Pick: Teenage Mutant Ninja Turtles"],
            ["X-Men Origins","X-Men Origins Seminar Room"],
            ["Bruce","Rafael"]
        ]
    for swap in swaps:
        imput = re.sub("(^|[^A-Za-z])"+swap[0]+"($|[^A-Za-z])(?i)",r"\1"+swap[1]+r"\2",imput)
    return imput


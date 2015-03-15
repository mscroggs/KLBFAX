from fonts.LetterBlock import LetterBlock
from fonts.exceptions import LetterNotDefined

alphabet = {}


def _add(letter, string):
    global alphabet
    alphabet[letter] = LetterBlock(string.strip())

_add("|", """
x
x
x
x
x
x
x
""")

_add("A", """
xxxxxxxx
xxx  xxx
xx    xx
xxxxxxxx
xx    xx
x      x
xxxxxxxx
""")

_add("C", """
xxxxxxxx
x      x
x  xxxxx
x  xxxxx
x  xxxxx
x      x
xxxxxxxx
""")

_add("I", """
xxxx
x  x
x  x
x  x
x  x
x  x
xxxx
""")

_add("E", """
xxxxxxxx
x      x
x  xxxxx
x    xxx
x  xxxxx
x      x
xxxxxxxx
""")

_add("P", """
xxxxxxxx
x     xx
x  xx  x
x     xx
x  xxxxx
x  xxxxx
xxxxxxxx
""")

_add("S", """
xxxxxxxx
x      x
x  xxxxx
x      x
xxxxx  x
x      x
xxxxxxxx
""")

_add("U", """
xxxxxxxx
x  xx  x
x  xx  x
x  xx  x
x  xx  x
x      x
xxxxxxxx
""")

_add("R", """
xxxxxxxxx
x      xx
x  xx   x
x     xxx
x  xx  xx
x  xxx  x
xxxxxxxxx
""")

def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError as e:
        raise LetterNotDefined(e)

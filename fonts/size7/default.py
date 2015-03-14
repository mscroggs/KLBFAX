import fonts.Letter

class LetterNotDefined(Exception):
    pass

alphabet = {}

def _add(letter, string):
    global alphabet
    alphabet[letter] = string.strip()

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

def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError as e:
        raise LetterNotDefined(e)

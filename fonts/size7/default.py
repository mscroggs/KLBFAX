from fonts.LetterBlock import LetterBlock
from fonts.exceptions import LetterNotDefined

SIZE = 7
alphabet = {}


def _add(letter, string):
    global alphabet
    letter_str = string.strip()
    assert len(letter_str.split("\n")) == SIZE
    alphabet[letter] = LetterBlock(letter_str)

_add("|", """
x
x
x
x
x
x
x
""")

_add("-", """
xxxxx
xxxxx
xxxxx
x   x
xxxxx
xxxxx
xxxxx
""")

_add("!", """
xxx
  x
  x
  x
xxx
  x
xxx
""")

_add("/", """
xxxxxx
xxxx x
xxx xx
xx xxx
x xxxx
 xxxxx
xxxxxx
""")

_add(" ","""
xxx
xxx
xxx
xxx
xxx
xxx
xxx
""")

_add("A", """
xxxxxxxx
xx   xxx
x xxx xx
       x
  xxx  x
  xxx  x
xxxxxxxx
""")

_add("B", """
xxxxxxx
     xx
  xx  x
    xxx
  xx  x
     xx
xxxxxxx
""")

_add("C", """
xxxxxxx
      x
  xxxxx
  xxxxx
  xxxxx
      x
xxxxxxx
""")

_add("D", """
xxxxxxx
     xx
  xx  x
  xx  x
  xx  x
     xx
xxxxxxx
""")

_add("E", """
xxxxxxx
      x
  xxxxx
    xxx
  xxxxx
      x
xxxxxxx
""")

_add("F", """
xxxxxxx
      x
  xxxxx
    xxx
  xxxxx
  xxxxx
xxxxxxx
""")

_add("G", """
xxxxxxx
      x
  xxxxx
  x   x
  xx  x
      x
xxxxxxx
""")

_add("H", """
xxxxxxx
  xx  x
  xx  x
      x
  xx  x
  xx  x
xxxxxxx
""")

_add("I", """
xxx
  x
xxx
  x
  x
  x
xxx
""")

_add("J", """
xxxxx
xx  x
xx  x
xx  x
xx  x
    x
xxxxx
""")

_add("K", """
xxxxxxx
  xx  x
  x  xx
    xxx
  x  xx
  xx  x
xxxxxxx
""")

_add("L", """
xxxxxxx
  xxxxx
  xxxxx
  xxxxx
  xxxxx
      x
xxxxxxx
""")

_add("M", """
xxxxxxxxxxx
   xxxx   x
    xx    x
  x    x  x
  xx  xx  x
  xxxxxx  x
xxxxxxxxxxx
""")

_add("N", """
xxxxxxxx
   xx  x
    x  x
  x    x
  xx   x
  xxx  x
xxxxxxxx
""")

_add("O", """
xxxxxxxx
       x
  xxx  x
  xxx  x
  xxx  x
       x
xxxxxxxx
""")

_add("P", """
xxxxxxx
     xx
  xx  x
     xx
  xxxxx
  xxxxx
xxxxxxx
""")

_add("Q", """
xxxxxxxxx
       xx
  xxx  xx
  x    xx
  xx   xx
        x
xxxxxx  x
""")

_add("R", """
xxxxxxxx
      xx
  xx   x
     xxx
  xx  xx
  xxx  x
xxxxxxxx
""")

_add("S", """
xxxxxxx
      x
  xxxxx
      x
xxxx  x
      x
xxxxxxx
""")

_add("T", """
xxxxxxx
      x
xx  xxx
xx  xxx
xx  xxx
xx  xxx
xxxxxxx
""")

_add("U", """
xxxxxxx
  xx  x
  xx  x
  xx  x
  xx  x
      x
xxxxxxx
""")

_add("V", """
xxxxxxx
  xx  x
  xx  x
  xx  x
x    xx
xx  xxx
xxxxxxx
""")

_add("W", """
xxxxxxxxx
  xxxx  x
  xxxx  x
  x  x  x
        x
x  xx  xx
xxxxxxxxx
""")

_add("X", """
xxxxxxxx
  xxx  x
x  x  xx
xx   xxx
x  x  xx
  xxx  x
xxxxxxxx
""")

_add("Y", """
xxxxxxxxx
  xxxx  x
x  xx  xx
xx    xxx
xxx  xxxx
xxx  xxxx
xxxxxxxxx
""")

_add("Z", """
xxxxxxx
      x
xxx  xx
xx  xxx
x  xxxx
      x
xxxxxxx
""")

_add("1", """
xxx
  x
  x
  x
  x
  x
xxx
""")

_add("2", """
xxxxxxx
      x
xxxx  x
      x
  xxxxx
      x
xxxxxxx
""")

_add("3", """
xxxxxxx
      x
xxxx  x
      x
xxxx  x
      x
xxxxxxx
""")

_add("4", """
xxxxxxx
  xx  x
  xx  x
      x
xxxx  x
xxxx  x
xxxxxxx
""")

_add("5", """
xxxxxxx
      x
  xxxxx
      x
xxxx  x
      x
xxxxxxx
""")

_add("6", """
xxxxxxx
      x
  xxxxx
      x
  xx  x
      x
xxxxxxx
""")

_add("7", """
xxxxxxx
      x
xxxx  x
xxxx  x
xxxx  x
xxxx  x
xxxxxxx
""")

_add("8", """
xxxxxxx
      x
  xx  x
      x
  xx  x
      x
xxxxxxx
""")

_add("9", """
xxxxxxx
      x
  xx  x
      x
xxxx  x
      x
xxxxxxx
""")

_add("0", """
xxxxxxx
      x
  xx  x
  xx  x
  xx  x
      x
xxxxxxx
""")


def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError as e:
        raise LetterNotDefined(e)

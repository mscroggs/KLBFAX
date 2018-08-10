from fonts.LetterBlock import LetterBlock
from fonts.exceptions import LetterNotDefined

SIZE = 4
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
""")

_add("A", """
xx''xxx
x xx xx
x ,, xx
x,xx,xx
""")

_add("B", """
x'''xxx
x '',xx
x xx xx
x,,,xxx
""")

_add("C", """
xx''xxx
x xx,xx
x xx'xx
xx,,xxx
""")

_add("D", """
x'''xxx
x xx xx
x xx xx
x,,,xxx
""")

_add("E", """
x''''xx
x ''xxx
x xxxxx
x,,,,xx
""")

_add("F", """
x''''xx
x ''xxx
x xxxxx
x,xxxxx
""")

_add("G", """
xx''xxx
x xx,xx
x x, xx
xx,,xxx
""")

_add("H", """
x'xx'xx
x '' xx
x xx xx
x,xx,xx
""")

_add("I", """
x''''xx
xx  xxx
xx  xxx
x,,,,xx
""")

_add("J", """
xxxx'xx
xxxx xx
x'xx xx
xx,,xxx
""")

_add("K", """
x'xx'xx
x ',xxx
x x,'xx
x,xx,xx
""")

_add("L", """
x'xxxxx
x xxxxx
x xxxxx
x,,,,xx
""")

_add("M", """
'xxxx'x
 ,'', x
 xxxx x
,xxxx,x
""")

_add("N", """
x'xx'xx
x ,' xx
x xx xx
x,xx,xx
""")

_add("O", """
xx''xxx
x xx xx
x xx xx
xx,,xxx
""")

_add("P", """
x'''xxx
x xx xx
x ,,xxx
x,xxxxx
""")

_add("Q", """
xx''xxx
x xx xx
x x' xx
xx,,,xx
""")

_add("R", """
x'''xxx
x xx xx
x ,,'xx
x,xx,xx
""")

_add("S", """
xx'''xx
x,''xxx
xxxx xx
x,,,xxx
""")

_add("T", """
''''''x
xx  xxx
xx  xxx
xx,,xxx
""")

_add("U", """
x'xx'xx
x xx xx
x xx xx
xx,,xxx
""")

_add("V", """
x'xxx'x
x xxx x
x x',xx
xx,xxxx
""")

_add("W", """
'xxxx'x
 xxxx x
 ',,' x
,xxxx,x
""")

_add("X", """
x'xx'xx
x,'',xx
x',,'xx
x,xx,xx
""")

_add("Y", """
x'xx'xx
x,'' xx
xxx',xx
xx,xxxx
""")

_add("Z", """
x''''xx
xxx',xx
x',xxxx
x,,,,xx
""")

_add("1", """
xxx'xxx
xx, xxx
xxx xxx
xxx,xxx
""")

_add("2", """
xx''xxx
x,x',xx
x',xxxx
x,,,,xx
""")

_add("3", """
xx''xxx
x,x',xx
x'xx xx
xx,,xxx
""")

_add("4", """
x'xxxxx
x x'xxx
x ' 'xx
xxx,xxx
""")

_add("5", """
x''''xx
x ''xxx
x'xx xx
xx,,xxx
""")

_add("6", """
xx''xxx
x ''xxx
x xx xx
xx,,xxx
""")

_add("7", """
x''''xx
xxxx xx
xx',xxx
xx,xxxx
""")

_add("8", """
xx''xxx
x,'',xx
x xx xx
xx,,xxx
""")

_add("9", """
xx''xxx
x xx xx
xx,, xx
xx,,xxx
""")

_add("0", """
xx''xxx
x xx xx
x xx xx
xx,,xxx
""")



def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError as e:
        return LetterBlock("""
xxxxxxx
x ,, xx
x '' xx
xxxxxxx
""".strip())

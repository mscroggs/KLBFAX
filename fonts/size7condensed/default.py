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
xx
xx
xx
 x
xx
xx
xx
""")

_add("'", """
 x
 x
xx
xx
xx
xx
xx
""")

_add("(", """
xxx
' x
 'x
 'x
 'x
, x
xxx
""")

_add(")", """
xxx
 'x
' x
' x
' x
 ,x
xxx
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
xx
xx
xx
xx
xx
xx
xx
""")

_add("A", """
xxxxxx
'   'x
  x  x
     x
  x  x
  x  x
xxxxxx
""")

_add("B", """
xxxxxx
    'x
  x  x
    'x
  x  x
    ,x
xxxxxx
""")

_add("C", """
xxxxx
'   x
  xxx
  xxx
  xxx
,   x
xxxxx
""")

_add("D", """
xxxxxx
    'x
  x  x
  x  x
  x  x
    ,x
xxxxxx
""")

_add("E", """
xxxxx
    x
  xxx
   xx
  xxx
    x
xxxxx
""")

_add("F", """
xxxxx
    x
  xxx
   xx
  xxx
  xxx
xxxxx
""")

_add("G", """
xxxxxx
'   'x
  xxxx
  x''x
  x  x
,    x
xxxxxx
""")

_add("H", """
xxxxxx
  x  x
  x  x
     x
  x  x
  x  x
xxxxxx
""")

_add("I", """
xxx
  x
  x
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
   ,x
xxxxx
""")

_add("K", """
xxxxxx
  x  x
  x ,x
   'xx
  x  x
  x  x
xxxxxx
""")

_add("L", """
xxxxx
  xxx
  xxx
  xxx
  xxx
    x
xxxxx
""")

_add("M", """
xxxxxx
 'x' x
     x
  x  x
  x  x
  x  x
xxxxxx
""")

_add("N", """
xxxxxx
    'x
  x  x
  x  x
  x  x
  x  x
xxxxxx
""")

_add("O", """
xxxxxx
'   'x
  x  x
  x  x
  x  x
,   ,x
xxxxxx
""")

_add("P", """
xxxxxx
    'x
  x  x
    ,x
  xxxx
  xxxx
xxxxxx
""")

_add("Q", """
xxxxxx
'   'x
  x  x
  x  x
  x  x
,    x
xxxxxx
""")

_add("R", """
xxxxxx
    'x
  x  x
    ,x
  x  x
  x  x
xxxxxx
""")

_add("S", """
xxxxx
'   x
  xxx
,  'x
xx  x
   ,x
xxxxx
""")

_add("T", """
xxxxx
    x
x  xx
x  xx
x  xx
x  xx
xxxxx
""")

_add("U", """
xxxxxx
  x  x
  x  x
  x  x
  x  x
,   ,x
xxxxxx
""")

_add("V", """
xxxxxx
  x  x
  x  x
  x  x
  x  x
   ,xx
xxxxxx
""")

_add("W", """
xxxxxx
  x  x
  x  x
  x  x
     x
 ,x, x
xxxxxx
""")

_add("X", """
xxxxxx
  x  x
  x  x
x   xx
  x  x
  x  x
xxxxxx
""")

_add("Y", """
xxxxxx
  x  x
  x  x
,    x
xxx  x
x   ,x
xxxxxx
""")

_add("Z", """
xxxxx
    x
xx' x
x   x
 ,xxx
    x
xxxxx
""")

_add("1", """
xxx
' x
  x
  x
  x
  x
xxx
""")

_add("2", """
xxxxxx
'   'x
,,x  x
x'  ,x
  ,xxx
     x
xxxxxx
""")

_add("3", """
xxxxxx
'   'x
,,x  x
xx  'x
''x  x
,   ,x
xxxxxx
""")

_add("4", """
xxxxxx
  x  x
  x  x
     x
xxx  x
xxx  x
xxxxxx
""")

_add("5", """
xxxxxx
     x
  xxxx
    'x
xxx  x
    xx
xxxxxx
""")

_add("6", """
xxxxxx
'   'x
  x,,x
    'x
  x  x
,   ,x
xxxxxx
""")

_add("7", """
xxxxxx
     x
xxx  x
xxx  x
xxx  x
xxx  x
xxxxxx
""")

_add("8", """
xxxxxx
'   'x
  x  x
x   xx
  x  x
,   ,x
xxxxxx
""")

_add("9", """
xxxxxx
'   'x
  x  x
,    x
''x  x
,   ,x
xxxxxx
""")

_add("0", """
xxxxxx
'   'x
  x  x
  x  x
  x  x
,   ,x
xxxxxx
""")

_add("*", """
xxxxx xxxxxx
x,'xx,xx',xx
xxx'   'xxxx
,,x     x,,x
xxx,   ,xxxx
x',xx'xx,'xx
xxxxx xxxxxx
""")

#cloud
_add("@", """
xxxxxxxxxxxxx
xxxx'''xxxxxx
x'',xxx,'xxxx
 xx,xxx',,,'x
,'''''''''',x
xxxxxxxxxxxxx
xxxxxxxxxxxxx
""")

#rain
_add("{", """
xxx',,,'xxxxx
',,'xxxx ''xx
 xxxxxx,xxx x
x,,,,,,,,,,xx
xx','xxxx'xxx
x,''',x',x,'x
xxxxxxx,''',x
""")

#moon
_add("}", """
xxx'' ,,x
x'   ,xxx
'   xxxxx
    xxxxx
,   xxxxx
x,   'xxx
xxx,, ''x
""")

# cloud sun
_add("~","""
xxxxxxxxxxxxxxxx
xxx',,,'xx xx'xx
',,'xxxx ''x,xxx
 xxxxxx,xxx x,,x
x,,,,,,,,,,x'xxx
xxxxxxxxxx xx,xx
xxxxxxxxxxxxxxxx
""")

# storm
_add("^","""
xxx',,,'xxxxx
',,'xxxx'xxxx
 xxxxxx, ''xx
x,,x'   ,,,'x
xxx,  'xxxx x
xxxxx,  'x',x
xxxx' ,x,x,xx
""")

# snow
_add("%","""
xxx',,,'xxxxx
',,'xxxx ''xx
 xxxxxx,xxx x
x,,,,,,,,,,xx
xxxxxx,',xxxx
x,',xx,x,xxxx
x,x,xxxxxxxxx
""")


def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError as e:
        raise LetterNotDefined(e)

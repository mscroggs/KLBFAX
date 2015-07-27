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
xxxx
xxxx
xxxx
   x
xxxx
xxxx
xxxx
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
xxxxxxx
x'  'xx
  xx  x
  ''  x
  ,,  x
  xx  x
xxxxxxx
""")

_add("B", """
xxxxxxx
     'x
  xx  x
     xx
  xx  x
     ,x
xxxxxxx
""")

_add("C", """
xxxxxxx
'    'x
  xx,,x
  xxxxx
  xx''x
,    ,x
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
'    'x
  xx,,x
  x'''x
  x,  x
,    ,x
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
xxxxxx
  xxxx
  xxxx
  xxxx
  xxxx
     x
xxxxxx
""")

_add("M", """
xxxxxxxxx
  xxxx  x
   ''   x
  ,  ,  x
  x,,x  x
  xxxx  x
xxxxxxxxx
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
xxxxxxx
'    'x
  xx  x
  xx  x
  xx  x
,    ,x
xxxxxxx
""")

_add("P", """
xxxxxxx
     'x
  xx  x
     ,x
  xxxxx
  xxxxx
xxxxxxx
""")

_add("Q", """
xxxxxxx
'    'x
  xx  x
  xx  x
  x'',x
, ',  x
xxxxxxx
""")

_add("R", """
xxxxxxx
     'x
  xx  x
     ,x
  xx 'x
  xx  x
xxxxxxx
""")

_add("S", """
xxxxxxx
'    'x
  xxxxx
,    'x
xxxx  x
,    ,x
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
,    ,x
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
xxxxxxx
  xx  x
x '' xx
xx  xxx
x ,, xx
  xx  x
xxxxxxx
""")

_add("Y", """
xxxxxxx
  xx  x
  xx  x
x    xx
xx  xxx
xx  xxx
xxxxxxx
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
xxxx
'  x
,  x
x  x
x  x
x  x
xxxx
""")

_add("2", """
xxxxxxx
'    'x
,,xx  x
x'   ,x
' ,xxxx
      x
xxxxxxx
""")

_add("3", """
xxxxxxx
'    'x
,,xx  x
xx   ,x
''xx  x
,    ,x
xxxxxxx
""")

_add("4", """
xxxxxxx
  xxxxx
  xxxxx
  x  xx
      x
xxx  xx
xxxxxxx
""")

_add("5", """
xxxxxxx
      x
  '''xx
,,,,  x
''xx  x
,    ,x
xxxxxxx
""")

_add("6", """
xxxxxxx
'    'x
  xx,,x
     'x
  xx  x
,    ,x
xxxxxxx
""")

_add("7", """
xxxxxxx
      x
xxxx  x
xx'  xx
xx  xxx
xx  xxx
xxxxxxx
""")

_add("8", """
xxxxxxx
'    'x
  xx  x
'    'x
  xx  x
,    ,x
xxxxxxx
""")

_add("9", """
xxxxxxx
'    'x
  xx  x
,     x
''xx  x
,    ,x
xxxxxxx
""")

_add("0", """
xxxxxxx
'    'x
  xx  x
  xx  x
  xx  x
,    ,x
xxxxxxx
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

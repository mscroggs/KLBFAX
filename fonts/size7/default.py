#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fonts.LetterBlock import LetterBlock
from fonts.exceptions import LetterNotDefined

SIZE = 7
alphabet = {}


def _add(letter, string):
    global alphabet
    letter_str = string.strip()
    assert len(letter_str.split("\n")) == SIZE
    alphabet[letter] = LetterBlock(letter_str)

_add("'", """
 x
 x
xx
xx
xx
xx
xx
""")

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

_add(".", """
xxx
xxx
xxx
xxx
xxx
  x
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

_add("?", """
xxxxxxx
'    'x
,,xx  x
xx'  ,x
xx,,xxx
xx  xxx
xxxxxxx
""")

_add("(", """
xxxx
x  x
  xx
 xxx
  xx
x  x
xxxx
""")

_add(")", """
xxxx
x  x
xx  
xxx 
xx  
x  x
xxxx
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

_add(u"£","""
xxxxxxx
x'   'x
x  x,,x
    xxx
x  xxxx
      x
xxxxxxx
""")

_add(u"$","""
xxxxxxx
xx  xxx
  ,,,,x
      x
''''  x
xx  xxx
xxxxxxx
""")

_add(u"€","""
xxxxxxx
x'   'x
'  'xxx
'  'xxx
x  xxxx
x,   ,x
xxxxxxx
""")

_add(u"฿","""
xxxxxxxxxxxxx
xxxxxx' ' 'xx
xxxxxx  xx  x
 , ,'x    ''x
 x x x  xx  x
 x x x, , ,xx
xxxxxxxxxxxxx
""")

_add(u"₺","""
xxxxxxx
x  x'xx
'  ,xxx
x  ',xx
,  x''x
x    ,x
xxxxxxx
""")

_add(u"¥","""
xxxxxxx
  xx  x
  ''  x
x,  ,xx
x,  ,xx
x,  ,xx
xxxxxxx
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
xxxxxxx xxxxxxxx
xxx,'xx,xx',xxxx
xxxxx'   'xxxxxx
xx,,x     x,,xxx
xxxxx,   ,xxxxxx
xxx',xx'xx,'xxxx
xxxxxxx xxxxxxxx
""")

#cloud
_add("@", """
xxxxxxxxxxxxxxxx
xxxx',,,,,'xxxxx
x'' xxxxxxx xxxx
 xxx,xxxx'',,,'x
 'xxxxxxxxxxxx x
x,,,,,,,,,,,,,xx
xxxxxxxxxxxxxxxx
""")

#cloud sun rain
_add("<", """
xxxxxxxxxxxxxxxx
xxx',,,'xx xx'xx
',,'xxxx ''x,xxx
 xxxxxx,xxx x,,x
x,x'x,,,,,,x'xxx
x',x,'xxxx xx,xx
xx,,,xxxxxxxxxxx
""")

#light rain
_add("[", """
xxxxxxxxxxxxxxxx
xxxxx',,,'xxxxxx
xx',,'xxxx ''xxx
xx xxxx'x,xxx xx
xxx,x',,'x,,,xxx
xxxx xxx xxxxxxx
xxxxx,,,xxxxxxxx
""")

#rain
_add("{", """
xxxxx',,,'xxxxxx
xx',,'xxxx ''xxx
xx xxxxxx,xxx xx
xxx,,,,,,,,,,xxx
xxxx','xxxx'xxxx
xxx,''',x',x,'xx
xxxxxxxxx,''',xx
""")

#moon
_add("}", """
xxxxxx'' ,,xxxxx
xxxx'   ,xxxxxxx
xxx'   xxxxxxxxx
xxx    xxxxxxxxx
xxx,   xxxxxxxxx
xxxx,   'xxxxxxx
xxxxxx,, ''xxxxx
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

# heavy rain
_add("]","""
xxxx'',,,'xxxxxx
',,,'xxxxx ''''x
 xxxxxxxx,xxxxx 
,''''''''''xx'x,
xx'xxxxx'xx',x,'
',x,'x',x,'x,,,x
x,,,xxx,,,xxxxxx
""")




# storm
_add("^","""
xxxx',,,'xxxxxx
x',,'xxxx ''xxx
x xxxxxx,xxx xx
xx,,x'   ,x,xxx
xxxx,  'xxxxxxx
xxxxxx,  xxxxxx
xxxxx' ,xxxxxxx
""")

# snow
_add("%","""
xxxxx',,,'xxxxxx
xx',,'xxxx ''xxx
xx xxxxxx,xxx xx
xxx,,,,,,,,,,xxx
xxxxxxxx,',xxxxx
xxx,',xx,x,xxxxx
xxx,x,xxxxxxxxxx
""")

from random import choice

# unknown
_add("`",
"\n".join(["".join([choice(["x",",","'"]) for i in range(13)]) for j in range(7)])
)


def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError as e:
        raise LetterNotDefined(e)

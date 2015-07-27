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

_add("!", """
xxx
 x
 x
 x
xx
 x
xx
""")

_add("/", """
xxxx
xx x
x',x
x xx
',xx
 xxx
xxxx
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
xxxx
' 'x
 x x
   x
 x x
 x x
xxxx
""")

_add("B", """
xxxx
  'x
 x x
  xx
 x x
  ,x
xxxx
""")

_add("C", """
xxxx
   x
 x,x
 xxx
 x'x
   x
xxxx
""")

_add("D", """
xxxx
  'x
 x x
 x x
 x x
  ,x
xxxx
""")

_add("E", """
xxx
  x
 xx
  x
 xx
  x
xxx
""")

_add("F", """
xxxx
  x
 xx
  x
 xx
 xx
xxx
""")

_add("G", """
xxxx
' 'x
 xxx
 x'x
 x x
,' x
xxxx
""")

_add("H", """
xxxx
 x x
 x x
   x
 x x
 x x
xxxx
""")

_add("I", """
xx
 x
 x
 x
 x
 x
xx
""")

_add("J", """
xxxx
xx x
xx x
xx x
'x x
, ,x
xxxx
""")

_add("K", """
xxxx
 x x
 x x
  xx
 x x
 x x
xxxx
""")

_add("L", """
xxxx
 xxx
 xxx
 xxx
 xxx
   x
xxxx
""")

_add("M", """
xxxxxx
 'x' x
 , , x
 x,x x
 xxx x
 xxx x
xxxxxx
""")

_add("N", """
xxxx
  'x
 x x
 x x
 x x
 x x
xxxx
""")

_add("O", """
xxxx
' 'x
 x x
 x x
 x x
, ,x
xxxx
""")

_add("P", """
xxxx
  'x
 x x
   x
 xxx
 xxx
xxxx
""")

_add("Q", """
xxxx
' 'x
 x x
 x x
 x x
,  x
xxxx
""")

_add("R", """
xxxx
  'x
 x x
  ,x
 x x
 x x
xxxx
""")

_add("S", """
xxxx
   x
 x,x
, 'x
'x x
   x
xxxx
""")

_add("T", """
xxxx
   x
x xx
x xx
x xx
x xx
xxxx
""")

_add("U", """
xxxx
 x x
 x x
 x x
 x x
, ,x
xxxx
""")

_add("V", """
xxxx
 x x
 x x
 x x
 x x
  ,x
xxxx
""")

_add("W", """
xxxxxx
 xxx x
 xxx x
 x'x x
 x x x
  ,  x
xxxxxx
""")

_add("X", """
xxxx
 x x
,',x
x xx
','x
 x x
xxxx
""")

_add("Y", """
xxxx
 x x
 x x
, ,x
x xx
x xx
xxxx
""")

_add("Z", """
xxxx
   x
xx x
x ,x
 xxx
   x
xxxx
""")

_add("1", """
xx
 x
 x
 x
 x
 x
xx
""")

_add("2", """
xxxx
   x
xx x
   x
 xxx
   x
xxxx
""")

_add("3", """
xxxx
   x
xx x
   x
xx x
   x
xxxx
""")

_add("4", """
xxxx
 x x
 x x
   x
xx x
xx x
xxxx
""")

_add("5", """
xxxx
   x
 xxx
   x
xx x
   x
xxxx
""")

_add("6", """
xxxx
   x
 xxx
   x
 x x
   x
xxxx
""")

_add("7", """
xxxx
   x
xx x
xx x
xx x
xx x
xxxx
""")

_add("8", """
xxxx
   x
 x x
   x
 x x
   x
xxxx
""")

_add("9", """
xxxx
   x
 x x
   x
xx x
   x
xxxx
""")

_add("0", """
xxxx
   x
 x x
 x x
 x x
   x
xxxx
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

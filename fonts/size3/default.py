#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
""")

_add("-", """
xxx
''x
xxx
xxx
""")

_add(u"–", """
xxx
''x
xxx
xxx
""")

_add("!", """
'x
 x
,x
,x
""")

_add("/", """
xxxxx
xx',x
',xxx
xxxxx
""")

_add(":", """
xx
'x
'x
xx
""")

_add(".","""
xx
xx
xx
,x
""")
_add(",","""
xx
xx
xx
 x
""")

_add("?","""
x''xx
,xx x
xx,xx
xx,xx
""")




_add("'","""
'x
,x
xx
xx
""")

_add(u"’","""
'x
,x
xx
xx
""")

_add(u"∨","""
xxxxx
'xx'x
 '',x
xxxxx
""")

_add(u"∧","""
xxxxx
'''xx
 xx x
xxxxx
""")

_add(u"¬","""
xxxxx
''''x
xxx x
xxxxx
""")

_add(u"⇾","""
xxxxx
xx'xx
,, ,x
xxxxx
""")

_add(u"⇿","""
xxxxxx
x'x'xx
, , ,x
xxxxxx
""")

_add("(","""
',x
 xx
 xx
,'x
""")

_add(u"°","""
x'xx
,',x
xxxx
xxxx
""")

_add(")","""
,'x
x x
x x
',x
""")

_add("&","""
xxxx
x'xx
, ,x
xxxx
""")

_add("$","""
x' 'x
,''xx
'xx x
x, xx
""")

_add(u"£","""
xx''x
' 'xx
x xxx
,,,,x
""")

_add(u"€","""
xx''x
' 'xx
x xxx
xx,,x
""")

_add(u"฿","""
xxxxxx' 'xx
''''xx '',x
 x x x xx x
,xxx,x, ,xx
""")

_add(u"₺","""
x'xxx
x 'xx
, x'x
x,,xx
""")

_add(u"¥","""
'xx'x
,'',x
x' 'x
xx,xx
""")

_add(u"㎎","""
xxxxxxxxxxx
 , ,'x',, x
 x x xx,, x
xxxxxx,,,xx
""")

_add(" ","""
xxx
xxx
xxx
xxx
""")

_add("A", """
','x
 ' x
,x,x
""")

_add("B", """
 ,'x
 , x
,,xx
""")

_add("C", """
',,x
 xxx
x,,x
""")

_add("D", """
 ,'x
 x x
,,xx
""")

_add("E", """
 ,,x
 ,xx
,,,x
""")

_add("F", """
 ,,x
 ,xx
,xxx
""")

_add("G", """
',,x
 x x
x,,x
""")

_add("H", """
 x x
 , x
,x,x
""")

_add("I", """
 x
 x
,x
""")

_add("J", """
xx x
'x x
x,xx
""")

_add("K", """
 x x
 ,'x
,x,x
""")

_add("L", """
 xxx
 xxx
,,,x
""")

_add("M", """
 ' x
 x x
,x,x
""")

_add("N", """
 ,'x
 x x
,x,x
""")

_add("O", """
','x
 x x
x,xx
""")

_add("P", """
 ,'x
 ,xx
,xxx
""")

_add("Q", """
','x
 x x
x,,x
""")

_add("R", """
 ,'x
 ,'x
,x,x
""")

_add("S", """
 ,,x
,, x
,,,x
""")

_add("T", """
, ,x
x xx
x,xx
""")

_add("U", """
 x x
 x x
,,,x
""")

_add("V", """
 x x
 x x
,,xx
""")

_add("W", """
 x x
 ' x
,x,x
""")

_add("X", """
 x x
','x
,x,x
""")

_add("Y", """
 x x
,, x
,,xx
""")

_add("Z", """
,, x
',xx
,,,x
""")

_add("1", """
x'x
, x
x x
x,x
""")

_add("2", """
x''xx
,x',x
',xxx
,,,,x
""")

_add("3", """
x''xx
,x',x
'xx x
x,,xx
""")

_add("4", """
'xxxx
 x'xx
 ' 'x
xx,xx
""")

_add("5", """
''''x
 ''xx
'xx x
x,,xx
""")

_add("6", """
x''xx
 ''xx
 xx x
x,,xx
""")

_add("7", """
''''x
xxx x
x',xx
x,xxx
""")

_add("8", """
x''xx
,'',x
 xx x
x,,xx
""")

_add("9", """
x''xx
 xx x
x,, x
x,,xx
""")

_add("0", """
x''xx
 xx x
 xx x
x,,xx
""")



def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError as e:
        raise LetterNotDefined(e)

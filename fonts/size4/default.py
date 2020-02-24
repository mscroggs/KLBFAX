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
x
""")

_add("@","""
',,, x
 x x x
 x   x
,''''x
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

_add("–", """
xxx
''x
xxx
xxx
""")

_add("_", """
xxx
xxx
xxx
,,x
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

_add("#", """
x'x'xx
, , ,x
, , ,x
xxxxxx
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

_add(u"▲","""
xxxxxx
xx'xxx
'   'x
xxxxxx
""")

_add(u"▼","""
xxxxxx
'''''x
x, ,xx
xxxxxx
""")

_add("%","""
'xxxx
xx',x
',xxx
xxx,x
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

_add(u"‘","""
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

_add("=","""
xxxxx
''''x
''''x
xxxxx
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
' 'xx
 '',x
 xx x
, ,xx
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

_add(u"₫","""
xxx'x
x , x
x,,,x
x,,,x
""")

_add(u"₽","""
x'''x
x ' x
' 'xx
x,xxx
""")

_add(u"㎎","""
xxxxxxxxxxx
 , ,'x',, x
 x x xx,, x
xxxxxx,,,xx
""")

_add(u"㏂","""
xxxxxxxxxx
x,'x , ,'x
', x x x x
x,,x,x,x,x
""")

_add(u"㏘","""
xxxxxxxxxx
 ,'x , ,'x
 ',x x x x
,xxx,x,x,x
""")

_add(" ","""
xxx
xxx
xxx
xxx
""")

_add("A", """
x''xx
 xx x
 ,, x
,xx,x
""")

_add("B", """
'''xx
 '',x
 xx x
,,,xx
""")

_add("C", """
x''xx
 xx,x
 xx'x
x,,xx
""")

_add("D", """
'''xx
 xx x
 xx x
,,,xx
""")

_add("E", """
''''x
 ''xx
 xxxx
,,,,x
""")

_add("F", """
''''x
 ''xx
 xxxx
,xxxx
""")

_add("G", """
x''xx
 xx,x
 x, x
x,,xx
""")

_add("H", """
'xx'x
 '' x
 xx x
,xx,x
""")

_add("I", """
'x
 x
 x
,x
""")

_add("J", """
xxx'x
xxx x
'xx x
x,,xx
""")

_add("K", """
'xx'x
 ',xx
 x,'x
,xx,x
""")

_add("L", """
'xxxx
 xxxx
 xxxx
,,,,x
""")

_add("M", """
'xxx'x
 ,', x
 xxx x
,xxx,x
""")

_add("N", """
'xx'x
 ,' x
 xx x
,xx,x
""")

_add("O", """
x''xx
 xx x
 xx x
x,,xx
""")

_add("P", """
'''xx
 xx x
 ,,xx
,xxxx
""")

_add("Q", """
x''xx
 xx x
 xx x
x,,'x
""")

_add("R", """
'''xx
 xx x
 ,,'x
,xx,x
""")

_add("S", """
x'''x
,''xx
xxx x
,,,xx
""")

_add("T", """
'''x
x xx
x xx
x,xx
""")

_add("U", """
'xx'x
 xx x
 xx x
x,,xx
""")

_add("V", """
'xx'x
 xx x
 x',x
,,xxx
""")

_add("W", """
'xxx'x
 xxx x
 ',' x
,xxx,x
""")

_add("X", """
'xx'x
,'',x
',,'x
,xx,x
""")

_add("Y", """
'xx'x
,'' x
xx',x
x,xxx
""")

_add("Z", """
''''x
xx',x
',xxx
,,,,x
""")

_add("a", """
xxxx
,,'x
', x
,,,x
""")

_add("b", """
'xxx
 ,'x
 x x
,,xx
""")

_add("c", """
xxxx
',,x
 xxx
x,,x
""")

_add("d", """
xx'x
', x
 x x
x,,x
""")

_add("e", """
xxxx
','x
 ,,x
x,,x
""")

_add("f", """
x'x
 'x
 xx
,xx
""")

_add("g", """
xxxx
', x
,' x
'',x
""")

_add("h", """
'xxx
 ,'x
 x x
,x,x
""")

_add("i", """
'x
'x
 x
,x
""")

_add("j", """
x'x
x'x
x x
',x
""")

_add("k", """
'xxx
 x x
 ,'x
,x,x
""")

_add("l", """
'x
 x
 x
,x
""")

_add("m", """
xxxxxx
 ,','x
 x x x
,xxx,x
""")

_add("n", """
xxxx
 ,'x
 x x
,x,x
""")

_add("o", """
xxxx
','x
 x x
x,xx
""")

_add("p", """
xxxx
 ,'x
 ',x
 xxx
""")

_add("q", """
xxxx
', x
,' x
xx x
""")

_add("r", """
xxxx
 ',x
 xxx
,xxx
""")

_add("s", """
xxxx
',,x
x,'x
,,xx
""")

_add("t", """
'xx
 ,x
 xx
x,x
""")

_add("u", """
xxxx
 x x
 x x
x,,x
""")

_add("v", """
xxxx
 x x
 x x
,,xx
""")

_add("w", """
xxxxxx
 x x x
 x x x
,,,,xx
""")

_add("x", """
xxxx
,',x
x xx
,x,x
""")

_add("y", """
xxxx
 x x
,' x
'',x
""")

_add("z", """
xxxx
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

_add(u"Đ", """
x'''xx
' 'x x
x xx x
x,,,xx
""")

_add(u"Š", """
x,',
',,x
x,'x
,,xx
""")


_add(u"Ü", """
'xx'x
'xx'x
 xx x
x,,xx
""")

_add(u"á", """
',xx
x,'x
', x
,,,x
""")
_add(u"ả", """
',xx
x,'x
', x
,,,x
""")

_add(u"ã", """
,,,x
,,'x
', x
,,,x
""")

_add("ç", """
xxxx
',,x
 xxx
x ,x
""")

_add(u"é", """
',xx
','x
 ,,x
x,,x
""")

_add(u"ğ", """
,',x
', x
x, x
,,xx
""")

_add(u"í", """
',x
'xx
 xx
,xx
""")

_add(u"ł", """
x'xx
' ,x
x xx
x,xx
""")

_add(u"ñ", """
'''x
''xx
 x x
,x,x
""")

_add(u"ø", """
xxxx'x
x','xx
x x xx
,x,xxx
""")

_add(u"ó", """
',xx
x'xx
 x x
x,xx
""")

_add(u"ô", """
'.'x
x'xx
 x x
x,xx
""")

_add(u"ö", """
'x'x
x'xx
 x x
x,xx
""")

_add("ō", """
,,,x
','x
 x x
x,xx
""")

_add(u"ộ", """
'.'x
x'xx
,',x
x'xx
""")

_add(u"ú", """
x',x
'x'x
 x x
x,,x
""")

_add(u"ü", """
'x'x
'x'x
 x x
x,,x
""")

_add(u"ý", """
x',x
'x'x
,, x
,,xx
""")

# Cyrillic =====================================================================

_add(u"А", """
x''xx
 xx x
 ,, x
,xx,x
""")

_add(u"Б", """
''''x
 ''xx
 xx x
,,,xx
""")

_add(u"В", """
'''xx
 '',x
 xx x
,,,xx
""")

_add(u"Г", """
''''x
 xxxx
 xxxx
,xxxx
""")

_add(u"Д", """
x'''x
 xx x
 '' x
,xx,x
""")

_add(u"Е", """
''''x
 ''xx
 xxxx
,,,,x
""")

_add(u"Ё", """
x,x,x
 ,,,x
 ,,xx
,,,,x
""")

_add(u"Ж", """
'xx'xx'x
x,' ',xx
',x x,'x
,xx,xx,x
""")

_add(u"З", """
x''xx
,x',x
'xx x
x,,xx
""")

_add(u"И", """
'xx'x
 ', x
 xx x
,xx,x
""")

_add(u"Й", """
x,,xx
 x' x
 ,x x
,xx,x
""")

_add(u"К", """
'xx'x
 ',xx
 x,'x
,xx,x
""")

_add(u"Л", """
x'''x
x x x
x x x
,xx,x
""")

_add(u"М", """
'xxx'x
 ,', x
 xxx x
,xxx,x
""")

_add(u"Н", """
'xx'x
 '' x
 xx x
,xx,x
""")

_add(u"О", """
x''xx
 xx x
 xx x
x,,xx
""")

_add(u"П", """
''''x
 xx x
 xx x
,xx,x
""")

_add(u"Р", """
'''xx
 xx x
 ,,xx
,xxxx
""")

_add(u"С", """
x''xx
 xx,x
 xx'x
x,,xx
""")

_add(u"Т", """
'''x
x xx
x xx
x,xx
""")

_add(u"У", """
'xx'x
,'' x
xx',x
x,xxx
""")

_add(u"Ф", """
xx'xxx
',,,'x
,''',x
xx,xxx
""")

_add(u"Х", """
'xx'x
,'',x
',,'x
,xx,x
""")

_add(u"Ц", """
'xx'x
 xx x
 xx x
,,, x
""")

_add(u"Ч", """
'xx'x
,'' x
xxx x
xxx,x
""")

_add(u"Ш", """
'x'x'x
 x x x
 x x x
,,,,,x
""")

_add(u"Щ", """
'x'x'x
 x x x
 x x x
,,,, x
""")

_add(u"Ъ", """
''xxxx
x ''xx
x xx x
x,,,xx
""")

_add(u"Ы", """
'xxxx'x
 ''xx x
 xx x x
,,,xx,x
""")

_add(u"Ь", """
'xxxx
 ''xx
 xx x
,,,xx
""")

_add(u"Э", """
x''xx
,x' x
'xx x
x,,xx
""")

_add(u"Ю", """
 xx''xx
 ' xx x
 x xx x
 xx,,xx
""")

_add(u"Я", """
x'''x
 xx x
',, x
,xx,x
""")

_add(u"а", """
xxxx
,,'x
', x
,,,x
""")

_add(u"б", """
x'xx
 ,'x
 x x
,,xx
""")

_add(u"в", """
xxxx
 ,'x
 ,'x
,,xx
""")

_add(u"г", """
xxxx
 ,,x
 xxx
,xxx
""")

_add(u"д", """
xxxx
', x
 ' x
,x,x
""")

_add(u"е", """
xxxx
','x
 ,,x
x,,x
""")

_add(u"ё", """
,x,x
','x
 ,,x
x,,x
""")

_add(u"ж", """
xxxxxx
 x x x
', ,'x
,x,x,x
""")

_add(u"з", """
xxxx
,,'x
,,'x
,,xx
""")

_add(u"и", """
xxxxx
 x' x
 ,x x
,xx,x
""")

_add(u"й", """
,,,,x
 x' x
 ,x x
,xx,x
""")

_add(u"к", """
xxxx
 x x
 ,'x
,x,x
""")

_add(u"л", """
xxxx
', x
 x x
,x,x
""")

_add(u"м", """
xxxxxx
 'x' x
 x x x
,xxx,x
""")

_add(u"н", """
xxxx
 x x
 , x
,x,x
""")

_add(u"о", """
xxxx
','x
 x x
x,xx
""")

_add(u"п", """
xxxx
 , x
 x x
,x,x
""")

_add(u"р", """
xxxx
 ,'x
 ',x
,xxx
""")

_add(u"с", """
xxxx
',,x
 xxx
x,,x
""")

_add(u"т", """
xxxx
, ,x
x xx
x,xx
""")

_add(u"у", """
xxxx
 x x
x, x
,,xx
""")

_add(u"ф", """
xx'xxx
x' 'xx
,''',x
xx,xxx
""")

_add(u"х", """
xxxx
,',x
x xx
,x,x
""")

_add(u"ц", """
xxxx
 x x
 x x
,, x
""")

_add(u"ч", """
xxxx
 x x
x, x
xx,x
""")

_add(u"ш", """
xxxxxx
 x x x
 x x x
,,,,,x
""")

_add(u"щ", """
xxxxxx
 x x x
 x x x
,,,, x
""")

_add(u"ъ", """
xxxx
, 'xx
x x x
x,,xx
""")

_add(u"ы", """
xxxxxx
 'xx x
 x x x
,,xx,x
""")

_add(u"ь", """
xxxx
 'xx
 x x
,,xx
""")

_add(u"э", """
xxxx
,,'x
x, x
,,xx
""")

_add(u"ю", """
xxxxxx
 '','x
 x x x
xxx,xx
""")

_add(u"я", """
xxxxx
',, x
',, x
,xx,x
""")

# Greek ========================================================================

_add(u"Α", """
x''xx
 xx x
 ,, x
,xx,x
""")

_add(u"Β", """
'''xx
 '',x
 xx x
,,,xx
""")

_add(u"Γ", """
''''x
 xxxx
 xxxx
,xxxx
""")

_add(u"Δ", """
x''xx
 xx x
 xx x
,,,,x
""")

_add(u"Ε", """
''''x
 ''xx
 xxxx
,,,,x
""")

_add(u"Ζ", """
''''x
xx',x
',xxx
,,,,x
""")

_add(u"Η", """
'xx'x
 '' x
 xx x
,xx,x
""")

_add(u"Θ", """
x''xx
 '' x
 xx x
x,,xx
""")

_add(u"Ι", """
'x
 x
 x
,x
""")

_add(u"Κ", """
'xx'x
 ',xx
 x,'x
,xx,x
""")

_add(u"Λ", """
x'''x
 xx x
 xx x
,xx,x
""")

_add(u"Μ", """
'xxx'x
 ,', x
 xxx x
,xxx,x
""")

_add(u"Ν", """
'xx'x
 ,' x
 xx x
,xx,x
""")

_add(u"Ξ", """
''''x
''''x
xxxxx
,,,,x
""")

_add(u"Ο", """
x''xx
 xx x
 xx x
x,,xx
""")

_add(u"Π", """
''''x
 xx x
 xx x
,xx,x
""")

_add(u"Ρ", """
'''xx
 xx x
 ,,xx
,xxxx
""")

_add(u"Σ", """
''''x
,'xxx
',xxx
,,,,x
""")

_add(u"Τ", """
'''x
x xx
x xx
x,xx
""")

_add(u"Υ", """
'xx'x
,'' x
xx xx
xx,xx
""")

_add(u"Φ", """
xx'xxx
', ,'x
,' ',x
xx,xxx
""")

_add(u"Χ", """
'xx'x
,'',x
',,'x
,xx,x
""")

_add(u"Ψ", """
'x'x'x
 x x x
,' ',x
xx,xxx
""")

_add(u"Ω", """
x'''xx
 xxx x
,'x',x
,,x,,x
""")

_add(u"α", """
xxxx
', x
 x x
x,,x
""")

_add(u"β", """
x'xx
 ',x
 ',x
,xxx
""")

_add(u"γ", """
xxxx
 x x
,',x
x,xx
""")

_add(u"δ", """
x'xx
,'xx
 x x
x,xx
""")

_add(u"ε", """
xxxx
',,x
 ,,x
x,,x
""")

_add(u"ζ", """
'''x
x',x
 xxx
x,,x
""")

_add(u"η", """
xxxx
 ,'x
 x x
xx,x
""")

_add(u"θ", """
x'xx
 ' x
 x x
x,xx
""")

_add(u"ι", """
xx
 x
 x
,x
""")

_add(u"κ", """
xxxx
 x x
 ,'x
,x,x
""")

_add(u"λ", """
''xx
x' x
 x x
,x,x
""")

_add(u"μ", """
xxxx
 x x
 x x
,,xx
""")

_add(u"ν", """
xxxx
,,'x
', x
,,,x
""")

_add(u"ξ", """
'''x
,''x
,''x
xx,x
""")

_add(u"ο", """
xxxx
','x
 x x
x,xx
""")

_add(u"π", """
xxxx
 , x
 x x
,x,x
""")

_add(u"ρ", """
xxxx
','x
 ',x
,xxx
""")

_add(u"σ", """
xxxxx
', ,x
 x xx
x,xxx
""")

_add(u"ς", """
xxxx
',,x
x,'x
,,xx
""")

_add(u"τ", """
xxxx
, ,x
x xx
xx,x
""")

_add(u"υ", """
xxxx
 x x
 x x
x,xx
""")

_add(u"φ", """
xx'xxx
x' 'xx
,' ',x
xx,xxx
""")

_add(u"χ", """
xxxx
 x x
','x
,x,x
""")

_add(u"ψ", """
xxxxxx
 x x x
,' ',x
xx,xxx
""")

_add(u"ω", """
xxxxxx
',x,'x
 x x x
x,,,xx
""")

# ==============================================================================



def get_letter(char):
    try:
        return alphabet[char]
    except KeyError as e:
        return LetterBlock("""
xxxxx
 ,, x
 '' x
xxxxx
""".strip())

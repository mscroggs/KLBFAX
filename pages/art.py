from page import Page
from random import choice

class ArtPage(Page):
    def __init__(self, num, title, art, tagline=None,show_title=False,color=None):
        super(ArtPage, self).__init__(num)
        self.title = title
        self.art = art
        self.in_index = False
        if tagline is not None:
            self.tagline = tagline
        self.show_title = show_title
        self.color = color

    def generate_content(self):
        if self.show_title:
            self.add_title(self.title)
        if self.color is None:
            self.add_text(self.art,fg=choice(["BRIGHTWHITE","PINK","LIGHTCYAN"]))
        else:
            self.add_text(self.art,fg=self.color)

class ArtImagePage(Page):
    def __init__(self, num, title, art, tagline=None):
        super(ArtImagePage, self).__init__(num)
        self.title = title
        self.art = art
        self.in_index = False
        if tagline is not None:
            self.tagline = tagline

    def generate_content(self):
        self.print_image(self.art)

class ArtIndex(Page):
    def __init__(self, num, range, ls):
        super(ArtIndex, self).__init__(num)
        self.title = "Art"
        self.index_num = range
        self.ls = ls

    def generate_content(self):
        self.add_title("Art")
        for i,page in enumerate(self.ls):
            self.add_text(page.number,fg="PINK")
            self.add_text(" "+page.title)
            if i%2==0:
                self.move_cursor(x=40)
            else:
                self.add_newline()



lisa = '''                           _,,ad8888888888bba,_
                      ,88888888I88888888888888888888a,
                   d88888PP"""" ""YY88888888888888888888b,
                ,8IIl'"                ;;l"ZZZIII8888888888,
             ,II88Zl;.                  ;llZZZZZ888888I888888,
           ,II8888Z;;                 `;;;;;''llZZ8888888I8888,
           II88888Z; _,aaa,      .,aaaaa,__.l;llZZZ88888888I888
           II88888IZZ<'(@@>Z|  |ZZZ<'(@@>ZZZZ;;llZZ888888888I88I
          ,II88888;   `""" ;|  |ZZ; `"""     ;;llZ8888888888I888
         ,II888888Z;           ;;;        .;;llZZZ8888888888I888I
         II88888888Z;;...;(_    _)      ,;;;llZZZZ88888888888I888,
         ]I888888888Z;;;;'   ";llllll;..;;;lllZZZZ88888888888I8888,
         II888888888Zl.;;"Y88bd888P";;,..;lllZZZZZ88888888888I8888I
         II888888888888Zl;;. `;;;l;;;;lllZZZZZZZZW88888888888I88888
          II8888888888888888ZbaalllZZZZZZZZZWWMZZZ8888888888I888888,
           `II88888888888888888;ZZMMMMMMZZZZZZZZllI888888888I8888888
             II8888888888888888, `;lllZZZZllllll;;.Y88888888I8888888b,
            II888888888888888PZI;.  .`;;;.;;;..; ...88888888I8888888888,
           ,II888888888PZ;;'                        `8888888I8888888888888b,
          ,II888888888                              ,888888I88888888888888888
      ,ad888888888888I                              8888888I8888ZZZZZZZZZZZZZ
  ,d888888888888P'8P'                               Y888ZZZZZZZZZZZZZZZZZZZZZ
d888888888888888,                                ,ZZZZZZZZZZZZZZZZZZZZZZZZZZZ
888888888888888888888ba,_d'                  ,ZZZZZZZZZZZZZZZZZ88888888888888
88888888888888888888888888888888888888888ZZZZZZZZZZZZZZZ888888888888888888888
888888888888888888888888888888888888888ZZZZZZZZZZZZZZ888888888888888888888888
88888888888888888888888888888888888ZZZZZZZZZZZZZZ8888888888888888888888888888
88888888888888888888888888888888ZZZZZZZZZZZZZZ8888888888888888888 Veilleux 88'''


venus = """                                    ,<<CCCCCCC>>,,..,,,<C> ,c' -;;,`C><   ,-
                                . <CCCCCCCCCCCCCCCCCCCCC> <C ,;, CCC `  ./
                              ,cC `CC>>>'' ,;;,,..`''''.,<C ,CC> CCCC>,<C>,<
                            .<CC' ,ccccccc  `<'CCCCCCCCCC>',cCC> <CCCCCCCCCC
                            CC> z$$$$$$$$$$cc,`'<C>>>>''',<CCCCCC,`<<<'.,.``
                          ,-C'.d$$$$$$$$$$$$$$c, -,<<<CCCCCCCCCCCC>CC>'''<C,
                         C' C $$$$$$$$$$P"'.."?h -<CCCC''.,,,.`CCC>  .<C> <C
                         \,<C $$$$$$$$$cc$?????$$.``<<CCCC'<CC `CCCC,`<CC>,c
                         ,C'  ?"'.,,$$$$$'    ,$$$ `> C<C .`<CCCCCC>>  `<CCC
                        -CCC> `$$"    $$$ccccd$$$$h >>C <CC>,`<<'',,<CC>.`<<
                         `<<,> "    ,r`$$$$$$$$$$$$ <CC,`<CCCC>.`<CCCCCCC>,,
                            CCC ?$$$$$ $$$$$$$$$$$$r`CCCC,cCCCCC, `'''',,<<<
                           ,<CC> ?$$$$ ??""3$$$$$$$$c`'CCC>>>CC,cCCCCCCCCCCC
                          C(`CC>, `$$$c,ccd$???$$$$$F   -,,<<CCCCCC>' ,;,``<
                          '  `<CC>.`?$$P"''  ,c$$$$' .,c, <CCCCCCC>>-`)CCC>,
                                CCC, `$hccccc$$$$F z$`<CC,  `<<<<'.,<<CCCCCC
                              ,<C>.<> .`"$$$$$$P'.$$$ CCC'   `-<CCCCCCCC>>>>
                              CC>.<> J$$c,`""\"',c$$$F,;>'.<C,  `'<C>'    ;.`
                             'CC><CC ?$$$$$$$$$$$$$P C,,; CC>           ,<>.
                       ,---;, CC CCC-<$$$$$$$$$$$$P <CCCC,CC>          ,<> >
                     ,',;-<C',c> CCC ..,.`"$$$$$$$ ,CCCC' C> , .       <C <C
                    ,C,cC,'',<' <CC',cCCCC $$$$$$'c.`>' ;C' <C C>,      <>,.
                    `<CCC>.''.<CCC' <<<<<C,`$$$$$$$$. <C> ;CC' CCCCC>,,,.``<
                   ,c,`CCCCCCCCC>',cCC>>.`C, "$$$$$$$h.`CCC' -CCC,.`<CCCCC>>
                ,c$$$$c `<<C>>' .,c`,.`'C, <> $$P"".,,;,.`CC>>,``<C>>,,;``<C
              .d$$$$$$$$$cccccd$$$$$$$$$ <C>,,.,,<CCCCCC>.`<CCCC>,.`<CCCC>,.
            zd$$$$$$$$$$$$$$$$$$$$$$$$$$>`CCCCCCCCC>>'''<C>.`<CCCCC>. <CCCCC
          .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ `<CCCCC>  -<CC;,<C> ``<<CCC>,`CCCC"""

jig = """------WWWWWWWWWWWWWWWWW-------
-----WWW-------------WWW------
----WWW---------------WWW-----
----WWW---------------WWW-----
---WWW-----------------WWW----
---WWW-----------------WWW----
--WWW----WW-------WW----WWW---
--WWW---W--W-----W--W---WWW---
-WWWW--W----W---W----W--WWWW--
-WWWW-W------W-W------W-WWWW--
-WWWW---WWWW-----WWWW---WWWWW-
-WWWW--WWWWW-----WWWWW--WWWWW-
WWWWW-WWRRRWW---WWRRRWW-WWWWW-
WWWWW-WWRRRWW---WWRRRWW-WWWWW-
WWWWW-WWRWRWW---WWRWRWW-WWWWW-
WWWWW-WWRWRWW---WWRWRWW-WWWWW-
WWWWW-WWRRRWW---WWRRRWW-WWWWW-
WWWWW-WWRRRW--W--WRRRWW-WWWWW-
WWWWW--WWWWW--W--WWWWW--WWWWW-
WWWW---------WWW---------WWWW-
WWW--WWW-----WWW-----WWW--WWW-
WWW-W---W----WWW----W---W-WWW-
WWW---W--W--WWWWW--W--W---WWW-
WWW--W-W-W--WWWWW--W-W-W--WWW-
WWW-W--W-W--WWWWW--W-W--W-WWW-
WWW-W--W-W--WWWWW--W-W--W-WWW-
WWW-W-W--W--WWWWW--W--W-W-WWW-
WWW-W----W-WWWWWWW-W----W-WWW-
WWW--WWWW--W-WWW-W--WWWW--WWW-
WWWW-------W--W--W-------WWWW-
WWWW---------------------WWWW-
WWWW---------------------WWWW-
-WWW---WRRRRRRRRRRRRRW---WWWW-
-WWW----RRRRRRRRRRRRR----WWWW-
-WWW-------W-----W-------WWWW-
-WWW-------W-----W-------WWWW-
-WWWW-----W-------W-----WWWWW-
-WWWW-----W-------W-----WWWWW-
---WWW---W----W----W---WWWWW--
---WWWW--W----W----W--WWWWWW--
-----WWWWWW--WWW--WWWWWW------
------WWWWWWWWWWWWWWWWW-------
----------W-------W-----------
----------WW-----WW-----------
-----------W-----W------------
----------WW-----WW-----------
--------WWWW-----WWWW---------
-------WWWWW-----WWWWW--------
------WWWWWWW---WWWWWWW-------
-----WWWWWWWW---WWWWWWWW------
----WWWWWWWWWWWWWWWWWWWWW-----
---WWWWWWWWWWWWWWWWWWWWWWW----
--WWWW---WWWWWWWWWWW---WWWW---
-WWWW----WWWWWWWWWWW----WWWW--
WWWW-----WWWWWWWWWWW-----WWWW-
WWW------WWWWWWWWWWW------WWW-
WWWWGG---WWWWWWWWWWW---GGWWWW-
WWWWGG---WWWWWWWWWWW---GGWWWW-
-----GG--WWWWWWWWWWW--GG------
-----GG--WWWWWWWWWWW--GG------
------GG-WWWWWWWWWWW-GG-------
------GG-WWWWWWWWWWW-GG-------
-------GGGGGGGGGGGGGGG--------
-------GGGGGGGGGGGGGGG--------
---------WWWWGGWWWWW----------
---------WWWWGGWWWWW----------
--------WWWWWGGWWWWWW---------
--------WWWWWGGWWWWWW---------
------WWWWWWWGGWWWWWWW--------
------WWWWWWWGGWWWWWWW--------
-----WWWWW--WGGW--WWWWW-------
-----WWWWW--WGGW--WWWWW-------"""

soup = '''          _______________________________
         [_______________________________]
         |===============================|
         |   __                          |
         |._/_.' _, ,__  ,_ /_ _  / /'   |
         | / _  / / /// / // /(-'/ / /|  |
         | \__)(_(_//(_/_/(_/(__(_(_/_/_ |
         |            /                  |
         |       C O N D E N S E D       |
         |                               |
         |            .-"""-.            |
         |           /:`:..':\           |
         |==========|.:::::..:|==========|
         |           \::::::./           |
         |            `-:::-'            |
         |    ___                        |
         |     |  _ ,_ _  _ ,_-|- _      |
         |     | (_)| | |(_||  |_(_)     |
         |                               |
         |V( )V( )V(  S O U P  )V( )V( )V|
         |----------           ----------|
         '===============================' '''


python = """------------BBBBBBBBBBBBBBB--------
------------BBBBBBBBBBBBBBB--------
------------BB--BBBBBBBBBBB--------
------------BB--BBBBBBBBBBB--------
------------BB--BBBBBBBBBBB--------
------------BB--BBBBBBBBBBB--------
------------BBBBBBBBBBBBBBB--------
------------BBBBBBBBBBBBBBB--------
---------------------BBBBBB--------
---------------------BBBBBB--------
----BBBBBBBBBBBBBBBBBBBBBBB-yyyyyyy
----BBBBBBBBBBBBBBBBBBBBBBB-yyyyyyy
----BBBBBBBBBBBBBBBBBBBBBBB-yyyyyyy
----BBBBBBBBBBBBBBBBBBBBBBB-yyyyyyy
----BBBBBBBBBBBBBBBBBBBBBB--yyyyyyy
----BBBBBBBBBBBBBBBBBBBBBB--yyyyyyy
----BBBBBBBBB-------------yyyyyyyyy
----BBBBBBBBB-------------yyyyyyyyy
----BBBBBBB--yyyyyyyyyyyyyyyyyyyyyy
----BBBBBBB--yyyyyyyyyyyyyyyyyyyyyy
----BBBBBBB-yyyyyyyyyyyyyyyyyyyyyyy
----BBBBBBB-yyyyyyyyyyyyyyyyyyyyyyy
----BBBBBBB-yyyyyyyyyyyyyyyyyyyyyyy
----BBBBBBB-yyyyyyyyyyyyyyyyyyyyyyy
------------yyyyyy-----------------
------------yyyyyy-----------------
------------yyyyyyyyyyyyyyy--------
------------yyyyyyyyyyyyyyy--------
------------yyyyyyyyyyy--yy--------
------------yyyyyyyyyyy--yy--------
------------yyyyyyyyyyy--yy--------
------------yyyyyyyyyyy--yy--------
------------yyyyyyyyyyyyyyy--------
------------yyyyyyyyyyyyyyy--------"""

scorp = """
       `.'##';.`
       +@#@@#; #@.      :#,
         .+@#+# .+,      `',   :#`
          `:+#';';;':    ;+',  ,#.   :+           `,,,,,,
              .`#; ,+;   :;', `+#,  :+,  `     .;#+.+:  ,@'#;`
                 ++++,   +'+: `#;  ;',   +.   :#:'';.;@'.#` ,',
                  ;;`;'  ',;; .#` :#;     ;##@#,          `#::':
                  ;#++` .:,:..@; ,#:  .+'  .,.             '` ;;
                  .;.`# .:::..'@:;;;;;;:                    +#+:
                 ` :@+#+';#;;+,+,+@#+++;```                +`,#;
                 '##'`;. '.;;.# ,:`,;;'+####+,        `;++@,;##:
                 +#,,' # ;`:; `, '.';.;,@;;;;,:;''::,,'' .''.
               `+':`.+`'`;`:; `, ,.;:,: @#@#,,';@:...,'#@++
                :#++@+.#`+'+;,+.;+,':.'';#;##;;+:+;:`:,
               .#@@@#'@'##;`,#+;@:+..+@@+@@##+.
               `+@@####++:;#+,,:;:;#@#+'@+:`
                  ;+'#:@;##+#@#;#+#;,.`
                 ,';;' +.':.,'',':,'+:`
              `.#:`,,  :',:;,`:`'`  ,#+
           .``#` ;.   .#' '',.`#.  `,''
       `;##@#,@''.   ,;',.:+:`;;@`   ``
    `++@@+,`,'+   .:,'@. .'+,.#+
    `##@++##+:    ,''`  ,'#..#'
      ,.

"""

class SqPage(Page):
    def __init__(self,page_num):
        super(SqPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Squirrel"
        self.tagline = "As found in Belgin's garden"

    def generate_content(self):
        from random import choice
        squ = """
          00000000000
      00000000       0000000           0
        000000             0000      0000  00
              00            00       00 0 0
             000          000     0000    00
            000          000  000000       0000
          000          000000000              00
        000           000000               00 00
      000            0000                 000 00
     000            0000             000      00
    00             000             0000000    00
   00             000                 000000000  00
  00              00                     00    0000
  00             000               000     00000  0
  00             00            000000000000    00  0
  00             00              0000     0000 000 0
  0             00                 00      000000 00
  00            00                  00      00   00
  00            00                  00      00000
    0        00000                0000000
     00000000    00                   00
                 0000000000000000  000
"""
        a = choice([
                           ("Waspy",squ,"ORANGE"),
                           ("Hazer",squ,"YELLOW"),
                           ("Yupeng",squ[::-1],"ORANGE"),
                           ("Chunxin",squ[::-1],"YELLOW"),
                           ("Q-bert",squ,"LIGHTGREEN"),
                           ("Jigsaw",squ[::-1],"PINK"),
                           ("Meatball","\n".join([a[::-1] for a in squ.split("\n")]),"PINK"),
                           ("Merlin","\n".join([a[::-1] for a in squ.split("\n")])[::-1],"PINK"),
                           ("Quickdraw","\n".join([a for a in squ.split("\n")]),"PINK"),
                           ("Wild Squirrel fled","","")
                          ])

        self.add_title(a[0])
        self.add_block(a[1],a[2])

emf = (
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyyyyyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbybbbbbbbbbbybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbybbbbbbbbbbbbybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbybbbbbbbbbbbbybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbybbbbbbbbbbbbbbybbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbybbbbyybbbbbbbbybbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbybbbybbybbbbybbybbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbybbybbbbybbybbbybbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbybbbbbbbbyybbbbybbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbybbbbbbbbbbbbbbybbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbybbbbbbbbbbbbybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbybbbbbbbbbbbbybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbybbbbbbbbbbybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyyyyyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbyybbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
            )

mate = (
                        "-----------------bbbbbbbbbbbbbbbbb---------------------------------------------\n"
                        "---------------bbbbbbbbbbbbbbbbbbbbb--------------------bbbbbbb----------------\n"
                        "-------------bbbbbbBBbbbbbbbbbBBbbbbbb------------------byyyyyb----------------\n"
                        "-----------bbbbwwwwwBbbbbbbbbbwwwwwwbbbb----------------bybbbbb----------------\n"
                        "---------bbbbwwwwwwwbbbbbbbbbbBwwwwwwwbbbb--------------byb--------------------\n"
                        "--------bbbwwwwwwwwwbbbbbbbbbbBwwwwwwwwwbbb-------------bybbbbb----------------\n"
                        "-------bbbwwwwwwwwwwbbbbbbbbbbbwwwwwwwwwwbbb------------byyyyyb----------------\n"
                        "------bbbwwwwwwwwwwBbbbbbbbbbbbBwwwwwwwwwwbbb-----------bbbbbbb----------------\n"
                        "-----bbbwwwwwwwwwwwBbbbbbbbbbbbBwwwwwwwwwwwbbb---------------------------------\n"
                        "----bbbwwwwwwwwwwwwBbbbbbbbbbbbbwwwwwwwwwwwwbbb---------bbb--------------------\n"
                        "---bbbwwwwwwwwwwwwwBbbbbbbbbbbbbwwwwwwwwwwwwwbbb--------byb--------------------\n"
                        "---bbbwwwwwwwwwwwwwBbbbbbbbbbbbbBwwwwwwwwwwwwbbb--------byb--------------------\n"
                        "--bbbwwwwwwwwwwwwwwBbbbbbbbbbbbbBwwwwwwwwwwwwwbbb-------byb--------------------\n"
                        "--bbwwwwwwwwwwwwwwwBbbbbbbbbbbbbBwwwwwwwwwwwwwwbb-------bybbbbb----------------\n"
                        "-bbbwwwwwwwwwwwwwwwBbbbbbbbbbbbbbbbbBBwwwwwBBBwbbb------byyyyyb----------------\n"
                        "-bbwwwwwwwwwwwwwwwwbbbbbbbbbbbbbbBBBwwBBBbbbbbwwbb------bbbbbbb----------------\n"
                        "bbbwwwwwwwwwwBBBbbbbbbbbbbBBBBBwwBBbbbbbbbbbbBwwbbb----------------------------\n"
                        "bbwwwwwwwwBBbbbbbbBwwwwwwwwwwwwBBbbbbbbbbbbBwwwwwbb-----bbb-bbb----------------\n"
                        "bbwwwwBBbbbbbbbbBBBBBBBBBBBBBbbbbbbbbbbbbBBwwwwwwbb-----byb-byb----------------\n"
                        "bbwwwwBbbbbbbbbbbbbbbbbbbbBbbbbBbbbbbbBBBwwwwwwwwbb-----byb-byb----------------\n"
                        "bbwwwwwBBBbbbbbbbbbbbbBbbbBwBBwwBbbbBBwwwwwwwwwwwbb-----byb-byb----------------\n"
                        "bbwwwwwwwwwwwwwwBBBBbbwwbbBwwwwwBbbbwwwwwwwwwwwwwbb-----bybbbyb----------------\n"
                        "bbwwwwwwwwwwwwwwwwwBbbBBbbBwwwwwBbBbwwwwwwwwwwwwwbb-----byyyyyb-------bbbbb----\n"
                        "bbwwwwwwwwwwwwwwwwBBBbbbbbbBBBBwBBBbwwwwwwwwwwwwwbb-----bbbbbbb------bbybybb---\n"
                        "bbwwwwwwwwwwwwwwwwBBBbbbbbBBbbBwBbbBwwwwwwBwwwwwwbb------------------bybybyb---\n"
                        "bbwwwwwwwwwwwwwwwwBBbBBbbbBBwwBwwBBwwwwwBwwwwwwwwbb-----bbbbbb-------bybybyb---\n"
                        "bbwwwwwwwwwwwwwwwwwBBwBbbwBBwwBwwwwwwwBwwwwbwBwwwbb-----byyyybb------bybbbyb---\n"
                        "bbwwwwwwwwwwwwwwwwwBBwBbbBwwwBBwwwwwwwBwBwbwwBwwwbb-----bybbyyb------byb-byb---\n"
                        "bbwwwwwwwwwwwwwwwwBbbbbbbbBBwbBwwwwwwwBwwwwwBBwwwbb-----bybbyyb------bbb-bbb---\n"
                        "bbwwwwwwwwwwwwwwBbbbbbbbbbbBwbBwwwwwwwBwwwbwBBwwwbb-----byyyybb----------------\n"
                        "bbwwwwwwwwwwwwwBbbbbbbbbbbbbwbbwwwwwwwBwBwwwBwwwwbb-----bybbyyb-------bbbbb----\n"
                        "bbwwwwwwwwwwwBbbbbbbbbbbbbbbbbbwwwwwwwBwwwwwBwwwwbb-----bybbyyb------bbyyybb---\n"
                        "bbwwwwwwwwwwBbbbbbbbbbbbbbbbbbbbwwwwwwBwwBBBbwwwwbb-----byyyybb------bybbbyb---\n"
                        "bbbwwwwwwwwBbbbbbbbbbbbbbbbbbbbbBwwwwBBwBBBBBwwwbbb-----bbbbbb-------bybbbyb---\n"
                        "bbbwwwwwwwwbbbbbbbbbbbbbbbbbbbbbbwwwBBBBBwwBwwwwbbb------------------byyyyyb---\n"
                        "-bbwwwwwwwbbbbbbbbbbbbbbbbbbbbbbbwBBBBBwwwBBwwwwbb-------------------bybbbyb---\n"
                        "-bbbwwwwwbbbbbbbbbbbbbbbbbbbbbbbbbbBwBBwwBbBwwwbbb-------------------bbb-bbb---\n"
                        "--bbwwwwBbbbbbbbbbbbbbbbbbbbbbbbbBwwwwwwBbbBwwwbb------------------------------\n"
                        "--bbbwwBbbbbbbbbbbbbbbbbbbbbbbbbbwwwwwwwwbbwwwbbb--------------------bbbbbbb---\n"
                        "---bbBBbbbbbbbbbbbbbbbbbbbbbbbbbBwwwwwwwwBBwwwbb---------------------byyyyyb---\n"
                        "---bbbbbbbbbbbbbbbbbbbbbbbbbbbbBwwwwwwwwBBwwwbbb---------------------bbbybbb---\n"
                        "----bbbbbbbbbbbbbbbbbbbbbbbbbbbBwwwwwwBbBwwwwbb------------------------byb-----\n"
                        "----bbbbbbbbbbbbbbbbbbbbbbbbbbbBwwBBbbbwwwwwbbb------------------------byb-----\n"
                        "-----bbbbbbbbbbbbbbbbbbbbbbbbbbBwwbbbbbwwwwbbb-------------------------byb-----\n"
                        "------bbbbbbbbbbbbbbbbbbbbbbbbbBwBbbbbbBwBbbb--------------------------bbb-----\n"
                        "-------bbbbbbbbbbbbbbbbbbbbbbbbbBbbbbbbbBbbb-----------------------------------\n"
                        "--------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb--------------------------bbbbbbb---\n"
                        "---------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb---------------------------byyyyyb---\n"
                        "----------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb----------------------------bybbbbb---\n"
                        "------------bbbbbbbbbbbbbbbbbbbbbbbbbbb------------------------------byyyb-----\n"
                        "--------------bbbbbbbbbbbbbbbbbbbbbbb--------------------------------bybbbbb---\n"
                        "----------------bbbbbbbbbbbbbbbbbbb----------------------------------byyyyyb---\n"
                        "---------------------bbbbbbbbb---------------------------------------bbbbbbb---\n"
                        "-------------------------------------------------------------------------------\n"
            )

scream = """  ```'    -;;;!'''''-  `.,..   .zJ$$$$$$$$$$$$$$$$$$$$$$$$$$c, `!!'' ,;!!'
!!-  ' `,;;;;;;;;;;'''''```' ,c$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$c,  ;!!'' ,;
,;;;!!!!!!!!''``.,;;;;!'`'  z$$$$$$$$???\"\"\"\"\"'.,,.`\"?$$$$$$$$$$$  ``,;;!!!
;;..       --''```_..,;;!  J$$$$$$??,zcd$$$$$$$$$$$$$$$$$$$$$$$$h  ``'``'
```'''   ,;;''``.,.,;;,  ,$$$$$$F,z$$$$$$$$$$$$$$$$$$$c,`\"\"?$$$$$h
!!!!;;;;,   --`!'''''''  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$h.`\"$$$$h .
`'''``.,;;;!;;;--;;   zF,$$$$$$$$$$?????$$$$$$$$$$$$$?????$$r ;?$$$ $.
!;.,..,.````.,;;;;  ,$P'J\"$$$$$$P\" .,c,,.J$$$$$$$$$\"',cc,_`?h.`$$$$ $L
'``````'    .,..  ,$$\". $ $$$$P\",c$$$$$$$$$$$$$$$$',$$$$$$$$$$ $$$$ $$c,
!!!!!!!!!!!!!'''  J$',$ $.`$$P c$$$$$$$$$$$$$$$$$$,$$$$$$$$$$$ $$$$ $$$$C
   ``            J$ ,$P $$ ?$',$$$$???$$$$$$$$$$$$$$$??\"\"\"?$$$ <$$$ $$$$$
c           ;,  z$F,$$  `$$ $ ?$\"      \"$$$.?$$$ $$$P c??c, ?$.<$$',$$$$$F
$$h.  -!>   ('  $\" $F ,F ?$ $ F ,=\"?$$c,`$$F $$\"z$$',$' ,$$P $h.`$ ?$$$$$r
$$$$$hc,. ``'  J$ $P J$ . $$F L \",,J$$$F <$hc$$ \"$L,`??????,J$$$.` z$$$$$
$$$$$$$$$$c,'' ?F,$',$F.: $$ c$c,,,,,c,,J$$$$$$$ ?$$$c,,,c$$$$$$F. $$$$$$
`\"$$$$$$$$$$$c, $$',$$ :: $$$$$$$$F\"',$$$$$$$$$$h ?$$$L;;$$$??$$$$ $$$$$$
   \"?$$$$$$$$$$ $$$$$$ : .`F\"$$$$$$$$$$$$\"\"\"\"?\"\"\"h $$$$$$$\"$,J$$$$ $$$$$'
      \"?$$$$$$$ $$$$$$.`.` h `$$$$$$$$$$$cccc$$c,zJ$$$$$P' $$$$$P',$$$$P
$.       `\"\"?$$ $$$$$$$  ` \"$c \"?$$$$$$$$$$$$??$$$$$$$$\" ,J$$$P\",J$$$$P
..           `\" ?$$$$$$h    ?$$c.`?$$$$$$$$$' . <$$$$$' ,$$$\"  ,$$$$$\"
!!>. .          `$$$$$$$h  . \"$$$c,\"$$$$$$$' `' `$$$P  ,$$$' ,c$$$$$'   ;!
     ```         `$$$$$$$c     \"$$$c`?$$$$$  : : $$$  ,$$P' z$$$$$$'   ;!!
$hc ```'  ;       `$$$$$$$.      ?$$c ?$$$$ .: : $$$  $$F ,J$$$$$$'   ;!!
.,..      '        `$$$$$$$       \"$$h`$$$$ .' ' $$$ ,$$ ,J$$$$$$'    !!!
????P               `$$$$$$L       $$$ $$$F :.: J$$P J$F J$$$$$P     ;!!
-=<                  ?$$.\"$$       `$$ ?$$' `' z$$$F $P  $$$$$$'     !!'
cc                   `$$$c`?        ?$.`$$hc, cd$$F ,$'  $$$$$$     ;!!
                      $$$$c         `$$c$$$$$$$$$\",c$'   $$$$$$     `!!
                      $$$$$          `?$$$$$$$$$$$$P'    $$$$$$> ..
                      $$$$$            `\"?$$$$$$$P\"      $$$$$$L $$c,
          !!         <$$$$$            zc,`\"\"\"',         <$$$$$$.`$$$$cc,"""

guern = """
                                               zc    \"?$$$$$$$$$$$$$$$$c,J$F
                                  ..      c   d$??.     \"?$$$$$$$$$$$$$$$$$
                              c$c,$$      $h,$c .d$c,     \"?$$$$$$$$$$$$$$'
                             J$$$$$F .  ; $$$$$,,$$$$c      `?$$$$$$$$$$$$
                             ?$$$$$F'!!!'.$$$$$$$$$$$??       `?$$$$$$$$$F
                             J$$$$$$c,.,c$$$$$$$$$$$\"  P        \"$$$$$$$$'
                             $$$$$$$$$$$$$$$$P??$$$\" \",$         `$$$$$PF
                            J$$$$$$$$$$$$$$$$h.    \"c,\"P          `$$$$$c
                            $$$$$$$$?????? . ?$h....$$.\"           `$$$$$.
                           z$$$$$$'  ;!;'; $ `???????\"              '$$$$h
                          .$$$$$$'    !!>';..!;; <;>                 ?$$$h
                         .$$$$$$P     `!! !!!;!!>`!>                 `$$$$
                         J$$$$$$'      !! !!!;!!! !!                  ?$$$.
                       .J$$$$$$$       !! !!!;!!! !!                   $$$L
                      .$$$$$$$$F       !! !!!!!!',!'                   ?$$$
                     z$$$$$$$$$L       .!'                              J$$
                , ?$$$$$$$$$$$$$$$L       '                             $$$F
               ,$h.\"$$$$$$$\"\"$$$$$$c                                    $$$$
               $$$$c`$$$$$' J$$$$$$$c                                  J$$$$
              d$$$$' `$$$P .$$$$$$$F\"r                                z$$$$$
             J$$$$$>   ,J',$$$$$$$$' ,c?$c                           <$$$$$$
            d$$$$$$'   ` ,$$$$$$$$$ P'..`?                              `\"\"\"
           d$$$$$$$r     `$$$$$$$$',cc$$h
          d$$$$$$$$F      `?$$$P\"..$$$$$$h
         J$$$$$$???'        .  c$ .\"\"??$$$$c,
        z$P\"' ,cccccd$$' - d$ ..r ??$cc,,.\"?$$ccc,.
    ,cc,.,c$c,`$$$$$$$' F.$$'.$P zcc,\"\"??$hc,\"?$$$$$$$cccc
  .$$$$$$$$$$$c`$$$$$'.d d$' $L.zc,\"?$$c,`\"?$$ .\"$$$$$ ?$P
  $$$$$$$$$$$$$ ?C\"\"'.d$.?$.d$$$$$P\"'??\"\"\"  ` z$r`$P\"
 $$$\"\"\"\"\"3$$$$$  3$$ J$$>,??$\"' ,nmnmMMMMP < $$$$. .d$c,
J$$$$cccc$$$$$F-`<$',$$$ Jh \"$$r`MMMMMMMP `$$$$$h.  \"\"\"
$F\"\"\"\"$$\"\"????$ `   $$$$h ;!!!;; MMMMM'  `''' $$$$\"\"$$c,
?h,.. ?',   ,dP     3$$$h !!!!!!>`MMM' `?hccc 3$$F'.`?$$F
 \"$$$'' d$$$$$'   !>'$$$$ `!!!!!! `M' $c,`??\" `$$L ?h. \"
  `??c,c$$$$\"    ;!! $$$$.`!!!!!!!  ;>`$$h ;;! 3$$  ?$c
     `\"\"\"\"'      !!! $$$$$.`!!!!!!>,!',$$P !!!> $P   ?$c
                !!!! \"$$$$h `!!!!!!!!,`\"\" ;!!!!;.\";   \"$-             ...;;!
               ;!!!!!;` ??\"  `!!!!!!!!!!!!!!!!!!!!!!                  ."""

eif = """            .
           .|.
           |||
           |||
           |||
           |||
           j_I
          .)_(.
          |===|
          /___\\
         //___\\\\
        /=======\\
       / .-\"\"\"-. \\
jgs   |__|     |__|"""

liberty = """        9+-,KY7)
         W9-Y3+7)
         W'=9WI7)
        ,W  '-YY)
         W    ::W                ,
        ,T     :X)              ()
        ()     '9W  'L.         ()         ,-
        (C     =:9   '9L        ()        ,T
        ()    ,,-7)    7WL      WW      ,F'
        ()    , T9)     '9WL    --    ,YF
        ()    '-/(W       -==+PE9P7===O)          -,
        'W, ,  T+/WX=L-. ,WP+()+3L3,),=WL  --==-T-
         7)    -,YW '-=9WPL+PT-- ':--L/=9WP=-'
         'W-,.-,++W.   WWHP    ,,-/  .9CP3)
          W  --':-9:7=9W-T ,-=FT''=++,(TFYW=====---,
          W    .-='/.  7W-,WE=--,,=-:9H=9W\"\"~~~~~~'
          ()   ':'/Y,  (L-9PXWWW,YWWX,(U3C
          9' ,,::/Y,/,  7LW+'-'7)()-'(MWW)
       ,,-/:',T,'-:',) ,3WWW, .Y=W'.(+WPW)
      ,F=T:9/:':C' /W),WMW9PO),m-+--9+WYW)
     ,3Y:/--.'-,',F=FHWWE/LMWU.'--X3CWW(WL
     YP:/:' -/'-Y-,W-T)9X,WCWWWX=WWWW39/OW
     7WF:=,/:-:P:,P(-'))PWWHYT79WWWHPW0W7W'
     'WU7C-:=-=-C9'WF,):):H7L   '7CI7WEXP'
      7L-,Y==3F:::,=,:-/,'P=.,  ':79UWEW)
      'WEW9P=/,)/ -:,P: / L7:'-=,-+YMWWW)
       'W)+=T,T()/-,F,,,),)  ',.-+(L=W9WW.
        '+C/:I'''',P:''/ '  ''9.  == '-'7-
         (W-+'. ,YF )/:'      ')-. ,-:FX-L
         'WM/',/CP /,:'    ..:)  ,T','/: 'W,
          W--,YXT /'')   ,P=-/',P'  '(:'  'W,
          (WEXWF Y' ,)  ,/'-,,YT    ///  ,,'W.
         ,WWWWT,,' .Y:/.',,-,=',- ,YY(). +3,W)
         WFXF:,'P ,,)/  ,',P',,- ,FI,))) I3'W)
         -HP,X'',/ '  ,/,/' ,/',,P3'I(:) W) W)       /=+=,
          9WY).,/'  ,/'-'   ,-=9-/'Y'((',W) PW      /'  '-==L,
          'WY,'    ,/,P   ,YP- C/',',)( (W'(WW.    /'       '7==L.
           ()'    /:/' ,,WT'  3F',' /)W (W (K()   /'   .        '7X
           ()   ,P,P',)T=:- ,WP'.' ,P,T (W (-9L ,Y)' ,X//, .    Y:P
          ,F   ,F,',--,/:' ,+P' '  Y):) (E' YHWLWT)-''-9/',-' ,,,WF
         ,P.,P,)-3-- ,-,' ,WF.    ,Y (' (L-WCTWEW30V-/',:'=/P+E7WF
         W- Y,P/C)',Y',' ,WT      Y) :  (P-=Y:UW9CX)3-=- ,W:9/PXXW.
        /T./:P/)' ,P',' YW-      ,P'',  9M).())WTHW3,C'  9C9='W3WW)
       ,EPOP/YR. /F ,',/W)       /'  :  (W)'W979WO0=WC:,..9LPXWWP-
       3H:WL-R' /' /' /WF       ,) ,,   (U'(HW=WWXO:--:,:'(W=WWF'
      ,WLWWWI:,F' /-'3WF '      Y  ) ,  (),T(0)WO9YPL.' ',WP=='
        --YWX-F  Y',WWT' :':   (' ()7)  (MT: WP)3C)-''  3C'
            WF  /' YW--,  ,    Y  W (),YM+C' 9+I3UV:' .YP'"""

cafe = """
   |---|| |---|-|     |                           |
   '.--'| |---|-|     |(`,         ,      _      ||
    '---' '---'-'     |-._   O           `-`    | |  ___
               ___    |  _`-._       .         _| | |-|-|
              |---|-. | |    |`.              /   | |-|-|
       |      |---|-|_| |____| |    ,-.    , |    | |-|-|
       |`.  _ |---|-|-|.       |    `-'      |    | '-'-'
          `| `|`-.|-|-||       | ,      .  |||    |
   `-._     \`.`-|'-|-||       |     ,^.  /  |: : |  ___
       `-._  \ `-.`-|`||.__    |   . |||_|   |    | |-|-|
   `-._    |  \   `-._`'._|``.-+._   |,' |   |    | |-|-|
   `-._`-._)   \      `-.._``'-||_/_,|  .| ,.|    | |-|-|
   -.,':-.,'    \          ``--._/   |: :| ::|    | '-'-'
     \ |  |      \    .-.._     :    |   |   |: : |
     : |-.|       \   '.._/     '    |   |   |    |
     | |  |        \  ,^.      :     |   |   |    |
   --| |  |. |`.    `.| |     :      |   |   |,._.--------
     | |  ||_|__|____|`,'----.'   :: |   |   / _|`.``.````
     | |  ||(|,'|)|`.|`.-.-. |       | ::|  ,|`'|-|  |
     | |  |' |  | | || | | | |       |   |  ||`'|-|  |.
     | |  |  |  | | ||_|_|_|_|--__---'--._`-||`'|-|__|
     | |  |  |  | | ,`,.'`,.' \`,.'   .   `-._`.|_|__|____
   --| |  |  |  | |__'  `'__`,.'  `__      .  `-----------
     | |  |  |  |_`-.-')_`-.-|| \`-.-'   .      -      -
     | |  |  |,'-.-'^. | |,^|||  \,^._`_ -   -     `-.
     | |  | ,'__,^. ,-.   ___   ,-.< ___ >         -  `-.
     | |  |'< __ >  |_| < ___ > |_|\`.|,' `.   -       - `
     | |  |___\/___ |._._`.|,'_ |._.,'|`. `.`.     -     -
   ,'| |  |-  )( -: '| | ,'|`.   | |      - `.`.-     -
     | |  |   -  '' -     ::     -     -     -`.`. -     -
     |_|,' -    ::     -  ::  -     -     -     `.`.  -
    ,'  -     -..   -     ::     -     -     -    `.`.   -
   '       -   ''-        ::  -     -     -     -   `.`SSt"""

dali = """       <!! !!!!>                ;!'`
       !!! `!!!!               !!`                                    ,c,
       !!!> !!!!>             ;`<             ,cc$$cc            .,r== $$c !
       !!!! !!!!!!.        ,<!' !!!!!>>>;;;;;;;;.`\"?$$c MMMMMMM )MM ,= \"$$.`
       <!!> !!!!!!!!!!!!!>'' ,>''''  ``````''''!!!; ?$$c`MMMMMM.`MMMP== `$h
       `!! ;!!!!!!''''.,;;;'''          JF !;;;,,,,; 3$$.`MMMMMb MMMnnnM $$h
       ;!! <!!!!.;;!!!''`               JF.!!!!!!!!!>`$$h `MMMMM MMMMMMM $$$
       ;!!>`!!!!!!'`                    ?> !!!!!!!!!> $$$  MMMMM MMMMMMM $$$
       <!! ;!!!!'                       `h !!!!!!!!!! $$$ MMMMMM MMMM\" M $$$
       `!>'!!!!                          b !!!!!!!!!! $$$ MMMMMM MMML,,`,$$$
,,,,,, ;! <!!!> ,,,,,,,,,,,,,,,,         $ !!!!!!!!!! $$$ MMMMMM MMMMML J$$F
!!!!!! !! !!!! `!!!!!!!!!!!!!!' ;        $ !!!!!!!!!! $$$ MMMMMP.MMMMMP $$$F
!!!!! ;!! !!!!> !!!!!!!!!!!!' ;' .`.`.`. ?.`!!!!!!!!! 3$$  MMMP `MMMMM>,$$P
!!!!' !!' !!!!> !!!!!!!!!!' ;!' `.`.`.`. `h !!!!!!!!! $$$  MMML  MMPPP J$$'.
!!!! !!!;!!!!!';!!!!!!!!' ;!'  .`.`.`.`.` ?,`!!!!!!!! ?$$ MMMMM.,MM_\"',$$F .
!!!';!!!.!!!!' <!!!!!!!` ;'  .`.`.`.`.`.`. ? `!!!!!!!>`$$ MMMMMbdML ` $$$  .
``` !!!> !!!! ```````` ;!  .`.`.`.`.`.`.`.` h `!!!!!!> $$ )MMMMMMMMM d$$' `.
!!' !!!''!!! <!!!!!!!> ' .`.`.`.`.`.`.`.`.` `?,`'!!!!! ?$h 4MMMMMMP z$$' .`.
'' <!!! !!!> ''''''''  .`.`.`.`.`.`.`.`.`.`.` ?h.``'`..`$$  MMMMMM ,$$F `.`.
` !!!! <!!!.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`. `\"??$F\". `$h.`MMMMM $$$'.`.`.
 <!'! .!!!!> .`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`. cccc  `$$.'4MMP.3$F .`.`.
<!''! !!!!!> .`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`. J$$$$$F . \"$h.\" . 3$h .`.`.
!' ! !!!!!!> .`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.  \"\"\"\" .`.`.`$$, 4 3$$ .`.`.
 ;! !!!!!!! `.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.  ?$h  J$F .`.`.
;'  !!!!!!! `.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`. \"$$$$P' .`.`.
'  <!!!!!!! `.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`. . .`.`.`.`.
,' !!!!!!! .`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.
!! !!!!!!',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  `.`.`.`.
!! !!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'  `.`.`.`.
!! <!!!!';!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ;! `.`.`.`.
!! ;!!!!>`!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' <!! `.`.`.`.
',,!!!!''.;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' <!!! `.`.`.`.
'''''.,;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' <!!!! `.`.`.`.
;!!!!!!!!!!!!!!!!!!!!!!!>>>'''''''''`````''''''<!!!!!!!!!!!' !!!!!! `.`.`.`.
!!!!!!!!!!!!!!!!!!''''_,,uunmnmnmdddPPPPPPbbbnmnyy,_```''!  !!!!!!! `.`.`.`.
!!!!!!!!!''_``!'`,nmMMPP\"\"\"',.,ccccccr==pccccc,,..`\"\"444n,.`<!!!!!! `.`.`.`.
!!!!!!!' ,dMM ,nMMP\"\",zcd$h.`$$$$$$$$L c  $$$$$$$$$$??cc`4Mn <!!!!! `.`.`.`.
!!!!!! ,MMMP uMMP ,d$$$$$$$$cd$F ??$$$$$cd$$$$$$$$$F, ??h.`Mx !!!!! `.`.`.`.
!!!!!! MMMP uMM\",F,c \".$$$$$$$P'   ?$$$$$$$$$$$$$$$$C',J$$.`M.`!!!! `.`.`.`."""

pearl = """                  _,,,`\"\"\"\"\"???$c,\"??$$$c,`\"?$$$\"?$c
             .,;<CCCCCC>>>>>;.:: \"?hc, \"??$cc,\"?h,`\"?.
           ,CCCCCCCCCCCCC>>>>>;`:>:.`\"?$cc`\"$$hc.\"?h.`.
        .<CCCCCCCCCCCCCCCCCCC>>>;````-: \"?$.`?$$$ c \"? \\
      ,<CCCCC>><<<<CCCCC<<CCCCCCCC>>`:``:: \"$c \"\" $r  ? \\
     ;CCCCCCCCCCCCC>>><CCCC;CCCCCCCC>``:.``.`?$c  $$ L -
    CCCCCCCCC>>;<<CCCCC><CCCC>`CCCC>>. ``:>`;: ?$ $$.`?c \\
   <CCCCCCCCCCCCC>;;,`<CC>CCCC> `<C>. `;::`  `; ` $$$  $c`
  :' ,ccccc.`<CCC>..`:.`C>.`<C`>>:`< ;:``;; `: ;: $$$  $$ .
   c$$$$$$$$hc.`<<C;>>.`:: `.\" :;>:: `;: `;;: `;; $$$ r'$r?.
  J$$$$$$$$$$$$$c.`'''< ``;.`::.`:;;;.`;; `;;: `; $$><$ $>`h
 J$$$$$$$$$$$$$$$$$c,`:-;: `: `;: `;;;: :; `;;; `;<$>`$ $$ 3>
 ?cc,`$$$$$$????$$$$$$c,``;:`;: :;:``;;: :: :;;: :`$$ ? $$.?>
  \"\"?,$$$CC>c?\"\"\"CC$$$$$$c `- `: `;;:`;;: `:`;;; ` $$c c`$L?h
 ,$   `$$C>>.-????\"\"?$$$$$$c.  `: `;;: ;;; ; :;;;' 3$$ $ $L`P
 ,\"=  ,$$C>;L c$     ,\"<<CCC>>.`:;:``;: `;:.: ;;;';<$$ $r?$ F
.$$$$$$iCC<<$c,`    ,J$c,>>>>>>;.`;::``; `;;; `;.;  $$c`F?$ $.
<$$$$$C$C<<C$$$$$$$$$$$$$$5CC>>>>;.`:; `;: :;'`;:;  $$$ F?$r`h
`$$$$C$C<<<C$$$$$$$$$$$$$$5CCCCCCC>;, `-`;:.; ;;;   $$$ F?$L`$c
 $$$F3C><<<<?$$$$$$$$$$$$CCCCCCCCCCC> ?,z, `::;'    $$$.`<$$ $$
 ?$C?C<<??<;<$$$$$$$$$$5C>>>CCCCCCCC.,c$$$F'`       $$$$ <$$ $?c
 `$$c;;`;;''<$$$$$$$$$5CCCCCCCCCC?$$$$$$$P'         $$$$e $$.? $
  ?$$$$$CCCC$$$$$$$$$55CCCCCCCCCC,\"\"???\"            <$$$$ $$L`,$b
  `$C??777CCC$$$$$$555CCCCCCCCCCC>'   ::            <$$$$ $$$.`$$c
   `C>;????=>;>3$$$555CCCCCCCCCC / xhn.`:.          <$$$$r<$$L <$$.
    `h<<Ccc=;iJ$$$$555CCCCCCCCC' >:MMMM.`:..        `$$$$F<$$$  ?$$
     `$6666655$$$$555CCCCCCC>'',<>'MMMM':'''  .,.    $$$$L`$$$> `$$F
      `$$$$$$XX$$$55CCCC>'',;<<<>>.\"\"\"  ,nmMMMMMMMM. $$$$$.?$$$  ?$h
       `??$$$$$???''''..:<<>>'''''.,,xnMMPPP\"\"\"\"'... $$$$$h`$$$r- ?$h
           ```     ?hi>>>'',nMMMMMMMMP\"\".::::::::::: ?$$$$$ $$$$ h $$.
                    \"?\".ndMMMMP\"\"' .:::::::::::::::::<$$$$$.`$$$ ? ?$h
                     xdMMMMP\" :!!>:::::::::::::::::::`$$$$$$ $$$  3 ?$c
                  .xMMMP\"\".:<!!!!>>:::::::::::::::::: $$$$$$ ?$$L`$F`$$.
                 ;MMP\" :!!!!!!!!!>>>::::::::::::::::: $$$$$$>`$$$.<$ ?$$
                ,P\" .:!!!!!!!!!!!:>:::::::::::::::::: $$$$$$$ ?$$>`$LJ$$L
                ' :!!!!!!!!!!!!!!:::::::::::::::::::: $$$$$$$.<$$h ?$$$$$c
                .!!!!!!!!!!!!!!!!:::::::::::::::::::: $$$$$$$L`$$$><$$$$$$
               <!!!!!!!!>''````,,.```'':::::::::::::: ?$$$$$$$ $$$><$$$$$$
              !!!!!!>';;;<!!!!!!!!!;;;:.``':::::::::: <$$$$$$$ $$$>`$$$$$'
             !!!!!';;<!!!!!!!!!!!!>;;<;>;;:. `:::::::.<$$$$$$$ ?$$> $$??'
            !!!!';<!!!!!!!!!!!!!!!;:;;>;>;<::: `'::::.<$$$$$$$>::::.?.
           ;!!!';!!!!!!!!!!!!!!!!!!!;:;>;<:::::::.``:.<$$$$$$$L'.`.`.`.
           <!!';!!!!!!!!!!!!!!!!!!!!!;::;:::::::::::. `$$$$$$P\" .`.`.`.
           ;!!!!!!!!!!!!!!!!!!!!!!!!!!!;::::::::::::::. \" . . .`.`. . ."""

manet = """                                             ::'.::::: z$$$$$$$$$$$$$$h`:
                                               .:'.::::: z$$$$$$?$$$$$P\"\"\"':
                            .,,,,,,,.          ':::'.:. z$$\".,,,,_ $$F  \"\" :
                       ,;<<!!,```'!!!!'<;,     :::.:::: $$$\"\"'   .,$$L ccJ `
                    ,;!!!!!!!!!''- `` `'<;     `::::::: `$$$hcccc$$$$$ `CC.
                ,;<!!!' ;;,```,c$hJJ$$$c `!     .``````: `$$$$$$$$$$$$h ?C>
             ,;!!',<',;!! ,,c$$$$$$$$$$$h `>    ::: <ch : <??$$$$???$$$>`C'
             !!',<!',<!!!>`$$$$$$$$$$$$$$h !    ::`: \"\" :.`$$$$$Cicc,,,,='.
             `,;!! ;!!!!' z$$$$?????$$$$$$r        ::` c`: `$$$$6???\"\"\"', ::
            <!!!<! `!!!' $$$$$>=-\"-,3$P\".,J          : \" ::.`?$$$hcc$??\"  ::
           !'',;!!!;!!! $$$$$    ,\"c3$   JF        ,:: b.`:::...\"\"?$$$c$P ::
            ;!!'!! ,,.` $$$$$$c,,,z$$$'<$cc     :::::::`Mn.``:::::..`....::
           ;!! ;!` ?F'h-\"$$$$$$$$$$$$$h,3$$  ,::::::::::`TMMn.``':::::::'` :
           `! !! <; ?cc$$$$$$$$$$$$\". \"\"`3F :::::::::::::.`4MMMn,.````` ,d':
             !!!<'!'. \"\"3$$$$$$$$$$???=?,',.''''::::::::::::.\"4MMMMMP <;   .
             !!! ;! `hccJ$$$$$$$$h,.  .,r $$cccccc,.``':::::::: \"4MM',!!!>'.
             `'' !!! `??$??$$$$$$$$$$ccP\" `$$$$$$$$$$$c `::::::::. \" <!!!> .
                 ```.?$c$h.`\"?$$$P\"\".,,ccd$$$$$$$$$$$$$h.`::::::::::: `!!! .
                 z$$$b.\"?$$$$c.\"\" ?????????\"?$??\"\"\"$$$$$h ::::::::::::: `' .
              ,J$$$$$$$$$$$$$$$$c   .ii+'.::...::: $$$$$$c :::::::::::::: `.
            ,J$C$$$$$$$$$$$$$$$$$> .....:::::::::: ?$$$$$$ ::::::::::::::. .
          ,J$CS$$$$$$$???$$$$$$$F ::::::::::::::::.`$$$$$$h :::::::::::::.`.
        .c$C3$$$$$$$$$hcccc.\"\"???'::::::::::::::::: $$$$$$$h ::::::::::::  .
       J$$C3$$$$$$$$$$$$$$$$$$cc. ::::::::::::::::: $$$$$$$$h :::::::::::.`.
      J$$7$$$$$$$$$$$$$$$$$$$$$$$c.``:::::::::::::: 3$$$$$$$$L`:::::::::: `.
     z$$?$$$$$$$$$$$$$$$$$$$$$$$$$$$c `::::::::::::.<$$$$$$$$$ `:::::::.`  .
   .J$$C3$$$$$$$$$$$$$$$$$$$$$$$$$$$$$c ``:::::::::.<$$$$$$$$$> `::::::.` `
  .$$$$C$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$hc,.```::::.<$$$$$$$$$C> :::`.:.`.`.
  J$$$C3$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$hc,.`` <$$$$$$$$$CC;`:.`:`. .
 J$$$$C$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$. <$$$$$$$$$CCC :::.:.`. .
,$$$$C3$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$h ?$$$$$$$$$CC ` ` ..`
J$$$$$$$$$$$$$$$$$$$Lz,.\"\"?$$$$$$$$$$$$$$$$$$$$$$$$$$.$$$$$$$$$CC'J$cc. `: .
$$$$$$$$$$$$$$$$$$$$$$\",c$c,`\"?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$CC $$$$$h, `.
$$$$$$$$$$$$$$$$$$$$$CJ$$$$$$hc,`\"?$$$$$$$$$$$$$$$$$$$$$$$$$$$$CC $$$$$$$$c.
$$$$$$$$$$$$$$$$$$$$3$$$$$$$$$$$$hc,`\"?$$$$$$$$$$$$$$$$$$$$$$$$C> $$$$$$$$$$
$$$$$$$$$$$$$$$$$$$3$$$$$$$$$$$$$$$$h c `\"??$$$$$$$$$$$$$$$$$$$C> $$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ '      `'<<<?CCCCCCCCCCCCC>,$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P'        ==- .,,.`'''<<CCCC' J$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$C???$$$$$$??\".       ccccccd$$$$$$$cc,..  J$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$hc,.`\"\"\"  ;;;     zd$$$$$$$$$$$$$$$$CC';$$$\"\"$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$CC>>>;;- .c$$$$$$$$$$$$$$$$$?CC>J$$C' ?$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$CCC>' .z$$$$$$$$$$$$$$$$$$CC>JJ$$C>>' `?$$$$$$"""

degas = """                                       , h $ F
                                       ?,$,$,F
                                       `$$$$$P  ,
                                        ?$$$$L,c'
                                         $$$$$\"'
                                        c$$P\"                                         .CC,
;;,                                  .z$$$F                                          <CCCC
!'',ccc                            ,c$$$P\"                                        ,;, `CC ;!.!;
 ,$$$$$\".                        zJ$$$$\"                        .z..             <!!!! ' <<!!!!;
> $\".,,c,.                     c$$$$$P'                        ,$$$$$c,.     ,cL !!!!! ;> ``!!!!!
 z$$,.,$$$F                   $$$$$$P                          J$$$$PP$$$hc  $$$ !!!!! `<!> !!!!!>;
z$$$$$$$$$=                  \"??$$$\"                           <$$$$$ $$P\"..`$$F !!!!!!>'!><!'!'!!!
$$$$$$$$$,ccc             zJ$$$$$P'                            `?$$$$c \" ??$c$$$ !!!!!!!.,.' .,.!!!
$$$$$$$$$$??\"         .zJ$$$$$P\"                        .,;;;!!; <$$$$.  =$$$$$$r`!!'``'!!!!!!! ``'
`$$$$$$$P\"     ,ccd$$$$$$$$$\"'                         <!!!!!'!! `\"?$$h <c$$$$$$h  .. <!!!!> !>
 $$$$$$$F  .zc???$??\"\"'..`\"         zcccc,,,.,..,..   `!!!!'  ' ;!; \"$$.`$$$$$$$$h,$P ;!!!' `'
J$$$$$$$L $P\" ,;;,;;!!!''          <$$$$$$$$$$$$P\",;,-``!(.-' .<!!!! `$L  \"?$$$$L.,.  ``! c?c,
$$$$$$$$$ ? ;!!!!!!'``,;;;;;;,      $$$$$\"\"\"???\" <!'  ' !' ;!!!!!!!!> $$h.   J$$$$$$$c   z, ? ,c$?hc,
$$$$$$$$'  <!!!'  ,;<!!!!!!!!!!>    ?$$$$$c     `!! ,;;!!;<`<!!!!!'`. $$$$. <$$$$$$$$$.  `\"\"? ' .==$$.
$$$$$$$$ ;!!!!'!!!!!!!!!!!!!!!       $$$$$$c     !! !!!!!' ;'`!'' ,$F.\"???$ J$$$$$$$$$h.,,cc.    .,$$$c
$$$$$$$' `(!!> !!!!!! ..`!!!' ,$     ?$$$$$$.      ;!!!' ;! ., z$$F zJh=y,?$$??\"'.,..`\"?$$$$$r';, `\"'?$c
$$$$$P  ;!!!!> !!!!' <F\" `' ,J$$      $$$$$$h     c, `..<'' `,J$$P  \" $r`F`'.,c$$$$$$$c $$$$$F`!!   ?$$$
$$$P\" <; ``!!! !!!' .`?chcc$$$L       `$$$$$$c    $$$c,.,ccc$$$$F cc  \".,c$$$$$$$$$$$$P $$$$$'`!! c <$$$
.\",;<!!!!>; ;! `' z$$L \",$$$$$$c       $$$$$$$c, J$$$$$$??????\" z$$$$ ! ?$$$$$$$$$$$P\",c$$$$F !!! $c ?$$
!!!!!!!!!!! `' c$$$$$$cd$$$$$$$\"\"      $$$$$$$$h $$$$$$$c,.,,zc$$$$$$.`! $$$$$$$$$\"',c$$$$$P <!! z$$c`$$
!!!!!!!!!!!!!`<$$$$$$$$$$$$$$??        ?$$$$$$$',$$$$$$$$$$$$$$$$$$$$F !><$$$$P\"\",c$$$$$$$$ ;!!' $$$$.?$
!!!!!!!!!!!!! J$$$$$$$\"$$$$$$F         `??$???',$$$$$$$$$$$$$$$$$$$$$ <!> \"\".,cd$$$$$$$$$$\" !'' `?$$$$$P
!!!!!!!!!!!' z$$$$$$$$ \"\"\"??\",$$F ,c$,c c  .- ,$$$$$$$$$$$$$$$$$$$$$\" !!>  ?$$$$$$$$$$$$F ;!!      \"\"??
!!!!!!!!!',c$$$$$$$$$\",$$$$cd$P  J$$$$$$$c=\". $$$$$$$$$$$$$$$$$$$$$\" !!!>';`?$$$$$$$$P\"\".!''
!!!!!!'`,c$$$$$$$$$$$ $$$$$$$F J $$$$$$$\"  \"F<$$$$$$$$$$$$$$$$$$$$\" <!!! <!;,\"\"\"???\".,;!!'
!!!'.,c$$$$$$$$$$$$$$$$$$$$$P J z$$$$P\".z$$cc,,.\"\"?$$$$$$$$$$$$$$P >'!!  ``'`!!!>;;!''`'
! ,J$$$$\"\".,... \"$$$$$$$$$$P / z$$$$P c$$$$$$$$$$$c,.\"???$$$$$$$\" <'`!!! !;;;;, !!,,;'
! ?$$$F ;!!!!!!!  `\"??$$$$F `,J$$$$$   `\"?$$$$$$$$$$$$hcc ?$$$$\" !! `!!! !!!!!!,;!!!>
! <$$\" <!!!!!!'.zc,`'-.,..- z$$$$$$'        \"\"???$$$$$$$$F`??\" ;!!! <!!! !!!!!!!!!!!
!> $\" !!!',,,zc$$$$$cc,_' ,J$$$$$$F        <!>;;;;,  $$$$$  ;!!!!!! !!!';!!!!!!!!!' .xx.  .
!! ' !!! J$$$$$$$$$$$$$$$$$$$$$$$\".         !!!!!!!!;`$$$$h `!!!!!  <!! <!!!!!''  nMMMMMb.\"MMMn,.
`' .<!! .\"\"???$$$$$$$$$$$$$$$$$$F !          `!!!!!!!;`$$$$$ <!!!! ;,.,;!!!' xJMbx`4MMMMMM 4MMMMMb.,..
Mx`<!'! !!!;;;,.\"\"\"?$$$$$$$$$$P\";!!           <!!!!!!!; $$$$c`!!! , `````.,.\"4MMMMn.\"4MMMML .\"4MMMMMMMMn
MMn ',`!!!!!!!!!!!>;,,,.\"\"\"??\" <!!             !!!!!!!!; ?$$$.`!>4MMMMMM MMMb 4MMMMMM,`4MMM Mb.\"MMMMMMMM
MMMb.`,`!!!!!!!!!!!!!!!!!!! ;!!!!              `!!!!!!!!; ?$$$ ' ,_\"\"4MMMMMMMbx`MMMMMMMx`4Mx,MMMMMMMMMMM"""

einstein = """           !MMMMMM$M! !MR$$$RMM8$8MXM8$$$$$$$$$$$$NMMM!MMM!!!?MRR$$RXM$$MR!M
           !M?XMM$$M.< !MMMMMMSUSRMXM$8R$$$$$$$$$$#$MM!MMM!X!t8$M$MMMHMRMMX$
    ,-,   '!!!MM$RMSMX:.?!XMHRR$RM88$$$8M$$$$$R$$$$8MM!MMXMH!M$$RMMMMRNMMX!$
   -'`    '!!!MMMMMMMMMM8$RMM8MBMRRMR8RMMM$$$$8$8$$$MMXMMMMM!MR$MM!M?MMMMMM$
          'XX!MMMMMMM@RMM$MM@$$BM$$$M8MMMMR$$$$@$$$$MM!MMMMXX$MRM!XH!!??XMMM
          `!!!M?MHMMM$RMMMR@$$$$MR@MMMM8MMMM$$$$$$$WMM!MMMM!M$RMM!!.MM!%M?~!
           !!!!!!MMMMBMM$$RRMMMR8MMMMMRMMMMM8$$$$$$$MM?MMMM!f#RM~    `~!!!~!
           ~!!HX!!~!?MM?MMM??MM?MMMMMMMMMRMMMM$$$$$MMM!MMMM!!
           '!!!MX!:`~~`~~!~~!!!!XM!!!?!?MMMM8$$$$$MMMMXMMM!!
            !!~M@MX.. <!!X!!!!XHMHX!!``!XMMMB$MM$$B$M!MMM!!
            !!!?MRMM!:!XHMHMMMMMMMM!  X!SMMX$$MM$$$RMXMMM~
             !M!MMMM>!XMMMMMMMMXMM!!:!MM$MMMBRM$$$$8MMMM~
             `?H!M$R>'MMMM?MMM!MM6!X!XM$$$MM$MM$$$$MX$f
              `MXM$8X MMMMMMM!!MM!!!!XM$$$MM$MM$$$RX@\"
               ~M?$MM !MMMMXM!!MM!!!XMMM$$$8$XM$$RM!`
                !XMMM !MMMMXX!XM!!!HMMMM$$$$RH$$M!~
                'M?MM `?MMXMM!XM!XMMMMM$$$$$RM$$#
                 `>MMk ~MMHM!XM!XMMM$$$$$$BRM$M\"
                  ~`?M. !M?MXM!X$$@M$$$$$$RMM#
                    `!M  !!MM!X8$$$RM$$$$MM#`
                      !% `~~~X8$$$$8M$$RR#`
                       !!x:xH$$$$$$$R$R*`
                        ~!?MMMMRRRM@M#`       -Sushil-
                         `~???MMM?M\"`
                             ``~~"""

troll = """d.         .:;'..         ..,'             .;,.               ...,,'';;'. ...
.         .;.              ;'              ';                      .'...'.
.         .                 ,.              .     ..',::ccc:;,..     ..
               ......       ;.                'cxOKK0OXWWWWWWWNX0kc.
            ;d0KKKKKXK0ko:...              .l0X0xc,...lXWWWWWWWWKO0Kx'
'......'. .dXWN0kkk0NWWWWWN0o.            :KN0;.  .,cokXWWNNNNWNKkxONK: .,:c:.      .'
'.         .,:lodxxkO00KXNWWWX000k.       oXNx;:okKX0kdl:::;'',;coxkkd, ...'. ...'''....
.                      ...;xNNOc,.         ,d0X0xc,.     .dOd,           ..;dOKXK00000Ox:
,oxkkkdl;'.                'KK'              ..           .dXX0o:'....,:oOXNN0d;.'. ..,lOKd
00kxoooxKXKx:..ld:         ;KK'                             .:dkO000000Okxl;.   c0;      :K
.    '' 'kNNNKKKk,      .,dKNO.                                   ....       .'c0NO'      :X
    .00. ..''...      .l0X0d;.             'dOkxo;...                    .;okKXK0KNXx;.   .0
   .dNK,            .;xXWKc.                .;:coOXO,,'.......       .,lx0XXOo;...oNWNXKk:.'K
  .dNWXl        .';l0NXNKl.          ,lxkkkxo' .cK0.          ..;lx0XNX0xc.     ,0Nx'.','.kX
 .oXWNNKo'    .'..  .'.'dKk;        .cooollox;.xXXl     ..,cdOKXXX00NXc.      'oKWK'     ;k
 ,KWX0NNNXOl'.           .o0Ooldk;            .:c;.':lxOKKK0xo:,.. ;XX:   .,lOXWWXd.
 cXWWWXooNWNXKko;'..       .lk0x;       ...,:ldk0KXNNOo:,..       ,OWNOxO0KXXNWNO,
 oNWWNo.cXK;;oOXNNXK0kxdolllllooooddxk00KKKK0kdoc:c0No        .'ckXWWWNXkc,;kNKl.
.dNWWX;.xNk.  .kNO::lodxkOXWN0OkxdlcxNKl,..        oN0'..,:ox0XNWWNNWXo.  ,ONO'
  oNWWN0xXWK, .oNKc       .ONx.      ;X0.          .:XNKKNNWWWWNKkl;kNk. .cKXo.
 cNWWWWWWWWKOkKNXxl:,'...;0Xo'.....'lXK;...',:lxk0KNWWWWNNKOd:..   lXKclON0:
 ;XWWWWWWWWWWWWWWWWWWNNNNNWWNNNNNNNNNWWNNNNNNWWWWWNXKNNk;..        .dNWWXd.
 .ONWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNK0ko:'..OXo          'l0NXx,
  :XNk0NWXKNWWWWWWWWWWWWWWWWWWWWWNNNX00NNx:'..       lXKc.     'lONN0l.
  .dNKoON0;lXNkcld0NXo::cd0NNO:;,,'.. .0Xc            lXXo..'l0NNKd,.
   .xNX0NKc.cXXl  ;KXl    .dN0.       .0No            .xNXOKNXOo,.
    .lKWN0d::OWK;  lXXc    .OX:       .ONx.     . .,cdk0XNXOd;.   .'''....
      .:dOKNNNWNKOxkXWXo:,,;ONk;,,,,,;c0NXOxxkO0XXNXKOdc,.  ..;::,...;l
          ..';cldxkOO0KKKXXXXXXXXXXKKKKK00Okxdol:;'..   .';::,..':ll
 .     ''            ..................             .,;:;,',;ccc;
.;      ,lc,.         ................        ..,,;;;;;;:::,.
 .'.      .;ccc;,'....              ....'',;;;;;;;;;;'..
   .;;,..       ....                ..''''''''....
      ..,;::;;,'.........................
"""

stroll = """                    ..',;:cllllllcc::;,'..',.
           .:kKXNKkoc;,,,,,,;,'''','.       'OK'
       .kKc..'::,.....';::;'.....';;'..;'      kK.
     :Nd     ...',,'.        ,.....',',:,.,.    dN.
     0.    ..       '       ;           '.'      oX
    dX        ...   ;        'xK0XWWWN0c          :X.
  lNl.'.....XNkkNWWNo      :N; .ckWNNWKxN:.::   .;;:kXx
 Nk;,'.           .;NO,     dXx,   dd      .dKK00O:  .'K,
;N, ; 0kooKK:.d     K'              .dO000kl. c;   K; . Xc
.Nc ,   .0 .'.   .00;       dko..          ;kX0Nx. .X , lX
 :Xc.. .NX    .;0XK.     lkko c0     .;xXXx.  ,N'''ko , Kx
  cN.  KXNNO'      oOlk      .c.:xKKx:. X: .lXWd   ..:.Kd
   dK  NWocK;ONX0xolloodx0KK0dccN    .cXWNk,kK.     ,Xk
   .N  oWNxW,.Nc   .N.   X.     :NKNWWKlkk cX.     .N;
   .X  XWWWWWWWWWNNWNNNNNWNNNWWNKN;.    dWX.      cO
   .X  :N0WKWWWWWWWWWWWNX0N:.    Xc   lN0.       oK
   :K   xXNccX ;X  .N.   .N      .NONO,        lX;
   0o    .dKNWKxXX:,Ok,,,cNOxOXNKd, .;:..ll.:KO.
   N'     '      .........      .;;';c;.'kXd.
  .N.  '   .cc,..       ..',;;;;;.  ;OXd.
   N'    .,:;,.............     .dXk'
   .Ko                  .:xkx00c.
     .dX0dc;,',;:ldOK0kl,.
            ..
"""

pika = """quu..__
 $$$b  `---.__
  \"$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$\"              .
     \"$b          -'            `-.-'            $$$\"              .'|
       \".                                       d$\"             _.'  |
         `.   /                              ...\"             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@\"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `\"--'             |    `-.     \\
        :##.       ==             .###.       `.      `.    `\\
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap\\
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'"""

batman = """                    ,.ood888888888888boo.,
               .od888P^\"\"            \"\"^Y888bo.
           .od8P''   ..oood88888888booo.    ``Y8bo.
        .odP'\"  .ood8888888888888888888888boo.  \"`Ybo.
      .d8'   od8'd888888888f`8888't888888888b`8bo   `Yb.
     d8'  od8^   8888888888[  `'  ]8888888888   ^8bo  `8b
   .8P  d88'     8888888888P      Y8888888888     `88b  Y8.
  d8' .d8'       `Y88888888'      `88888888P'       `8b. `8b
 .8P .88P            \"\"\"\"            \"\"\"\"            Y88. Y8.
 88  888                                              888  88
 88  888                                              888  88
 88  888.        ..                        ..        .888  88
 `8b `88b,     d8888b.od8bo.      .od8bo.d8888b     ,d88' d8'
  Y8. `Y88.    8888888888888b    d8888888888888    .88P' .8P
   `8b  Y88b.  `88888888888888  88888888888888'  .d88P  d8'
     Y8.  ^Y88bod8888888888888..8888888888888bod88P^  .8P
      `Y8.   ^Y888888888888888LS888888888888888P^   .8P'
        `^Yb.,  `^^Y8888888888888888888888P^^'  ,.dP^'
           `^Y8b..   ``^^^Y88888888P^^^'    ..d8P^'
               `^Y888bo.,            ,.od888P^'
                    \"`^^Y888888888888P^^'\"         LS"""

penguin = """                 .88888888:.
                88888888.88888.
              .8888888888888888.
              888888888888888888
              88' _`88'_  `88888
              88 88 88 88  88888
              88_88_::_88_:88888
              88:::,::,:::::8888
              88`:::::::::'`8888
             .88  `::::'    8:88.
            8888            `8:888.
          .8888'             `888888.
         .8888:..  .::.  ...:'8888888:.
        .8888.'     :'     `'::`88:88888
       .8888        '         `.888:8888.
      888:8         .           888:88888
    .888:88        .:           888:88888:
    8888888.       ::           88:888888
    `.::.888.      ::          .88888888
   .::::::.888.    ::         :::`8888'.:.
  ::::::::::.888   '         .::::::::::::
  ::::::::::::.8    '      .:8::::::::::::.
 .::::::::::::::.        .:888:::::::::::::
 :::::::::::::::88:.__..:88888:::::::::::'
  `'.:::::::::::88888888888.88:::::::::'
        `':::_:' -- '' -'-' `':_::::'` """

banksy = """                        .s$$$Ss.
            .8,         $$$. _. .              ..sS$$$$$\"  ...,.;
 o.   ,@..  88        =.$\"$'  '          ..sS$$$$$$$$$$$$s. _;\"'
  @@@.@@@. .88.   `  ` \"\"l. .sS$$.._.sS$$$$$$$$$$$$S'\"'
   .@@@q@@.8888o.         .s$$$$$$$$$$$$$$$$$$$$$'
     .:`@@@@33333.       .>$$$$$$$$$$$$$$$$$$$$'
     .: `@@@@333'       ..>$$$$$$$$$$$$$$$$$$$'
      :  `@@333.     `.,   s$$$$$$$$$$$$$$$$$'
      :   `@33       $$ S.s$$$$$$$$$$$$$$$$$'
      .S   `Y      ..`  ,\"$' `$$$$$$$$$$$$$$
      $s  .       ..S$s,    . .`$$$$$$$$$$$$.
      $s .,      ,s ,$$$$,,sS$s.$$$$$$$$$$$$$.
      / /$$SsS.s. ..s$$$$$$$$$$$$$$$$$$$$$$$$$.
     /`.`$$$$$dN.ssS$$'`$$$$$$$$$$$$$$$$$$$$$$$.
    ///   `$$$$$$$$$'    `$$$$$$$$$$$$$$$$$$$$$$.
   ///|     `S$$S$'       `$$$$$$$$$$$$$$$$$$$$$$.
  / /                      $$$$$$$$$$$$$$$$$$$$$.
                           `$$$$$$$$$$$$$$$$$$$$$s.
                            $$$\"'        .?T$$$$$$$
                           .$'        ...      ?$$#\
                           !       -=S$$$$$s
                         .!       -=s$$'  `$=-_      :
                        ,        .$$$'     `$,       .|
                       ,       .$$$'          .        ,
                      ,     ..$$$'
                          .s$$$'                 `s     .
                   .   .s$$$$'                    $s. ..$s
                  .  .s$$$$'                      `$s=s$$$
                    .$$$$'                         ,    $$s
               `   \" .$$'                               $$$
               ,   s$$'                              .  $$$s
            ` .s..s$'                                .s ,$$
             .s$$$'                                   \"s$$$,
          -   $$$'                                     .$$$$.
        .\"  .s$$s                                     .$',',$.
        $s.s$$$$S..............   ................    $$....s$s......
         `\"\"'           `     ```\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"         `\"\"   ``
                                                           [banksy]dp """

felix = """                        b                         .$
                        4r                       .$$
                        4$r                     z$$$
                        $$$c                   d. $$
                        $$d$$c.eeeeePeee..   z\"4-'P$
                       J$$$$$dP3\"\"\"*$*$$ee$$$$$ \" $$F
                      z$*.P*$ \"- .=\"         '\  $$$$
                    .P    'F\" *e\"               \/$$$
                    \"      4  ^                  ^ $$b
                           4$%                    ^$$$r
                            F                      4$$$
                           4                        $$$b
                .    4$b   P           .ec          $$$$b
                     $\"               4$P\"\"         $$$$$$c
               ^    4$$$r 4\"          4$eec        4$$$$P\"*$e
     \         .     $$$   4          ^$$$F        $$$$$E.zd$$$\"
      ^\       F            r                     d$$P\"  *$$$P .^
         -.    .        %   ^.                   J$P      $$F.      /
              \"$\    .z.      -                 $P\" ^    .P      .^
                  \"\"3$$$$$$e    \".           .d\"     ^   $F  -\"
                ^   $$$$$$$$L       ^\"\"==\"\"\"\"\"      /   ^
                 -  3$ee= \"$\"                      /  .\"
                  ^. ^****\"                      z\"  ^
                                               z\"  /
                      -.                   .e$\"  =
                        ^ ec..... ....ee$$*\"  .^
                         \".  \"\"\"**\"\"\"     .=^
                              \"  === \"\"\"                                 """

homer = """          _ _,---._
       ,-','       `-.___
      /-;'               `._
     /\/          ._   _,'o \
    ( /\       _,--'\,','\"`. )
     |\      ,'o     \'    //\
     |      \        /   ,--'\"\"`-.
     :       \_    _/ ,-'         `-._
      \        `--'  /                )
       `.  \`._    ,'     ________,','
         .--`     ,'  ,--` __\___,;'
          \`.,-- ,' ,`_)--'  /`.,'
           \( ;  | | )      (`-/
             `--'| |)       |-/
               | | |        | |
               | | |,.,-.   | |_
               | `./ /   )---`  )
              _|  /    ,',   ,-'
     -hrr-   ,'|_(    /-<._,' |--,
             |    `--'---.     \/ \
             |          / \    /\  \
           ,-^---._     |  \  /  \  \
        ,-'        \----'   \/    \--`.
       /            \              \   \ """

tubemap = """  m       m         o                                     o      c
   m      m         o                      n       p  o  o       c            e
 mmmmmmmmmm         o                      n       p  o o        c           e
          m         o                    n n       p  oo    o    c          e
      c    m        o           n         nn       p  o     o    ccccc     e
      c     m       o   j        n         n       p  o     o    c   c    eo
  mpmpmpmpm  m      b   j         n        n    oopoooooo   o    c   c   e  o
      c    pmmmmmmmmmmmm j         n       n   o pvvvvvvvvvvvv   c   c  e    o
      c     p       o   m j         n   ooonooo pv    o   o o    ccccc e      d
      c     p       b    m joooo     n o   n   p v    o    oooooocoooee      d
       c    p       o     mojjjjoooooonoo n   p  v     o  o      c  eo      d
        c   p      oboooooommmmmj      n nooopooovooooo oo      c ee  o    d
         c  p     o b           mj      n   p    voooo oooooooocojr   o   d
          c p    o  b           mj     n nvpvvvvvv    o       c ejr   oo d
           cp   oo   bbbbbbbbbbbmj    n vnpnnnnn      o      c e jr     h
            c   o oeeeeihihihihihmhimhimhimh   n   cccccccccc e  jr    d
            pc  oe o  h   idid   b   vn  p  i  n  ceeeedhdhdhdhdhdhdhdh
            p ceo   oi    d      jb v n  p   mhimhimh heeeeeer   jr
      eeeeeepeeco    h    i    cccccccccpccc   nc   ido      r   jr
     e     cpcccccccccccccdcccc  jv b np    ccccrrrrm o      r   jr
    e       p   o    i  o i     ppppppp       didididrrrrrrrrrrrrjrrrrrrr
    e       p   o    h  o d    p  vj  b      iwn      o      r   j    r  r
    e      pppppppppppppppipppp   v j nb    dw n      o      r   j     r  r
    e     p  ddddddddddddddididididididididiw jnjjjjjjjjjjjjjjjjjj      r  r
    e    p     o        od        v   nbwwww jn       o      r           r  r
    e   p      d         do       v   nbjjjjjn        o      r            r  r
    e  p       o         d o      v   nb    n         o      r            r
   pppp        d         d  o     v   nb nnn         ooo     r            r
  p e p                  d  o     v   nbn           o o o    r
  p e p                  d  o      v  nb           o  o  o   r
   ppp                   d   oooooo v n           o   o      r
                          t        oonoooooooooooo    o
                          t         n v               o             ttttttttttt
                          t        n   v           oooo            t
                          t       n                   o           tttttt
                          t      n                 tttttttt      t
                           t    n                  t      t     t
                            tttntttttttttttttttttttttttttttttttt
                              n                                 ttttttttttttt    """
tubelines = ["b","c","i","d","h","j","m","n","p","v","w","r","o","e","t"," "]
tubelines2 = ["[" + i + "]" for i in tubelines]
tubecolors = ["o","r","y","g","p","K","m","W","b","B","C","c","R","p","G","-"]
for i in range(len(tubelines)):
    tubemap = tubemap.replace(tubelines[i],tubelines2[i])
for i in range(len(tubelines)):
    tubemap = tubemap.replace(tubelines2[i],tubecolors[i])

pagels = []
pagels.append(ArtPage("273","Mona Lisa",lisa,"The Mona Lisa  by  Leonardo da Vinci",True))
pagels.append(ArtPage("274","Venus",venus,"The Birth of Venus  by  Sandro Botticelli"))
pagels.append(ArtImagePage("275","Jigsaw",jig,"Do you want to play a game?"))
pagels.append(ArtPage("276","Soup",soup,"Soup!"))
pagels.append(ArtImagePage("277","Python",python))
pagels.append(ArtPage("278","SCORPIONS",scorp,"SCORPIONS",True))
pagels.append(SqPage("279"))
pagels.append(ArtImagePage("280","EMF Logo",emf))
pagels[-1].importance = 3
pagels.append(ArtImagePage("281","Club Mate",mate))
pagels[-1].importance = 3
pagels.append(ArtPage("282","The Scream",scream,"The Scream  by  Edvard Munch"))
pagels.append(ArtPage("283","Guernica",guern,"Guernica  by  Pablo Picasso"))
pagels.append(ArtPage("284","The Eiffel Tower",eif))
pagels.append(ArtPage("285","The Statue of Liberty",liberty))
pagels.append(ArtPage("286","Cafe Terrace by Night",cafe,"Cafe Terrace by Night   by  Vincent Van Gogh"))
pagels.append(ArtPage("287","The Persistence of Memory",dali,"The Persistence of Memory  by  Salvador Dali"))
pagels.append(ArtPage("288","The Girl with a Pearl Earring",pearl,"The Girl with a Pearl Earring  by  Jan Vermeer"))
pagels.append(ArtPage("289","The Picnic",manet,"The Picnic  by  Edouard Manet"))
pagels.append(ArtPage("290","Four Dancers",degas,"Four Dancers  by  Edgar Degas"))
pagels.append(ArtPage("291","Einstein",einstein))
pagels.append(ArtPage("292","Troll Face",troll))
pagels.append(ArtPage("293","Smaller Troll Face",stroll))
pagels.append(ArtPage("294","Pikachu",pika,"PIKA!"))
pagels.append(ArtPage("295","The Batman",batman))
pagels.append(ArtPage("296","Linux",penguin))
pagels.append(ArtPage("297","Banksy",banksy))
pagels.append(ArtPage("298","Felix The Cat",felix))
#pagels.append(ArtPage("299","Homer Simpson",homer,color="YELLOW"))
pagels.append(ArtImagePage("299","Tube map",tubemap))

page0 = ArtIndex("272","272-299",pagels)

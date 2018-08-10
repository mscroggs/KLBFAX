from page import Page


class MonaLisaPage(Page):
    def __init__(self,page_num,index_num):
        super(MonaLisaPage, self).__init__(page_num)
        self.title = "Art"
        self.index_num = index_num
        self.tagline = "Are you warm,are you real,Mona Lisa? Or just a cold & lonely lovely work of art?"

    def generate_content(self):
        content = self.add_title("Mona Lisa")
        self.add_text('''                           _,,ad8888888888bba,_
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
88888888888888888888888888888888ZZZZZZZZZZZZZZ8888888888888888888 Veilleux 88
''')

class VenusPage(Page):
    def __init__(self,page_num):
        super(VenusPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Venus"
        self.tagline = "Here, it is a nude Venus who emerges from the shell, floating on waves."

    def generate_content(self):
        self.add_title("Venus")
        self.add_text("""                                    ,<<CCCCCCC>>,,..,,,<C> ,c' -;;,`C><   ,-
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
          .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ `<CCCCC>  -<CC;,<C> ``<<CCC>,`CCCC

""")

class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Jigsaw"
        self.tagline = "Do you want to play a game?"

    def generate_content(self):
        self.add_title("Jigsaw")
        jig = """     ,XX'''''''''''''XX,,
    XXX               XXX
   XXX                 XXX
  XXX   ,'',     ,'',   XXX
 XXXX ,'    ', ,'    ', XXXX
 XXXX  ,XXXX     XXXX,  XXXXX
XXXXX XXRRRXX   XXRRRXX XXXXX
XXXXX XXRXRXX   XXRXRXX XXXXX
XXXXX XXRRRX' , 'XRRRXX XXXXX
XXXX'  ''''' ,X, '''''  'XXXX
XXX ,''',    XXX    ,''', XXX
XXX  ,', X  XXXXX  X ,',  XXX
XXX X  X X  XXXXX  X X  X XXX
XXX X '  X ,XXXXX, X  ' X XXX
XXX, ''''  X 'X' X  '''' ,XXX
XXXX                     XXXX
 XXX   'RRRRRRRRRRRRR'   XXXX
 XXX       X     X       XXXX
 XXXX     X       X     XXXXX
   XXX,  X    X    X  ,XXXXX
     'XXXXX,,XXX,,XXXXX'
          X,     ,X
          ,X     X,
       ,XXXX     XXXX,
     ,XXXXXXX   XXXXXXX,
   ,XXXXXXXXXXXXXXXXXXXXX,
 ,XXX'   XXXXXXXXXXX   'XXX,
XXX'     XXXXXXXXXXX     'XXX
XXXXGG   XXXXXXXXXXX   GGXXXX
     GG  XXXXXXXXXXX  GG
      GG XXXXXXXXXXX GG
       GGGGGGGGGGGGGGG
         XXXXGGXXXXX
        XXXXXGGXXXXXX
      XXXXXXXGGXXXXXXX
     XXXXX  XGGX  XXXXX"""

        for line in jig.split("\n"):
            for c in line:
                if c=="X":
                    self.add_text(u"\u2588")
                elif c=="'":
                    self.add_text(u"\u2580")
                elif c==",":
                    self.add_text(u"\u2584")
                elif c=="R":
                    self.start_fg_color("RED")
                    self.add_text(u"\u2588")
                    self.end_fg_color()
                elif c=="G":
                    self.start_fg_color("GREY")
                    self.add_text(u"\u2588")
                    self.end_fg_color()
                else:
                    self.add_text(" ")
            self.add_newline()

class SoupPage(Page):
    def __init__(self,page_num):
        super(SoupPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Soup"
        self.tagline = "Soup!"

    def generate_content(self):
        self.add_text('''
          _______________________________
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
         '==============================='
''')


class PyPage(Page):
    def __init__(self,page_num):
        super(PyPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Python"
        self.tagline = "Python"

    def generate_content(self):
        self.add_title("Python")
        self.add_newline()
        self.add_block("""
            000000000000000
            00  00000000000
            00  00000000000
            000000000000000
                     000000
    00000000000000000000000 1111111
    00000000000000000000000 1111111
    0000000000000000000000  1111111
    000000000             111111111
    0000000  1111111111111111111111
    0000000 11111111111111111111111
    0000000 11111111111111111111111
            111111
            111111111111111
            11111111111  11
            11111111111  11
            111111111111111
""","BLUE","YELLOW")

class ScorPage(Page):
    def __init__(self,page_num):
        super(ScorPage, self).__init__(page_num)
        self.in_index = False
        self.title = "SCORPIONS"
        self.tagline = "SCORPIONS"

    def generate_content(self):
        self.add_title("SCORPIONS",font="size4")
        self.add_text("""
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

""")

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

class EMFPage(Page):
    def __init__(self, num):
        super(EMFPage, self).__init__(num)
        self.in_index = False
        self.title = "EMF Logo"

    def generate_content(self):
        self.print_image(
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

class MatePage(Page):
    def __init__(self, num):
        super(MatePage, self).__init__(num)
        self.in_index = False
        self.title = "Club Mate"

    def generate_content(self):
        self.print_image(
                        "-----------------bbbbbbbbbbbbbbbbb---------------------------------------------\n"
                        "---------------bbbbbbbbbbbbbbbbbbbbb--------------------bbbbbbb----------------\n"
                        "-------------bbbbbbccbbbbbbbbbccbbbbbb------------------byyyyyb----------------\n"
                        "-----------bbbbwwwwwcbbbbbbbbbwwwwwwbbbb----------------bybbbbb----------------\n"
                        "---------bbbbwwwwwwwbbbbbbbbbbcwwwwwwwbbbb--------------byb--------------------\n"
                        "--------bbbwwwwwwwwwbbbbbbbbbbcwwwwwwwwwbbb-------------bybbbbb----------------\n"
                        "-------bbbwwwwwwwwwwbbbbbbbbbbbwwwwwwwwwwbbb------------byyyyyb----------------\n"
                        "------bbbwwwwwwwwwwcbbbbbbbbbbbcwwwwwwwwwwbbb-----------bbbbbbb----------------\n"
                        "-----bbbwwwwwwwwwwwcbbbbbbbbbbbcwwwwwwwwwwwbbb---------------------------------\n"
                        "----bbbwwwwwwwwwwwwcbbbbbbbbbbbbwwwwwwwwwwwwbbb---------bbb--------------------\n"
                        "---bbbwwwwwwwwwwwwwcbbbbbbbbbbbbwwwwwwwwwwwwwbbb--------byb--------------------\n"
                        "---bbbwwwwwwwwwwwwwcbbbbbbbbbbbbcwwwwwwwwwwwwbbb--------byb--------------------\n"
                        "--bbbwwwwwwwwwwwwwwcbbbbbbbbbbbbcwwwwwwwwwwwwwbbb-------byb--------------------\n"
                        "--bbwwwwwwwwwwwwwwwcbbbbbbbbbbbbcwwwwwwwwwwwwwwbb-------bybbbbb----------------\n"
                        "-bbbwwwwwwwwwwwwwwwcbbbbbbbbbbbbbbbbccwwwwwcccwbbb------byyyyyb----------------\n"
                        "-bbwwwwwwwwwwwwwwwwbbbbbbbbbbbbbbcccwwcccbbbbbwwbb------bbbbbbb----------------\n"
                        "bbbwwwwwwwwwwcccbbbbbbbbbbcccccwwccbbbbbbbbbbcwwbbb----------------------------\n"
                        "bbwwwwwwwwccbbbbbbcwwwwwwwwwwwwccbbbbbbbbbbcwwwwwbb-----bbb-bbb----------------\n"
                        "bbwwwwccbbbbbbbbcccccccccccccbbbbbbbbbbbbccwwwwwwbb-----byb-byb----------------\n"
                        "bbwwwwcbbbbbbbbbbbbbbbbbbbcbbbbcbbbbbbcccwwwwwwwwbb-----byb-byb----------------\n"
                        "bbwwwwwcccbbbbbbbbbbbbcbbbcwccwwcbbbccwwwwwwwwwwwbb-----byb-byb----------------\n"
                        "bbwwwwwwwwwwwwwwccccbbwwbbcwwwwwcbbbwwwwwwwwwwwwwbb-----bybbbyb----------------\n"
                        "bbwwwwwwwwwwwwwwwwwcbbccbbcwwwwwcbcbwwwwwwwwwwwwwbb-----byyyyyb-------bbbbb----\n"
                        "bbwwwwwwwwwwwwwwwwcccbbbbbbccccwcccbwwwwwwwwwwwwwbb-----bbbbbbb------bbybybb---\n"
                        "bbwwwwwwwwwwwwwwwwcccbbbbbccbbcwcbbcwwwwwwcwwwwwwbb------------------bybybyb---\n"
                        "bbwwwwwwwwwwwwwwwwccbccbbbccwwcwwccwwwwwcwwwwwwwwbb-----bbbbbb-------bybybyb---\n"
                        "bbwwwwwwwwwwwwwwwwwccwcbbwccwwcwwwwwwwcwwwwbwcwwwbb-----byyyybb------bybbbyb---\n"
                        "bbwwwwwwwwwwwwwwwwwccwcbbcwwwccwwwwwwwcwcwbwwcwwwbb-----bybbyyb------byb-byb---\n"
                        "bbwwwwwwwwwwwwwwwwcbbbbbbbccwbcwwwwwwwcwwwwwccwwwbb-----bybbyyb------bbb-bbb---\n"
                        "bbwwwwwwwwwwwwwwcbbbbbbbbbbcwbcwwwwwwwcwwwbwccwwwbb-----byyyybb----------------\n"
                        "bbwwwwwwwwwwwwwcbbbbbbbbbbbbwbbwwwwwwwcwcwwwcwwwwbb-----bybbyyb-------bbbbb----\n"
                        "bbwwwwwwwwwwwcbbbbbbbbbbbbbbbbbwwwwwwwcwwwwwcwwwwbb-----bybbyyb------bbyyybb---\n"
                        "bbwwwwwwwwwwcbbbbbbbbbbbbbbbbbbbwwwwwwcwwcccbwwwwbb-----byyyybb------bybbbyb---\n"
                        "bbbwwwwwwwwcbbbbbbbbbbbbbbbbbbbbcwwwwccwcccccwwwbbb-----bbbbbb-------bybbbyb---\n"
                        "bbbwwwwwwwwbbbbbbbbbbbbbbbbbbbbbbwwwcccccwwcwwwwbbb------------------byyyyyb---\n"
                        "-bbwwwwwwwbbbbbbbbbbbbbbbbbbbbbbbwcccccwwwccwwwwbb-------------------bybbbyb---\n"
                        "-bbbwwwwwbbbbbbbbbbbbbbbbbbbbbbbbbbcwccwwcbcwwwbbb-------------------bbb-bbb---\n"
                        "--bbwwwwcbbbbbbbbbbbbbbbbbbbbbbbbcwwwwwwcbbcwwwbb------------------------------\n"
                        "--bbbwwcbbbbbbbbbbbbbbbbbbbbbbbbbwwwwwwwwbbwwwbbb--------------------bbbbbbb---\n"
                        "---bbccbbbbbbbbbbbbbbbbbbbbbbbbbcwwwwwwwwccwwwbb---------------------byyyyyb---\n"
                        "---bbbbbbbbbbbbbbbbbbbbbbbbbbbbcwwwwwwwwccwwwbbb---------------------bbbybbb---\n"
                        "----bbbbbbbbbbbbbbbbbbbbbbbbbbbcwwwwwwcbcwwwwbb------------------------byb-----\n"
                        "----bbbbbbbbbbbbbbbbbbbbbbbbbbbcwwccbbbwwwwwbbb------------------------byb-----\n"
                        "-----bbbbbbbbbbbbbbbbbbbbbbbbbbcwwbbbbbwwwwbbb-------------------------byb-----\n"
                        "------bbbbbbbbbbbbbbbbbbbbbbbbbcwcbbbbbcwcbbb--------------------------bbb-----\n"
                        "-------bbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbcbbb-----------------------------------\n"
                        "--------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb--------------------------bbbbbbb---\n"
                        "---------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb---------------------------byyyyyb---\n"
                        "----------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb----------------------------bybbbbb---\n"
                        "------------bbbbbbbbbbbbbbbbbbbbbbbbbbb------------------------------byyyb-----\n"
                        "--------------bbbbbbbbbbbbbbbbbbbbbbb--------------------------------bybbbbb---\n"
                        "----------------bbbbbbbbbbbbbbbbbbb----------------------------------byyyyyb---\n"
                        "---------------------bbbbbbbbb---------------------------------------bbbbbbb---\n"
                        "-------------------------------------------------------------------------------\n"
            )

page1 = MonaLisaPage("272","272-299")
page2 = VenusPage("273")
page3 = JigPage("274")
page4 = SoupPage("275")
page5 = PyPage("276")
page6 = ScorPage("277")
page7 = SqPage("278")
page8 = EMFPage("279")
page9 = MatePage("280")

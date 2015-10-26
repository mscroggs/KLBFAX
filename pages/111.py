from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from time import strftime
import screen


class VenusPage(Page):
    def __init__(self,page_num):
        super(VenusPage, self).__init__(page_num)
        self.title = "Venus"
        self.tagline = "Here, it is a nude Venus who emerges from the shell, floating on waves."

    def generate_content(self):
        import urllib2
        content = colour_print(printer.text_to_ascii("Venus",fill=True))
        content += "\n"
        content += """                                    ,<<CCCCCCC>>,,..,,,<C> ,c' -;;,`C><   ,-
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
          
"""        


        
        '''
                           _,,ad8888888888bba,_
                        ,ad88888I888888888888888ba,
                      ,88888888I88888888888888888888a,
                    ,d888888888I8888888888888888888888b,
                   d88888PP"""" ""YY88888888888888888888b,
                 ,d88"'__,,--------,,,,.;ZZZY8888888888888,
                ,8IIl'"                ;;l"ZZZIII8888888888,
               ,I88l;'                  ;lZZZZZ888III8888888,
             ,II88Zl;.                  ;llZZZZZ888888I888888,
            ,II888Zl;.                .;;;;;lllZZZ888888I8888b
           ,II8888Z;;                 `;;;;;''llZZ8888888I8888,
           II88888Z;'                        .;lZZZ8888888I888b
           II88888Z; _,aaa,      .,aaaaa,__.l;llZZZ88888888I888
           II88888IZZZZZZZZZ,  .ZZZZZZZZZZZZZZ;llZZ88888888I888,
           II88888IZZ<'(@@>Z|  |ZZZ<'(@@>ZZZZ;;llZZ888888888I88I
          ,II88888;   `""" ;|  |ZZ; `"""     ;;llZ8888888888I888
          II888888l            `;;          .;llZZ8888888888I888,
         ,II888888Z;           ;;;        .;;llZZZ8888888888I888I
         III888888Zl;    ..,   `;;       ,;;lllZZZ88888888888I888
         II88888888Z;;...;(_    _)      ,;;;llZZZZ88888888888I888,
         II88888888Zl;;;;;' `--'Z;.   .,;;;;llZZZZ88888888888I888b
         ]I888888888Z;;;;'   ";llllll;..;;;lllZZZZ88888888888I8888,
         II888888888Zl.;;"Y88bd888P";;,..;lllZZZZZ88888888888I8888I
         II8888888888Zl;.; `"PPP";;;,..;lllZZZZZZZ88888888888I88888
         II888888888888Zl;;. `;;;l;;;;lllZZZZZZZZW88888888888I88888
         `II8888888888888Zl;.    ,;;lllZZZZZZZZWMZ88888888888I88888
          II8888888888888888ZbaalllZZZZZZZZZWWMZZZ8888888888I888888,
          `II88888888888888888b"WWZZZZZWWWMMZZZZZZI888888888I888888b
           `II88888888888888888;ZZMMMMMMZZZZZZZZllI888888888I8888888
            `II8888888888888888 `;lZZZZZZZZZZZlllll888888888I8888888,
             II8888888888888888, `;lllZZZZllllll;;.Y88888888I8888888b,
            ,II8888888888888888b   .;;lllllll;;;.;..88888888I88888888b,
            II888888888888888PZI;.  .`;;;.;;;..; ...88888888I8888888888,
            II888888888888PZ;;';;.   ;. .;.  .;. .. Y8888888I88888888888b,
           ,II888888888PZ;;'                        `8888888I8888888888888b,
           II888888888'                              888888I8888888888888888b
          ,II888888888                              ,888888I88888888888888888
         ,d88888888888                              d888888I8888888888ZZZZZZZ
      ,ad888888888888I                              8888888I8888ZZZZZZZZZZZZZ
    ,d888888888888888'                              888888IZZZZZZZZZZZZZZZZZZ
  ,d888888888888P'8P'                               Y888ZZZZZZZZZZZZZZZZZZZZZ
 ,8888888888888,  "                                 ,ZZZZZZZZZZZZZZZZZZZZZZZZ
d888888888888888,                                ,ZZZZZZZZZZZZZZZZZZZZZZZZZZZ
888888888888888888a,      _                    ,ZZZZZZZZZZZZZZZZZZZZ888888888
888888888888888888888ba,_d'                  ,ZZZZZZZZZZZZZZZZZ88888888888888
8888888888888888888888888888bbbaaa,,,______,ZZZZZZZZZZZZZZZ888888888888888888
88888888888888888888888888888888888888888ZZZZZZZZZZZZZZZ888888888888888888888
8888888888888888888888888888888888888888ZZZZZZZZZZZZZZ88888888888888888888888
888888888888888888888888888888888888888ZZZZZZZZZZZZZZ888888888888888888888888
8888888888888888888888888888888888888ZZZZZZZZZZZZZZ88888888888888888888888888
88888888888888888888888888888888888ZZZZZZZZZZZZZZ8888888888888888888888888888
8888888888888888888888888888888888ZZZZZZZZZZZZZZ88888888888888888 Normand  88
88888888888888888888888888888888ZZZZZZZZZZZZZZ8888888888888888888 Veilleux 88
8888888888888888888888888888888ZZZZZZZZZZZZZZ88888888888888888888888888888888
'''
        
        self.content = content

page = VenusPage("231")

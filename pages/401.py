from page import Page


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

page = VenusPage("401")

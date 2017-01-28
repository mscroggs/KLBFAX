from page import Page


class MonaLisaPage(Page):
    def __init__(self,page_num):
        super(MonaLisaPage, self).__init__(page_num)
        self.title = "Art"
        self.index_num = "400-420"
        self.tagline = "Are you warm,are you real,Mona Lisa? Or just a cold & lonely lovely work of art?"

    def generate_content(self):
        import urllib2
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

page = MonaLisaPage("400")

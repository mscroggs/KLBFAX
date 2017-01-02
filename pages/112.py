from page import Page


class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Jigsaw"
        self.tagline = "Do you want to play a game?"

    def generate_content(self):
        import urllib2
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

page = JigPage("112")

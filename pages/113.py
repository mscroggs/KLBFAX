from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from time import strftime
import screen


class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Jigsaw"
        self.tagline = "Do you want to play a game?"

    def generate_content(self):
        import urllib2
        content = colour_print(printer.text_to_ascii("Jigsaw",fill=True))
        content += "\n"
        jig = """     ,XXTTTTTTTTTTTTTXX,,
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
        jig = "\u2588".join(jig.split("X")
        jig = "\u2580".join(jig.split("'")
        jig = "\u2584".join(jig.split(",")
        jig = (self.colours.Foreground.RED+"\u2588"+self.colours.Foreground.DEFAULT).join(jig.split("R")
        jig = (self.colours.Foreground.BLACK+self.colours.Style.BOLD+"\u2588"+self.colours.Foreground.DEFAULT+self.colours.Style.Default).join(jig.split("G")
        content += jig
        
        self.content = content

page = JigPage("113")

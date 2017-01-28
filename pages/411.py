from page import Page
import datetime

class TeaPage(Page):
    def __init__(self):
        super(TeaPage, self).__init__("411")
        self.title = "I'm a Teapot"
        self.in_index=False

    def generate_content(self):
        self.add_title("411",font="size4")
        self.add_text("""                                     ,o.
                                    c.o8o
                                   (CoC8@)
     /).                            CcC@8
     V@@8.                        ..o@8@o..                ,.oooo.
      `@88`.              ,cc@8@88C'cc:cc`C88@88o.    ,ooc***"'.:*Oo.
       `OCCo8          .OCc**@@8@88@CoCoC@88@8@@**'oCOOoo::.....oo:.o.
        8Cooc8       .oocococccc**8@8CcC8@8**OCOO8O88@88ooC@88@@@@8c:o
         8c:c:8.   .'cocc:c:c:::::c:c:ccocooCoCCOCOO8O888o88'    8*cc8
         `8:.:.8@@8@8occcc:c:::::::c:ccccooooCCOCOO8O88@@@8      8o o8
          8.. ..@8OC8@c:c::.:.....:.::c:ccocooCoCCOO8O88@8@.    ,C:.C;
          `8.:..@coCC@cc::.:.. . ..:.::ccocooCoCCOO8O88@8@@8   ;C:.o;
           *c.o88OC8@8c::.:..     ..:.::ccccooCoCCOOOO88@8@@ ,8C:o8'
            `*@8@@8@'occ::.:.. . ..:.::ccocooCoCCOO8O88@8@@@*8OC8C'
               `88;cocc:c::.:.....:.::c:ccocooCoCCOO8O88@8@@OCC8@'
                 8oooocccc:c:::::::c:ccccooooCCOCOO8O88@@@@@88@'
                 `Coococc:c:c:::::c:c:ccocooCoCCOCOO8O88@@@C@'
                  `8oCoocococccccccococooCoCCOCOO8O88@8@@@*'
                    'CcoocococococococooooCoCCOCOO8O88@@8
                      `8CCoCoooooooCoCoCCCCOCOO8O88@8@8'
                        'c8cCoCoCoCoCoCCCCOCOO8@888@"
                           `**cCCC8@8@@8@@@8@C8@8*""")

t = TeaPage()

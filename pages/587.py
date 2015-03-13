#width:79
#height: 30

import os
from page import Page

page_number = os.path.splitext(os.path.basename(__file__))[0]
recipe_page = Page(page_number)
recipe_page.title = "Recipe"
recipe_page.content=recipe_page.colours.colour_print("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxx      xxx      xx      xx  xx     xxx      xx      xxxxxxxxxxxxxxxxxxxx
xxxxxxxxx  xx   xx  xxxxxx  xxxxxx  xx  xx  xx  xxxxxx  xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxx     xxxx    xxxx  xxxxxx  xx     xxx    xxxx      xxxxxxxxxxxxxxxxxxxx
xxxxxxxxx  xx  xxx  xxxxxx  xxxxxx  xx  xxxxxx  xxxxxxxxxx  xxxxxxxxxxxxxxxxxxxx
xxxxxxxxx  xxx  xx      xx      xx  xx  xxxxxx      xx      xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx""",recipe_page.colours.Background.RED,recipe_page.colours.Foreground.BLUE)+"""

BAD-TEMPERED CAKE (A.K.A. Tiffin)

  1/2 lb    Rich tea and/or digestive biscuits
    4 oz    Margarine
    1 dsp   Sugar
    3 dsp   Cocoa
    3 dsp   Drinking chocolate
1 1/2 tbsp  Golden syrup
    2 oz    Sultanas
    2 bars  Milk chocolate

1. Break the biscuits.
2. Melt the margarine, sugar, cocoa, drinking chocolate and syrup over a medium
   heat.
3. Mix with biscuits and sultanas and press down in baking tray.
4. Cover with melted milk chocolate.
5. Leave in the fridge to set
"""

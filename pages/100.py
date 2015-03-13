#width:79
#height: 30

from page import Page

index_page=Page("100")

index_page.content=index_page.colours.colour_print("""
xxxxxxxxxxxxxxxxxxxxxx       xxxxxxxxx       xxxxxxxxx
xxxxxxxxxxxxxxxx  x  x         x    xx         x     x
xxxxxxxxxxxxxxxx    xx xxxxxxx x  x  x xxxxxxx x  x  x xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx   xxx x  xxxx x    xx x     x x     x x  x  xxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx  x  x x  xxxx x  x  x x  xxxx x  x  x x  x  xxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx  x  x x  xxxx x    xx x    xx x  x  x xx   xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxx x  xxxx xxxxxxx x  xxxx xxxxxxx x  x  xxxxxxxxxxxxxxxxxxx
                       x     x         x  xxxx         x  x  xxxxxxxxxxxxxxxxxxx
                     xxxxxxxxx       xxxxxxxxx       xxxxxxxxxxxxxxxxxxxxxxxxxxx
""")+"""
KLBFAX is under construction. Check regularly for updates.

The source code of KLBFAX is available at https://github.com/mscroggs/KLBFAX. If
you would like to add features/pages to KLBFAX, ask Scroggs to add you to the
repository.

Press A on the SNES controller to add a cup of tea.

INDEX
"""+index_page.colours.Foreground.MAGENTA+"100"+index_page.colours.Foreground.DEFAULT+""" Index                        """+index_page.colours.Foreground.MAGENTA+"888"+index_page.colours.Foreground.DEFAULT+""" Subtitles
"""+index_page.colours.Foreground.MAGENTA+"150"+index_page.colours.Foreground.DEFAULT+""" Events
"""+index_page.colours.Foreground.MAGENTA+"200"+index_page.colours.Foreground.DEFAULT+""" Letters
"""+index_page.colours.Foreground.MAGENTA+"401"+index_page.colours.Foreground.DEFAULT+""" Weather
"""

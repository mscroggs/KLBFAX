#width:79
#height: 30

from colours import Foreground,Background,colour_print
page=colour_print("""
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
"""+Foreground.MAGENTA+"100"+Foreground.DEFAULT+""" Index                        """+Foreground.MAGENTA+"888"+Foreground.DEFAULT+""" Subtitles
"""+Foreground.MAGENTA+"150"+Foreground.DEFAULT+""" Events
"""+Foreground.MAGENTA+"401"+Foreground.DEFAULT+""" Weather
"""

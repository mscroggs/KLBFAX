from page import Page
import sys

try:
    from imp import reload
except:
    pass

page_file_no_ext = sys.argv[1]

module = getattr(__import__("pages", fromlist=[page_file_no_ext]),
                 page_file_no_ext)
reload(module)
for filename in dir(module):
    obj = getattr(module, filename)
    if isinstance(obj, Page):
        obj.background()
        obj.reload()
        obj.generate_content()

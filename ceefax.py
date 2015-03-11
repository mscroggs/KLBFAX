# width:79
# height: 30

from os import listdir
from random import choice
from os.path import isfile
import os
from base_page import PageFactory,Page

class ConfigError(Exception):
    pass


def is_page_file(f):
    if "_" in f:
        return False
    if "pyc" in f:
        return False
    return True


pages_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pages")
if not os.path.exists(pages_dir):
    try:
        os.makedirs(pages_dir)
    except OSError:
        raise ConfigError("The pages folder doesn't exist" +
                          "and cannot be created: " + pages_dir)

only_page_files = [f for f in listdir(pages_dir)
             if isfile(os.path.join(pages_dir, f)) and is_page_file(f)]

try:
    isinstance(pages,PageFactory)
except NameError:
    pages = PageFactory()

for f in only_page_files:
    load_me = f.split(".")[0]
    module = getattr(__import__("pages", fromlist=[load_me]), load_me)
    reload(module)
    for object in dir(module):
        obj = getattr(module,object)
        if isinstance(obj,Page):
            try:
                pages.add(obj)
            except:
                pass

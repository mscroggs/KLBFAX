# width:79
# height: 30

from os import listdir
from os.path import isfile
import os
from page import PageFactory, Page


class ConfigError(Exception):
    pass


def is_page_file(f):
    if "_" in f:
        return False
    if "pyc" in f:
        return False
    return True


pages_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../pages")
if not os.path.exists(pages_dir):
    try:
        os.makedirs(pages_dir)
    except OSError:
        raise ConfigError("The pages folder doesn't exist" +
                          "and cannot be created: " + pages_dir)

only_page_files = [f for f in listdir(pages_dir)
                   if isfile(os.path.join(pages_dir, f)) and is_page_file(f)]

pageFactory = PageFactory()

for page_file in only_page_files:
    page_file_no_ext = os.path.splitext(page_file)[0]
    module = getattr(__import__("pages", fromlist=[page_file_no_ext]),
                     page_file_no_ext)
    reload(module)
    for object in dir(module):
        obj = getattr(module, object)
        if isinstance(obj, Page):
            try:
                pageFactory.add(obj)
            except:
                pass

pageFactory.print_all()

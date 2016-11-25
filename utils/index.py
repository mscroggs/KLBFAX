#!/usr/bin/env python
import sys
sys.path.insert(0,'..')

# width:79
# height: 30

from os import listdir
from os.path import isfile
import os
from page import PageFactory, Page


def is_page_file(f):
    if "_" in f:
        return False
    if "pyc" in f:
        return False
    return True


pages_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../pages")
only_page_files = [f for f in listdir(pages_dir)
                   if isfile(os.path.join(pages_dir, f)) and is_page_file(f)]

pageFactory = PageFactory()

for page_file in only_page_files:
    try:
        page_file_no_ext = str(os.path.splitext(page_file)[0])
        module = getattr(__import__("pages", fromlist=[page_file_no_ext]),
                         page_file_no_ext)
        reload(module)
        for object in dir(module):
            obj = getattr(module, object)
            if isinstance(obj, Page):
                    pageFactory.add(obj)
    except:
        pass

pageFactory.print_all()
pageFactory.export_all()



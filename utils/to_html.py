#!/usr/bin/env python
import sys
sys.path.insert(0,'..')

from page import PageManager, Page

page_manager = PageManager(None)

page_manager.load_all_pages()

page_manager.export_all_to_html()

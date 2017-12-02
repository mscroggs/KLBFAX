#!/usr/bin/env python
import sys
sys.path.insert(0,'..')

from page import PageManager, Page

page_manager = PageManager(None)

page_manager.test_all_pages()

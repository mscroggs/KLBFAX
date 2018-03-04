#!/usr/bin/env python3
import sys
sys.path.insert(0,'..')

from page import PageManager, Page
from cupt import DummyScreen

page_manager = PageManager(DummyScreen())

page_manager.test_all_pages()

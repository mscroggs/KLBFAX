#!/usr/bin/env python3
import sys
sys.path.insert(0,'..')

import os
os.environ["WWW"] = "1"

from page import PageManager, Page
from ceefax import Ceefax
from cupt import DummyScreen

cee = Ceefax()

page_manager = PageManager(DummyScreen())
cee.page_manager = page_manager

page_manager.export_all_to_html()


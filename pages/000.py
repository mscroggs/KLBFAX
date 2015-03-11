#width:79
#height: 30

from base_page import Page
test_page = Page("000")

test_page.content="""
TEST PAGE
"""
for i in range(0,len(test_page.Foreground.list)):
    test_page.content+=test_page.Foreground.list[i]+test_page.Foreground.delist[i]+test_page.Foreground.DEFAULT+"""
"""
for i in range(0,len(test_page.Background.list)):
    test_page.content+=test_page.Background.list[i]+test_page.Background.delist[i]+test_page.Background.DEFAULT+"""
"""
for i in range(0,len(test_page.Style.list)):
    test_page.content+=test_page.Style.list[i]+test_page.Style.delist[i]+test_page.Style.DEFAULT+"""
"""


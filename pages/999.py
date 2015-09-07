import os
import page

page_number = os.path.splitext(os.path.basename(__file__))[0]
events_page = page.PrisonersPage(page_number)

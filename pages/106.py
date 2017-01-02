from page import Page
from random import shuffle,choice

class StephenPage(Page):
    def __init__(self, page_num):
        super(StephenPage, self).__init__(page_num)
        self.title = "Stephen's Skills"

    def generate_content(self):
        skills = ["Conversation",
                  "Law",
                  "French",
                  "Spanish",
                  "Australian",
                  "Relationships (la petit amor)",
                  "Korean",
                  "Russian",
                  "Fashion",
                  "Keepy uppies",
                  "Probability",
                  "Squash",
                  "Cycling",
                  "Maths",
                  "Taxidermy",
                  "After-dinner speeches",
                  "Writing blogs",
                  "Literary theory",
                  "Reading",
                  "Academic discourse",
                  "The discus",
                  "Water sports",
                  "Bear-baiting",
                  "Editor of magazine",
                  "Patting on head while rubbing stomach",
                  "Football",
                  "Levitation",
                  "Living near Huda",
                  "Greek mythology",
                  "Being a lovely chap",
                  "Pool parties",
                  "Backstroke",
                  "Beamer",
                  "PG Seminars",
                  "Reflective",
                  "Being here most afternoons",
                  "Always paying his debts",
                  "Chivalry",
                  "Softball",
                  "Counting to infinity (backwards)",
                  "Laissez-faire economics",
                  "Coffee",
                  "Typing",
                  "Lunch from UCLU",
                  "Riddlery",
                  "Russian puzzles",
                  "Puzzles",
                  "Art",
                  "Creativity",
                  "Camping",
                  "Self-awareness",
                  "Down-to-earth",
                  "Making tea",
                  "Guitar solos",
                  "Restaurant recommendations",
                  "Djing",
                  "Calendar reading",
                  "Calendar having",
                  "Curing disease",
                  "Karaoke",
                  "Not making a scene",
                  "Politeness",
                  "Navigation",
                  "Proposing",
                  "Sculpture",
                  "Poetry",
                  "Quotes",
                  "Thoughts",
                  "Chocolate fountains",
                  "Programming Scroggsbot",
                  "Hogwarts house-sorting",
                  "Deeper voice than Anna or Grego",
                  "Leadership",
                  "Architecture",
                  "Graphic design",
                  "Entrepeneurship",
                  "Spelling",
                  "Venture capital",
                  "Merges and acquisiitons",
                  "Email",
                  "Excel",
                  "Talking to Richard P.",
                  "Leviticus",
                  "Water into wine",
                  "Jesus",
                  "Eternal life",
                  "Roti King",
                  "Vocabulary",
                  "Handwriting",
                  "Cultural awareness",
                  "Postcards",
                  "Wine tasting",
                  "Problem solving class",
                  "Keeping calm",
                  "Carrying on",
                  "Handsomeness",
                  "Nice smell",
                  "Talking to the elderly",
                  "Painting with all colours of the wind",
                  "Consensus-building",
                  "Modesty",
                  "Opening champagne bottles with just a knife",
                  "Passing vivas"]
        shuffle(skills)
        self.add_title("Stephen's Skills")
        next = 0
        for skill in skills:
            self.start_random_fg_color()
            self.add_text(skill)
            self.end_fg_color()
            if next == 0:
                self.move_cursor(x=38)
            else:
                self.add_newline()
            next += 1
            next %= 2


stephen_page = StephenPage("106")

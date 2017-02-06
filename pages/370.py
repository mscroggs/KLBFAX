from page import Page
import time

def get_tag(t,text):
    if '<td class="'+t+'"' not in text:
        return ""
    return text.split('<td class="'+t+'"')[1].split(">",1)[1].split("</td>")[0]

flags = {"Italy":   "\ngggwwwrrr\ngggwwwrrr\ngggwwwrrr\ngggwwwrrr\ngggwwwrrr\ngggwwwrrr\n",
         "England": "\nwwwrrrwww\nwwwrrrwww\nrrrrrrrrr\nrrrrrrrrr\nwwwrrrwww\nwwwrrrwww\n",
         "Scotland":"\nwwbbbbbww\nbwwbbbwwb\nbbwwbwwbb\nbbbwwwbbb\nbbwwbwwbb\nbwwbbbwwb\n",
         "Wales":   "\nwwwwwwwww\nwrrwwwwrw\nwrrwwwwrw\nwwrrrrrrw\nggrrggrgg\nggggggggg\n",
         "France":  "\nbbbwwwrrr\nbbbwwwrrr\nbbbwwwrrr\nbbbwwwrrr\nbbbwwwrrr\nbbbwwwrrr\n",
         "Ireland": "\ngggwwwooo\ngggwwwooo\ngggwwwooo\ngggwwwooo\ngggwwwooo\ngggwwwooo\n"
        }

class RugbyPage(Page):
    def __init__(self):
        super(RugbyPage, self).__init__("370")
        self.title = "Six Nations"
        self.tagline = "CROUCH! BIND! SET!"

    def background(self):
        import urllib2

        req = urllib2.urlopen('http://www.rbs6nations.com/en/matchcentre/league_table.php')
        results = req.read().split('<td class="titletxt" colspan="2">RBS 6 Nations Table</td>')[1].split("</table>")[0].split("</tr>")[1:]
        self.res = []
        for line in results:
            ls = []
            for a in ["TeamDisplay","Played","Win","Draw","Lose","Points"]:
                ls.append(get_tag("field_"+a,line))
            if "" not in ls:
                self.res.append(ls)
            

    def generate_content(self):
        self.add_title("six nations",font="size4")
        for i,line in enumerate(self.res):
            self.print_image(flags[line[0]],4+4*i)
            for j,k in [(1,10),(2,15),(3,20),(4,25),(5,30)]:
                self.move_cursor(y=5+4*i,x=k)
                self.add_text(line[j])
        self.start_fg_color("RED")
        for j,k in [("P",10),("W",15),("D",20),("L",25),("Pts",30)]:
            self.move_cursor(y=4,x=k)
            self.add_text(j)
        self.end_fg_color()
            

rugby_page = RugbyPage()

from page import Page

lipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
predictions = {
    "Aries":        "There are days when you feel totally blocked. Like you just can't do anything. This is not one of those days. Today you flex your muscles and loosen your tongue and stretch your imagination. Then you get started making things happen. It's a beautiful process, when your internal horizons open up and your external realities start to reflect this expansive state of being. So implement, implement, implement.",
    "Taurus":       "Do you always have tiffs with someone you love over the same stupid things? Today is a really good day to take a harder look at some of these patterns. Chances are, the pettier the ostensible reason for the fight, the more important it is to uncover the real reason behind what's happening. Are you playing out an old wound with this new person? Are you still not sure you can trust another human being with your feelings? Think about it, anyway. Maybe there's a better way.",
    "Gemini":       "You give a whole new meaning to the term 'fresh idea.' Your idea is so fresh it's as if it never even heard of a refrigerator. Your idea is so fresh it's like the refrigerator was never even invented. It's so fresh it still smells like the warm earth you plucked it out of. It's so fresh it lets off a little spray of juice when you bite into it. It's so fresh -- well, you get the idea. Put it into action before it gets stale.",
    "Cancer":       "Yep, your internal touchstone -- the place you touch when you want to see how things are going, how you are feeling and whether or not the path you've chosen is the right one -- is more of a muscle than a rock. Yep, it's thump, thump, thumping away, and it's actually not a bit like a stone. That's right: Your touchstone is your very own heart, and today is a good day to listen to it beating.",
    "Leo":          "There are very few problems that come across your kitchen table that you can't solve. No more OJ? Run to the store. All out of eggs? Call up whoever's on their way over for breakfast. They can pick up a dozen! No sugar? Ask the neighbors for a cup. No syrup? Go out to the front yard and see if you can't drain a little from that decorative Japanese maple. If not, use the neighbor's sugar. You're a problem-solver -- good for you!",
    "Virgo":        "What, you say? It's ridiculous to say you care and then never pick up the phone or write an email or send an old-fashioned postcard? Well, right you are. But don't forget that other folks just aren't as good at communicating as you are. And if they've been a little flaky, it's just bad habits. They really do care about you. So this time around, why not send that first email or pick up the phone yourself?",
    "Libra":        "Life has you moving faster than a speeding bullet lately, hasn't it? You've barely had time to catch your breath between leaping tall buildings and making quick wardrobe changes in telephone booths. The world has got to be saved sometimes, absolutely, and you're often really the only one out there for the job. Today, though, go ahead and take a rest. There'll be villains to tackle tomorrow.",
    "Scorpio":     ("         (        )           ___ __              \n"
                    "         O        O         _{___{__}\                \n"
                    "         ()      ()        {_}      `\)                \n"
                    "          Oo.nn.oO        {_}        `            _.-''''--.._      \n"
                    "           _mmmm_         {_}                    //'.--.  \___`.    \n"
                    "         \/_mmmm_\/        { }__,_.--~~~-~~~-~~-::.---. `-.\  `.)   \n"
                    "         \/_mmmm_\/         `-.{_{_{_{_{_{_{_{_//  -- 8;=- `        \n"
                    "         \/_mmmm_\/            `-:,_.:,_:,_:,.`\\._ ..'=- ,         \n"
                    "         \/ mmmm \/                // // // //`-.`\`   .-'/         \n"
                    "             nn             jgs   << << << <<    \ `--'  /----)     \n"
                    "             ()                    ^  ^  ^  ^     `-.....--'''      \n"
                    "             ()                        \n"
                    "              ()    /                  \n"
                    "         apc   ()__()                  \n"
                    "                '--'                   "),
    "Sagittarius":  "Maybe you feel like sleeping late, getting up slowly, cooking a big batch of pancakes and doing a whole lot of nothing at all, all morning long. Go for it! You've been working really hard lately, and you've accomplished a whole heck of a lot. You've more than earned a morning off. Call in late and enjoy a leisurely breakfast.",
    "Capricorn":    "Whether you're a novelist or second in command in charge of deciding what text goes with what greeting-card design, you're used to working with words. Ditto if you're a soccer coach or store manager. After all, without words you couldn't verbalize your ideas, and nobody would be able to do what they're supposed to do. Revel in your abilities to make sense. And the people you're talking to will appreciate it, as well.",
    "Aquarius":     "If you started something a while back, it's now well on its way. Whether you've been gardening or raising puppy dogs, or both, you've got results. The daisies are blooming. The litter is growing. There's enough fertilizer to last you through next spring. It's terrific! Not to mention that all your friends always want to hang out at your house -- everybody likes flowers and doggies.",
    "Pisces":       "Today is a day to act! Whatever it is -- an opportunity, a decision, an invitation -- act right away. Don't think too long or too hard, unless it's a really gigantic thing that involves a lot of people other than yourself. Even so, now is the time for doing. Later, it will be time for reviewing. Chances are you'll be happy with what you've done."
}
logos = {
    "Aries":       ("-WW------WW-\n"
                    "W--W----W--W\n"
                    "---W----W---\n"
                    "----W--W----\n"
                    "----W--W----\n"
                    "----W--W----\n"
                    "-----WW-----\n"
                    "-----WW-----\n"
                    "-----WW-----\n"
                    "-----WW-----\n"
                    "-----WW-----\n"
                    "-----WW-----"),
    "Taurus":      ("------------\n"
                    "W----------W\n"
                    "WW--------WW\n"
                    "-WW------WW-\n"
                    "--WW----WW--\n"
                    "---WWWWWW---\n"
                    "-WWW----WWW-\n"
                    "WW--------WW\n"
                    "W----------W\n"
                    "WW--------WW\n"
                    "-WWW----WWW-\n"
                    "---WWWWWW---"),
    "Gemini":      ("WW--------WW\n"
                    "-WWWWWWWWWW-\n"
                    "----W--W----\n"
                    "----W--W----\n"
                    "----W--W----\n"
                    "----W--W----\n"
                    "----W--W----\n"
                    "----W--W----\n"
                    "----W--W----\n"
                    "----W--W----\n"
                    "-WWWWWWWWWW-\n"
                    "WW--------WW"),
    "Cancer":      ("------------\n"
                    "--WWWWWWWW--\n"
                    "-W--W-----W-\n"
                    "-W--W-----W-\n"
                    "--WW-----W--\n"
                    "------------\n"
                    "------------\n"
                    "--W-----WW--\n"
                    "-W-----W--W-\n"
                    "-W-----W--W-\n"
                    "--WWWWWWWW--\n"
                    "------------"),
    "Leo":         ("------------\n"
                    "---WW-------\n"
                    "--W--W------\n"
                    "--W---W-----\n"
                    "-WW---W-----\n"
                    "W--W--W-----\n"
                    "W--W--W---W-\n"
                    "-WW---W--W--\n"
                    "------W-W---\n"
                    "-------W----\n"
                    "------------\n"
                    "------------"),
    "Virgo":       ("W-----------\n"
                    "W-WW--WW----\n"
                    "WW--WW--W---\n"
                    "W---W---W---\n"
                    "W---W---W---\n"
                    "W---W---W-WW\n"
                    "W---W---WW-W\n"
                    "W---W---W--W\n"
                    "--------W--W\n"
                    "------WWWWW-\n"
                    "----WW--W---\n"
                    "--------WW--"),
    "Libra":       ("------------\n"
                    "----WWWW----\n"
                    "---WW--WW---\n"
                    "--WW----WW--\n"
                    "--W------W--\n"
                    "--WW----WW--\n"
                    "---WW--WW---\n"
                    "WWWWW--WWWWW\n"
                    "------------\n"
                    "------------\n"
                    "WWWWWWWWWWWW\n"
                    "------------"),
    "Scorpio":     ("w-----------\n"
                    "W-WW--WW----\n"
                    "WW--WW--W---\n"
                    "W---W---W---\n"
                    "W---W---W---\n"
                    "W---W---W---\n"
                    "W---W---W---\n"
                    "W---W---W---\n"
                    "--------W---\n"
                    "--------W-W-\n"
                    "--------WWWW\n"
                    "----------W-"),
    "Sagittarius": ("-------WWWWW\n"
                    "----------WW\n"
                    "---------W-W\n"
                    "--------W--W\n"
                    "---W---W---W\n"
                    "----W-W-----\n"
                    "-----W------\n"
                    "----W-W-----\n"
                    "---W---W----\n"
                    "--W---------\n"
                    "-W----------\n"
                    "W-----------"),
    "Capricorn":   ("------------\n"
                    "W---W-------\n"
                    "-W-W-W------\n"
                    "-W-W-W------\n"
                    "-W-W--W-----\n"
                    "--W---W-----\n"
                    "------W-WWW-\n"
                    "-------W---W\n"
                    "------W-W--W\n"
                    "---W--W--WW-\n"
                    "----WW------\n"
                    "------------"),
    "Aquarius":    ("------------\n"
                    "--W---W---W-\n"
                    "-W-W-W-W-W-W\n"
                    "W--WW--WW--W\n"
                    "------------\n"
                    "------------\n"
                    "--W---W---W-\n"
                    "-W-W-W-W-W-W\n"
                    "W--WW--WW--W\n"
                    "------------\n"
                    "------------\n"
                    "------------"),
    "Pisces":      ("W----------W\n"
                    "-W--------W-\n"
                    "--W------W--\n"
                    "--W------W--\n"
                    "---W----W---\n"
                    "-WWWWWWWWWW-\n"
                    "---W----W---\n"
                    "--W------W--\n"
                    "--W------W--\n"
                    "-W--------W-\n"
                    "W----------W\n"
                    "------------")
}

class HoroPage(Page):
    def __init__(self, page_num, sign, dates):
        super(HoroPage, self).__init__(page_num)
        self.title = sign
        self.dates = dates
        self.in_index = False

    def generate_content(self):
        self.add_title(self.title,font="size4bold",fg="BLACK",bg="MAGENTA")
        self.print_image(logos[self.title],0,68)
        self.move_cursor(y=5,x=0)
        self.add_text(self.dates,fg="RED")
        self.add_newline()
        self.add_wrapped_text(predictions[self.title])



class HoroIndex(Page):
    def __init__(self, page_num, hls):
        super(HoroIndex, self).__init__(page_num)
        self.title = "Horoscope"
        self.index_num = "107-119"
        self.hls = hls

    def generate_content(self):
        self.add_title("Horoscope")
        for page in self.hls:
            self.move_cursor(x=3)
            self.add_text(page.number,fg="GREEN")
            self.move_cursor(x=7)
            self.add_text(page.title)
            self.move_cursor(x=20)
            self.add_text(page.dates,fg="RED")
            self.add_newline()
pagels = []

pagels.append(HoroPage("108", "Aries", "21 March - 19 April"))
pagels.append(HoroPage("109", "Taurus", "20 April - 20 May"))
pagels.append(HoroPage("110", "Gemini", "21 May - 20 June"))
pagels.append(HoroPage("111", "Cancer", "21 June - 22 July"))
pagels.append(HoroPage("112", "Leo", "23 July - 22 August"))
pagels.append(HoroPage("113", "Virgo", "23 August - 22 September"))
pagels.append(HoroPage("114", "Libra", "23 September - 22 October"))
pagels.append(HoroPage("115", "Scorpio", "23 October - 21 November"))
pagels.append(HoroPage("116", "Sagittarius", "22 November - 21 December"))
pagels.append(HoroPage("117", "Capricorn", "22 December - 19 January"))
pagels.append(HoroPage("118", "Aquarius", "20 January - 18 February"))
pagels.append(HoroPage("119", "Pisces", "19 February - 20 March"))
h00 = HoroIndex("107", pagels)

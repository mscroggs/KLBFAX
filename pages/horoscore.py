from page import Page

predictions = {
    "Aries":        "As Jupiter forms a regular polygon with some other planets, you will look back at past loves, past lives, past jobs, wondering where it all went wrong. Don't be tempted to rekindle old flames, it would be far more prudent for you to make a run for it. I'll be right behind you as soon as I get these damn handcuffs off.",
    "Taurus":       "The elliptical orbit of the outer planets can loom ahead like a long thin corridor. Add in the comets and space dust intermittedly reflecting the sun's light and you have your classic creepy corridor with flickering lights and pools of water on the ground for some reason. This month, you will find yourself wondering which way to turn, getting lost and doubling back on yourself. No matter how lost you are, remember to keep moving forward because they are behind you and if you don't keep moving they will get you.",
    "Gemini":       "Given there is a full moon this month, you would be wise to assume that anything you say in confidence to some people could well be gossip by the end of the hour. Bearing that in mind, tread carefully past open doors that do not lead where you want to go. Also bear in mind that where you want to go could be behind a closed door. Feel free to fling it open but don't pause for too long when you feel the sun on your face. You must keep moving or they will get you.",
    "Cancer":       "It's tempting to think that because things are looking up for you, that they will continue this way. However, the wheel of fortune is always turning and oh wait that's tarot. Ok, the rotation of Mars means that just because you have freedom from oppressive things in your life it doesn't mean that trees aren't armed guards and birds aren't bullets. We have to get over the wall, never mind about the barbed wire. Your lucky colour is blood red this month anyhow.",
    "Leo":          "After a trying few months for you, Mercury is finally in retrograde and that means you can rest easy. Fluffy pillows, a heavy duvet, and your first real bed since you escaped. Even the walls are soft, padded, even and whenever you move there is a pleasant twinkling sound that sounds like starlight, or chains. Why can't I move my hands below my head?",
    "Virgo":        "Due to the influence of Venus in the fourth portal, you will feel more inclined to make impulsive decisions. Try to resist, or if you can't, at least leave some beer for the rest of us.  You are also going to in receipt of money this month. This could be due to Andromeda passing through Jupiter, meaning monetary fortune is on your horizon, or it could be because it's your birthday this month.",
    "Libra":        "Neptune is entering Uranus this month but you don't have to tell everyone about it. Remember, discretion is the better part of valour. Having said that, valour is the worst part of EMF, and who am I to deny everyone your goss? Beware though, the Milky Way is entering its fourth cycle later this month and you will have to decide who is a friend and who is just giving you advice that makes no sense.",
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
    "Sagittarius":  "As Pluto enters its re-alignment with the rest of the solar system, you will find yourself wondering if it's all been worth it. Whilst only you can answer that, remember that the devil makes work for idle thumbs and no matter what Charon is up to, someone is imprisoned in a horoscope-writing factory, chained to a desk and you need to save them.",
    "Capricorn":    "Neptune is all about new beginnings, that's why the start with the same first two letters. Embrace the changes that are happening in your life as I embrace the change in mine with my new job by the way does anyone know what happened to the last writer? She apparently left in a bit of a hurry. Neptune is rising or I'd ask someone else.",
    "Aquarius":     "Jupiter in descent means whatever you are worried about can be safely put to bed. Others may be pressuring you to dwell on the past but focussing on the future means that you will be ready to accept new opportunities when Jupiter why am I handcuffed to the desk finally rises in September.",
    "Pisces":       "Don't worry about Mercury entering the fourth dimension, just focus on yourself. Traditionally, a planet moving into the fourth dimension means disaster in your future but because Venus is in retrograde, a new acquisition means any imminent disaster can be averted. Like me for example, I have acquired a key to the handcuffs."
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

pagels.append(HoroPage("108", "Virgo", "23 August - 22 September"))
pagels.append(HoroPage("109", "Libra", "23 September - 22 October"))
pagels.append(HoroPage("110", "Scorpio", "23 October - 21 November"))
pagels.append(HoroPage("111", "Sagittarius", "22 November - 21 December"))
pagels.append(HoroPage("112", "Capricorn", "22 December - 19 January"))
pagels.append(HoroPage("113", "Aquarius", "20 January - 18 February"))
pagels.append(HoroPage("114", "Pisces", "19 February - 20 March"))
pagels.append(HoroPage("115", "Aries", "21 March - 19 April"))
pagels.append(HoroPage("116", "Taurus", "20 April - 20 May"))
pagels.append(HoroPage("117", "Gemini", "21 May - 20 June"))
pagels.append(HoroPage("118", "Cancer", "21 June - 22 July"))
pagels.append(HoroPage("119", "Leo", "23 July - 22 August"))
h00 = HoroIndex("107", pagels)

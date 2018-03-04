from page import Page


class SunrisePage(Page):
    def __init__(self):
        super(SunrisePage, self).__init__("323")
        self.title = "Sunrise & sunset"
        self.in_index = False
        self.tagline = "Here comes the sun"

    def generate_content(self):
        from astral import Astral
        city_name = 'London'
        a = Astral()
        a.solar_depression = 'civil'
        city = a[city_name]
        sun = city.sun(local=True)
        sunrise = sun['sunrise'].strftime("%H:%M")
        sunset = sun['sunset'].strftime("%H:%M")

        self.add_title("Sunrise/sunset")
        self.add_title(" * "+sunrise, bg="YELLOW",fg="BLACK")
        self.add_title(" } "+sunset, bg="LIGHTRED",fg="BLACK")

sunrise_page = SunrisePage()

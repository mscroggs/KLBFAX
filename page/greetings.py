class GreetingChooser:
    def __init__(self):
        self.greetings = ["Hi","Hello","Bonjour","Bello","Merhaba",
                          "nuqneH","Hola","Salut","Hallo","Hey",
                          "Yo","Dia dhuit","Salve","Ciao","Shwmae",
                          "Booyakasha","Ahoy there"]
        self.morning = ["Good morning","Guten morgen","God morgen"]
        self.evening = ["Guten abend","Good evening"]
        self.twitter = ["\xe4\xbd\xa0\xe5\xa5\xbd"]

    def random(self):
        from random import choice
        return choice(self.greetings + self.get_daytime())

    def random_twitter(self):
        from random import choice
        return choice(self.greetings + self.get_daytime() + self.twitter)

    def get_daytime(self):
        import now
        if now.now().hour < 12:
            return self.morning
        if now.now().hour > 17:
            return self.evening
        return []

greetings = GreetingChooser()

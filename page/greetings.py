class GreetingChooser:
    def __init__(self):
        self.greetings = ["Hi","Hello","Bonjour","Bello","Merhaba",
                          "nuqneH","Hola","Salut","Hallo","Hey",
                          "Yo","Dia dhuit","Salve","Ciao","Shwmae",
                          "Booyakasha","Ahoy there"]
        self.morning = ["Good morning","Guten morgen","God morgen"]
        self.evening = ["Guten abend","Good evening"]

    def random(self):
        import now
        from random import choice
        if now.now().hour < 12:
            return choice(self.greetings + self.morning)
        if now.now().hour > 17:
            return choice(self.greetings + self.evening)
        return choice(self.greetings)

greetings = GreetingChooser()

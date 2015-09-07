from page import Page
import thread_communication
import ceefax
import Keyboard


class PrisonersPage(Page):
    def __init__(self, page_num):
        super(PrisonersPage, self).__init__(page_num)
        self.is_enabled = False
        self.in_index = False
        self.title = "Prisoner's Dilemma Score"
        self.tagline = "Let's play a game! Press 000 to go back!"

    def keyboard_handler(self, input):
        if input == "000":
            thread_communication.should_interrupt = False
            ceefax.loop_manager.current = ceefax.loop_manager.standard
            Keyboard.restore_subscribers()

    def reload(self):
        Page.reload(self)
        Keyboard.save_subscribers()
        Keyboard.clear_subscribers()
        self.keyboard_handler('333')
        Keyboard.subscribe(self.keyboard_handler)

        thread_communication.should_interrupt = True
        ceefax.loop_manager.current = self.loop

    def generate_content(self):
        self.content = "A game will appear here shortly..."

    def loop(self):
        pass

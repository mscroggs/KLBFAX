from page import Page
#import ceefax
import Keyboard
import ThreadSignaller


class PrisonersPage(Page):
    def __init__(self, page_num):
        super(PrisonersPage, self).__init__(page_num)
        self.is_enabled = False
        self.in_index = False
        self.title = "Prisoner's Dilemma Score"
        self.tagline = "Let's play a game! Press 000 to go back!"

    def keyboard_handler(self, input):
        if input == "000":
            ThreadSignaller.queue.put(ThreadSignaller.InterruptWait)
            Keyboard.restore_subscribers()
            ceefax.loop_manager.current = ceefax.loop_manager.standard

    def reload(self):
        Page.reload(self)
        Keyboard.save_subscribers()
        Keyboard.clear_subscribers()
        Keyboard.subscribe(self.keyboard_handler)

        ceefax.loop_manager.current = self.loop

    def generate_content(self):
        self.content = "A game will appear here shortly..."

    def loop(self):
        ceefax.sleep(10)

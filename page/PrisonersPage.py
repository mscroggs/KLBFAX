from page import Page
import ceefax
import Keyboard
import ThreadSignaller
import pd.state
import os.path


class PrisonersPage(Page):
    def __init__(self, page_num):
        super(PrisonersPage, self).__init__(page_num)
        self.is_enabled = False
        self.in_index = False
        self.title = "Prisoner's Dilemma Score"
        self.tagline = "Let's play a game! Press 000 to go back!"
        self.state = pd.StateHolder(os.path.join('pd', 'game0.db'))

    def keyboard_handler(self, input):
        if input == "000":
            Keyboard.restore_subscribers()
            ceefax.loop_manager.current = ceefax.loop_manager.standard

        if input in [str(x[1]) for x in self.state.allPlayers()]:
            print "Hello " + self.state.getPlayerName(input)

    def reload(self):
        Page.reload(self)
        ThreadSignaller.queue.put(ThreadSignaller.InterruptStandardLoop)
        Keyboard.save_subscribers()
        Keyboard.clear_subscribers()
        Keyboard.subscribe(self.keyboard_handler)

        ceefax.loop_manager.current = self.loop

    def _show_player_selection(self):
        content = "Select your name: \n\n"
        for playerName, id in self.state.allPlayers():
            content += "%-20s %s\n" % (playerName, str(id))

        return content

    def generate_content(self):
        self.content = self._show_player_selection()

    def loop(self):
        pass

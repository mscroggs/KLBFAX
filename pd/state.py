import sqlite3


moves = {'cooperate': "cooperate", 'defect': "defect"}


class StateHolder(object):
    def __init__(self, dbname):
        self.dbname = dbname
        self.connection = sqlite3.connect(dbname)
        self._players = None

    def playMove(self, player1, player2, move):
        pass

    def isPlayed(self, player1, player2, move):
        pass

    def allPlayers(self):
        if not self._players:
            self._players = self.connection.execute('''SELECT * FROM
                                                    players''').fetchall()

        return self._players

    def getPlayerName(self, id):
        for playerName, pid in self._players:
            if str(pid) == str(id):
                return playerName

    def interrupt(self):
        self.connection.close()

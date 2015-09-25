import sqlite3


moves = {'cooperate': "cooperate", 'defect': "defect"}


class StateHolder(object):
    def __init__(self, dbname):
        self.dbname = dbname
        self.connection = sqlite3.connect(dbname)

    def playMove(self, player1, player2, move):
        pass

    def isPlayed(self, player1, player2, move):
        pass

    def allPlayers(self):
        return self.connection.execute('''SELECT * FROM players''').fetchall()

    def interrupt(self):
        self.connection.close()

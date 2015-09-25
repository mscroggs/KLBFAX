#!/usr/bin/env python2

import sqlite3


names = ['Scroggs', 'Tom', 'Adam', 'Jigsaw']

conn = sqlite3.connect('game0.db')

c = conn.cursor()

try:
    c.execute('''DROP TABLE players''')
except sqlite3.OperationalError:
    pass

c.execute('''CREATE TABLE players
             (name text, id INTEGER PRIMARY KEY AUTOINCREMENT)''')

for name in names:
    c.execute("INSERT INTO players(name) VALUES ('" + name + "')")

conn.commit()

conn.close()

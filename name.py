from os import getenv as _getenv

if _getenv("SLAVE"):
    NAME = "28JHFAX"
else:
    NAME = "KLBFAX"

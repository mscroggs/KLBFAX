from os import getenv as _getenv

if _getenv("SLAVE") and not _getenv("EXPORT_ME"):
    NAME = "28JHFAX"
else:
    NAME = "KLBFAX"

from os import getenv as _getenv

if _getenv("SLAVE") and not _getenv("EXPORT_ME"):
    NAME = "28JHFAX"
elif _getenv("EMF"):
    NAME = "EMFFAX"
else:
    NAME = "KLBFAX"

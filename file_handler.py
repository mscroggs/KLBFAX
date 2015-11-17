from os.path import join as _join
from os.path import expanduser as _expanduser
from os.path import dirname as _dirname
from os.path import realpath as _realpath
from os import getenv as _getenv
import json as _json

def open_local(f_name, method="r"):
    try:
        return open(_join(_expanduser("~"), ".klb/" + f_name),method)
    except:
        folder = _dirname(_realpath(__file__))
        return open(_join(folder, "blank_file"))

def f_readlines(f_name):
    ret = []
    try:
        with open(_join(_expanduser("~"), ".klb/" + f_name)) as f:
            ret += f.readlines()
    except:
        pass
    if _getenv("SLAVE"):
        try:
            with open(_join(_expanduser("~"), ".slave/" + f_name)) as f:
                ret += f.readlines()
        except:
            pass
    for i in range(len(ret)):
        ret[i] = ret[i].strip("\n")
    return ret

def f_read(f_name):
    ret = ""
    try:
        with open(_join(_expanduser("~"), ".klb/" + f_name)) as f:
            ret += f.read()
    except:
        pass
    if _getenv("SLAVE"):
        try:
            with open(_join(_expanduser("~"), ".slave/" + f_name)) as f:
                ret += f.read()
        except:
            pass
    return ret

def f_read_json(f_name):
    ret = {}
    try:
        with open(_join(_expanduser("~"), ".klb/" + f_name)) as f:
            temp = _json.load(f)
            for a in temp:
                ret[a] = temp[a]
    except:
        pass
    if _getenv("SLAVE"):
        try:
            with open(_join(_expanduser("~"), ".slave/" + f_name)) as f:
                temp = _json.load(f)
                for a in temp:
                    ret[a] = temp[a]
        except:
            pass
    return ret

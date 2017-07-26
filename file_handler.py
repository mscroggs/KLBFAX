from os.path import join as _join
from os.path import expanduser as _expanduser
from os.path import dirname as _dirname
from os.path import realpath as _realpath
from os.path import isdir as _isdir
from os import mkdir as _mkdir
from os import getenv as _getenv
import json as _json
import pickle
import config

if _getenv("SLAVE"):
    default_path = _join(_expanduser("~"), ".slave/")
else:
    default_path = _join(_expanduser("~"), ".klb/")

def test_dir(directory):
    if not _isdir(directory):
        try:
            _mkdir(directory)
        except:
            pass

test_dir(default_path)

def open_local(f_name, method="r"):
    try:
        return open(_join(_expanduser("~"), ".klb/" + f_name),method)
    except:
        folder = _dirname(_realpath(__file__))
        return open(_join(folder, "blank_file"))

def open_html(f_name, method="r"):
    html = _join(_dirname(_realpath(__file__)), "html")
    test_dir(html)
    return open(_join(html, f_name), method)

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

def f_read_pickle(f_name, path=None):
    if path == None:
        path = default_path
    try:
        with open(_join(path, f_name), "r") as f:
            return pickle.load(f)
    except:
        pass

def f_write_pickle(f_name, var, path=None):
    if path == None:
        path = default_path
    try:
        with open(_join(path, f_name), "w") as f:
            pickle.dump(var, f)
    except:
        pass

def load_file(f_name):
    with open(_join(_join(config.current_dir,'files'),f_name)) as f:
        return f.read()

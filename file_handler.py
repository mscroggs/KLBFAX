from os.path import join as _join
from os.path import expanduser as _expanduser
from os.path import dirname as _dirname
from os.path import realpath as _realpath
from os.path import isdir as _isdir
from os import mkdir as _mkdir
from os import getenv as _getenv
import json as _json

default_path = _join(_expanduser("~"), ".klb/")
ceefax_path = _dirname(_realpath(__file__))

def test_dir(directory):
    if not _isdir(directory):
        try:
            _mkdir(directory)
        except:
            pass

test_dir(default_path)

def open_local(f_name, method="r"):
    try:
        return open(_join(default_path, f_name),method)
    except:
        return open(_join(current_path, "blank_file"))

def open_html(f_name, method="r"):
    html = _join(ceefax_path, "html")
    test_dir(html)
    return open(_join(html, f_name), method)

def f_readlines(f_name):
    with open_local(f_name) as f:
        return [r.strip("\n") for r in f.readlines()]

def f_read(f_name):
    with open_local(f_name) as f:
        return f.read()

def f_read_json(f_name):
    try:
        with open_local(f_name) as f:
            return _json.load(f)
    except:
        return {}

def f_write_json(data, f_name):
    with open_local(f_name,"w") as f:
        return _json.dump(data, f)

def load_file(f_name):
    with open(_join(ceefax_path,'files',f_name)) as f:
        return f.read()

from os.path import join as _join
import json as _json
from config import test_dir, default_path, ceefax_path

class DummyFile():
    def read():
        return ""
    def readlines():
        return []

def open_local(f_name, method="r"):
    try:
        return open(_join(default_path, f_name),method)
    except:
        return DummyFile()

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

def load_csv_file(f_name):
    import csv
    with open(_join(ceefax_path,'files',f_name)) as f:
        reader = csv.reader(f, delimiter=',')
        return list(reader)

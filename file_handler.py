from os.path import join, expanduser, dirname, realpath

def open_local(f_name, method="r"):
    try:
        return open(join(expanduser("~"), ".klb/" + f_name),method)
    except:
        folder = dirname(realpath(__file__))
        if ".json" in f_name:
            return open(join(folder, "empty_files/normal.json"))
        return open(join(folder, "empty_files/normal"))

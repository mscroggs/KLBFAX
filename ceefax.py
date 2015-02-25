#width:79
#height: 30

from os import listdir
from random import choice
from os.path import isfile, join
from global_vars import PATH 
root = join(PATH,"pages")
onlyfiles = [ f for f in listdir(root) if isfile(join(root,f)) and "_" not in f and "pyc" not in f]

load_me=choice(onlyfiles).split(".")[0]

module = getattr(__import__("pages",fromlist=[load_me]), load_me)
reload(module)

#page = getattr(__import__("pages."+load_me, fromlist=["page"]), "page")
page = module.page

try:
    #tag = getattr(__import__("pages."+load_me, fromlist=["tag"]), "tag")
    tag = module.tag
except:
    tag = "KLBFAX: The world at your fingertips"


import json
from os.path import expanduser,join

def update_status(status=None):
    if status is not None:
        with open(join(expanduser('~'),'.klb/tweet_me'),'a+') as f:
            f.write("\n"+status)

def add_points(house,number):
    try:
        with open(join(expanduser('~'),'.klb/points'),'r') as f:
            data = json.load(f)
    except:
        data = {}
    if house in data:
        data[house]+=number
    else:
        data[house]=number
    with open(join(expanduser('~'),'.klb/points'),'w+') as f:
        json.dump(data,f)
    if number==1:
        update_status(status=str(number)+" point to "+house+"!")
    else:
        update_status(status=str(number)+" points to "+house+"!")

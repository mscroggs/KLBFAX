import json

def update_status(status=None):
    if status is not None:
        with open("/home/pi/.klb/tweet_me","a") as f:
            f.write("\n"+status)

def add_points(house,number):
    with open('/home/pi/.klb/points') as f:
        data = json.load(f)
    if house in data:
        data[house]+=number
    else:
        data[house]=number
    with open('/home/pi/.klb/points','w') as f:
        json.dump(data,f)
    update_status(status=str(number)+" points to "+house+"!")

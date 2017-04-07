import json
import config
from os.path import expanduser, join
import os

def update_status(status=None):
    if config.NAME in ["KLBFAX","602FAX"]:
        if status is not None:
            with open(join(expanduser('~'), '.klb/tweet_me'), 'a+') as f:
                f.write("\n"+status)

def add_one_random(printing=False):
    from random import choice
    house = choice(["Gryffindor","Hufflepuff","Slytherin","Ravenclaw","Durmstrang","Squib","Postdoc"])
    if printing:
        print("1 point to "+house)
    add_points(house,1)
    return house

def add_points(house, number, deets=""):
    if config.NAME in ["KLBFAX","602FAX"]:
        if deets != "":
            if deets[-1] != " ":
                if deets[-2] not in [".","!",":","?"]:
                    deets += "."
                deets += " "
            elif deets[-2] not in [".","!",":","?"]:
                deets = deets[:-2] + ". "
            
        while u"\u0000" in house:
            house = house.strip(u"\u0000")
        if config.NAME == "KLBFAX":
            try:
                with open(join(expanduser('~'), '.klb/points'), 'r') as f:
                    data = json.load(f)
            except:
                data = {}
            if house in data:
                data[house] += number
            else:
                data[house] = number
            with open(join(expanduser('~'), '.klb/points'), 'w+') as f:
                json.dump(data, f)
            if number == 1:
                update_status(status=deets + str(number)+" point to "+house+"!")
            else:
                update_status(status=deets + str(number)+" points to "+house+"!")
        else:
            with open(join(expanduser('~'), '.points/602points'), 'a') as f:
                if number == 1:
                    f.write(house+","+str(number)+","+deets + str(number)+" point to "+house+"!\n")
                else:
                    f.write(house+","+str(number)+","+deets + str(number)+" points to "+house+"!\n")
            

def should_add_morning_points(time, house, lines, oldname):
    if config.NAME in ["KLBFAX","602FAX"]:
        if house is not None and "used" not in lines:
            if time in ["08", "09"]:
                return True
        return False


def num_of_morning_points(time):
    from datetime import datetime
    i=1
    if datetime.today().weekday() in [5,6]:
        i=-1
    if time == "08":
        return 20*i
    elif time == "09":
        return 10*i


def add_morning_points(time, house, oldname, deets):
    if config.NAME in ["KLBFAX","602FAX"]:
        with open("/home/pi/cards/" + oldname, "a") as f:
            f.write("\nused")
            points_added = num_of_morning_points(time)
            add_points(house, points_added, deets)
        return points_added
    return 0


def read_name_file(namefile_path):
    with open(namefile_path) as f:
        lines = f.readlines()

    return lines


def get_name_house(input):
    lines = read_name_file(input)

    name = lines[0].strip("\n")
    try:
        house = lines[1].strip("\n")
    except:
        house = None
    try:
        twitter = lines[2].strip("\n")
        if twitter == "used":
            twitter = None
    except:
        twitter = None

    return (name, house, twitter)


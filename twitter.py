def update_status(status=None):
    if not isNone(status):
        with open("/home/pi/.klb/tweet_me","a") as f:
            f.write(status)

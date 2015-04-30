def update_status(status=None):
    if status is not None:
        with open("/home/pi/.klb/tweet_me","a") as f:
            f.write("\n"+status)

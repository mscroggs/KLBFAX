import config

def reboot():
    from os import system
    system("sudo shutdown -r now")

def git_pull():
    from os import system
    print("Pulling newest version.")
    try:
        system("cd "+config.ceefax_path+";git pull")
        system("cd "+config.ceefax_path+";sudo pip install -r requirements.txt")
        restart_ceefax()
    except:
        pass

def restart_ceefax():
    from os import path
    with open(path.join(config.default_path,"FAX_status"),"w") as f:
        f.write("1")
    kill_ceefax()

def kill_ceefax():
    from os import system
    system("sudo kill $(pgrep -f run.py)")

if __name__ == "__main__":
    print("Updating")
    git_pull()

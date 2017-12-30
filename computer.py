import autoconfig

def reboot():
    from os import system
    system("sudo shutdown -r now")

def git_pull():
    from os import system
    print("Pulling newest version.")
    try:
        system("cd "+autoconfig.current_dir+";git pull")
        system("cd "+autoconfig.current_dir+";sudo pip install -r requirements.txt")
        restart_ceefax()
    except:
        pass

def restart_ceefax():
    from os import path
    with open(path.join(autoconfig.config_dir,"KLBFAX_status"),"w") as f:
        f.write("1")
    kill_ceefax()

def kill_ceefax():
    from os import system
    system("sudo kill $(pgrep -f run.py)")

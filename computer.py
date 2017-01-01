def reboot():
    from os import system
    system("sudo shutdown -r now")

def git_pull():
    from os import system
    from name import NAME
    print("Pulling newest version.")
    try:
        system("cd /home/pi/ceefax;git pull")
        if NAME == "KLBFAX":
            with open("/home/pi/ceefax/temp","w") as f:
                f.write("YES")
        elif NAME == "28JHFAX":
            system("KLBur")
        try:
            with open("/home/pi/ceefax/requirements-satisfied.txt") as f:
                satis = [s.strip("\n") for s in f.readlines()]
        except:
            satis = []
        with open("/home/pi/ceefax/requirements.txt") as f:
            for line in f.readlines():
                line = line.strip("\n")
                if line not in satis:
                    print("installing "+line)
                    with open("/home/pi/ceefax/requirements-satisfied.txt","a+") as g:
                        g.write(line+"\n")
                    system("sudo pip install "+line)
                    print("installed "+line)
        from ceefax import Ceefax
        Ceefax().kill()
    except:
        pass

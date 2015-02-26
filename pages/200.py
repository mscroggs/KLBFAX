import gmail
from os.path import join,expanduser

details = []
with open(join(expanduser("~"),".klb/gmail")) as f:
    for line in f.readlines():
        details.append(line.strip("\n"))

g = gmail.login(details[0],details[1])


unread = g.inbox().mail(unread=True)

with open(join(expanduser("~"),".klb/emails")) as f:
    letters = f.read()

for mail in unread:
    mail.fetch()
    lines = "".join(mail.body.split("\r")).split("\n")
    if lines[0] == "EVENT":
      try:
        with open('/var/www/klb/events','a') as f:
            for line in lines:
                if line!="EVENT":
                    f.write(line+"""
""")
        mail.read()
      except:
        pass
    else:
        print mail.body
        letters=mail.body+"""
from """+mail.fr+"""

"""+letters
        mail.read()

letters = letters.split("\n")
if len(letters)>100:
    letters = letters[:100]
letters = """
""".join(letters)

with open(join(expanduser("~"),".klb/emails"),"w") as f:
    f.write(letters)
        
page = """LETTERS
"""+letters
tag = "Email klbscroggsbot@gmail.com and your letter will appear here"
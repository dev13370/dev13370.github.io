import requests
import sys

A = '\033[1;10m'
B = '\033[1;30m'
C ='\033[1;36m'
D =('='*40)

print(f"""{A}{D}
<>---<>---<>---<>---<>---<>---<>---<>---<>
[*] Extracting tracks within the site [*]  
<>---<>---<>---<>---<>---<>---<>---<>---<>        
      >> Naplon ◕_◕ <<
 _   _             _             
| \ | |           | |            
|  \| | __ _ _ __ | | ___  _ __  
| . ` |/ _` | '_ \| |/ _ \| '_ \ 
| |\  | (_| | |_) | | (_) | | | |{C}
|_| \_|\__,_| .__/|_|\___/|_| |_|
            | | instagram: 3h6h                 
            |_| Telegram: naplon0
                 
<>---<>---<>---<>---<>---<>---<>---<> 
//Link must contain http or https\\
<>---<>---<>---<>---<>---<>---<>---<>
{D}""")

host = str(input("Enter the website link: "))
file = input("Enter tracks name file: ")
fi = open(f'{file}', "r")
re = fi.read()
fire = re.splitlines()

try:

    for word in fire:
        url = host + "/" + word
        req = requests.get(url)

        if req.status_code == 200:
            print("[*]>>Found : " + url)

except:
    print("Exit..")
    sys.exit()
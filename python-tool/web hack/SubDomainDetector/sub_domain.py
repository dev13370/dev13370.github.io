import requests
import sys

print('''
<>---<>---<>---<>---<>---<>---<>---<>---<>
       [*] Subdomain Detector [*]  
<>---<>---<>---<>---<>---<>---<>---<>---<>        
      >> Naplon ◕_◕ << 
 _   _             _             
| \ | |           | |            
|  \| | __ _ _ __ | | ___  _ __  
| . ` |/ _` | '_ \| |/ _ \| '_ \ 
| |\  | (_| | |_) | | (_) | | | |
|_| \_|\__,_| .__/|_|\___/|_| |_|
            | | instagram: 3h6h                 
            |_| Telegram: naplon0
                 
<>---<>---<>---<>---<>---<>---<>---<>--<>--<>
The link should be this way >>example.com<<
<>---<>---<>---<>---<>---<>---<>---<>--<>--<>
''')

host = str(input("Enter the host name: "))
file = input("Enter sub domain list file: ")
f = open(f"{file}", "r")
r = f.read()
sublist = r.splitlines()
for sub in sublist:
    domain = "http://" + sub + "." + host
    
    try:
        r = requests.get(domain, "http.parser")
        if r.status_code == 200:
            print("[*]You have discovered a subdomain : " + domain)

            fil = open("subsave.txt", "a")
            fil.write('\n'+domain)
            fil.close()
    except requests.ConnectionError:
        pass
    except KeyboardInterrupt:
        print("Exit..")
        sys.exit()





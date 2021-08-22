import sys
import threading
import random
import os
import requests

A = '\033[0;32m'
B = '\033[1;91m'

text = "wqertyuiopasdfghjklzxcvmnb"

try:
    nap1 = int(input("How many characters are in an email ?: "))
except:
    print('=' * 40)
    print("Please choose a number, not text !!")
    exit(0)

os.system("clear")

NapHed = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Connection": "close",
    "Host": "odc.officeapps.live.com",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
    "uaid": "d06e1498e7ed4def9078bd46883f187b",
    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
}

Na = 0
Nb = 0 

def nap():
    global Na
    global Nb

    while True:
        naprun = str("".join(random.choice(text)for n in range(nap1)))
        url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress="+naprun+'@hotmail.com'+ "&_=1604288577990"
        data = ''
        req = requests.get(url, data=data, headers=NapHed)

        if 'MSAccount' in req.text:
            Na+=1
            print(f"""\rNot Available: {B}{Na}{A} :Available: {A}{Nb}{A};{naprun}@hotmail.com""", end="")
            with open("Not_Available.txt ", "a")as n:
                n.write(naprun+'@hotmail.com'+ '\n')
        
        else:
            Nb+=1
            print(f"""\rNot Available: {B}{Na}{A} :Available:{A}{Nb}{A} ;{naprun}@hotmail.com""", end="")
            with open("Available.txt ", "a")as n:
                n.write(naprun+'@hotmail.com'+ '\n')

thread = []
for n in range(100):
    thread1 = threading.Thread(target=nap)
    thread1.start()      
    thread.append(thread1) 
for thread2 in thread:
    thread2.join



from requests import get
import sys as n
import time as mm

def sl(k):
	for c in k + "\n":
		n.stdout.write(c)
		n.stdout.flush()
		mm.sleep(0.4 / 150)
print("\t       [•]Text decoration🤩[•] ")

sl(""" 
		 _   _             _             
		| \ | |           | |            
		|  \| | __ _ _ __ | | ___  _ __  
		| . ` |/ _` | '_ \| |/ _ \| '_ \ 
		| |\  | (_| | |_) | | (_) | | | |
		|_| \_|\__,_| .__/|_|\___/|_| |_|
		            | |                  
		            |_| 
	--------------------------------------
	|       -> By >> Naplon ◕_◕          |
	|       -> Instagram: 3h6h           |
	|       -> Telegram: naplon0         | 
	--------------------------------------    
""")
print('من الافضل ان العنوان لا يكون طويلاً')
print('>>Enter title for tracery<<')
def title():
 	ti = input('[*] ادخل العنوان للزخرفه: ')
 	print('=' * 40)
 	
 	url_title = get('http://artii.herokuapp.com/make?text={}'.format(ti)).text
 	print(url_title)
 	print('=' * 40)
title()


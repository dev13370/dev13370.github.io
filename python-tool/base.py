import base64
import pyperclip
from string import ascii_lowercase
import sys
import hashlib
import os

print(""" 
------------------------------------------
The place for encoding and decoding only. 
				🔒👾👾🔓
------------------------------------------
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
	|       -> SnapChat: tv-of           |
	|       -> Instagram: 3h6h           |
	|       -> Twitter : _naplon         |
	|       -> Telegram: naplon0         | 
	-------------------------------------- 
""")
print("""
1)Encrypt base64
2)Decoding base64
3)Caesar cipher
4)Decoding the caesar
""")
user = input('>> ')
print('=' * 40)
if user == '1':
	print('=' * 40)
	us = input("🔒Enter the text to encode it: ")
	u = us.encode('utf-8')
	encode = base64.b64encode(u)
	us1 = encode.decode('utf-8')
	print("✅Your encryption is: ",us1)


elif user == '2':
	print("=" * 40)
	us = input("🔓Enter the text to decode: ")
	u = us.encode('utf-8')
	decode = base64.b64decode(u)
	us1 = decode.decode('utf-8')
	print("✅It has been decrypted: ",us1)


if user == '3':
	us = list(input('Enter anything to encrypt: '))
	key = int(input('key: '))
	def Encrypt(txt, key):
		cilist = []
		for i in txt:
			p = ord(i)
			lit = chr(p + key)
			cilist.append(lit)
		n = ''.join(cilist)
		print(n)
Encrypt(us,key)


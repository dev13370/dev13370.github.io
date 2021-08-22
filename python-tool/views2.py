import time 
from selenium import webdriver

dr = int(input("[*]Enter the number of views: "))

url = input("[*]Enter Url: ")

time_ref = int(input("After how much you want the page to occur !:"))
drivers = []

for n in range(dr):
    drivers.append(webdriver.Chrome(executable_path="/Users/naplo/Desktop/chromedriver"))
    drivers[n].get(url)

    while True:
        drivers[n].refresh()
        time.sleep(time_ref)

        for n in range(dr):
           drivers[n].refresh()




#https://youtu.be/WeZsM1Rm06c
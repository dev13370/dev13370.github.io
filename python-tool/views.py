from selenium import webdriver
from time import sleep

driver1 = webdriver.Chrome(executable_path="/Users/naplo/Desktop/chromedriver")
driver2 = webdriver.Chrome(executable_path="/Users/naplo/Desktop/chromedriver")
driver3 = webdriver.Chrome(executable_path="/Users/naplo/Desktop/chromedriver")

driver1.get("https://www.youtube.com/watch?v=PKxVZFk4Sy4")
driver2.get("https://www.youtube.com/watch?v=G2hyAzOZHUE&t=27s")
driver3.get("https://www.youtube.com/watch?v=swKxOjJVAkM")

while True:
    sleep(60)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
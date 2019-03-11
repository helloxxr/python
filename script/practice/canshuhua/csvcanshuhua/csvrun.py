import csv
from csvcanshuhua.csvparameterizationlogin import *
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://localhost")
driver.implicitly_wait(10)
data=csv.reader(open('login.csv','r'))
for user in data:
    print(user[0])
    print(user[1])
    username=user[0]
    password=user[1]
    Login().user_login(driver, username, password)
    sleep(3)
    Login().user_logout(driver)
    sleep(6)
driver.quit()


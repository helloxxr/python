from xml.dom import minidom
from xmlcanshuhua.a import *
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://localhost")
driver.implicitly_wait(10)
dom=minidom.parse('login.xml')
root=dom.documentElement
logins=root.getElementsByTagName('login')
'''取第一个值时'''
username=logins[0].getAttribute("username")
print(username)
password=logins[0].getAttribute("password")
print(password)
Login().user_login(driver, username, password)
sleep(3)
Login().user_logout(driver)
sleep(6)
driver.quit()
'''取第二个值时'''
driver = webdriver.Firefox()
driver.get("http://localhost")
driver.implicitly_wait(10)
dom=minidom.parse('login.xml')
root=dom.documentElement
logins=root.getElementsByTagName('login')
username=logins[1].getAttribute("username")
print(username)
password=logins[1].getAttribute("password")
print(password)
Login().user_login(driver, username, password)
sleep(3)
Login().user_logout(driver)
sleep(6)
driver.quit()




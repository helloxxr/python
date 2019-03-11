#coding:utf-8
from txt01.parameterizationlogin import *
from selenium import webdriver
from time import sleep
import unittest
'''将文本格式参数化直接调用为参数化数据'''
driver = webdriver.Firefox()
driver.get("http://localhost")
driver.implicitly_wait(10)
f = open('F:\python\script\practice\canshuhua\login.txt', 'r')
lines = f.readlines()
f.close()
for line in lines:
    # line = line.strip('\n')
    username = line.split(',')[0]
    password = line.split(',')[1]
    print(username, password)
    Login().user_login(driver, username, password)
    sleep(3)
    Login().user_logout(driver)
    sleep(6)
driver.quit()
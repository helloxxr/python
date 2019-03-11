#coding:utf-8
from txt.canshuhualoginlogout import *
from time import sleep
from txt.txtzhuanweizidian import *
'''将文本格式转换位字典的形式'''
# f=open('login.txt','r')
info=zidian()
# print(info)
driver = webdriver.Firefox()
driver.get("http://localhost")
driver.implicitly_wait(10)
sleep(3)
for k,v in info.items():
    print(k)
    print(v)
    Login().user_login(driver,k,v)
    sleep(3)
    Login().user_logout(driver)
    sleep(6)

driver.quit()








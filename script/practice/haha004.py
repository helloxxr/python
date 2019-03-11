from selenium import webdriver
from time import sleep
'''上传文件'''
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")

driver.find_element_by_css_selector(".soutu-btn").click()
sleep(2)
driver.find_element_by_css_selector(".upload-pic").send_keys(r"C:\Users\Administrator\Desktop\QQ图片20190111134444.png")

sleep(6)
driver.quit()

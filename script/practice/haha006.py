from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
cookie=driver.get_cookies()
print(cookie)
driver.get_screenshot_as_file(r"F:\python\script\baidu.jpeg")
driver.get("http://www.51zxw.net")
driver.get_screenshot_as_file(r"F:\python\script\51zxw.png")

sleep(6)
# driver.quit()
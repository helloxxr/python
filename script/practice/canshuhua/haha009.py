from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://localhost")
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("51zxw")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_class_name("inputSub").submit()
sleep(6)
driver.find_element_by_partial_link_text("退出").click()
driver.switch_to_alert().accept()
sleep(6)
driver.quit()

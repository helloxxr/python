from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net/list.aspx?cid=615")

selenium_index=driver.current_window_handle

driver.find_element_by_partial_link_text("2-1").click()
sleep(3)
driver.switch_to.window(selenium_index)
driver.find_element_by_partial_link_text("3-1").click()
sleep(5)
driver.switch_to.window(selenium_index)
sleep(2)
driver.quit()
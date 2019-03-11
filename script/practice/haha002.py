from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.alert import Alert
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
element=driver.find_element_by_link_text('设置')
# driver.find_element_by_link_text('设置').click()
'''引入鼠标事件，模拟鼠标移动至“设置”按钮处'''
ActionChains(driver).move_to_element(element).perform()
sleep(2)
driver.find_element_by_link_text('搜索设置').click()
sleep(3)

driver.find_element_by_link_text('保存设置').click()
# driver.find_element_by_link_text('恢复默认').click()
sleep(3)

#处理警告窗口
driver.switch_to_alert().accept()
sleep(2)

driver.quit()
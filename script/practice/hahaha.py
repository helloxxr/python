from selenium import webdriver
from time import sleep
'''联系元素定位及窗口切换的操作'''
driver=webdriver.Firefox()
driver.get("https://baidu.com/")
# driver.get("http://www.51zxw.net/")
sleep(3)
# driver.maximize_window()
# sleep(3)
# driver.set_window_size(500,600)
# sleep(2)
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").submit()
# driver.find_element_by_partial_link_text("登录").click()
'''通过css_selector的id进行定位'''
driver.find_element_by_css_selector("#kw").clear()
driver.find_element_by_css_selector("#kw").send_keys("自学网1")
sleep(2)

'''通过css_selector的class进行定位'''
driver.find_element_by_css_selector(".s_ipt").clear()
driver.find_element_by_css_selector(".s_ipt").send_keys("自学网2")
sleep(2)
'''通过css_selector的属性进行定位'''
driver.find_element_by_css_selector("[autocomplete='off']").clear()
driver.find_element_by_css_selector("[autocomplete='off']").send_keys("自学网3")
sleep(3)
driver.find_element_by_css_selector("[id=kw]").clear()
driver.find_element_by_css_selector("[id=kw]").send_keys("自学网4")

sleep(2)
# driver.find_element_by_css_selector("#kw").send_keys("selenium")
sleep(2)
# driver.find_element_by_css_selector("#su").submit()
driver.find_element_by_css_selector('[type="submit"]').submit()
sleep(3)
# driver.refresh()
# sleep(2)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
driver.quit()






from selenium import webdriver
from time import sleep
'''数据参数化'''
search_text={'python','selenium','软件测试'}

for text in search_text:
    print("百度搜索%s开始."%text)
    driver=webdriver.Firefox()
    driver.get("https://www.baidu.com")
    sleep(2)
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys(text)
    sleep(3)
    driver.find_element_by_id("su").click()
    sleep(5)
    driver.quit()
    sleep(2)
    print("百度所搜索%s完毕."%text)
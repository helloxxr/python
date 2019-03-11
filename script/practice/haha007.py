from selenium import  webdriver
from time import sleep
'''基于cookie绕过验证码自动登录'''
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.add_cookie({'name':'BAIDUID','value':'08AE18660FC10586967ED5CAFD03B7DA:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'E5jZ2xjcHRhV0FrVWxtV1dMeFN4SXh2a0NWaE4zb1dOd3p4YUZHTUNoWFI4MkJjQUFBQUFBJCQAAAAAAAAAAAEAAACSF-RfcmVkX3N1bm55MjAxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANFmOVzRZjlce'})
# driver.get("https://www.12306.cn/index/")
# driver.add_cookie({'name':'JSESSIONID','value':'B54EB03632BFBBD111063BC0DF4FA9E0'})
# driver.add_cookie({'name':'RAIL_DEVICEID','value':'qRThbIaVbdHk970g-Wplwj1WS9Spfy_NoH9b5C8srP5O3y8BxrdrFPDVy0qYblO6x2is9uhRd8fvg7bx6Xt7zuXAdlRhbrh-M5xsYudeYIraNCh6BhFosvE1baRV5Ftkx8Z0uH6lJi4FuK8yAoPnChpuAub1fIMX'})



sleep(6)
driver.refresh()
driver.quit()
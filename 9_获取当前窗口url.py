from selenium import webdriver

dr=webdriver.Chrome()
dr.implicitly_wait(10)
dr.maximize_window()
url='https://www.baidu.com'

dr.get(url)
urlb=dr.current_url
print(urlb)
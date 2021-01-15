from selenium import webdriver
dr=webdriver.Chrome()

url1='http://www.baidu.com'
print('打开网站 %s'%(url1))
dr.get(url1)
url2='http://news.baidu.com'
print('打开网站 %s'%(url2))
dr.get(url2)
print('返回到 %s'%(url1))
dr.back()
print('前进到 %s'%(url2))
dr.forward()
str='刷新%s'%(dr.current_url)
print(str[0:-1])
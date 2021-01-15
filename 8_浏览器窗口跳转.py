from selenium import webdriver
import time

dr=webdriver.Chrome()
url='https://www.baidu.com'
dr.get(url)

# 获取当前句柄
search_handle=dr.window_handles

dr.find_element_by_link_text('登录').click()
time.sleep(2)
dr.find_element_by_link_text('立即注册').click()

# 获取所有句柄
all_handles=dr.window_handles
print(all_handles)
time.sleep(3)

# 遍历句柄并跳转到指定句柄窗口
for handle in all_handles:
    if handle != search_handle:
        dr.switch_to.window(handle)
        print(dr.title)
        dr.close()
# 跳转到指定句柄
dr.switch_to.window(search_handle)
print(dr.title)

#不指定句柄则操作的还是第一个打开的窗口 所以想操作第二个窗口时要利用句柄跳转到第二个窗口
from selenium import webdriver
dr=webdriver.Chrome()

url='http://127.0.0.1/iWebShop/index.php?controller=simple&action=login'
dr.get(url)
dr.maximize_window()
dr.set_window_size(600,600)
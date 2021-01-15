from selenium import webdriver
dr=webdriver.Chrome()

url='http://127.0.0.1/iWebShop/index.php?controller=simple&action=login'
dr.get(url)
dr.find_element_by_xpath('/html/body/div[3]/section/section/form/dl[1]/dd/input').clear()

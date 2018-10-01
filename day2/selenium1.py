__author__ = 'computer'
from selenium import  webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.find_element_by_xpath('//input[@id="kw"]').send_keys("柠檬班")
sleep(1)
driver.find_element_by_xpath('//input[@id="su"]').click()
driver.quit()

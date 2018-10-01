__author__ = 'computer'
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("http://39.108.136.60/login.html#!/login")
# driver.implicitly_wait(8)
# driver.find_element_by_xpath('//input[@name="userName"]').send_keys("pingzi")
# driver.find_element_by_xpath('//input[@name="password"]').send_keys("123456")
# sleep(2)
# try:
#     driver.find_element_by_css_selector('body > div.login-main.ng-scope > div > div.login-form > form > div.form-actions > div > label').is_selected()
#     driver.find_element_by_css_selector('body > div.login-main.ng-scope > div > div.login-form > form > div.form-actions > div > label').click()
# except:
#     driver.find_element_by_css_selector('body > div.login-main.ng-scope > div > div.login-form > form > div.form-actions > div > label').click()
#
# driver.find_element_by_tag_name('button').click()

def dologon(url,usname,password):
    driver.get(url)
    driver.implicitly_wait(8)
    driver.find_element_by_xpath('//input[@name="userName"]').send_keys(usname)
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
    sleep(2)
    try:
        driver.find_element_by_css_selector('body > div.login-main.ng-scope > div > div.login-form > form > div.form-actions > div > label').is_selected()
        driver.find_element_by_css_selector('body > div.login-main.ng-scope > div > div.login-form > form > div.form-actions > div > label').click()
    except:
        driver.find_element_by_css_selector('body > div.login-main.ng-scope > div > div.login-form > form > div.form-actions > div > label').click()
    driver.find_element_by_tag_name('button').click()
    return [usname,password]

url = "http://39.108.136.60/login.html#!/login"
usname = "pingzi"
password = "123456"
list = dologon(url,usname,password)
print(list)
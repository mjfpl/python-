__author__ = 'computer'
from selenium import webdriver  #导入驱动 webdriver 这个类\
# import selenium
#from time import  ctime
#driver = webdriver.Firefox() # 创建一个对象
driver = webdriver.Chrome()
driver.maximize_window() # 浏览器最大化
driver.get("https://www.baidu.com") # 打开百度
driver.find_element_by_id("kw").send_keys("柠檬班") # 定位百度的搜索框 跟输入要查询的语句
driver.find_element_by_id("su").click() # 定位百度的按钮 并点击
driver.find_element_by_link_text(u"新闻").click()
#driver.quit() # 关闭
__author__ = 'computer'
from selenium import webdriver
import time
driver = webdriver.Chrome() #创建一个谷歌浏览器的对象
# driver.maximize_window() # 浏览器最大化
# driver.get("http://www.baidu.com") # 打开百度
# driver.find_element_by_id("kw").send_keys("柠檬班") # z找到输入框并输入要查询的东西
# driver.find_element_by_id("su").click() # 定位到百度一下的按钮并点击
# driver.back() # 返回
# driver.forward() # 前进
# time.sleep(3) #延时三秒
# driver.refresh() #刷新页面
# driver.close() #关闭当前页面
# driver.quit() # 关闭
driver.maximize_window()
driver.get("http://120.78.128.25:8765/Index/login.html")
driver.find_element_by_xpath('//input[@name="phone"]').send_keys("17600151417")
# driver.find_element_by_xpath('.//*input[@name="phone"]').send_keys("17600151417")  顶级目录下的所有input[@name="phone"] 标签
time.sleep(1)
driver.find_element_by_xpath('//input[@name="password"]').send_keys("zhao17600151418")
time.sleep(1)
try:
    driver.find_element_by_xpath('//input[@name="remember_me"]').is_selected()
except :
    print("异常")
time.sleep(1)
# driver.find_element_by_partial_link_text("新").click() 模糊链接定位法 类似于数据库里面的 like
driver.find_element_by_xpath('//button').click()
driver.quit()



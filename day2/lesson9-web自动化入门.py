from selenium import webdriver
import time
#开启与chrome浏览器之间的会话,打开一个浏览器
driver = webdriver.Chrome()

#将浏览器最大化
driver.maximize_window()

#访问一个网址
driver.get("http://www.baidu.com")
# driver.get("http://www.taobao.com")
# #回退到上一个页面
# driver.back()
# #前进到下一个页面
# driver.forward()
# #刷新当前页面
# driver.refresh()

# #通过id找到此元素：
# element = driver.find_element_by_id("kw")
# #通过name属性找元素：
#1、找到一个元素
#ele_2 = driver.find_element_by_name("wd")
#eles_list = driver.find_elements_by_name("wd")

# #通过class属性来查找元素
# ele_3 = driver.find_element_by_class_name("s_ipt")
#
# #通过标签名来找
# driver.find_element_by_tag_name("input")

# #仅针对链接的两种定位方式
# driver.find_element_by_link_text("地图")
# driver.find_element_by_partial_link_text("产品")

#xpath,css
driver.find_element_by_xpath('//input[@name="phone" and @datatype="m"]')


ele_2 = driver.find_element_by_name("wd")
#print(element)
#元素执行输入操作
ele_2.send_keys("柠檬班")
driver.find_element_by_id("su").click()

time.sleep(3)

#关闭当前窗口
driver.close()
#关闭与浏览器之间的会话
driver.quit()

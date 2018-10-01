__author__ = 'computer'
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("http://www.baidu.com")
# sleep(2)
# driver.find_element_by_xpath('.//input[@id="kw"]').send_keys("图片")
# sleep(2)
# driver.find_element_by_xpath('.//input[@id="su"]').click()
# sleep(2)
# driver.quit()
driver.get("https://mail.163.com/")
sleep(1)
'''
在定位的时候发现有些元素定位不到，最后发现有iframe。

如果ifame 有name或id的话，直接使用switch_to_frame("name值")
或switch_to_frame("id值")，这是最理想的方法，也是最简单好用的方法。

此时可以使用xpath先对iframe进行定位：iframe = find_element_by_xpath（"//div/iframe"）
然后再使用switch_to_frame()函数：switch_to_frame(iframe)
'''
iframe = driver.find_element_by_xpath('//iframe[@id="x-URS-iframe"]')
driver.switch_to_frame(iframe)
driver.find_element_by_xpath('//input[@name="email"]').send_keys("17600151417")
sleep(1)
driver.find_element_by_xpath('//input[@name="password"]').send_keys("zhao17600151417")
sleep(1)
driver.find_element_by_xpath('//a[@id="dologin"]').click()
'''
问题又来了，iframe我们进来了，那么该怎么出去呢，出不去就没法操作其他元素。

那就该使用：driver.switch_to_default_content()，返回到主content，也就是主界面中
'''
driver.switch_to_default_content()
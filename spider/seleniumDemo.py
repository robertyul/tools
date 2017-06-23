# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
第一部分：send request
'''
driver = webdriver.PhantomJS(executable_path=r'''C:\Users\robertpicyu\Downloads\phantomjs-2.1.1-windows\bin\phantomjs.exe''')
#driver = webdriver.Chrome()
#url = "http://www.baidu.com"
url = "http://www.kankanwu.com/Animation/jidongqiangxishidibazu/"


'''
第二部分：处理请求
'''
try:
    driver.set_page_load_timeout(4)
    try:
        html = driver.get(url)
    except Exception,e:
        print "page time out: "
    head = driver.find_element_by_xpath(r'''//*[@id="detail-box"]/div[3]/h1''');
    print head.text
finally:
    driver.quit()
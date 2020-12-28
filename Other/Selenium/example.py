#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
sleep(5)
driver.get("https://www.citilink.ru/")
sleep(5)
assert "СИТИЛИНК" in driver.title
print('OK')
sleep(5)
elem = driver.find_element_by_name("text")
sleep(5)
elem.clear()
sleep(5)
elem.send_keys("DL4310")
sleep(5)
elem.send_keys(Keys.RETURN)
sleep(5)
#price = driver.find_element_by_class_name('num')
price = driver.find_element_by_class_name('num')
sleep(5)
print(price)
sleep(10)
#assert "No results found." not in driver.page_source
#sleep(5)"""
driver.close()
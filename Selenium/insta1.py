from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("http://www.instagram.com")
#don't forget assert
driver.find_element_by_link_text('Вход').click()

inputs = driver.find_element_by_xpath('//form/div/div/div/input')

ActionChains(driver)\
   .move_to_element(inputs[0].click())\
   .send_keys('victor_shalaginov')\
   .move_to_element(inputs[1].click())\
   .send_keys('123')\
   .perform()

login_button = driver.find_element_by_xpath('//form/span/button[text()="Войти"]')

ActionChains(driver)\
   .move_to_element(login_button)\
   .click().perform()



#
from selenium import webdriver
import time
driver = webdriver.Chrome()

url = "http://www.baidu.com"

driver.get(url)
text =driver.find_element_by_id("wrapper").text
print(text)
print(driver.title)
driver.save_screenshot("d1.png")
driver.find_element_by_id("kw").send_keys(u"dnf")
driver.find_element_by_id("su").click()
time.sleep(15)
driver.save_screenshot("dnf.png")
driver.find_element_by_id("kw").clear()
print(driver.get_cookies())
driver.find_element_by_id("kw").send_keys(u"虎")
driver.find_element_by_id("su").click()
time.sleep(10)
driver.save_screenshot("h2u.png")
driver.find_element_by_id("kw").clear()
driver.quit()
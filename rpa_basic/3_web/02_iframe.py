import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

browser.switch_to.frame('iframeResult') # frame 전환

browser.find_element_by_xpath('//*[@id="html"]').click() # 성공

browser.switch_to.default_content() # 상위로 빠져 나옴

browser.find_element_by_xpath('//*[@id="html"]').click() # 실패

time.sleep(3)
browser.quit()
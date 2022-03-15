import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

browser.switch_to.frame('iframeResult')

# elem = browser.find_element_by_xpath('//*[@id="vehicle1"]')
# elem = browser.find_element(By.XPATH, '//*[@id="vehicle1"]')
elem = browser.find_element(By.ID, 'vehicle1')

time.sleep(3)

if elem.is_selected() == False:
    print("선택되어 있지 않으므로 선택")
    elem.click()
else:
    print("선택되어 있으므로 동작 안함")

time.sleep(3)

browser.quit()
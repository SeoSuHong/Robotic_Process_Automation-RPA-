import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://flight.naver.com/')

browser.find_element_by_class_name('tabContent_option__2y4c6').click()

time.sleep(1)

browser.find_elements_by_class_name('sc-crzoAE')[27].click() # 3월 28일 출발
browser.find_elements_by_class_name('sc-crzoAE')[34].click() # 4월 4일 도착

# 도착지 선택 (제주)
browser.find_elements_by_class_name('select_code__d6PLz')[1].click()
browser.find_elements_by_class_name('autocomplete_Collapse__tP3pM')[0].click()
browser.find_elements_by_class_name('autocomplete_Airport__3_dRP')[1].click()

# 항공권 검색 클릭
browser.find_element_by_class_name('searchBox_search__2KFn3').click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]/div')))
    print(elem.text)
except:
    print('실패')

time.sleep(3)

browser.quit()
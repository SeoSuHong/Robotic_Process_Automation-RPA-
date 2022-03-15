import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(3)

# 특정 영역 스크롤
elem = browser.find_element_by_link_text('HTML Tag List')

# 방법 1 : ActionChain
actions = ActionChains(browser)
actions.move_to_element(elem).perform()

# 방법 2 : 좌표 정보 이용
xy = elem.location_once_scrolled_into_view # 함수가 아니니깐 () 사용X
print("type : ", type(xy)) # dict
print("value : ", xy) # {'x': 0, 'y': 255}

elem.click()

time.sleep(3)

browser.quit()
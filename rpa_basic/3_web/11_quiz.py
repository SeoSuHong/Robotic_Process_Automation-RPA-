# 1. https://www.w3schools.com 접속 (URL은 구글에서 w3schools 검색)
# 2. 화면 중간 LEARN HTML 클릭
# 3. 상단 메뉴 중 HOW TO 클릭
# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# 5. 입력란에 아래 값 입력
#   First Name : 서
#   Last Name : 수홍
#   Country : Canada
#   Subject : 퀴즈 완료.
#   - 위 값들은 변수로 미리 저장
# 6. 3초 대기 후 Submit 버튼 클릭
# 7. 3초 대기 후 브라우저 종료

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 1. https://www.w3schools.com 접속 (URL은 구글에서 w3schools 검색)
browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/')
browser.maximize_window()

# 2. 화면 중간 LEARN HTML 클릭
browser.find_element_by_link_text('Learn HTML').click()

# 3. 상단 메뉴 중 HOW TO 클릭
browser.find_element_by_link_text('HOW TO').click()

# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
elem = browser.find_element_by_link_text('Contact Form')
actions = ActionChains(browser)
actions.move_to_element(elem).perform()
elem.click()

#   First Name : 서
#   Last Name : 수홍
#   Country : Canada
#   Subject : 퀴즈 완료.
#   - 위 값들은 변수로 미리 저장

first_name = "서"
last_name = "수홍"
country = "Canada"
subject = "퀴즈 완료."

# 5. 입력란에 아래 값 입력
browser.find_element_by_id('fname').send_keys(first_name)
browser.find_element_by_id('lname').send_keys(last_name)
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)

# 6. 3초 대기 후 Submit 버튼 클릭
time.sleep(3)
browser.find_element_by_link_text('Submit').click()

# 7. 3초 대기 후 브라우저 종료
time.sleep(3)
browser.quit()
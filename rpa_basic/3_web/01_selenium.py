from selenium import webdriver

# browser = webdriver.Chrome("./chromedriver.exe")
browser = webdriver.Chrome()

# 네이버 이동
browser.get("http:/naver.com")

# 카페 메뉴 찾기
elem = browser.find_element_by_link_text("카페")

# 속성 가져오기
elem.get_attribute('href')
elem.get_attribute('class')

# 클릭
browser.click()

# 뒤로 가기
browser.back()

# 앞으로 가기
browser.forward()

# 새로고침
browser.refresh()

# 검색창 찾기 (개발자 도구 이용)
elem = browser.find_element_by_id('query')

# 글자 입력하기
elem.send_keys('글자')

# enter
from selenium.webdriver.common.keys import Keys
elem.send_keys(Keys.ENTER)

# a 태그 찾기
elem = browser.find_element_by_tag_name("a")
elem.get_attribute('href')

# 태그 모두 찾기
elems = browser.find_elements_by_tag_name("a")
for e in elems:
    e.get_attribute('href')

# 다음으로 이동
browser.get('http')
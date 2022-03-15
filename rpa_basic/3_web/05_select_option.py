import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult')

# cars 에 해당하는 element 를 찾고, 드롭다운 내부에 있는 4번째 옵션을 선택
browser.find_element_by_xpath('//*[@id="cars"]/option[4]').click()
# option[1] : 첫번째 항목
# option[2] : 두번째 항목
# ...

# text 값으로 옵션 선택하는 방법
# text 값이 완전히 일치하는 항목 선택
browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]').click()

# text 값이 부분 일치하는 항목 선택
browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]').click()

time.sleep(3)

browser.quit()
# 1. 그림판 실행 (단축키 : win + r, 입력값 : mspaint) 및 최대화
# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
#  - 입력 글자 : "참 잘했습니다."
# 3. 5초 대기 후 그림판 종료
#  이 때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함

import pyautogui
import pyperclip
import time
import sys

# 1. 그림판 실행 (단축키 : win + r, 입력값 : mspaint) 및 최대화

pyautogui.hotkey("win", "r") # 단축키 : win + r 입력
pyautogui.write("mspaint") # 프로그램 명 입력
pyautogui.press("enter") # 엔터 키 입력

pyautogui.sleep(1)

window = pyautogui.getWindowsWithTitle("그림판")[0]
window.activate() # 활성화
if window.isMaximized == False:
    window.maximize() # 최대화

# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
#  - 입력 글자 : "참 잘했습니다."

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        sys.exit()

my_click("txt_btn.png", 10)

pyautogui.move(0, 200)
pyautogui.click()

pyperclip.copy("참 잘했습니다.")
pyautogui.hotkey("ctrl", "v")

# 3. 5초 대기 후 그림판 종료
#  이 때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함

pyautogui.sleep(1)

window.close()

pyautogui.sleep(1)

pyautogui.press("n")

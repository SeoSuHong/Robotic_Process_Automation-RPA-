import pyautogui

# 이미지 찾기 (locateOnScreen)
file_menu = pyautogui.locateOnScreen("file_menu.png")
print(file_menu)
pyautogui.click(file_menu)

trash_icon = pyautogui.locateOnScreen("trash_icon.png")
pyautogui.moveTo(trash_icon)

# 찾을 이미지가 없을 시
screen = pyautogui.locateOnScreen("screenshot.png")
print(screen) # None

# 찾을 이미지가 두개 이상일 시 (locateAllOnScreen)
# locateOnScreen : 하나의 동일한 이미지만 적용
checkbox = pyautogui.locateOnScreen("checkbox.png")
pyautogui.click(checkbox)

# locateAllOnScreen : 두개 이상의 동일한 이미지도 적용
for i in pyautogui.locateAllOnScreen("checkbox.png"):
    print(i)
    pyautogui.click(i, duration=0.25)

 

# 이미지 찾는 속도 개선

trash_icon = pyautogui.locateOnScreen("trash_icon.png")
pyautogui.moveTo(trash_icon)

# 1. GrayScale=True (화면을 흑백으로 전환 후 이미지 찾기)
trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
pyautogui.moveTo(trash_icon)

# 2. region=(x, y, width, height) (범위 지정)
trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1654, 673, 1908 - 1654, 928 - 673))
pyautogui.moveTo(trash_icon)

# 3. 정확도 조정 (pip install opencv-python 필요)
run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.5) # 50%
pyautogui.moveTo(run_btn)


# 자동화 대상이 바로 보여지지 않는 경우

# 1. 계속 기다리기
# 1-1. if문 사용
new_file = pyautogui.locateOnScreen("new_file.png")
if new_file:
    pyautogui.click(new_file)
else:
    print("발견 실패")

# 1-2. while문 사용
new_file = None

while new_file is None:
    new_file = pyautogui.locateOnScreen("new_file.png")
    print("발견 실패")

pyautogui.click(new_file)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

timeout = 10 # 10초 대기

# 2-1. 반복문 사용

start = time.time() # 시작 시간 설정
new_file = None

while new_file is None:
    new_file = pyautogui.locateOnScreen("new_file.png")
    end = time.time() # 종료 시간 설정
    if end - start > timeout: # 지정한 10초를 초과하면
        print('시간 종료')
        sys.exit()

pyautogui.click(new_file)

# 2-2. 함수 사용

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
        print(f"[TimeOut {timeout}s] Target not found ({img_file}). Terminate program")
        sys.exit()

my_click("new_file.png", 10)
import pyautogui

pyautogui.sleep(3) # 3초 대기
print(pyautogui.position())

pyautogui.click(1024, 17, duration=1) # 1초 동안 (1024, 17) 좌표로 이동 후 마우스 클릭
pyautogui.click()
pyautogui.mouseDown()
pyautogui.mouseUp()

# pyautogui.doubleClick() # 더블클릭
# pyautogui.click(clicks=500) # 500번 클릭
# pyautogui.rightClick() # 마우스 오른쪽 클릭
# pyautogui.middleClick() # 마우스 휠 클릭

# 드래그
pyautogui.moveTo(200, 200)
pyautogui.mouseDown() # 마우스 버튼 누른 상태
pyautogui.moveTo(300, 300)
pyautogui.mouseUp() # 마우스 버튼 뗀 상태

pyautogui.moveTo(660, 180)
pyautogui.drag(300, 0) # 현재 위치 기준으로 x 300 만큼, y 0 만큼 드래그
pyautogui.drag(300, 0, duration=0.25) # 너무 빠른 동작으로 drag 수행이 안될때는 duration 값 설정
pyautogui.dragTo(960, 180, duration=0.25) # 절대 좌표 기준으로 x 960, y 180 으로 드래그

pyautogui.scroll(300) # 양수이면 위 방향, 음수이면 아래 방향으로 300만큼 스크롤
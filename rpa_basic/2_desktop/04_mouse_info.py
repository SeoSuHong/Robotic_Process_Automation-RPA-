import pyautogui
pyautogui.FAILSAFE = False # 커서를 귀퉁이로 가져가도 작업이 끝나지 않음
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# pyautogui.mouseInfo() # 마우스의 정보(좌표, 색상 등)를 알려주는 GUI

for i in range(5):
    pyautogui.move(100, 100)
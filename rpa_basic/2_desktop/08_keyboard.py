import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate() # 활성화

# 한글은 작성이 안됨
pyautogui.write("12345")
pyautogui.write("SuHong", interval=0.25)
pyautogui.write("수홍")

pyautogui.write(['t', 'e', 's', 't', 'left', 'left', 'right', 'l', 'a', 'enter'], interval=1)
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향기 2번, l a 순서대로 적고 enter 입력

# 특수 문자
# shift 4 -> $
pyautogui.keyDown("shift") # shift 키를 누른 상태에서
pyautogui.keyDown("4") # 숫자 4를 입력하고
pyautogui.keyUp("shift") # shift 키를 뗀다

# 조합키
pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a") # press("a")
pyautogui.keyUp("ctrl") # Ctrl + A

# 간편한 조합키 (Hot Key)
pyautogui.hotkey("ctrl", "alt", "shift", "a")
# Ctrl > Alt > Shift > A > A > Shift > Alt > Ctrl (순서대로 누른 후 뗌)
pyautogui.hotkey("ctrl", "a")

# 한글 처리 (pip install pyperclip 필요)
import pyperclip

pyperclip.copy("파이썬") # "파이썬" 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("파이썬")

# 자동화 프로그램 종료 키
# win : ctrl + alt + del
# mac : cmd + shift + option + q
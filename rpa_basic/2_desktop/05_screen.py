import pyautogui

# 스크린 샷 찍기
img = pyautogui.screenshot()
img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 29,19 57,168,242 #39A8F2

pixel = pyautogui.pixel(29, 19)
print(pixel)

print(pyautogui.pixelMatchesColor(29, 19, (57, 168, 242))) # True
print(pyautogui.pixelMatchesColor(29, 19, pixel)) # True
print(pyautogui.pixelMatchesColor(29, 19, (57, 168, 142))) # False
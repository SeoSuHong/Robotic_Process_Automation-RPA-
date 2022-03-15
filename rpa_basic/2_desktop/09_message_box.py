import pyautogui

print("곧 시작합니다...")
pyautogui.countdown(3)
print("자동화 시작")

# alert : 확인 버튼만 있는 팝업
pyautogui.alert("자동화 수행에 실패하였습니다.", "경고")

# confirm : 확인, 취소
result = pyautogui.confirm("계속 진행하시겠습니까?", "확인")
print(result) # 확인 : OK, 취소 : Cancel

# prompt : 사용자 입력
result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력")
print(result) # OK : 사용자 입력, Cancel : None

# password : 암호 입력 (*로 표시)
result = pyautogui.password("암호를 입력하세요.")
print(result) # OK : 사용자 입력, Cancel : None
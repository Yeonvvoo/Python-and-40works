import pyautogui
import time
import pyperclip

# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)

#### 서울날씨 자동 검색
pyautogui.moveTo(1019, 229, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("command", "v")
time.sleep(0.5)

pyautogui.write(['enter'])
time.sleep(1)


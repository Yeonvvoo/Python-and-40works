import pyautogui
import pyperclip
import os
import time
import threading

def send_message():
    threading.Timer(10, send_message().start())

picPosition = pyautogui.locateOnScreen('./src1.jpeg')
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('./src2.jpeg')
    print(picPosition)
if picPosition is None:
    picPosition = pyautogui.locateOnScreen('./test.jpeg')
    print(picPosition)

clickPosition = pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)

pyperclip.copy("이 메세지는 자동으로 보내는 메세지 입니다~~~")
pyautogui.hotkey("command", "v")
time.sleep(1.0)

send_message()

pyautogui.write(["enter"])
time.sleep(1.0)

pyautogui.write(["escape"])
time.sleep(1.0)


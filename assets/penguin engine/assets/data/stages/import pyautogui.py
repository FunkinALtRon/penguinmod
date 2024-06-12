import pyautogui
import time

counter = 0

time.sleep(2)

while True:
    pyautogui.hotkey("ctrlleft", "v")
    pyautogui.press("enter")
    counter += 1
    print(counter)
    time.sleep(2)
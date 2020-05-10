import os
import time
import pyautogui

time.sleep(1)

# pyautogui.click()

key5_location = pyautogui.locateCenterOnScreen("pyautogui/src/key5.png")
pyautogui.click(key5_location)

plus_location = pyautogui.locateCenterOnScreen("pyautogui/src/pluskey.png")
print(plus_location)
pyautogui.click(plus_location)

pyautogui.click(key5_location)

pyautogui.press('enter')


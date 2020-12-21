import time
import pyautogui

time.sleep(3)

pyautogui.click()

distance = 800

while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance -= 50
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance -= 50
    pyautogui.dragRel(0, -distance, duration=0.2)

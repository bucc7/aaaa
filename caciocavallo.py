import time
import pyautogui
import keyboard


print("caciocavallo spam v0.1")
time.sleep(5)
for i in range(9693):
    pyautogui.click(button='right')
    for i in range(8):
        keyboard.press_and_release("down")
        time.sleep(0.1)
    keyboard.press_and_release("right")
    time.sleep(0.1)
    keyboard.press_and_release("down")
    time.sleep(0.1)
    keyboard.press_and_release("down")
    time.sleep(0.12)
    keyboard.press_and_release("enter")
    time.sleep(0.3)
    keyboard.press_and_release("tab")
    time.sleep(0.2)
    keyboard.press_and_release("enter")
    time.sleep(0.5)
    continue
exit()
import screen_brightness_control
import pyautogui

print(pyautogui.position())

def brightnessIncrease():
    screen_brightness_control.set_brightness(screen_brightness_control.get_brightness()[0] + 7)

def brightnessDecrease():
    screen_brightness_control.set_brightness(screen_brightness_control.get_brightness()[0] - 7)

def KeyboardInterrupt():
    pyautogui.hotkey('ctrl','c')

def click():
    pyautogui.leftClick()

def doubleClick():
    pyautogui.doubleClick()

def screenshot():
    pyautogui.hotkey('win','prtsc')

def profileswitch():
    i = i + 1

def mouseLeft(x):
    pyautogui.moveRel(-x)

def mouseRight(x):
    print(pyautogui.position())

def mouseUp():
    print(pyautogui.position())

def mouseDown():
    print(pyautogui.position())

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

def mouseMove(x,y):
    max_speed = 8
    normal_speed = 4
    if(x > 0.5 or x < -0.5):
        x *= max_speed
    else:
        x *= normal_speed
    if(y > 0.5 or y < -0.5):
        y *= max_speed
    else:
        y *= normal_speed
    pyautogui.moveRel(x,y)





    

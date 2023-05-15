import screen_brightness_control
import pyautogui

def brightnessIncrease():
    screen_brightness_control.set_brightness(screen_brightness_control.get_brightness()[0] + 15)

def brightnessDecrease():
    screen_brightness_control.set_brightness(screen_brightness_control.get_brightness()[0] - 15)

def keyboardInterrupt():
    pyautogui.hotkey('ctrl','c')

def click():
    pyautogui.leftClick()

def doubleClick():
    pyautogui.doubleClick()

def screenshot():
    pyautogui.hotkey('win','prtsc')

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

brightnessIncrease()





    

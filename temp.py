id = 0
PROFILE_NAME = "General"
A = "enter"
B = "keyboardInterrupt"
X = "click"
Y = "screenshot"
START = "win"
BACK = "esc"
LJ = "volumemute"
RJ = "doubleClick"
LB = "switchProfile"
RB = "tab"
LJ_XN = "left"
LJ_XP = "right"
LJ_YN = "up"
LJ_YP = "down"
RJ_XN = "mouseMove"
RJ_XP = "mouseMove" 
RJ_YN = "mouseMove"             
RJ_YP = "mouseMove"
LT = "alt"
RT = "shift"
TOP = "brightnessIncrease"
BOTTOM = "brightnessDecrease"
LEFT = "volumedown"
RIGHT = "volumeup"
TOP_LEFT = "["
TOP_RIGHT = "]"
BOTTOM_LEFT = "b"
BOTTOM_RIGHT = "f"

#{id},{PROFILE_NAME},{A},{B},{X},{Y},{START},{BACK},{LJ},{RJ},{LB},{RB},{LJ_XN},{LJ_XP},{LJ_YN},{LJ_YP},{RJ_XN},{RJ_XP},{RJ_YN},{RJ_YP},{LT},{RT},{TOP},{BOTTOM},{LEFT},{RIGHT},{TOP_LEFT},{TOP_RIGHT},{BOTTOM_LEFT},{BOTTOM_RIGHT}
import pyautogui
from macros import *
import pygame

# pygame.init()
# pygame.joystick.init()
# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
# print(joysticks)

# while True:
#     if pygame.joystick.get_count() == 0:
#         break
#     for event in pygame.event.get():
#         if event.type == pygame.JOYAXISMOTION:
#             LEFT_JOYSTICK_X = pygame.joystick.Joystick(0).get_axis(0)
#             LEFT_JOYSTICK_Y = pygame.joystick.Joystick(0).get_axis(1)
#             RIGHT_JOYSTICK_X = pygame.joystick.Joystick(0).get_axis(2)
#             RIGHT_JOYSTICK_Y = pygame.joystick.Joystick(0).get_axis(3)
#             LEFT_TRIGGER = pygame.joystick.Joystick(0).get_axis(4)
#             RIGHT_TRIGGER = pygame.joystick.Joystick(0).get_axis(5)

#             if(LEFT_JOYSTICK_X != -3.0517578125e-05):
#                 print(pygame.joystick.Joystick(0).get_axis(0))
#             if(LEFT_JOYSTICK_Y != -3.0517578125e-05):
#                 print(pygame.joystick.Joystick(0).get_axis(1))    
#             if(RIGHT_JOYSTICK_X != -3.0517578125e-05):
#                 print(pygame.joystick.Joystick(0).get_axis(2))
#             if(RIGHT_JOYSTICK_Y != -3.0517578125e-05):
#                 print(pygame.joystick.Joystick(0).get_axis(3))
#             if(LEFT_TRIGGER != -1):
#                 print(pygame.joystick.Joystick(0).get_axis(4))
#             if(RIGHT_TRIGGER != -1):
#                 print(pygame.joystick.Joystick(0).get_axis(5))

sugg_data = ['screenshot','mouseMove','brightnessIncrease','brightnessDecrease','KeyboardInterrupt','click','doubleClick','\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',  ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt','altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites','browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']

dict = {"mouseMove_macro" : "mouseMove",
"brightnessIncrease_macro" : "brightnessIncrease",
"brightnessDecrease_macro" : "brightnessDecrease",
"screenshot_macro" : "screenshot"}

fun = "mouseMove"
globals()[fun](10,10)

PROFILE_NAME_KEY = PROFILE_NAME_entry.get()
B_KEY = B_entry.get()
A_KEY = A_entry.get()
X_KEY = X_entry.get()
Y_KEY = Y_entry.get()
START_KEY = START_entry.get()
BACK_KEY = BACK_entry.get()
LJ_KEY = LJ_entry.get()
RJ_KEY = RJ_entry.get()
LB_KEY = LB_entry.get()
RB_KEY = RB_entry.get()
LJ_XN_KEY = LJ_XN_entry.get()
LJ_XP_KEY = LJ_XP_entry.get()
LJ_YN_KEY = LJ_YN_entry.get()
LJ_YP_KEY = LJ_YP_entry.get()
RJ_XN_KEY = RJ_XN_entry.get()
RJ_XP_KEY =  RJ_XP_entry.get() 
RJ_YN_KEY =  RJ_YN_entry.get()                   
RJ_YP_KEY = RJ_YP_entry.get()
LT_KEY = LT_entry.get()
RT_KEY = RT_entry.get()
TOP_KEY = TOP_entry.get()
BOTTOM_KEY = BOTTOM_entry.get()
LEFT_KEY = LEFT_entry.get()
RIGHT_KEY = RIGHT_entry.get()
TOP_LEFT_KEY = TOP_LEFT_ENTRY.get()
TOP_RIGHT_KEY = TOP_RIGHT_ENTRY.get()
BOTTOM_LEFT_KEY = BOTTOM_LEFT_entry.get()
BOTTOM_RIGHT = BOTTOM_RIGHT_entry.get()

import tkinter as tk

window = tk.Tk()

row = 5
col = 3
i = 1
j = 1
def create_widget(label_text, default_value):
    global i,j,col,row
    label = tk.Label(window, text=label_text)
    label.grid(row = i*2 - 1, column = j, padx= 5)
    entry = tk.Entry(window)
    entry.insert(0, default_value)
    entry.grid(row = i*2, column = j, padx= 5, pady= 2)
    i = i + 1
    if(i > row):
        i = 1
        j = j + 1
    return entry

create_widget("ABC","89")
create_widget("ABC","89")
create_widget("ABC","89")
create_widget("ABC","89")
create_widget("ABC","89")
create_widget("ABC","89")
create_widget("ABC","89")
create_widget("ABC","89")
create_widget("ABC","89")
create_widget("ABC","89")
create_widget("ABC","89")
create_widget("ABC","89")

window.mainloop()
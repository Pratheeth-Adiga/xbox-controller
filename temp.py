#{id},{PROFILE_NAME},{A},{B},{X},{Y},{START},{BACK},{LJ},{RJ},{LB},{RB},{LJ_XN},{LJ_XP},{LJ_YN},{LJ_YP},{RJ_XN},{RJ_XP},{RJ_YN},{RJ_YP},{LT},{RT},{TOP},{BOTTOM},{LEFT},{RIGHT},{TOP_LEFT},{TOP_RIGHT},{BOTTOM_LEFT},{BOTTOM_RIGHT}
import pyautogui
import pygame

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

while True:
    if pygame.joystick.get_count() == 0:
        break
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            LEFT_JOYSTICK_X = pygame.joystick.Joystick(0).get_axis(0)
            LEFT_JOYSTICK_Y = pygame.joystick.Joystick(0).get_axis(1)
            RIGHT_JOYSTICK_X = pygame.joystick.Joystick(0).get_axis(2)
            RIGHT_JOYSTICK_Y = pygame.joystick.Joystick(0).get_axis(3)
            LEFT_TRIGGER = pygame.joystick.Joystick(0).get_axis(4)
            RIGHT_TRIGGER = pygame.joystick.Joystick(0).get_axis(5)

            if(LEFT_JOYSTICK_X != -3.0517578125e-05):
                print(pygame.joystick.Joystick(0).get_axis(0))
            if(LEFT_JOYSTICK_Y != -3.0517578125e-05):
                print(pygame.joystick.Joystick(0).get_axis(1))    
            if(RIGHT_JOYSTICK_X != -3.0517578125e-05):
                print(pygame.joystick.Joystick(0).get_axis(2))
            if(RIGHT_JOYSTICK_Y != -3.0517578125e-05):
                print(pygame.joystick.Joystick(0).get_axis(3))
            if(LEFT_TRIGGER != -1):
                print(pygame.joystick.Joystick(0).get_axis(4))
            if(RIGHT_TRIGGER != -1):
                print(pygame.joystick.Joystick(0).get_axis(5))

['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',
  ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', 
';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 
'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt',
'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites',
'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop',
 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 
'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 
'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 
'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 
'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 
'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 
'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 
'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 
'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 
'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 
'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 
'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']
import pygame
from macros import *
from getFromDB import getProfiles

pygame.init()
pygame.joystick.init()
pyautogui.FAILSAFE = False
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
data = getProfiles()

i = 0
def switchProfile():
    i += 1
    i = i%len(data)

def fun1(x,vert = None,hor = None):
    if(pyautogui.isValidKey(data[i][x])):
        pyautogui.press(data[i][x])
    else:
        if(vert == None or hor == None):
            globals()[data[i][x]]
        else:
            globals()[data[i][x]](vert,hor)

while True:
    if pygame.joystick.get_count() == 0:
        break
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            BUTTON_A = pygame.joystick.Joystick(0).get_button(0)
            BUTTON_B = pygame.joystick.Joystick(0).get_button(1)
            BUTTON_X = pygame.joystick.Joystick(0).get_button(2)
            BUTTON_Y = pygame.joystick.Joystick(0).get_button(3)
            BUTTON_LEFT_SHOULDER = pygame.joystick.Joystick(0).get_button(4)
            BUTTON_RIGHT_SHOULDER = pygame.joystick.Joystick(0).get_button(5)
            BUTTON_BACK = pygame.joystick.Joystick(0).get_button(6)
            BUTTON_START = pygame.joystick.Joystick(0).get_button(7)
            BUTTON_LEFT_JOYSTICK = pygame.joystick.Joystick(0).get_button(8)
            BUTTON_RIGHT_JOYSTICK = pygame.joystick.Joystick(0).get_button(9)

            if(BUTTON_A):
                fun1(2)
            if(BUTTON_B):
                fun1(3)          
            if(BUTTON_X):
                fun1(4)
            if(BUTTON_Y):
                fun1(5)
            if(BUTTON_START):
                fun1(6)
            if(BUTTON_BACK):
                fun1(7)
            if(BUTTON_LEFT_JOYSTICK):
                fun1(8)
            if(BUTTON_RIGHT_JOYSTICK):
                fun1(9)
            if(BUTTON_LEFT_SHOULDER):
                fun1(10)
            if(BUTTON_RIGHT_SHOULDER):
                fun1(11)
            

        if event.type == pygame.JOYAXISMOTION:
            LEFT_JOYSTICK_X = pygame.joystick.Joystick(0).get_axis(0)
            LEFT_JOYSTICK_Y = pygame.joystick.Joystick(0).get_axis(1)
            RIGHT_JOYSTICK_X = pygame.joystick.Joystick(0).get_axis(2)
            RIGHT_JOYSTICK_Y = pygame.joystick.Joystick(0).get_axis(3)
            LEFT_TRIGGER = pygame.joystick.Joystick(0).get_axis(4)
            RIGHT_TRIGGER = pygame.joystick.Joystick(0).get_axis(5)

            if(LEFT_JOYSTICK_X < -0.3 and LEFT_JOYSTICK_X != -3.0517578125e-05):
                fun1(12)
            if(LEFT_JOYSTICK_X > 0.3):
                fun1(13)
            if(LEFT_JOYSTICK_Y < -0.3 and LEFT_JOYSTICK_Y != -3.0517578125e-05):
                fun1(14)
            if(LEFT_JOYSTICK_Y > 0.3):
                fun1(15)
            if RIGHT_JOYSTICK_X != 0 or RIGHT_JOYSTICK_Y != 0:
                if(RIGHT_JOYSTICK_Y != -3.0517578125e-05 and RIGHT_JOYSTICK_X != -3.0517578125e-05):
                    fun1(16,RIGHT_JOYSTICK_X,RIGHT_JOYSTICK_Y)
            if(LEFT_TRIGGER != -1):
                fun1(20)
            if(RIGHT_TRIGGER != -1):
                fun1(21)

        if event.type == pygame.JOYHATMOTION:
            HAT_TOP = (pygame.joystick.Joystick(0).get_hat(0)) == (0,1)
            HAT_BOTTOM = (pygame.joystick.Joystick(0).get_hat(0)) == (0,-1)
            HAT_LEFT = (pygame.joystick.Joystick(0).get_hat(0)) == (-1,0)
            HAT_RIGHT = (pygame.joystick.Joystick(0).get_hat(0)) == (1,0)
            HAT_TOP_LEFT = (pygame.joystick.Joystick(0).get_hat(0)) == (-1,1)
            HAT_TOP_RIGHT = (pygame.joystick.Joystick(0).get_hat(0)) == (1,1)
            HAT_BOTTOM_LEFT = (pygame.joystick.Joystick(0).get_hat(0)) == (-1,-1)
            HAT_BOTTOM_RIGHT = (pygame.joystick.Joystick(0).get_hat(0)) == (1,-1)
            
            if(HAT_TOP):
                fun1(22)
            if(HAT_BOTTOM):
                fun1(23)
            if(HAT_LEFT):
                fun1(24)
            if(HAT_RIGHT):
                fun1(25)
            if(HAT_TOP_LEFT):
                fun1(26)
            if(HAT_TOP_RIGHT):
                fun1(27)
            if(HAT_BOTTOM_LEFT):
                fun1(28)
            if(HAT_BOTTOM_RIGHT):
                fun1(29)

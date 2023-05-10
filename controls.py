import pygame

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

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
            BUTTON_NEXT = pygame.joystick.Joystick(0).get_button(7)
            BUTTON_LEFT_JOYSTICK = pygame.joystick.Joystick(0).get_button(8)
            BUTTON_RIGHT_JOYSTICK = pygame.joystick.Joystick(0).get_button(9)

            if(BUTTON_A):
                print("Pressed A")
            if(BUTTON_B):
                print("Pressed B")           
            if(BUTTON_X):
                print("Pressed x")
            if(BUTTON_Y):
                print("Pressed y")
            if(BUTTON_LEFT_SHOULDER):
                print("ls")
            if(BUTTON_RIGHT_SHOULDER):
                print("right shoulder")
            if(BUTTON_BACK):
                print("back")
            if(BUTTON_NEXT):
                print("next")
            if(BUTTON_LEFT_JOYSTICK):
                print("ljb")
            if(BUTTON_RIGHT_JOYSTICK):
                print("right joystick button")

        if event.type == pygame.JOYAXISMOTION:
            LEFT_JOYSTICK_X = pygame.joystick.Joystick(0).get_axis(0)
            LEFT_JOYSTICK_Y = pygame.joystick.Joystick(0).get_axis(1)
            RIGHT_JOYSTICK_X = pygame.joystick.Joystick(0).get_axis(2)
            RIGHT_JOYSTICK_Y = pygame.joystick.Joystick(0).get_axis(3)
            LEFT_TRIGGER = pygame.joystick.Joystick(0).get_axis(4)
            RIGHT_TRIGGER = pygame.joystick.Joystick(0).get_axis(5)

            if(LEFT_JOYSTICK_X):
                print(pygame.joystick.Joystick(0).get_axis(0))
            if(LEFT_JOYSTICK_Y):
                print(pygame.joystick.Joystick(0).get_axis(1))    
            if(RIGHT_JOYSTICK_X):
                print(pygame.joystick.Joystick(0).get_axis(2))
            if(RIGHT_JOYSTICK_Y):
                print(pygame.joystick.Joystick(0).get_axis(3))
            if(LEFT_TRIGGER != -1):
                print(pygame.joystick.Joystick(0).get_axis(4))
            if(RIGHT_TRIGGER != -1):
                print(pygame.joystick.Joystick(0).get_axis(5))

        if event.type == pygame.JOYHATMOTION:
            HAT_UP = (pygame.joystick.Joystick(0).get_hat(0))[1] == 1
            HAT_DOWN = (pygame.joystick.Joystick(0).get_hat(0))[1] == -1
            HAT_LEFT = (pygame.joystick.Joystick(0).get_hat(0))[0] == -1
            HAT_RIGHT = (pygame.joystick.Joystick(0).get_hat(0))[0] == 1

            if(HAT_UP):
                print("up")
            if(HAT_DOWN):
                print("down")
            if(HAT_LEFT):
                print("left")
            if(HAT_RIGHT):
                print("right")
            
                
    
    
        
"""

"""

import pygame


pygame.init()


# Initialize the joysticks.
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

# -------- Main Program Loop -----------
while True:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
            print(event)
            # print(pygame.key.get_pressed())
            # a = pygame.key.get_pressed()
            # al = list(a)
            # alt = [i for (i, e) in enumerate(al) if e]
            # print(alt)
            # print(any(a))
            # print([joysticks[0].get_button(i) for i in range(joysticks[0].get_numbuttons())])
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            print(event)
            # a = pygame.key.get_pressed()
            # al = list(a)
            # alt = [i for (i, e) in enumerate(al) if e]
            # print(alt)
            # print(any(a))
        elif event.type == pygame.JOYAXISMOTION:
            print("Joystick moved")
            print(event)
        elif event.type == pygame.JOYHATMOTION:
            print("Joy hat motion")
            print(event)
        else:
            print(event.type)

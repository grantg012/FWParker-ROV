import pygame
import serial
import time


arduino_port = serial.Serial(port = 'COM4', baudrate = 115200, timeout = 0.1)

pygame.init()


# Initialize the joysticks.
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)


def write_read(message: bytes):
    global arduino_port
    arduino_port.write(message)
    data = arduino_port.readline()
    return data


# -------- Main Program Loop -----------
while True:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        print(event)
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
            write_read(b'P')
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
    time.sleep(0.01)

"""

PS2 - right joy maps to right buttons
XBOX - 
"""

from inputs import get_gamepad

opt = 0

if opt == 0:
    while True:
        events = get_gamepad()
        # print(events)
        for event in events:
            # print(event)
            if(event.ev_type in ["Key", "Absolute"]):
                print(event.ev_type)
                try:
                    print(event.status)
                except Exception:
                    pass
                print(event.code)
                print(event.state, end='\n\n')
            # if event.ev_type == 'Absolute':
            #     if event.code == 'ABS_X':
            #         print(f'Left joystick x: {event.state}')
            #     elif event.code == 'ABS_Y':
            #         print(f'Left joystick y: {event.state}')
            #     elif event.code == 'ABS_RX':
            #         print(f'Right joystick x: {event.state}')
            #     elif event.code == 'ABS_RY':
            #         print(f'Right joystick y: {event.state}')
elif opt == 1:
    from inputs import devices
    gp = devices.gamepads[0]
    while True:
        print(gp.read())
    # print(gp._GamePad__read_device())
    # print(gp)

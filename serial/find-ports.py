import serial.tools.list_ports
print(*[p.__dict__ for p in serial.tools.list_ports.comports()], sep = '\n')


# lower("arduino")

"whatever".lower()

def function_name():
    return correctdevice
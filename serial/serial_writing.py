import serial


arduino_port = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600, timeout = 0.1)


def write_read(message: bytes):
    global arduino_port
    arduino_port.write(message)
    data = arduino_port.readline()
    return data


while True:
    user_input = input("Enter a number: ") # Taking input from user
    value = write_read(user_input.encode())
    print(value) # printing the value

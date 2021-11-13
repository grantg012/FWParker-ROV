import serial


ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600, timeout = 0.1)

ser.write(b'L')



while True:
    command = input( "sent to the arduino")
    ser.write(command.encode())

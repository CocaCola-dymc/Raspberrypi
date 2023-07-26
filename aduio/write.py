import time
import serial

ser = serial.Serial('/dev/serial0',9600)
counter = 0

while 1:
    ser.write(counter)
    time.sleep(2)
    counter += 1
    print(counter)
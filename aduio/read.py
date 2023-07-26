import time
import serial

ser = serial.Serial(port='/dev/ttyAMA0',baudrate=9600,timeout=1)

try:
    while True:
        # 获得接收缓冲区字符
        count = ser.inWaiting()
        if count != 0:
            # 读取内容
            recv = ser.readline()
            print(recv.decode())
            ser.write(recv)
        # 清空接收缓冲区
        ser.flushInput()
        # 必要的软件延时
        time.sleep(0.5)
except KeyboardInterrupt:
    if ser != None:
        ser.close()
    
    
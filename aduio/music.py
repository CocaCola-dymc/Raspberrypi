import pygame
import serial
import time


ser = serial.Serial(port='/dev/ttyAMA0',baudrate=9600,timeout=1)

while True:
        # 获得接收缓冲区字符
        count = ser.inWaiting()
        if count != 0:
            # 读取内容
            recv = int(ser.readline().decode())
            #print(recv.decode())
            #print(type(recv))
            ser.write(recv)
            # 清空接收缓冲区
            ser.flushInput()
            
            pygame.mixer.init()
            pygame.mixer.music.load('/home/pi/aduio/warning.wav')
            pygame.mixer.music.set_volume(float(recv/100))
            pygame.mixer.music.play()
            #while pygame.mixer.music.get_busy():
                #pass
        # 必要的软件延时
        time.sleep(0.1)

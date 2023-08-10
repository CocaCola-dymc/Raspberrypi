from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import random
import time
import _thread
import serial
import pygame
import re
import matplotlib.animation as animation

class Function(object):
    # 嵌入matplotlib方法
    def set_matplotlib(self):
        # 创建画布
        self.fig = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.fig)
        # 把画布放进widget组件,设定位置
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.canvas)
        self.canvaswidget = QtWidgets.QWidget(self.widget)
        self.canvaswidget.setLayout(self.vlayout)
        self.canvaswidget.setGeometry(QtCore.QRect(0, -30, 910, 700))
        self.canvaswidget.setObjectName("matplotlib")
        self.canvaswidget.lower()      #将图形界面的层级置于底层
        # 初始化matplotlib显示区域
        self.ax = self.fig.subplots()
        #设置边界是否可见
        self.ax.spines['top'].set_visible(False)  # 顶边界不可见
        self.ax.spines['right'].set_visible(False)  # 右边界不可见


        #执行绘图函数
        _thread.start_new_thread(self.plotfig,())
        _thread.start_new_thread(self.serial,())
        _thread.start_new_thread(self.keyPressEvent,())
        #_thread.start_new_thread(self.buttonEvent,())
        #_thread.start_new_thread(self.music,())
        _thread.start_new_thread(self.battery,())

    #开始绘图
    def plotfig(self):          #(0.5s)
        self.y = [0,0,0,0,0,0]
        while True:
            if(self.recv.strip() != '' and re.match("^\d+$",self.recv.strip())):        #判断是否为空和整数
                self.data = int(self.recv.strip())
                if(self.data > 100):
                    self.data = 100
                elif(self.data <0):
                    self.data = 0
                else:
                    pass
            else:
                self.data = 0

            self.ax.autoscale_view()        #(0.004s)
            self.ax.cla()                   #清空画布(0.2s)
            self.x = ['1', '2', '3', '4', '5', '6']
            self.probe = int(self.probe)
            #设置y轴的范围
            self.ax.set_ylim(0,100)
            if(self.probe != self.probe_temp or self.probe == 0):
                self.probe_temp = self.probe
                #self.y = [0,0,0,0,0,0]
                for i in range(1,7):
                    self.erji[i].setPixmap(QtGui.QPixmap("images/erji.jpg"))
            else:
                pass

            for i in range(1,7):
                if(self.probe == i):
                    self.erji[i].setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
                    self.y[i-1] = self.data
                    self.ax.text(self.x[i-1],self.y[i-1]+2,self.y[i-1],ha='center',size=24)
                else:
                    pass

            #生成柱状图
            self.ax.bar(self.x,self.y,color=(1,0.5,0),width=0.6)

            #将数值显示在对应的柱子上
            #第一个x表示在x轴的位置,第一个y表示在y轴的位置,+2表示往上移动一点位置,以免挡住数字，
            #第二个y表示显示的内容,ha='center'表示数字居中，size为数字大小
            self.fig.canvas.draw()          # 画布重绘 self.figs.canvas(0.25s)
            self.fig.canvas.flush_events()  # 画布刷新 self.figs.canvas
            #break
            time.sleep(0.1)
        #_thread.start_new_thread(self.plotfig,())

    def keyPressEvent(self, event):         #(0.1s+0.5s)
        while True:
            #print("press:" + str(event.key()))
            if(event.key() == Qt.Key_7):
                self.probe = 1
                self.send = 1
            elif(event.key() == Qt.Key_Asterisk):
                self.probe = 2
                self.send = 2
            elif(event.key() == Qt.Key_F1):
                self.probe = 3
                self.send = 3
            elif(event.key() == Qt.Key_4):
                self.probe = 4
                self.send = 4
            elif(event.key() == Qt.Key_1):
                self.probe = 5
                self.send = 5
            elif(event.key() == Qt.Key_0):
                self.probe = 6
                self.send = 6
            #elif(event.key() == Qt.Key_Plus):
                #self.operate = 'up'
            #elif(event.key() == Qt.Key_Minus):
                #self.operate = 'down'
            #elif(event.key() == Qt.Key_Asterisk):
                #self.operate = 'left'
            #elif(event.key() == Qt.Key_Slash):
                #self.operate = 'right'
            #elif(event.key() == Qt.Key_Equal):
                #self.operate = 'ok'
            elif(event.key() == Qt.Key_9):
                self.send = 7
                self.operate = 'up'
            elif(event.key() == Qt.Key_Minus):
                self.send = 8
                self.operate = 'down'
            elif(event.key() == Qt.Key_F3):
                self.send = 9
                self.operate = 'menu'
            elif(event.key() == Qt.Key_6):
                self.send = 0
                self.operate = 'confirm'
            else:
                pass
            break
        _thread.start_new_thread(self.buttonEvent,())
        time.sleep(0.1)
        #_thread.start_new_thread(self.keyPressEvent,())

    def buttonEvent(self):          #(0.1s+0.5s)
        #print(self.operate)
        #while True:
        self.button1.setStyleSheet("QPushButton{border-radius: 10%;border: 1px solid black;background: url(/home/pi/aduio/images/filter_high.png) no-repeat cover center;}")
        self.button2.setStyleSheet("QPushButton{border-radius: 10%;border: 1px solid black;background: url(/home/pi/aduio/images/filter_low.png) no-repeat cover center;}")
        self.button3.setStyleSheet("QPushButton{border-radius: 10%;border: 1px solid black;background: url(/home/pi/aduio/images/brightness.png) no-repeat cover center;}")
#        self.button5.setStyleSheet("QPushButton{border-radius: 10%;border: 1px solid black;background: url(/home/pi/aduio/images/com_probe.png) no-repeat cover center;}")
#        self.button4.setStyleSheet("QPushButton{border-radius: 10%;border: 1px solid black;background: url(/home/pi/aduio/images/battery_levels.png) no-repeat cover center;}")
        self.button1.setShortcut('')
        self.button2.setShortcut('')
        self.button3.setShortcut('')
#        self.button4.setShortcut('')
#        self.button5.setShortcut('')

        if(self.operate == 'menu'):
            self.menu_flag = not self.menu_flag
            if(self.index == 0):
                self.index = 1
            else:
                self.index = 0
            self.operate = ''

        elif(self.operate == 'up'):
            if(self.menu_flag):
                if(self.index == 1):
                    self.index = 3
                    self.choose_value.setProperty("value", self.brightness)
                elif(self.index == 2):
                    self.index = 1
                    self.choose_value.setProperty("value", self.high_wave)
                elif(self.index == 3):
                    self.index = 2
                    self.choose_value.setProperty("value", self.low_wave)
            elif(self.choose_flag):
                if(self.index == 1):
                    self.high_wave += 5
                    if(self.high_wave>100):
                        self.high_wave = 100
                    self.choose_value.setProperty("value", self.high_wave)
                elif(self.index == 2):
                    self.low_wave += 5
                    if(self.low_wave>100):
                        self.low_wave = 100
                    self.choose_value.setProperty("value", self.low_wave)
                elif(self.index == 3):
                    self.low_wave += 5
                    if(self.brightness>100):
                        self.brightness = 100
                    self.choose_value.setProperty("value", self.brightness)
                else:
                    pass
            self.operate = ''

        elif(self.operate == 'down'):
            if(self.menu_flag):
                if(self.index == 1):
                    self.index = 2
                    self.choose_value.setProperty("value", self.low_wave)
                elif(self.index == 2):
                    self.index = 3
                    self.choose_value.setProperty("value", self.brightness)
                elif(self.index == 3):
                    self.index = 1
                    self.choose_value.setProperty("value", self.high_wave)
            elif(self.choose_flag):
                if(self.index == 1):
                    self.high_wave -= 5
                    if(self.high_wave<0):
                        self.high_wave = 0
                    self.choose_value.setProperty("value", self.high_wave)
                elif(self.index == 2):
                    self.low_wave -= 5
                    if(self.low_wave<0):
                        self.low_wave = 0
                    self.choose_value.setProperty("value", self.low_wave)
                elif(self.index == 3):
                    self.low_wave -= 5
                    if(self.brightness<0):
                        self.brightness = 0
                    self.choose_value.setProperty("value", self.brightness)
                else:
                    pass
            self.operate = ''

        elif(self.operate == 'confirm'):
            self.choose_flag = not self.choose_flag
            self.menu_flag = not self.menu_flag
            if(self.choose_flag):
                self.choose_value.setStyleSheet("QProgressBar{text-align: center;border:5px solid red;font-weight:bold;font-size:36px}QProgressBar::chunk{background-color: rgb(255,127,0);}")
            elif(self.menu_flag):
                self.choose_value.setStyleSheet("QProgressBar{text-align: center;border:5px solid black;font-weight:bold;font-size:36px}QProgressBar::chunk{background-color: rgb(255,127,0);}")
                if(self.index == 1):
                    self.choose_value.setProperty("value", self.high_wave)
                elif(self.index == 2):
                    self.choose_value.setProperty("value", self.low_wave)
                elif(self.index == 3):
                    self.choose_value.setProperty("value", self.brightness)
                else:
                    self.choose_value.setProperty("value", 0)
            self.operate = ''

        else:
            pass

        if(self.menu_flag):
            if(self.index == 1):
                self.button1.setStyleSheet("QPushButton{border-radius: 10%;border: 5px solid red;background: url(/home/pi/aduio/images/filter_high.png) no-repeat cover center;}")
#                self.button1.setShortcut('6')
            elif(self.index == 2):
                self.button2.setStyleSheet("QPushButton{border-radius: 10%;border: 5px solid red;background: url(/home/pi/aduio/images/filter_low.png) no-repeat cover center;}")
#                self.button2.setShortcut('6')
            elif(self.index == 3):
                self.button3.setStyleSheet("QPushButton{border-radius: 10%;border: 5px solid red;background: url(/home/pi/aduio/images/brightness.png) no-repeat cover center;}")
#                self.button3.setShortcut('6')
                #self.choose_value.setStyleSheet("QProgressBar{text-align: center;border:5px solid black;font-weight:bold}QProgressBar::chunk{background-color: rgb(255,127,0);}")
            #break
        #print(self.menu_flag,self.choose_flag)
        time.sleep(0.5)
        #_thread.start_new_thread(self.buttonEvent,())


    def serial(self):       #(0.12s)
        ser = serial.Serial('/dev/ttyAMA0',9600,timeout=0.1)
        count = 0
        while True:
            # 获得接收缓冲区字符
            count = ser.inWaiting()
            if count != 0:
                self.recv = ser.readline().decode()
                #print(self.recv.strip())
            if (self.send_temp != self.send):
                self.send_temp = self.send
                ser.write(str(self.send).encode())
            # 清空接收缓冲区
            ser.flushInput()
            # 必要的软件延时
            time.sleep(0.1)
            #ser.close()
        #_thread.start_new_thread(self.serial,())

    def music(self):
        while True:
            #当传入音量大小以及音量大小与上次不同的时候才重新播放音频
            if(self.recv and int(self.recv) != self.volume):
                self.recv = int(self.recv)
                #将当前音量存储在volume中,用于判断音量是否变化
                self.volume = self.recv
                pygame.mixer.init()
                pygame.mixer.music.load('warning.wav')
                pygame.mixer.music.set_volume(self.recv/100)
                pygame.mixer.music.play()
                #while pygame.mixer.music.get_busy():  # 在音频播放为完成之前不退出程序
                    #pass
            else:
                pass 
        time.sleep(0.1)

    def battery(self):
        while True:
            self.power = self.data
            #print(self.power)
            if(self.power_temp != self.power):
                self.power_temp = self.power
                self.battery_power.setProperty("value", self.power)
                if(self.power > 80):
                    self.label.setStyleSheet("background-image: url(images/power_100.png);background-repeat: no-repeat;")
                    self.battery_power.setStyleSheet("QProgressBar{border:2px solid gray;}QProgressBar::chunk{background-color: rgb(26,250,41);}")
                elif(self.power > 60 and self.power <= 80):
                    self.label.setStyleSheet("background-image: url(images/power_80.png);background-repeat: no-repeat;")
                    self.battery_power.setStyleSheet("QProgressBar{border:2px solid gray;}QProgressBar::chunk{background-color: rgb(87,180,7);}")
                elif(self.power > 40 and self.power <= 60):
                    self.label.setStyleSheet("background-image: url(images/power_60.png);background-repeat: no-repeat;")
                    self.battery_power.setStyleSheet("QProgressBar{border:2px solid gray;}QProgressBar::chunk{background-color: rgb(223,196,29);}")
                elif(self.power > 20 and self.power <= 40):
                    self.label.setStyleSheet("background-image: url(images/power_40.png);background-repeat: no-repeat;")
                    self.battery_power.setStyleSheet("QProgressBar{border:2px solid gray;}QProgressBar::chunk{background-color: rgb(244,234,41);}")
                elif(self.power <= 20):
                    self.label.setStyleSheet("background-image: url(images/power_20.png);background-repeat: no-repeat;")
                    self.battery_power.setStyleSheet("QProgressBar{border:2px solid gray;}QProgressBar::chunk{background-color: rgb(254,67,42);}")
                else:
                    pass
            else:
                pass
            #break
            time.sleep(0.1)
        #_thread.start_new_thread(self.battery,())


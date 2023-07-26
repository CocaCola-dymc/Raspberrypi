# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import random
import time
import _thread
import serial
import json
import pygame
import matplotlib.animation as animation

class Ui_Sound_Detection(object):
    def setupUi(self, Sound_Detection):
        Sound_Detection.setObjectName("Sound_Detection")
        Sound_Detection.resize(1080, 720)
        Sound_Detection.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Sound_Detection)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1080, 720))
        self.widget.setStyleSheet("background-color: white;")
        self.widget.setObjectName("widget")

        self.set_matplotlib()
        self.probe = 0
        self.probe_temp = 0
        self.recv = ''
        self.volume = 0

        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 613, 671, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.erji1 = QtWidgets.QLabel(self.layoutWidget)
        self.erji1.setText("")
        self.erji1.setPixmap(QtGui.QPixmap("images/erji.jpg"))
        self.erji1.setObjectName("erji1")
        self.horizontalLayout.addWidget(self.erji1, 0, QtCore.Qt.AlignLeft)
        self.erji2 = QtWidgets.QLabel(self.layoutWidget)
        self.erji2.setMinimumSize(QtCore.QSize(75, 52))
        self.erji2.setText("")
        self.erji2.setPixmap(QtGui.QPixmap("images/erji.jpg"))
        self.erji2.setObjectName("erji2")
        self.horizontalLayout.addWidget(self.erji2)
        self.erji3 = QtWidgets.QLabel(self.layoutWidget)
        self.erji3.setText("")
        self.erji3.setPixmap(QtGui.QPixmap("images/erji.jpg"))
        self.erji3.setObjectName("erji3")
        self.horizontalLayout.addWidget(self.erji3)
        self.erji4 = QtWidgets.QLabel(self.layoutWidget)
        self.erji4.setText("")
        self.erji4.setPixmap(QtGui.QPixmap("images/erji.jpg"))
        self.erji4.setObjectName("erji4")
        self.horizontalLayout.addWidget(self.erji4)
        self.erji5 = QtWidgets.QLabel(self.layoutWidget)
        self.erji5.setText("")
        self.erji5.setPixmap(QtGui.QPixmap("images/erji.jpg"))
        self.erji5.setObjectName("erji5")
        self.horizontalLayout.addWidget(self.erji5)
        self.erji6 = QtWidgets.QLabel(self.layoutWidget)
        self.erji6.setText("")
        self.erji6.setPixmap(QtGui.QPixmap("images/erji.jpg"))
        self.erji6.setObjectName("erji6")
        self.horizontalLayout.addWidget(self.erji6)
        self.vertical_line = QtWidgets.QFrame(self.widget)
        self.vertical_line.setGeometry(QtCore.QRect(900, 40, 141, 20))
        self.vertical_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.vertical_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line.setObjectName("vertical_line")
        self.horizontal_line = QtWidgets.QFrame(self.widget)
        self.horizontal_line.setGeometry(QtCore.QRect(870, 90, 20, 471))
        self.horizontal_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.horizontal_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontal_line.setObjectName("horizontal_line")
        self.filter_high = QtWidgets.QPushButton(self.widget)
        self.filter_high.setGeometry(QtCore.QRect(910, 80, 127, 82))
        self.filter_high.setMinimumSize(QtCore.QSize(91, 0))
        self.filter_high.setAutoFillBackground(False)
        self.filter_high.setStyleSheet("border-radius: 10%;\n"
"border: 1px solid black;\n"
"background-image: url(/home/pi/aduio/images/filter_high.png);\n"
"background-repeat: no-repeat;")
        self.filter_high.setText("")
        self.filter_high.setAutoDefault(False)
        self.filter_high.setDefault(False)
        self.filter_high.setFlat(False)
        self.filter_high.setObjectName("filter_high")
        self.filter_low = QtWidgets.QPushButton(self.widget)
        self.filter_low.setGeometry(QtCore.QRect(910, 190, 127, 82))
        self.filter_low.setMinimumSize(QtCore.QSize(91, 0))
        self.filter_low.setStyleSheet("border-radius: 10%;\n"
"border: 1px solid black;\n"
"background-image: url(/home/pi/aduio/images/filter_low.png);\n"
"background-repeat: no-repeat;")
        self.filter_low.setText("")
        self.filter_low.setAutoDefault(False)
        self.filter_low.setDefault(False)
        self.filter_low.setFlat(False)
        self.filter_low.setObjectName("filter_low")
        self.com_probe = QtWidgets.QPushButton(self.widget)
        self.com_probe.setGeometry(QtCore.QRect(910, 300, 127, 82))
        self.com_probe.setMinimumSize(QtCore.QSize(91, 0))
        self.com_probe.setStyleSheet("border-radius: 10%;\n"
"border: 1px solid black;\n"
"background-image: url(/home/pi/aduio/images/com_probe.png);\n"
"background-repeat: no-repeat;")
        self.com_probe.setText("")
        self.com_probe.setAutoDefault(False)
        self.com_probe.setDefault(False)
        self.com_probe.setFlat(False)
        self.com_probe.setObjectName("com_probe")
        self.brightness = QtWidgets.QPushButton(self.widget)
        self.brightness.setGeometry(QtCore.QRect(910, 520, 127, 82))
        self.brightness.setMinimumSize(QtCore.QSize(91, 0))
        self.brightness.setStyleSheet("border-radius: 10%;\n"
"border: 1px solid black;\n"
"background-image: url(/home/pi/aduio/images/brightness.png);\n"
"background-repeat: no-repeat;")
        self.brightness.setText("")
        self.brightness.setAutoDefault(False)
        self.brightness.setDefault(False)
        self.brightness.setFlat(False)
        self.brightness.setObjectName("brightness")
        self.battery_levels = QtWidgets.QPushButton(self.widget)
        self.battery_levels.setGeometry(QtCore.QRect(910, 410, 127, 82))
        self.battery_levels.setMinimumSize(QtCore.QSize(91, 0))
        self.battery_levels.setStyleSheet("border-radius: 10%;\n"
"border: 1px solid black;\n"
"background-image: url(/home/pi/aduio/images/battery_levels.png);\n"
"background-repeat: no-repeat;")
        self.battery_levels.setText("")
        self.battery_levels.setAutoDefault(False)
        self.battery_levels.setDefault(False)
        self.battery_levels.setFlat(False)
        self.battery_levels.setObjectName("battery_levels")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(940, 20, 68, 22))
        self.label.setObjectName("label")

        self.retranslateUi(Sound_Detection)
#        self.filter_high.clicked.connect(Sound_Detection.filter_high1)
        QtCore.QMetaObject.connectSlotsByName(Sound_Detection)

    def retranslateUi(self, Sound_Detection):
        _translate = QtCore.QCoreApplication.translate
        Sound_Detection.setWindowTitle(_translate("Sound_Detection", "Sound_Detection"))
        self.label.setText(_translate("Sound_Detection", "TextLabel"))

    # 嵌入matplotlib方法
    def set_matplotlib(self):
#        # 创建画布
        self.fig = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.fresh_flag = False

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
        _thread.start_new_thread(self.music,())

    #开始绘图
    def plotfig(self):
        while True:
            self.ax.autoscale_view()
            self.ax.cla()       #清空画布
            self.x = ['1', '2', '3', '4', '5', '6']
#            self.y = [0,0,0,0,0,0]
            self.probe = int(self.probe)
            #设置y轴的范围
            self.ax.set_ylim(0,100)

#            if(self.recv):
#                for data in self.recv:
#                    print(data)
#                    self.probe.append(data['probe'])
#                    self.value.append(data['value'])
#                    print(type(self.probe[0]),type(self.value[0]))
#            else:
#                pass

            if(self.probe != 0 and self.probe != self.probe_temp):
                self.probe_temp = self.probe
                self.y = [0,0,0,0,0,0]
                self.erji1.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji2.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji3.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji4.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji5.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji6.setPixmap(QtGui.QPixmap("images/erji.jpg"))

#                if(self.probe == 1):
#                    self.erji1.setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
#                    self.y[self.probe-1] = 10
#                    self.ax.text(self.x[0],self.y[0]+2,self.y[0],ha='center',size=24)
#                elif(self.probe == 2):
#                    self.erji2.setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
#                    self.y[self.probe-1] = 20
#                    self.ax.text(self.x[1],self.y[1]+2,self.y[1],ha='center',size=24)
#                elif(self.probe == 3):
#                    self.erji3.setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
#                    self.y[self.probe-1] = 30
#                    self.ax.text(self.x[2],self.y[2]+2,self.y[2],ha='center',size=24)
#                elif(self.probe == 4):
#                    self.erji4.setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
#                    self.y[self.probe-1] = 40
#                    self.ax.text(self.x[3],self.y[3]+2,self.y[3],ha='center',size=24)
#                elif(self.probe == 5):
#                    self.erji5.setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
#                    self.y[self.probe-1] = 50
#                    self.ax.text(self.x[4],self.y[4]+2,self.y[4],ha='center',size=24)
#                elif(self.probe == 6):
#                    self.erji6.setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
#                    self.y[self.probe-1] = 60
#                    self.ax.text(self.x[5],self.y[5]+2,self.y[5],ha='center',size=24)
#                else:
#                    pass
                for i in range(1,6):
                    if(self.probe == i):
                        self.erji[i].setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
                        self.y[i-1] = 60
                        self.ax.text(self.x[i-1],self.y[i-1]+2,self.y[i-1],ha='center',size=24)

            elif(self.probe == 0):
                self.y = [0,0,0,0,0,0]
                self.erji1.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji2.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji3.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji4.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji5.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji6.setPixmap(QtGui.QPixmap("images/erji.jpg"))

            #生成柱状图
            self.ax.bar(self.x,self.y,color=(1,0.5,0),width=0.6)
            #将数值显示在对应的柱子上
            #第一个x表示在x轴的位置,第一个y表示在y轴的位置,+2表示往上移动一点位置,以免挡住数字，
            #第二个y表示显示的内容,ha='center'表示数字居中，size为数字大小
#            self.ax.text(self.x[self.probe-1],self.y[self.probe-1]+2,self.y[self.probe-1],ha='center',size=24)

            self.fig.canvas.draw()          # 画布重绘 self.figs.canvas
            self.fig.canvas.flush_events()  # 画布刷新 self.figs.canvas
            time.sleep(0.1)
            break
        _thread.start_new_thread(self.plotfig,())

    def keyPressEvent(self, event):
        while True:
#            print("press:" + str(event.key()))
            if(event.key() == Qt.Key_0):
                self.probe = 0
            elif(event.key() == Qt.Key_1):
                self.probe = 1
            elif(event.key() == Qt.Key_2):
                self.probe = 2
            elif(event.key() == Qt.Key_3):
                self.probe = 3
            elif(event.key() == Qt.Key_4):
                self.probe = 4
            elif(event.key() == Qt.Key_5):
                self.probe = 5
            elif(event.key() == Qt.Key_6):
                self.probe = 6
            else:
                pass
            time.sleep(0.1)
            break
            _thread.start_new_thread(self.keyPressEvent,())

    def serial(self):
        ser = serial.Serial('/dev/ttyAMA0',9600,timeout=1)
        count = 0
        while True:
            # 获得接收缓冲区字符
            count = ser.inWaiting()
            if count != 0:
                self.recv = ser.readline().decode()
#                print(self.recv)
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
#                while pygame.mixer.music.get_busy():  # 在音频播放为完成之前不退出程序
#                    pass
            else:
                pass
        time.sleep(0.1)



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
import matplotlib.animation as animation

class Function(object):

    # 嵌入matplotlib方法
    def set_matplotlib(self):
        # 创建画布
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
        _thread.start_new_thread(self.battery,())

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

            if(self.probe != self.probe_temp or self.probe == 0):
                self.probe_temp = self.probe
                self.y = [0,0,0,0,0,0]
                self.erji1.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji2.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji3.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji4.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji5.setPixmap(QtGui.QPixmap("images/erji.jpg"))
                self.erji6.setPixmap(QtGui.QPixmap("images/erji.jpg"))
            else:
                pass

            if(self.probe == 1):
                self.erji1.setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
                self.y[self.probe-1] = 10
                self.ax.text(self.x[0],self.y[0]+2,self.y[0],ha='center',size=24)
            elif(self.probe == 2):
                self.erji2.setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
                self.y[self.probe-1] = 20
                self.ax.text(self.x[1],self.y[1]+2,self.y[1],ha='center',size=24)
            elif(self.probe == 3):
                self.erji3.setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
                self.y[self.probe-1] = 30
                self.ax.text(self.x[2],self.y[2]+2,self.y[2],ha='center',size=24)
            elif(self.probe == 4):
                self.erji4.setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
                self.y[self.probe-1] = 40
                self.ax.text(self.x[3],self.y[3]+2,self.y[3],ha='center',size=24)
            elif(self.probe == 5):
                self.erji5.setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
                self.y[self.probe-1] = 50
                self.ax.text(self.x[4],self.y[4]+2,self.y[4],ha='center',size=24)
            elif(self.probe == 6):
                self.erji6.setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
                self.y[self.probe-1] = 60
                self.ax.text(self.x[5],self.y[5]+2,self.y[5],ha='center',size=24)
            else:
                pass

    #            for i in range(1,7):
    #                if(self.probe == i):
    #                    self.erji[i].setPixmap(QtGui.QPixmap("images/erji_active.jpg"))
    #                    self.y[i-1] = 60
    #                    self.ax.text(self.x[i-1],self.y[i-1]+2,self.y[i-1],ha='center',size=24)

            #生成柱状图
            self.ax.bar(self.x,self.y,color=(1,0.5,0),width=0.6)
            #将数值显示在对应的柱子上
            #第一个x表示在x轴的位置,第一个y表示在y轴的位置,+2表示往上移动一点位置,以免挡住数字，
    #            第二个y表示显示的内容,ha='center'表示数字居中，size为数字大小
    #            self.ax.text(self.x[self.probe-1],self.y[self.probe-1]+2,self.y[self.probe-1],ha='center',size=24)

            self.fig.canvas.draw()          # 画布重绘 self.figs.canvas
            self.fig.canvas.flush_events()  # 画布刷新 self.figs.canvas
            time.sleep(0.1)
            break
        _thread.start_new_thread(self.plotfig,())

    def keyPressEvent(self, event):
        while True:
            print("press:" + str(event.key()))
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

    def battery(self):
        while True:
            while self.power > 0:
                self.power -= 2
                time.sleep(0.5)
                break
            self.progressBar.setProperty("value", self.power)
            if(self.power >20 and self.power <= 100):
                self.label.setStyleSheet("background-image: url(images/power_g.png);background-repeat: no-repeat;")
                self.progressBar.setStyleSheet("QProgressBar{text-align: center;border:2px solid black}QProgressBar::chunk{background-color: rgb(26,250,41);}")
            elif(self.power >10 and self.power <= 20):
                self.label.setStyleSheet("background-image: url(images/power_y.png);background-repeat: no-repeat;")
                self.progressBar.setStyleSheet("QProgressBar{text-align: center;border:2px solid black}QProgressBar::chunk{background-color: rgb(244,234,41);}")
            elif(self.power <= 10):
                self.label.setStyleSheet("background-image: url(images/power_r.png);background-repeat: no-repeat;")
                self.progressBar.setStyleSheet("QProgressBar{text-align: center;border:2px solid black}QProgressBar::chunk{background-color: rgb(254,67,42);}")
            else:
                pass
#            _thread.start_new_thread(self.battery,())

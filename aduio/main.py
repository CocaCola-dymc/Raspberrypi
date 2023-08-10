#This Python file uses the following encoding: utf-8
#python -m PyQt5.uic.pyuic form.ui -o form.py       //.ui -> .py

import sys
import os

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
#from PyQt5.QtChart import *
from form import *  #导入form.py
from function import *


class Sound_Detection(QtWidgets.QWidget,Ui_Sound_Detection,Function):
    def __init__(self):
        super(Sound_Detection, self).__init__()
        self.setupUi(self)
        self.set_matplotlib()
#        start_time = time.time()
#        end_time = time.time()
#        print("程序运行时间：%f 秒" % (end_time - start_time))

        #全局变量
        self.probe = 0
        self.probe_temp = 0
        self.send = 0
        self.send_temp = 0
        self.erji = [0, self.erji1, self.erji2, self.erji3, self.erji4, self.erji5, self.erji6]
        self.recv = ''
        self.volume = 0
        self.power = 0
        self.power_temp = 0
        self.operate = ''
        self.index = 0
        self.data = 0
        self.menu_flag = False
        self.choose_flag = False
        self.high_wave = 0
        self.low_wave = 0
        self.brightness = 0

#    def filter_high(self):
#        while True:
#            self.choose_value.setStyleSheet("QProgressBar{text-align: center;border:5px solid red;font-weight:bold}QProgressBar::chunk{background-color: rgb(255,127,0);}")
#            if(self.operate == 'up'):
#                self.high_wave += 5
#                self.choose_value.setProperty("value", self.high_wave)
#            elif(self.operate == 'down'):
#                self.high_wave -= 5
#                self.choose_value.setProperty("value", self.high_wave)
#        self.power = 40
#            self.operate = ''
#            break

#    def filter_low(self):
#        while True:
#            self.choose_value.setStyleSheet("QProgressBar{text-align: center;border:5px solid red;font-weight:bold}QProgressBar::chunk{background-color: rgb(255,127,0);}")
#            if(self.operate == 'up'):
#                self.low_wave += 5
#                self.choose_value.setProperty("value", self.low_wave)
#            elif(self.operate == 'down'):
#                self.low_wave -= 5
#                self.choose_value.setProperty("value", self.low_wave)
#        self.power = 20
#            self.operate = ''
#            break

#    def com_probe(self):
#        self.power = 40

#    def battery_levels(self):
#        self.power = 20

#    def brightness(self):
#        self.power = 10


if __name__ == "__main__":
    #start_time = time.time()
    app = QApplication([])
    widget = Sound_Detection()
    widget.show()
    #end_time = time.time()
    #print("程序运行时间：%f 秒" % (end_time - start_time))
    sys.exit(app.exec_())


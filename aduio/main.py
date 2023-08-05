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

    def filter_high(self):
        self.power = 50

    def filter_low(self):
        self.power = 20

#    def com_probe(self):
#        self.power = 40

#    def battery_levels(self):
#        self.power = 20

    def brightness(self):
        self.power = 10


if __name__ == "__main__":
    #start_time = time.time()
    app = QApplication([])
    widget = Sound_Detection()
    widget.show()
    #end_time = time.time()
    #print("程序运行时间：%f 秒" % (end_time - start_time))
    sys.exit(app.exec_())


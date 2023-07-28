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

        #全局变量
        self.probe = 0
        self.probe_temp = 0
        self.recv = ''
        self.volume = 0
        self.power = 100
        self.power_temp = 0
        self.direction = ''

    def filter_high1(self):
        self.power = 100

    def filter_low1(self):
        self.power = 80

    def com_probe1(self):
        self.power = 40

    def battery_levels1(self):
        self.power = 20

    def brightness1(self):
        self.power = 10


if __name__ == "__main__":
    app = QApplication([])
    widget = Sound_Detection()
    widget.show()
    sys.exit(app.exec_())

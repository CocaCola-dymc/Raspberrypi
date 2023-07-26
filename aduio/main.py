#This Python file uses the following encoding: utf-8
#python -m PyQt5.uic.pyuic form.ui -o form.py       //.ui -> .py

import sys
import os
from tkinter import *

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
#from PyQt5.QtChart import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import random
import matplotlib.animation as animation
import serial
#from form import Ui_Sound_Detection       #import new create .py file
from form import *  #导入form.py


class Sound_Detection(QtWidgets.QWidget,Ui_Sound_Detection):
    def __init__(self):
        super(Sound_Detection, self).__init__()
#        self.load_ui()
        self.setupUi(self)

#    def filter_high1(self):

#        self.fresh_flag = not self.fresh_flag       #将标志位取反
#        self.label.setText(str(self.s))
#        self.keyPressEvent()
#        self.plotfig()

#    def filter_low1(self):
#        self.label.setText("filter_low")

#    def com_probe1(self):
#        self.label.setText("com_probe")

#    def battery_levels1(self):
#        self.label.setText("battery_levels")

#    def brightness1(self):
#        self.label.setText("brightness")


if __name__ == "__main__":
    app = QApplication([])
    widget = Sound_Detection()
    widget.show()
    sys.exit(app.exec_())

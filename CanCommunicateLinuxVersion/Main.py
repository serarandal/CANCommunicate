# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import PyQt5.QtCore
#import can
import can
from PyQt5 import QtCore, QtGui, QtWidgets
import Utility
import os
#from time import sleep
import RealMainWindow
import PreMadeWindow
import SaveMessageWindow
import PasswordWindow
import ManMadeWindow
import AddNewMessages
import FrequencyWindow


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow2 = QtWidgets.QMainWindow()
    MainWindow3 = QtWidgets.QMainWindow()
    MainWindow4 = QtWidgets.QMainWindow()
    MainWindow5 = QtWidgets.QMainWindow()
    MainWindow6 = QtWidgets.QMainWindow()
    MainWindow7 = QtWidgets.QMainWindow()
    PopupWindow = QtWidgets.QWidget()
    PopupWindow2 = QtWidgets.QWidget()
    PopupWindow3 = QtWidgets.QWidget()
    PopupWindow4 = QtWidgets.QWidget()
    PopupWindow5 = QtWidgets.QWidget()
    PopupWindow6 = QtWidgets.QWidget()
    PopupWindow7 = QtWidgets.QWidget()
    PopupWindow8 = QtWidgets.QWidget()
    ui = RealMainWindow.Ui_MainWindow()
    ui2 = PreMadeWindow.Ui_MainWindow2()
    ui3 = ManMadeWindow.Ui_MainWindow3()
    ui4 = AddNewMessages.Ui_MainWindow4()
    ui5 = SaveMessageWindow.Ui_MainWindow5()
    ui6 = PasswordWindow.Ui_MainWindow6()
    ui7 = PasswordWindow.Popup()
    ui8 = PasswordWindow.Popup2()
    ui9 = FrequencyWindow.Ui_MainWindow7()
    ui10 = FrequencyWindow.Popup3()
    ui11 = FrequencyWindow.Popup4()
    ui12 = SaveMessageWindow.Popup5()
    ui13 = SaveMessageWindow.Popup6()
    ui14 = AddNewMessages.Popup7()
    ui15 = AddNewMessages.Popup8()
    ui.setupUi(MainWindow,MainWindow2,MainWindow3,MainWindow4,MainWindow6,MainWindow7)
    ui2.setupUi(MainWindow2,MainWindow3)
    ui3.setupUi(MainWindow3,MainWindow2,MainWindow5)
    ui4.setupUi(MainWindow4,PopupWindow7,PopupWindow8)
    ui5.setupUi(MainWindow5,ui2,PopupWindow5,PopupWindow6)
    ui6.setupUi(MainWindow6,PopupWindow,PopupWindow2)
    ui7.setupUi(PopupWindow)
    ui8.setupUi(PopupWindow2)
    ui9.setupUi(MainWindow7,PopupWindow3,PopupWindow4)
    ui10.setupUi(PopupWindow3)
    ui11.setupUi(PopupWindow4)
    ui12.setupUi(PopupWindow5)
    ui13.setupUi(PopupWindow6)
    ui14.setupUi(PopupWindow7)
    ui15.setupUi(PopupWindow8)
    MainWindow.show()
    sys.exit(app.exec_())

#TODO
# 1- Fix send message, need two clicks to send it through. -> can.ThreadSafeBus -> my_bus = can.ThreadSafeBus(interface=’socketcan’, channel=’vcan0’) # Need to test it
# 2- Split data in premade send -> Done
# 3- Split last data byte in read.-> Done
# Future Lines
# 1-Add filter to the read display, like only show with x id...
# 2-Translate the error messages to readable text.
# 3-Add a box for each byte -> Choose from both.
# 4-Add better commentary and traces.
# erase the old messages,or save them.
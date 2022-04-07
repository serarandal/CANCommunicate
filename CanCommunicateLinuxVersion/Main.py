#Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#
from PyQt5 import QtCore, QtGui, QtWidgets

import FilterWindow
import RealMainWindow
import PreMadeWindow
import SaveMessageWindow
import PasswordWindow
import ManMadeWindow
import AddNewMessages
import FrequencyWindow
import platform
#import PremadeWindow #TEST2
#import SendWindowManTEST
import Utility

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
    MainWindow8 = QtWidgets.QMainWindow()
   # MainWindow9 = QtWidgets.QMainWindow() #TEST
 #   MainWindow10 = QtWidgets.QMainWindow() #TEST2
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
    ui16 = FilterWindow.Ui_MainWindow8()
    ui.setupUi(MainWindow,MainWindow2,MainWindow3,MainWindow4,MainWindow6,MainWindow7,MainWindow8)
    ui2.setupUi(MainWindow2,MainWindow3)
    ui3.setupUi(MainWindow3,MainWindow2,MainWindow5)
    ui4.setupUi(MainWindow4,PopupWindow7,PopupWindow8,ui2)
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
    ui16.setupUi(MainWindow8)
    if platform.system() != 'Linux': #need the serial number of the usb2can to be able to work in windows
        Utility.findSerialNumberKorlan()
    MainWindow.show()
    sys.exit(app.exec_())

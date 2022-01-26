import PyQt5.QtCore
#import can
from PyQt5 import QtCore, QtGui, QtWidgets

import Utility
import os
import time

class Popup(object):
    def setupUi(self,PopupWindow):
        PopupWindow.setObjectName("Form")
        PopupWindow.resize(400, 300)
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        self.gridLayout = QtWidgets.QGridLayout(PopupWindow)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(PopupWindow)
        self.label.setObjectName("label")
        self.label.setFont(self.Font)
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(PopupWindow)
        QtCore.QMetaObject.connectSlotsByName(PopupWindow)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Popup1"))
        self.label.setText(_translate("Form", "Contraseña Guardada"))

class Popup2(object):
    def setupUi(self,PopupWindow2):
        PopupWindow2.setObjectName("Form")
        PopupWindow2.resize(400, 300)
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        self.gridLayout = QtWidgets.QGridLayout(PopupWindow2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(PopupWindow2)
        self.label.setObjectName("label")
        self.label.setFont(self.Font)
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(PopupWindow2)
        QtCore.QMetaObject.connectSlotsByName(PopupWindow2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Popup2"))
        self.label.setText(_translate("Form", "Fallo al guardar"))

class Ui_MainWindow6(object):
    def setupUi(self, MainWindow6,PopupWindow,PopupWindow2):
        self.Popup = PopupWindow
        self.Popup2 = PopupWindow2
        self.MainWindow6 = MainWindow6
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        MainWindow6.setObjectName("MainWindow6")
        MainWindow6.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow6)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setFont(self.Font)
        self.gridLayout.addWidget(self.plainTextEdit, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setObjectName("pushButton")
        self.pushButton6.clicked.connect(self.b1)
        self.pushButton6.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton6, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        MainWindow6.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow6)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow6.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow6)
        self.statusbar.setObjectName("statusbar")
        MainWindow6.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow6)

    def retranslateUi(self, MainWindow6):
        _translate = QtCore.QCoreApplication.translate
        MainWindow6.setWindowTitle(_translate("MainWindow", "MainWindow6"))
        self.pushButton6.setText(_translate("MainWindow", "AddPassword"))

    def b1(self):
        print("Pushed add new password button:")
        pas=self.plainTextEdit.toPlainText()
        savePass = Utility.setPassword(pas)
        if savePass == True:
            self.Popup.show()
            self.MainWindow6.close()
        else:
            self.Popup2.show()



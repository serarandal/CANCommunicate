#Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#

import PyQt5.QtCore
#import can
from PyQt5 import QtCore, QtGui, QtWidgets
import Utility
import os
#from time import sleep
class Popup7(object): #UI class
    def setupUi(self, PopupWindow7):
        PopupWindow7.setObjectName("Form")
        PopupWindow7.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(PopupWindow7)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(PopupWindow7)
        self.label.setObjectName("label")
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        self.label.setFont(self.Font)
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(PopupWindow7)
        QtCore.QMetaObject.connectSlotsByName(PopupWindow7)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Popup"))
        self.label.setText(_translate("Form", "Nuevos mensajes generados"))

class Popup8(object): #UI class
    def setupUi(self, PopupWindow8):
        PopupWindow8.setObjectName("Form")
        PopupWindow8.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(PopupWindow8)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(PopupWindow8)
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        self.label.setFont(self.Font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(PopupWindow8)
        QtCore.QMetaObject.connectSlotsByName(PopupWindow8)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Popup2"))
        self.label.setText(_translate("Form", "Fallo al guardar,revise permisos y si existe el archivo .xmt"))

class Ui_MainWindow4(object): #UI class
    def setupUi(self, MainWindow4,PopupWindow7,PopupWindow8):
        self.MainWindow4 = MainWindow4
        self.PopupWindow7 = PopupWindow7
        self.PopupWindow8 = PopupWindow8
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        MainWindow4.setObjectName("MainWindow4")
        MainWindow4.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow4)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.text = QtWidgets.QLineEdit(self.centralwidget)
        self.text.setObjectName("text")
        self.text.setFont(self.Font)
        self.gridLayout.addWidget(self.text, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setObjectName("pushButton")
        self.pushButton4.clicked.connect(self.setBrowerPath)
        self.pushButton4.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton4, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.pushButton4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4_2.setObjectName("pushButton_2")
        self.pushButton4_2.clicked.connect(self.addMessages)
        self.pushButton4_2.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton4_2, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        MainWindow4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow4)
        self.statusbar.setObjectName("statusbar")
        MainWindow4.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow4)

    def retranslateUi(self, MainWindow4):
        _translate = QtCore.QCoreApplication.translate
        MainWindow4.setWindowTitle(_translate("MainWindow", "AddMessage"))
        self.text.setText(_translate("MainWindow", ""))
        self.pushButton4.setText(_translate("MainWindow", "Explore"))
        self.pushButton4_2.setText(_translate("MainWindow", "AddMessage"))

    def setBrowerPath(self): #use to pick the path , it opens an explorer window
        try:
            file_path, file_type = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow4, 'open file','./Messages')
            self.text.setText(file_path)
            self.text.selectAll()
            self.text.setFocus()
        except:
            print("Cannot open file browser,try to add rights to this code ")

    def addMessages(self): # use to add new messages based on the file choosed on the explorer
        filepath = self.text.text()
        a = Utility.processCreationNewMessages(filepath)
        if a == True:
            self.PopupWindow7.show()
            self.MainWindow4.close()
        else :
            self.PopupWindow8.show()
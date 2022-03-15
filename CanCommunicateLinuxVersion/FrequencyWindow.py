#Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#

import PyQt5.QtCore
from PyQt5 import QtCore, QtGui, QtWidgets

import Utility

class Popup3(object): #UI class
    def setupUi(self, PopupWindow3):
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        PopupWindow3.setObjectName("Form")
        PopupWindow3.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(PopupWindow3)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(PopupWindow3)
        self.label.setObjectName("label")
        self.label.setFont(self.Font)
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(PopupWindow3)
        QtCore.QMetaObject.connectSlotsByName(PopupWindow3)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Popup1"))
        self.label.setText(_translate("Form", "Frecuencia Guardada"))

class Popup4(object): #UI class
    def setupUi(self, PopupWindow4):
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        PopupWindow4.setObjectName("Form")
        PopupWindow4.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(PopupWindow4)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(PopupWindow4)
        self.label.setObjectName("label")
        self.label.setFont(self.Font)
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(PopupWindow4)
        QtCore.QMetaObject.connectSlotsByName(PopupWindow4)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Popup2"))
        self.label.setText(_translate("Form", "Fallo al guardar"))

class Ui_MainWindow7(object): #UI class
    def setupUi(self, MainWindow7,PopupWindow,PopupWindow2):
        self.Popup = PopupWindow
        self.Popup2 = PopupWindow2
        self.MainWindow7 = MainWindow7
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        MainWindow7.setObjectName("MainWindow7")
        MainWindow7.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow7)
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
        self.pushButton6.clicked.connect(self.saveNewFrequencyButton)
        self.pushButton6.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton6, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        MainWindow7.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow7)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow7.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow7)
        self.statusbar.setObjectName("statusbar")
        MainWindow7.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow7)
        QtCore.QMetaObject.connectSlotsByName(MainWindow7)

    def retranslateUi(self, MainWindow7):
        _translate = QtCore.QCoreApplication.translate
        MainWindow7.setWindowTitle(_translate("MainWindow", "MainWindow7"))
        self.pushButton6.setText(_translate("MainWindow", "Set frecuency"))

    def saveNewFrequencyButton(self):
        print("Pushed save new frequency button:")
        frec=self.plainTextEdit.toPlainText()
        savePass = Utility.setFrequency(frec)
        if savePass == True:
            self.Popup.show()
            self.MainWindow7.close()
        else:
            self.Popup2.show()



import PyQt5.QtCore
#import can
from PyQt5 import QtCore, QtGui, QtWidgets
import Utility
import os
#from time import sleep

class Worker(QtCore.QObject):

    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(str)

    def run(self):
        print("Starting the reading worker gui thread")
        i = 0
        j = 0
        while 1 :
            if i == 700000 :
                msg = Utility.testOneCan()
                i = 0
                if msg == "" or msg == None :
                    if j == 0:
                        self.progress.emit("NoMessages")
                        j=1
                    else:
                        None
                else :
                    self.progress.emit(msg)
                    j = 0
            else :
                i = i+1

        self.finished.emit()


class Ui_MainWindow6(object):
    def setupUi(self, MainWindow6):
        MainWindow6.setObjectName("MainWindow6")
        MainWindow6.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow6)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setObjectName("pushButton")
        self.pushButton6.clicked.connect(self.b1)
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
        Utility.setPassword(pas)

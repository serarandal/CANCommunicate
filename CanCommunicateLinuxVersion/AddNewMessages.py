
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

class Ui_MainWindow4(object):
    def setupUi(self, MainWindow4):
        self.MainWindow4 = MainWindow4
        MainWindow4.setObjectName("MainWindow4")
        MainWindow4.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow4)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.text = QtWidgets.QLineEdit(self.centralwidget)
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setObjectName("pushButton")
        self.pushButton4.clicked.connect(self.setBrowerPath)
        self.gridLayout.addWidget(self.pushButton4, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.pushButton4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4_2.setObjectName("pushButton_2")
        self.pushButton4_2.clicked.connect(self.addMessages)
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

    def setBrowerPath(self):
        file_path, file_type = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow4, 'open file','./Messages')
        self.text.setText(file_path)
        self.text.selectAll()
        self.text.setFocus()

    def addMessages(self):
        filepath = self.text.text()
        Utility.processCreationNewMessages(filepath)

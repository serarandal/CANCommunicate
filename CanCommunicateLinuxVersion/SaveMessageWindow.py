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


class Ui_MainWindow5(object):
    def setupUi(self,MainWindow5):
        MainWindow5.setObjectName("MainWindow5")
        MainWindow5.resize(800,600)
        self.centralwidget = QtWidgets.QWidget(MainWindow5)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20,40,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem,3,2,1,1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit,2,2,1,1)
        self.pushButton5_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5_2.setObjectName("pushButton5_2")
        self.pushButton5_2.clicked.connect(self.b1)
        self.gridLayout.addWidget(self.pushButton5_2,2,3,1,1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        MainWindow5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow5)
        self.menubar.setGeometry(QtCore.QRect(0,0,800,22))
        self.menubar.setObjectName("menubar")
        MainWindow5.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow5)
        self.statusbar.setObjectName("statusbar")
        MainWindow5.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow5)

    def b1(self):
        name=self.lineEdit.text()
        print(name)
        print("Pushed add new message button:")
        Utility.createNewPreMadeMessage(name)

    def retranslateUi(self, MainWindow5):
        _translate = QtCore.QCoreApplication.translate
        MainWindow5.setWindowTitle(_translate("MainWindow5", "CreateNewMessage"))
        self.pushButton5_2.setText(_translate("MainWindow5", "Create"))
        self.label.setText(_translate("MainWindow5", "Add new name to this message"))

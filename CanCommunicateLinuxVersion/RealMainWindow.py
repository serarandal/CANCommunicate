# -*- coding: utf-8 -*-

#Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#

import time
import PyQt5.QtCore
#import can
from PyQt5 import QtCore, QtGui, QtWidgets
import Utility
import os
a = 0

class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(str)
    def run(self):
        print("Starting the reading worker gui thread")
        self.isKilled = False
        j = 0
        z = 0
        t0 = time.perf_counter()
        t1 = time.perf_counter()
        msg2 = ""
        while 1 and self.isKilled==False:
            if t1 - t0 >0.1 :
                msg = Utility.testOneCan()
                t0 = time.perf_counter()
                if msg == "" or msg == None :
                    if j == 0:
                        self.progress.emit("NoMessages")
                        j=1
                    else:
                        None
                elif msg is msg2 :
                    if z == 0:
                        self.progress.emit("NoNewMessages")
                        z=1
                    else:
                        None
                else:
                    msg2 = msg
                    self.progress.emit(msg)
                    j = 0
                    z = 0
            else :
                t1 = time.perf_counter()

        self.finished.emit()

    def stop(self):
        self.isKilled = True

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,MainWindow2,MainWindow3,MainWindow4,MainWindow6,MainWindow7,MainWindow8):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 609)
        self.MainWindow2 = MainWindow2
        self.MainWindow3 = MainWindow3
        self.MainWindow4 = MainWindow4
        self.MainWindow6 = MainWindow6
        self.MainWindow7 = MainWindow7
        self.MainWindow8 = MainWindow8
        self.i = 0
        self.connected = False
        self.model = QtGui.QStandardItemModel()
        self.Font = PyQt5.QtGui.QFont('Arial', 12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.b3)
        self.pushButton_3.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_3, 12, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.b5)
        self.pushButton_5.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.b1)
        self.pushButton.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.b2)
        self.pushButton_2.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_2, 7, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 5, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 10, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 13, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.b8)
        self.pushButton_8.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_8, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Send premade messages"))
        self.pushButton_5.setText(_translate("MainWindow", "Add new messages from PEAK"))
        self.pushButton.setText(_translate("MainWindow", "Connect CAN"))
        self.pushButton_2.setText(_translate("MainWindow", "Read CAN"))
        self.pushButton_6.setText(_translate("MainWindow", "Set new password"))
        self.pushButton_4.setText(_translate("MainWindow", "Send messages manually"))
        self.pushButton_7.setText(_translate("MainWindow", "Set new frequency"))
        self.pushButton_8.setText(_translate("MainWindow", "Filter"))

    def b1(self):
        print("Pushed connect to can button:")
        status = Utility.connectCan()
        it = QtGui.QStandardItem(status)
        self.model.appendRow(it)

    def b2(self):
        global a
        if a == 0:
            a = 1
            print("Pushed reading can button:")
            self.runLongTask()
        else:
            print("Already reading(ManuallyMadeWindow)")
            print("stopping")
            self.stopLongTask()
            a = 0

    def b3(self):
        print("Pushed show premade gui:")
        self.MainWindow2.show()

    def b4(self):
        print("Pushed show manmade gui:")
        self.MainWindow3.show()

    def b5(self):  # wait 10 seconds and close it
        print("Pushed show add new messages gui:")
        self.MainWindow4.show()

    def b6(self):
        print("Pushed show password gui:")
        self.MainWindow6.show()

    def b7(self):
        print("Pushed change frequency gui:")
        self.MainWindow7.show()

    def b8(self):
        print("Pushed filter gui:")
        self.MainWindow8.show()

    def reportProgress(self, n):
        n = str(n)
        it = QtGui.QStandardItem(n)
        if self.i >= 40:
            self.model.removeRows(self.i - 39, 3)
            self.i = 38
            self.model.appendRow(it)
            self.listView.scrollToBottom()
        else:
            self.model.appendRow(it)
            self.listView.scrollToBottom()
            self.i += 1

    def runLongTask(self):
        self.thread = QtCore.QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        self.thread.start()

    def stopLongTask(self):
        print("here")
        self.worker.stop()
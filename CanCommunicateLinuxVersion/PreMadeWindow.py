#Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#

import PyQt5.QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import Utility
import os
import time

a=0

class Worker(QtCore.QObject): # reading thread
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
                msg = Utility.testOneCan()
                t0 = time.perf_counter()
                if msg == "" or msg == None and t1 - t0 > 100:
                    if j == 0:
                        self.progress.emit("NoMessages")
                        j=1
                    else:
                        None
                elif msg is msg2 and t1 - t0 > 100:
                    if z == 0:
                        self.progress.emit("NoNewMessages")
                        z=1
                    else:
                        None
                else:
                    msg2 = msg
                    self.progress.emit(msg)
                    z = 0
                    t1 = time.perf_counter()

        self.finished.emit()

    def stop(self):
        self.isKilled = True

class Ui_MainWindow2(object): #UI class
    def setupUi(self, MainWindow2,MainWindow3):
        self.MainWindow2 = MainWindow2
        self.MainWindow3 = MainWindow3
        self.i = 0
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(800, 600)
        self.model2 = QtGui.QStandardItemModel()
        self.model2_2 = QtGui.QStandardItemModel()
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setObjectName("listView_2")
        #self.listView_2.setViewMode(QtWidgets.QListView.IconMode)
        #self.size=PyQt5.QtCore.QSize(500,500)
        #self.listView_2.setIconSize(self.size)
        self.Font=PyQt5.QtGui.QFont('Arial',16)
        self.Font2=PyQt5.QtGui.QFont('Arial',20)
        self.listView_2.setFont(self.Font2)
        self.listView_2.setModel(self.model2)
        self.listView_2.setAutoScroll(False)
        self.gridLayout.addWidget(self.listView_2, 4, 0, 1, 1)
        self.pushButton2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2_2.setObjectName("pushButton2_2")
        self.pushButton2_2.clicked.connect(self.b1)
        self.gridLayout.addWidget(self.pushButton2_2, 5, 0, 1, 1)
        self.listView2_2 = QtWidgets.QListView(self.centralwidget)
        self.listView2_2.setObjectName("listView")
        self.listView2_2.setModel(self.model2_2)
        self.listView2_2.setFont(self.Font)
        self.listView2_2.setAutoScroll(False)
        self.gridLayout.addWidget(self.listView2_2, 1, 0, 1, 1)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.b3)
        self.gridLayout.addWidget(self.pushButton2, 2, 0, 1, 1)
        self.pushButton2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2_3.setObjectName("pushButton_3")
        self.pushButton2_3.clicked.connect(self.b2)
        self.gridLayout.addWidget(self.pushButton2_3, 0, 0, 1, 1)
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)
        self.addItemsListView()
        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow2"))
        self.pushButton2_2.setText(_translate("MainWindow2", "ChangeMode"))
        self.pushButton2.setText(_translate("MainWindow2", "SendData"))
        self.pushButton2_3.setText(_translate("MainWindow2", "ReadCan"))

    def b1(self):
        print("Pushed change window button:")
        self.MainWindow3.show()
        self.MainWindow2.hide()

    def b2(self):
        global a
        if a == 0:
            a=1
            print("Pushed reading can button:")
            self.pushButton2_3.setStyleSheet("background-color:green")
            self.runLongTask()
        else:
            print("Already reading(ManuallyMadeWindow)")
            print("stopping")
            self.pushButton2_3.setStyleSheet("")
            self.stopLongTask()
            a = 0

    def b3(self):
        finish = False
        i = 2
        print("Send_Premade_Data:")
        index=self.listView_2.selectedIndexes()
        data=Utility.sendPremadeData(index[0].data())
        patata = data.split("/")
        data = patata[1]
        length = len(data)
        while finish == False:
            if i >= length:
                finish = True
            data = data[:i] + " " + data[i:]
            i = i + 3
        if length == 16:
            data = data[:length + 4] + " " + data[length + 4:]
        if length == 14:
            data = data[:length + 3] + " " + data[length + 3:]
        if length == 12:
            data = data[:length + 2] + " " + data[length + 2]
        patata = "Tx" + " 0x" + patata[0] + " " + data
        it = QtGui.QStandardItem(patata)
        self.model2_2.appendRow(it)
        self.listView2_2.scrollToBottom()

    def addItemsListView(self):
        self.model2.clear()
        for file in sorted(os.listdir("Messages")):
            it = QtGui.QStandardItem(file)
            self.model2.appendRow(it)

    def reportProgress(self, n):
        n = str(n)
        it = QtGui.QStandardItem(n)
        if self.i >= 40:
            self.model2_2.removeRows(self.i - 39, 3)
            self.i = 38
            self.model2_2.appendRow(it)
            self.listView2_2.scrollToBottom()
        else:
            self.model2_2.appendRow(it)
            self.listView2_2.scrollToBottom()
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
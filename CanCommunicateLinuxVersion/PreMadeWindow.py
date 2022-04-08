# Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#

import PyQt5.QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import Utility
import os
import time

a = 0


class Worker(QtCore.QObject):  # reading thread
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
        msgStorage = []
        while 1 and self.isKilled == False:
            msg = Utility.testOneCan()
            if msg !="":
                msgStorage.append(msg)
            t1 = time.perf_counter()
            if msg == "" or msg == None and t1 - t0 > 100 and len(msgStorage)==0:
                if j == 0:
                    self.progress.emit("No hay mensajes")
                    j = 1
                else:
                    None
            elif msg is msg2 and t1 - t0 > 100:
                if z == 0:
                    self.progress.emit("No hay nuevos mensajes")
                    z = 1
                else:
                    None
            else:
                msg2 = msg
                if t1 - t0 > 0.0001:
                    t0 = time.perf_counter()
                    self.progress.emit(msgStorage.pop(0))
                    z = 0
                    t1 = time.perf_counter()
                else:
                    None

        self.finished.emit()

    def stop(self):
        self.isKilled = True


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2,MainWindow3):
        MainWindow2.setObjectName("MainWindow")
        MainWindow2.resize(800, 600)
        self.MainWindow2 = MainWindow2
        self.MainWindow3 = MainWindow3
        self.status = False
        self.i = 0
        self.model2 = QtGui.QStandardItemModel()
        self.model2_2 = QtGui.QStandardItemModel()
        self.model2_3 = QtGui.QStandardItemModel()
        self.Font = PyQt5.QtGui.QFont('Arial', 16)
        self.Font2 = PyQt5.QtGui.QFont('Arial', 20)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.splitter, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setMinimumSize(QtCore.QSize(200, 200))
        self.listView.setMaximumSize(QtCore.QSize(950, 16777215))
        self.listView.setObjectName("listView")
        self.listView.setFont(self.Font)
        self.listView.setModel(self.model2_2)
        self.listView.setAutoScroll(False)
        self.horizontalLayout.addWidget(self.listView)
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setMinimumSize(QtCore.QSize(200, 200))
        self.listView_2.setMaximumSize(QtCore.QSize(950, 16777215))
        self.listView_2.setObjectName("listView_2")
        self.listView_2.setFont(self.Font)
        self.listView_2.setModel(self.model2_3)
        self.listView_2.setAutoScroll(False)
        self.horizontalLayout.addWidget(self.listView_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(2000, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.b3)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.listView_3 = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_3.sizePolicy().hasHeightForWidth())
        self.listView_3.setSizePolicy(sizePolicy)
        self.listView_3.setMinimumSize(QtCore.QSize(200, 200))
        self.listView_3.setMaximumSize(QtCore.QSize(1920, 350))
        self.listView_3.setObjectName("listView_3")
        self.listView_3.setFont(self.Font2)
        self.listView_3.setModel(self.model2)
        self.listView_3.setAutoScroll(False)
        self.verticalLayout.addWidget(self.listView_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(2000, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.b1)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.b2)
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)
        self.addItemsListView()
        self.setStatus(False)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Recibidos"))
        self.label_2.setText(_translate("MainWindow", "Enviados"))
        self.pushButton_2.setText(_translate("MainWindow", "Enviar mensaje"))
        self.pushButton_3.setText(_translate("MainWindow", "Cambiar a modo manual"))
        self.pushButton.setText(_translate("MainWindow", "Leer CAN"))


    def setStatus(self,status):
        self.status = status

    def b1(self):
        print("Pushed change window button:")
        self.MainWindow3.show()
        self.MainWindow2.hide()

    def b2(self):
        global a
        if a == 0:
            a = 1
            print("Pushed reading can button:")
            if self.status != True:
                self.pushButton.setStyleSheet("background-color: yellow")
                patata = "No esta conectado el usb2can, o falta pulsar el boton de conectar"
                it = QtGui.QStandardItem(patata)
                self.model2_2.appendRow(it)
                a = 0
            else:
                self.pushButton.setStyleSheet("background-color:green")
                self.runLongTask()
        else:
            print("Already reading(RealMainWindow)")
            print("stopping")
            self.pushButton.setStyleSheet("")
            self.stopLongTask()
            a = 0

    def b3(self):
        finish = False
        i = 2
        print("Send_Premade_Data:")
        index=self.listView_3.selectedIndexes()
        data=Utility.sendPremadeData(index[0].data())
        patata = data.split("/")
        data = patata[1]
        length = len(data)
        try:
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
            self.model2_3.appendRow(it)
            self.listView_2.scrollToBottom()
        except:
            print("Error in message data format, check again")

    def addItemsListView(self):
        self.model2.clear()
        for file in sorted(os.listdir("Messages")):
            it = QtGui.QStandardItem(file)
            self.model2.appendRow(it)

    def reportProgress(self, n):
        n = str(n)
        Utility.logWriting(n)
        it = QtGui.QStandardItem(n)
        if self.i >= 40:
            self.model2_2.removeRows(self.i - 39, 3)
            self.i = 38
            self.model2_2.appendRow(it)
            self.listView.scrollToBottom()
        else:
            self.model2_2.appendRow(it)
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
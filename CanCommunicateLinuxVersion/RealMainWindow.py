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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,MainWindow2,MainWindow3,MainWindow4,MainWindow6):
        self.MainWindow2 = MainWindow2
        self.MainWindow3 = MainWindow3
        self.MainWindow4 = MainWindow4
        self.MainWindow6 = MainWindow6
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.connected = False
        self.model = QtGui.QStandardItemModel()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.listView.setModel(self.model)
        self.listView.setAutoScroll(True)
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.b3)
        self.gridLayout.addWidget(self.pushButton_3, 10, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.b5)
        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.b2)
        self.gridLayout.addWidget(self.pushButton_2, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.b1)
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.b6)
        self.gridLayout.addWidget(self.pushButton_6, 3, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.b4)
        self.gridLayout.addWidget(self.pushButton_4, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 11, 0, 1, 1)
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
        self.pushButton_2.setText(_translate("MainWindow", "ReadCan"))
        self.pushButton.setText(_translate("MainWindow", "ConnectCan"))
        self.pushButton_3.setText(_translate("MainWindow", "SendPreMadeMessage"))
        self.pushButton_4.setText(_translate("MainWindow", "SendManMessage"))
        self.pushButton_5.setText(_translate("MainWindow","AddMessages"))
        self.pushButton_6.setText(_translate("MainWindow", "SetPassword"))

    def b1(self):
        print("Pushed connect to can button:")
        status = Utility.connectCan("500000")
        it = QtGui.QStandardItem(status)
        self.model.appendRow(it)
    def b2(self):
        print("Pushed reading can button:")
        self.runLongTask()

    def b3(self):
        print("Pushed show premade gui:")
        self.MainWindow2.show()
    def b4(self):
        print("Pushed show manmade gui:")
        self.MainWindow3.show()

    def b5(self): #wait 10 seconds and close it
        print("Pushed show add new messages gui:")
        self.MainWindow4.show()

    def b6(self):
        print("Pushed show password gui:")
        self.MainWindow6.show()

    def reportProgress(self,n):
        n = str(n)
        it = QtGui.QStandardItem(n)
        self.model.appendRow(it)
        self.listView.scrollToBottom()
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
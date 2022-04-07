# Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#

import time
import PyQt5.QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import Utility

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
        while 1 and self.isKilled == False:
            msg = Utility.testOneCan()
            t0 = time.perf_counter()
            if msg == "" or msg == None and t1 - t0 > 100:
                if j == 0:
                    self.progress.emit("NoMessages")
                    j = 1
                else:
                    None
            elif msg is msg2 and t1 - t0 > 100:
                if z == 0:
                    self.progress.emit("NoNewMessages")
                    z = 1
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,MainWindow2,MainWindow3,MainWindow4,MainWindow6,MainWindow7,MainWindow8):
        self.MainWindow2 = MainWindow2
        self.MainWindow3 = MainWindow3
        self.MainWindow4 = MainWindow4
        self.MainWindow6 = MainWindow6
        self.MainWindow7 = MainWindow7
        self.MainWindow8 = MainWindow8
        # self.MainWindow9 = MainWindow9 # TEST
        #self.MainWindow10 = MainWindow10 # TEST2
        self.i = 0
        self.connected = False
        self.model = QtGui.QStandardItemModel()
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.newmessagesWindowButton)
        self.pushButton_3.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_3, 10, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setFont(self.Font)
        self.pushButton_4.clicked.connect(self.filterWindowButton)
        self.gridLayout.addWidget(self.pushButton_4, 8, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.readingCanButton)
        self.pushButton_8.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_8, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.connectCanButton)
        self.pushButton_5.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.passwordWindowButton)
        self.pushButton_7.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.manmadeWindowButton)
        self.pushButton.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.listView.setModel(self.model)
        self.listView.setFont(self.Font)
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.premadeWindowButton)
        self.pushButton_2.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.frequencyWindowButton)
        self.pushButton_6.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_6, 4, 0, 1, 1)
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
        self.pushButton_3.setText(_translate("MainWindow", "Add new messages from PEAK"))
        self.pushButton_4.setText(_translate("MainWindow", "Filter"))
        self.pushButton_8.setText(_translate("MainWindow", "Read CAN"))
        self.pushButton_5.setText(_translate("MainWindow", "Connect to CAN"))
        self.pushButton_7.setText(_translate("MainWindow", "Set password"))
        self.pushButton.setText(_translate("MainWindow", "Send messages manually window"))
        self.pushButton_2.setText(_translate("MainWindow", "Send premade messages window"))
        self.pushButton_6.setText(_translate("MainWindow", "Set frequency"))


    def connectCanButton(self):
        print("Pushed connect to can button:")
        status = Utility.connectCan()
        it = QtGui.QStandardItem(status)
        self.model.appendRow(it)
        self.pushButton_5.setStyleSheet("background-color: green")

    def readingCanButton(self):#it executes the reading thread
        global a
        if a == 0:
            a = 1
            print("Pushed reading can button:")
            self.pushButton_8.setStyleSheet("background-color:green")
            #open file for log
            self.runLongTask()
        else:
            print("Already reading(RealMainWindow)")
            print("stopping")
            self.pushButton_8.setStyleSheet("")
            #close file for log
            self.stopLongTask()
            a = 0

    def premadeWindowButton(self): #Premadewindow
        print("Pushed show premade gui:")
        self.MainWindow2.show()


    def manmadeWindowButton(self): #Manmadewindow
        print("Pushed show manmade gui:")
        self.MainWindow3.show()
        #self.MainWindow9.show()

    def newmessagesWindowButton(self):  # New messages window
        print("Pushed show add new messages gui:")
        self.MainWindow4.show()

    def passwordWindowButton(self): #Password gui
        print("Pushed show password gui:")
        self.MainWindow6.show()

    def frequencyWindowButton(self): #Frequency gui
        print("Pushed change frequency gui:")
        self.MainWindow7.show()

    def filterWindowButton(self): #Filter gui
        print("Pushed filter gui:")
        self.MainWindow8.show()

    def reportProgress(self, n): #use to print the reading thread into the list view
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

    def runLongTask(self): #use to execute the reading thread
        self.thread = QtCore.QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        self.thread.start()

    def stopLongTask(self): #use to stop the reading thread
        print("here")
        self.worker.stop()

#Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#

import PyQt5.QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import Utility
import time

a = 0


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


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3,MainWindow2,MainWindow5):
        self.id = "a"
        self.data = "0"
        self.i = 0
        self.MainWindow3 = MainWindow3
        self.MainWindow2 = MainWindow2
        self.MainWindow5 = MainWindow5
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        self.model3 = QtGui.QStandardItemModel()
        MainWindow3.setObjectName("MainWindow")
        MainWindow3.resize(669, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setFont(self.Font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(20, 20))
        self.textEdit.setMaximumSize(QtCore.QSize(400, 50))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 8, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.changetoPremadeWindowButton)
        self.pushButton_4.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_4, 9, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setFont(self.Font)
        self.gridLayout.addWidget(self.label, 7, 3, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setFont(self.Font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMinimumSize(QtCore.QSize(20, 20))
        self.textEdit_2.setMaximumSize(QtCore.QSize(200, 50))
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 8, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.setIdDataButton)
        self.gridLayout.addWidget(self.pushButton, 8, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(self.Font)
        self.gridLayout.addWidget(self.label_2, 7, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.saveMessageButton)
        self.gridLayout.addWidget(self.pushButton_2, 9, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.sendMessageButton)
        self.gridLayout.addWidget(self.pushButton_3, 6, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.clicked.connect(self.readingCanButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_5.setMaximumSize(QtCore.QSize(10000, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 2, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.listView.setModel(self.model3)
        self.listView.setAutoScroll(False)
        self.listView.setFont(self.Font)
        self.gridLayout.addWidget(self.listView, 5, 2, 1, 1)
        self.listView2 = QtWidgets.QListView(self.centralwidget)
        self.listView2.setObjectName("listView")
        self.gridLayout.addWidget(self.listView2, 5, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(self.Font)
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(self.Font)
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        MainWindow3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 22))
        self.menubar.setObjectName("menubar")
        MainWindow3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow3)
        self.statusbar.setObjectName("statusbar")
        MainWindow3.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow", "ManMessages"))
        self.pushButton_4.setText(_translate("MainWindow", "ChangeMode"))
        self.label.setText(_translate("MainWindow", "Data please put it in like:22 22 22 with an space between bytes"))
        self.pushButton.setText(_translate("MainWindow", "SetIdData"))
        self.label_2.setText(_translate("MainWindow", "ID"))
        self.pushButton_2.setText(_translate("MainWindow", "SaveMessage"))
        self.pushButton_3.setText(_translate("MainWindow", "SendMessage"))
        self.pushButton_5.setText(_translate("MainWindow", "ReadCan"))
        self.label_3.setText(_translate("MainWindow", "Read"))
        self.label_4.setText(_translate("MainWindow", "Write"))

    def changetoPremadeWindowButton(self):
        print("Pushed change window button:")
        self.MainWindow2.show()
        self.MainWindow3.hide()

    def setIdDataButton(self):
        print("Pushed button to set id and data:")
        self.id = self.textEdit.toPlainText()
        self.data = self.textEdit_2.toPlainText()
        Utility.processManData(self.id, self.data)

    def readingCanButton(self):
        global a
        if a == 0:
            a = 1
            print("Pushed reading can button:")
            self.pushButton_5.setStyleSheet("background-color:green")
            self.runLongTask()
        else:
            print("Already reading(ManuallyMadeWindow)")
            print("stopping")
            self.pushButton_5.setStyleSheet("")
            self.stopLongTask()
            a = 0

    def sendMessageButton(self):
        print("Pushed send message button:")
        patata = self.id
        patata = "Tx" + " 0x" + patata + " " + self.data
        it = QtGui.QStandardItem(patata)
        self.model3.appendRow(it)
        self.listView.scrollToBottom()
        Utility.sendData()

    def saveMessageButton(self):
        print("Pushed show save message gui:")
        self.MainWindow5.show()

    def b6(self):
        print("Pushed Change Mode Data")

    def reportProgress(self, n):  # use to print the reading thread into the list view
        n = str(n)
        it = QtGui.QStandardItem(n)
        if self.i >= 40:
            self.model3.removeRows(self.i - 39, 3)
            self.i = 38
            self.model3.appendRow(it)
            self.listView.scrollToBottom()
        else:
            self.model3.appendRow(it)
            self.listView.scrollToBottom()
            self.i += 1

    def runLongTask(self):  # use to execute the reading thread
        self.thread = QtCore.QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        self.thread.start()

    def stopLongTask(self):  # use to stop the reading thread
        print("here")
        self.worker.stop()

#Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#

import PyQt5.QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import Utility
import time

a = 0

class Worker(QtCore.QObject): #reading thread class
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

class Ui_MainWindow3(object): #UI class
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
        MainWindow3.resize(1382, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.readingCanButton)
        self.pushButton_4.setFont(self.Font)
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.listView.setModel(self.model3)
        self.listView.setAutoScroll(True)
        self.listView.setFont(self.Font)
        self.verticalLayout_3.addWidget(self.listView)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sendMessageButton)
        self.pushButton.setFont(self.Font)
        self.verticalLayout_3.addWidget(self.pushButton)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.saveMessageButton)
        self.pushButton_5.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_5, 1, 5, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.setFont(self.Font)
        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setFont(self.Font)
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(50, 50))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setFont(self.Font)
        self.gridLayout.addWidget(self.plainTextEdit, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(self.Font)
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.setIdDataButton)
        self.pushButton_2.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.b6)
        self.pushButton_6.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_6, 2, 4, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.changetoPremadeWindowButton)
        self.pushButton_3.setFont(self.Font)
        self.verticalLayout_3.addWidget(self.pushButton_3)
        MainWindow3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1382, 22))
        self.menubar.setObjectName("menubar")
        MainWindow3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow3)
        self.statusbar.setObjectName("statusbar")
        MainWindow3.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow", "MainWindow3"))
        self.pushButton_4.setText(_translate("MainWindow", "Read Can"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton_5.setText(_translate("MainWindow", "Save as new message"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "DATA (put the bytes with a blank space in between ej:\"82 82 82\")"))
        self.pushButton_2.setText(_translate("MainWindow", "Set ID and DATA"))
        self.pushButton_6.setText(_translate("MainWindow", "Change Mode Data"))
        self.pushButton_3.setText(_translate("MainWindow", "Change Mode"))

    def changetoPremadeWindowButton(self):
        print("Pushed change window button:")
        self.MainWindow2.show()
        self.MainWindow3.hide()


    def setIdDataButton(self):
        print("Pushed button to set id and data:")
        self.id = self.plainTextEdit.toPlainText()
        self.data = self.plainTextEdit_2.toPlainText()
        Utility.processManData(self.id, self.data)

    def readingCanButton(self):
        global a
        if a == 0:
            a=1
            print("Pushed reading can button:")
            self.runLongTask()
        else:
            print("Already reading(ManuallyMadeWindow)")
            print("stopping")
            self.stopLongTask()
            a=0

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

    def reportProgress(self, n):# use to print the reading thread into the list view
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

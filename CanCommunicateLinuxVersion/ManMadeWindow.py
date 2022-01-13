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


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3,MainWindow2,MainWindow5):
        self.MainWindow3 = MainWindow3
        self.MainWindow2 = MainWindow2
        self.MainWindow5 = MainWindow5
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(1382, 726)
        self.id = "a"
        self.data = "0"
        self.model3 = QtGui.QStandardItemModel()
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton3_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton3_4.sizePolicy().hasHeightForWidth())
        self.pushButton3_4.setSizePolicy(sizePolicy)
        self.pushButton3_4.setObjectName("pushButton_4")
        self.pushButton3_4.clicked.connect(self.b4)
        self.verticalLayout_3.addWidget(self.pushButton3_4)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.listView.setModel(self.model3)
        self.listView.setAutoScroll(True)
        self.verticalLayout_3.addWidget(self.listView)
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton3.sizePolicy().hasHeightForWidth())
        self.pushButton3.setSizePolicy(sizePolicy)
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.clicked.connect(self.b1)
        self.verticalLayout_3.addWidget(self.pushButton3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 6, 1, 1)
        self.pushButton3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3_2.setObjectName("pushButton_2")
        self.pushButton3_2.clicked.connect(self.b2)
        self.gridLayout.addWidget(self.pushButton3_2, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(50, 50))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 2, 1, 1)
        self.pushButton3_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3_5.setObjectName("pushButton_5")
        self.pushButton3_5.clicked.connect(self.b5)
        self.gridLayout.addWidget(self.pushButton3_5, 1, 5, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.pushButton3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3_3.setObjectName("pushButton_3")
        self.pushButton3_3.clicked.connect(self.b3)
        self.verticalLayout_3.addWidget(self.pushButton3_3)
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
        MainWindow3.setWindowTitle(_translate("MainWindow3", "MainWindow3"))
        self.pushButton3_4.setText(_translate("MainWindow3", "ReadCan"))
        self.pushButton3.setText(_translate("MainWindow3", "SendData"))
        self.pushButton3_2.setText(_translate("MainWindow3", "SetId_Data"))
        self.pushButton3_3.setText(_translate("MainWindow3", "ChangeMode"))
        self.pushButton3_5.setText(_translate("MainWindow3","SaveMessage"))

    def b3(self):
        print("Pushed change window button:")
        self.MainWindow2.show()
        self.MainWindow3.hide()

    def b2(self):
        print("Pushed button to set id and data:")
        self.id = self.plainTextEdit.toPlainText()
        self.data = self.plainTextEdit_2.toPlainText()
        Utility.processManData(self.id, self.data)

    def b4(self):
        print("Pushed reading can button:")
        self.runLongTask()

    def b1(self):
        print("Pushed send message button:")
        patata = self.id
        patata = "Tx" + " 0x" + patata + " " + self.data
        it = QtGui.QStandardItem(patata)
        self.model3.appendRow(it)
        self.listView.scrollToBottom()
        Utility.sendData()

    def b5(self):
        print("Pushed show save message gui:")
        self.MainWindow5.show()

    def reportProgress(self, n):
        it = QtGui.QStandardItem(n)
        self.model3.appendRow(it)
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



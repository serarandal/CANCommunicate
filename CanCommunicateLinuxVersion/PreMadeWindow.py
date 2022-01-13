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


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2,MainWindow3):
        self.MainWindow2 = MainWindow2
        self.MainWindow3 = MainWindow3
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
        self.listView_2.setViewMode(QtWidgets.QListView.IconMode)
        self.size=PyQt5.QtCore.QSize(500,500)
        self.listView_2.setIconSize(self.size)
        self.Font=PyQt5.QtGui.QFont('Arial',12)
        self.listView_2.setFont(self.Font)
        self.listView_2.setModel(self.model2)
        self.listView_2.setAutoScroll(True)
        self.gridLayout.addWidget(self.listView_2, 4, 0, 1, 1)
        self.pushButton2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2_2.setObjectName("pushButton2_2")
        self.pushButton2_2.clicked.connect(self.b1)
        self.gridLayout.addWidget(self.pushButton2_2, 5, 0, 1, 1)
        self.listView2_2 = QtWidgets.QListView(self.centralwidget)
        self.listView2_2.setObjectName("listView")
        self.listView2_2.setModel(self.model2_2)
        self.listView2_2.setAutoScroll(True)
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
        print("Pushed reading can button:")
        self.runLongTask()
    def b3(self):
        print("Send_Premade_Data:")
        index=self.listView_2.selectedIndexes()
        data=Utility.sendPremadeData(index[0].data())
        patata = data.split("/")
        patata = "Tx" + " 0x" + patata[0] + " " + patata[1]
        it = QtGui.QStandardItem(patata)
        self.model2_2.appendRow(it)
        self.listView2_2.scrollToBottom()

    def addItemsListView(self):
        icon = QtGui.QIcon("icon.png")
        for file in sorted(os.listdir("Messages")):
            it = QtGui.QStandardItem(icon,file)
            self.model2.appendRow(it)
    def reportProgress(self,n):
        it = QtGui.QStandardItem(n)
        self.model2_2.appendRow(it)
        self.listView2_2.scrollToBottom()
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
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import can
from PyQt5 import QtCore, QtGui, QtWidgets
import Utility
from time import sleep

class Worker(QtCore.QObject):

    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(str)

    def run(self):
        print("hola")
        while 1 :
            sleep(1)
            msg=Utility.readOneCan()
            self.progress.emit(msg)
        self.finished.emit()


class Ui_MainWindow4(object):
    def setupUi(self, MainWindow4):
        MainWindow4.setObjectName("MainWindow4")
        MainWindow4.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow4)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton4, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.pushButton4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton4_2, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        MainWindow4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow4)
        self.statusbar.setObjectName("statusbar")
        MainWindow4.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow4)

    def retranslateUi(self, MainWindow4):
        _translate = QtCore.QCoreApplication.translate
        MainWindow4.setWindowTitle(_translate("MainWindow", "AddMessage"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton4.setText(_translate("MainWindow", "Explore"))
        self.pushButton4_2.setText(_translate("MainWindow", "AddMessage"))

class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow")
        MainWindow3.resize(800, 600)
        self.id = "a"
        self.data = "0"
        self.model3 = QtGui.QStandardItemModel()
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton3_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton3.sizePolicy().hasHeightForWidth())
        self.pushButton3.setSizePolicy(sizePolicy)
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.clicked.connect(self.b1)
        self.verticalLayout_3.addWidget(self.pushButton3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.pushButton3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3_2.setObjectName("pushButton_2")
        self.pushButton3_2.clicked.connect(self.b2)
        self.gridLayout.addWidget(self.pushButton3_2, 0, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.pushButton3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3_3.setObjectName("pushButton_3")
        self.pushButton3_3.clicked.connect(self.b3)
        self.verticalLayout_3.addWidget(self.pushButton3_3)
        MainWindow3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
    def b3(self):
        MainWindow2.show()
        MainWindow3.hide()
    def b2(self):
        self.id = self.plainTextEdit.toPlainText()
        self.data = self.plainTextEdit_2.toPlainText()
        Utility.setId_Data(int(self.id),self.data)
    def b4(self):
        self.runLongTask()
    def b1(self):
        patata = self.id
        patata = "Tx"+ " "+ patata +" " + self.data
        it = QtGui.QStandardItem(patata)
        self.model3.appendRow(it)
        self.listView.scrollToBottom()
        Utility.sendData()
        print("ohohohohohoho feliz navidad")
    def reportProgress(self,n):
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

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
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
        with open('Messages/Mensajes CAN_CANADAD_TENSION.xmt','r',encoding='iso-8859-1') as f:
            content=f.readlines()

        print(content[11])

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow2"))
        self.pushButton2_2.setText(_translate("MainWindow2", "ChangeMode"))
        self.pushButton2.setText(_translate("MainWindow2", "SendData"))
        self.pushButton2_3.setText(_translate("MainWindow2", "ReadCan"))
    def b1(self):
        MainWindow3.show()
        MainWindow2.hide()
    def b2(self):
        self.runLongTask()
    def b3(self):
        print("Send_Premade_Data")
        #TODO send data from list view
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.model = QtGui.QStandardItemModel()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.listView.setModel(self.model)
        self.listView.setAutoScroll(True)
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.b3)
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.b5)
        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.b2)
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.b1)
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.b4)
        self.gridLayout.addWidget(self.pushButton_4, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 9, 0, 1, 1)
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

    def b1(self):
        print("Pulsado boton 1:")
        status = Utility.connectCan("500000")
        it = QtGui.QStandardItem(status)
        self.model.appendRow(it)
    def b2(self):
        print("Pulsado boton 2:")
        self.runLongTask()
        #msg = Utility.readOneCan()
        #msg = Utility.processMessage(msg)
        #it = QtGui.QStandardItem(msg)
        #self.model.appendRow(it)
    def b3(self):
        print("Pulsado boton 3:")
        MainWindow2.show()
    def b4(self):
        print("Pulsado boton 4:")
        MainWindow3.show()
    def b5(self):
        print("Pulsado boton 5:")
        MainWindow4.show()
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow2 = QtWidgets.QMainWindow()
    MainWindow3 = QtWidgets.QMainWindow()
    MainWindow4 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui2 = Ui_MainWindow2()
    ui3 = Ui_MainWindow3()
    ui4 = Ui_MainWindow4()
    ui.setupUi(MainWindow)
    ui2.setupUi(MainWindow2)
    ui3.setupUi(MainWindow3)
    ui4.setupUi(MainWindow4)
    MainWindow.show()
    sys.exit(app.exec_())


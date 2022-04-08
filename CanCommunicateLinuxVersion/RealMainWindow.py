# Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#

import time
import PyQt5.QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import Utility
from time import sleep
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,MainWindow2,MainWindow3,MainWindow4,MainWindow6,MainWindow7,MainWindow8,ui2,ui3,ui16):
        self.MainWindow2 = MainWindow2
        self.MainWindow3 = MainWindow3
        self.MainWindow4 = MainWindow4
        self.MainWindow6 = MainWindow6
        self.MainWindow7 = MainWindow7
        self.MainWindow8 = MainWindow8
        self.ui2 = ui2
        self.ui3 = ui3
        self.ui16 = ui16
        self.i = 0
        self.connected = False
        self.status = False
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
        self.pushButton_3.setText(_translate("MainWindow", "Añadir mensajes del PEAK"))
        self.pushButton_4.setText(_translate("MainWindow", "Filtro"))
        self.pushButton_8.setText(_translate("MainWindow", "Leer CAN"))
        self.pushButton_5.setText(_translate("MainWindow", "Conectar al CAN"))
        self.pushButton_7.setText(_translate("MainWindow", "Poner nueva contraseña"))
        self.pushButton.setText(_translate("MainWindow", "ventana de envio de mensajes manuales"))
        self.pushButton_2.setText(_translate("MainWindow", "ventana de envio de mensajes ya creados"))
        self.pushButton_6.setText(_translate("MainWindow", "poner nueva frecuencia"))


    def connectCanButton(self):
        print("Pushed connect to can button:")
        self.status = Utility.connectCan()
        self.ui2.setStatus(self.status)
        self.ui3.setStatus(self.status)
        self.ui16.setStatus(self.status)
        if self.status == True:
            it = "Conectado al bus CAN"
        else:
            it = "Error intentando conectar al bus CAN, intente de nuevo con el usb2can conectado"
        it = QtGui.QStandardItem(it)
        self.model.appendRow(it)
        if self.status == True:
            self.pushButton_5.setStyleSheet("background-color: green")
        else:
            self.pushButton_5.setStyleSheet("background-color: yellow")
    def readingCanButton(self):#it executes the reading thread
        global a
        if a == 0:
            a = 1
            print("Pushed reading can button:")
            if self.status != True:
                self.pushButton_8.setStyleSheet("background-color: yellow")
                patata = "No esta conectado el usb2can, o falta pulsar el boton de conectar"
                it = QtGui.QStandardItem(patata)
                self.model.appendRow(it)
                a = 0
            else:
                self.pushButton_8.setStyleSheet("background-color:green")
                self.runLongTask()
        else:
            print("Already reading(RealMainWindow)")
            print("stopping")
            self.pushButton_8.setStyleSheet("")
            self.stopLongTask()
            a = 0

    def premadeWindowButton(self): #Premadewindow
        print("Pushed show premade gui:")
        self.MainWindow2.show()


    def manmadeWindowButton(self): #Manmadewindow
        print("Pushed show manmade gui:")
        self.MainWindow3.show()

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
        Utility.logWriting(n)
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

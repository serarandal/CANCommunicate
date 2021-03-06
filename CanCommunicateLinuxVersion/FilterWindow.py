#Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import Utility

a = 0
b = ""
d = ""
c = ""
y = 0
b2Pressed = False
deviceName = "Not in devices.txt"

class Worker(QtCore.QObject): #Reading thread class
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(str)

    def run(self):
        global a
        global b
        global c
        print("Starting the reading worker gui thread")
        self.isKilled = False
        j = 0
        z = 0
        x = 0
        t0 = time.perf_counter()
        t1 = time.perf_counter()
        msg2 = ""
        while 1 and self.isKilled == False:
            if t1 - t0 > 0.1:
                msg = Utility.testTwoCan()
                t0 = time.perf_counter()
                if msg == "" or msg == None:
                    if j == 0:
                        self.progress.emit("No hay mensajes de esa fuente")
                        j = 1
                    else:
                        None
                elif msg is msg2:
                    if z == 0:
                        self.progress.emit("no hay nuevos mensajes de esa fuente")
                        z = 1
                    else:
                        None
                else:
                    msg2 = msg
                    msgsplited = msg.split("/")
                    msgid = int(msgsplited[0], 16)
                    if msgid == int(c, 16):
                        self.progress.emit(msg)
                        j = 0
                        z = 0
                    elif x == 0:
                        self.progress.emit("No hay mensajes de esa fuente")
                        x = 1
                    else:
                        None
            else:
                t1 = time.perf_counter()

        self.finished.emit()

    def stop(self):
        self.isKilled = True

class Ui_MainWindow8(object):
    def setupUi(self, MainWindow8,Dialog):
        self.Dialog = Dialog
        MainWindow8.setObjectName("MainWindow")
        MainWindow8.resize(800, 600)
        self.Font = PyQt5.QtGui.QFont('Arial', 14)
        self.i = 0
        self.model = QtGui.QStandardItemModel()
        self.centralwidget = QtWidgets.QWidget(MainWindow8)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(self.Font)
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.startFilterButton)
        self.pushButton.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.listView.setModel(self.model)
        self.gridLayout.addWidget(self.listView, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setFont(self.Font)
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(20, 20))
        self.textEdit.setMaximumSize(QtCore.QSize(200, 50))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(self.Font)
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFont(self.Font)
        self.pushButton_2.clicked.connect(self.addDataTranslationButton)
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_config = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_config.setObjectName("pushButton_config")
        self.pushButton_config.clicked.connect(self.configWindow)
        self.pushButton_config.setFont(self.Font)
        self.gridLayout.addWidget(self.pushButton_config, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow8.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow8)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow8.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow8)
        self.statusbar.setObjectName("statusbar")
        MainWindow8.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow8)
        QtCore.QMetaObject.connectSlotsByName(MainWindow8)

    def retranslateUi(self, MainWindow8):
        _translate = QtCore.QCoreApplication.translate
        MainWindow8.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Datos"))
        self.pushButton.setText(_translate("MainWindow", "Filtrar por id sin traducir"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.pushButton_2.setText(_translate("MainWindow", "Cambiar a modo traducir el dato"))
        self.pushButton_config.setText(_translate("MainWindow", "Config"))


    def setStatus(self,status):
        self.status = status

    def startFilterButton(self):
        global b
        global a
        global d
        global c
        global deviceName
        b = self.textEdit.toPlainText()
        c = b  # this is needed bc you change b into integer below
        if d == b:
            alreadyopen = 1
            if b == "000":
                b = 0
            elif b == "00":
                b = 0
            elif b == "0":
                b = 0
            else:
                try:
                    b = int(b, 16)
                except:
                    print("id vacio, intentalo de nuevo")
        else:
            d = c  # c is nedded instead of b.
            alreadyopen = 0
        if alreadyopen == 0:
            try:
                with open("devices.txt") as f:
                    content = f.readlines()
            except:
                print("Cannot open devices.txt, make sure it is created and you have reading rights")
            for item in content:
                stritem = str(item)
                stritem = stritem.split("/")
                strdi2 = stritem[0].split(" ")
                if strdi2[1] == b:
                    if strdi2[0] != "" and strdi2[0] != None:
                        deviceName = strdi2[0]
                    else:
                        deviceName = "Not in devices.txt"
        else:
            alreadyopen = 1
        if a == 0:
            a = 1
            print("Pushed reading can button:")
            self.pushButton.setStyleSheet("background-color:green")
            self.runLongTask()
        else:
            print("Already reading(ManuallyMadeWindow)")
            print("stopping")
            self.pushButton.setStyleSheet("")
            self.stopLongTask()
            a = 0

    def addDataTranslationButton(self): #with this, you change the ui printing hex to real data
        global b2Pressed
        global y
        print("Pressed b2")
        if y == 0:
            b2Pressed = True
            y = 1
        else:
            b2Pressed = False
            y = 0
            n = str("Se para la traduci??n de datos")
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


    def reportProgress(self, n): #use to print the reading thread into the list view
        global deviceName
        global b2Pressed
        if n == "NoMessagesFromThatSource" or n == "NoNewMessagesFromThatSource":
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
        elif b2Pressed == False:
            n = str(n)
            g = n.split("/")
            n = deviceName + "               " + g[1] + "                     " + g[2]
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
        else:
            if deviceName == "Not in devices.txt" or deviceName == None or deviceName == "":
                x = "Not in devices.txt"
            else:
                if deviceName != "steeringSensor":
                    deviceName = "everythingElse"
                x = Utility.filterDevices(deviceName, n)
                Utility.logWriting(x)
            it = QtGui.QStandardItem(x)
            if self.i >= 40:
                self.model.removeRows(self.i - 39, 3)
                self.i = 38
                self.model.appendRow(it)
                self.listView.scrollToBottom()
            else:
                self.model.appendRow(it)
                self.listView.scrollToBottom()
                self.i += 1


    def configWindow(self):
        self.Dialog.show()


    def runLongTask(self):#use to execute the reading thread
        self.thread = QtCore.QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        self.thread.start()

    def stopLongTask(self):#use to stop the reading thread
        print("here")
        n = "Se para la lectura"
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
        self.worker.stop()
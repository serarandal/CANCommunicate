from ctypes import *
#self.pushButton.clicked.connect(self.b1)
#self.plainTextEdit.toPlainText()
mydll = cdll.LoadLibrary("C:\\usb2can.dll")

def connectCan(serialNumber):
    mydll.canalOpen(serialNumber, 500)

def canGetStatus():
     return mydll.CanalGetStatus()

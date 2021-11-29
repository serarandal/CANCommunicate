from ctypes import *
from datetime import datetime

class CANALMSG(Structure):
    _fields_ = [("flags",c_ulong),("obid",c_ulong),("id",c_ulong),("count",c_char),("data",c_char_p*8),("timestamp",c_ulong)]
#self.pushButton.clicked.connect(self.b1)
#self.plainTextEdit.toPlainText()
mydll = cdll.LoadLibrary("C:\\usb2can.dll")

def connectCan(serialNumber):
    mydll.canalOpen(serialNumber, 500)

def canGetStatus():
     return mydll.CanalGetStatus()

def canSendMessage(id,count,data):
    msg=CANALMSG()
    msg.flags = '1000000000000000000000000000000'
    msg.id = id
    msg.count = count
    for x in data:
        msg.data[x] = data[x]
    msg.timestamp = time()

    return mydll.CanalSend(0,msg)

def time():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    print(timestamp)
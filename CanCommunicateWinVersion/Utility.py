from ctypes import *
from datetime import datetime
import can


#self.pushButton.clicked.connect(self.b1)
#self.plainTextEdit.toPlainText()
bus = can.interface.Bus(bustype='usb2can', channel='can0', bitrate=500000)

def canGetStatus():
    return bus.state
def canSendMessage(id,count,data):
    return 0
def canGetMessage():
    return 0

def time():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    print(timestamp)
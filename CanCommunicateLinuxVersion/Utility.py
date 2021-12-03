# This is a sample Python script.
import can
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import subprocess as sp

msg = can.Message()

def readCan():
    global bus
    for msg in bus:
        print(msg.data)

def readOneCan():
    global bus
    msg = bus.recv()
    return processMessage(msg)

def connectCan(frequency):
    global bus
    output = sp.getoutput("echo password | sudo -S ip link set can0 up type can bitrate "+frequency+" loopback on")
    output2 = sp.getoutput("echo password | sudo -S ip link set up can0")
    bustype = 'socketcan'
    can_interface = 'can0'
    bus = can.interface.Bus(can_interface, bustype=bustype)
    return output +"\n"+  output2

def setId_Data(id,data):
    global msg

    data=bytearray.fromhex(data)
    print(data)
    msg = can.Message(arbitration_id=id,
                      data=data,
                      is_extended_id=0)
def sendData():
    global bus
    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message NOT sent"+bus.state)

def processMessage(msg):
    imagen = "Rx"+" " +str(hex(msg.arbitration_id))
    imagen = imagen +" "+ msg.data.hex()
    imagen = imagen +" "+ str(msg.timestamp)
    return imagen


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

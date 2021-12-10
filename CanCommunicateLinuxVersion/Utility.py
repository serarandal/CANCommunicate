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


def processCreationNewMessages(filepath):
    with open(filepath, 'r', encoding='iso-8859-1') as f:
        content = f.readlines()
    print(content[11])
    for i in range(0, 11):
        content.pop(0)

    for x in range(len(content)):
        a = content[x].split(";")
        name=a[1]
        name = name.replace(" ","_")
        name = name[1:]
        name = name[:-1]
        name = name+".txt"
        sp.getoutput("touch "+name)
        b = a[0].split()
        id = b[0][:-1]
        data = b [4][:-1] +" "+b[5][:-1]+" "+b[6][:-1]+" "+b[7][:-1]+" "+b[8][:-1]+" "+b[9][:-1]+" "+b[10][:-1]+" "+b[11][:-1]+" "
        sp.getoutput("echo "+id+" "+data+" > "+name)
        sp.getoutput("mv *.txt Messages")

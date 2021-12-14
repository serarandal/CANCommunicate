# This is a sample Python script.
import can
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import subprocess as sp

msg = can.Message()
idG = ""
dataG = ""

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
    output = sp.getoutput("echo Sergio | sudo -S ip link set can0 up type can bitrate "+frequency+" loopback off")
    output2 = sp.getoutput("echo Sergio | sudo -S ip link set up can0")
    bustype = 'socketcan'
    can_interface = 'can0'
    bus = can.interface.Bus(can_interface, bustype=bustype)
    return output +"\n"+  output2

def setId_Data(id,data):
    global msg

    print(data) #arbitration_id hex del id -> 0x608 #data=[]cada hex en su correspondiente int
    msg = can.Message(arbitration_id=int(id,16),
                      data=data,
                      is_extended_id=False)
def sendData():
    global bus
    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message NOT sent"+bus.state)

def processMessage(msg):
    finish = False
    i=2
    imagen = "Rx"+" " +str(hex(msg.arbitration_id))
    data = msg.data.hex()
    length=len(data)
    while finish == False:
        if i >= length :
            finish = True
        data = data[:i]+" "+data[i:]
        i = i+3
    imagen = imagen + " " + data
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
        try:
            name=a[1]
            name = name.replace(" ", "_")
            name = name[1:]
            name = name[:-1]
            name = name + ".txt"
        except IndexError:
            name = "noname.txt"
        sp.getoutput("touch "+name)
        b = a[0].split()
        id = b[0][:-1]
        data = b [4][:-1] +" "+b[5][:-1]+" "+b[6][:-1]+" "+b[7][:-1]+" "+b[8][:-1]+" "+b[9][:-1]+" "+b[10][:-1]+" "+b[11][:-1]+" "
        sp.getoutput("echo "+id+" "+data+" > "+name)
        sp.getoutput("mv *.txt Messages")


def sendPremadeData(filename):
    dataF = []
    with open("Messages/"+filename, 'r', encoding='iso-8859-1') as f:
        content = f.readline()
        print(content)
    b = content.split()
    id = b[0]
    data = b[1]+ b[2] +  b[3] +  b[4] + b[5] + b[6] +b[7] +b[8]
    print(data)
    b.pop(0)
    for i in range(len(b)):
        dataF.append(int(b[i],16))
    setId_Data(id,dataF)
    sendData()

def processManData(id,data):
    global idG
    global dataG
    idG = id
    dataG = data

    dataF = []
    print(id)
    b = data.split()
    length = len(b)
    for i in range(length):
        dataF.append(int(b[i],16))
    setId_Data(id,dataF)

def createNewPreMadeMessage(name):
    global idG
    global dataG

    name = name + ".txt"
    sp.getoutput("echo " + idG + " " + dataG + " > " + name)
    sp.getoutput("mv *.txt Messages")
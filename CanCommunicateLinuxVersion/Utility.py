#Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#
import subprocess

import can
import platform
import subprocess as sp
import threading
import re

msg = can.Message()
msg2 = can.Message()
processedMsg = None
processedMsgFiltered = None
idG = ""
dataG = ""
password = ""
ready = False
sistema = platform.system()
frequency =""
serialNumber =""
import usb2canAbstractionFile
import usb2canInteface


def setPassword(passW): #LW
    global password
    with open("password.txt",'r')as f:
        data = f.read()
    if data == passW :
        return True
    else:
        with open("password.txt",'w') as f:
            f.write(passW)
        password = passW
        return True


def setFrequency(fre): #LW
    global frequency
    if fre == "":
        return False
    else:
        with open("frequency.txt",'r')as f:
            data = f.read()
        if data == fre :
            return True
        else:
            with open("frequency.txt",'w') as f:
                f.write(fre)
            frequency = fre
            return True

def debugReadCan(): #not in use
    global bus
    for msg in bus:
        print(msg.data)

def readOneCan():#not in use
    global bus
    msg = bus.recv()
    return processMessage(msg)

def testOneCan():#Normal reading
    global processedMsg
    return processedMsg

def testTwoCan():#Filter reading
    global processedMsgFiltered
    return processedMsgFiltered

def connectCan():#LW
    global bus
    global password
    global frequency

    if sistema =='Linux':
        try:
            with open("password.txt") as f:
                password = f.read()
        except:
            print("Cannot open password.txt, make sure it is created and you have reading rights")
    try:
        with open("frequency.txt") as f:
            frequency = f.read()
    except:
        print("Cannot open frequency.txt, make sure it is created and you have reading rights")
    if sistema == 'Linux':
       try:
            output = sp.getoutput("echo "+password+" | sudo -S ip link set can0 up type can bitrate "+frequency+" loopback off") #if you need to debug just put on instead
            output2 = sp.getoutput("echo "+password+" | sudo -S ip link set up can0")
            bustype = 'socketcan'
            can_interface = 'can0'
            bus = can.ThreadSafeBus(can_interface,bustype=bustype)
       except:
           print("No usb2can connected")
    else:
        try:
            bus = usb2canInteface.Usb2canBus(channel=serialNumber,dll="./usb2can.dll")
            print(bus.state)
        except:
            print("No usb2can connected")
    try:
        initThreads()
    except:
        print("Error threads")
    if sistema == 'Linux':
        return output +"\n"+  output2
    else:
        return "intentado conectar al korlan"

def setId_Data(id,data): #LW
    global msg

    print(data) #arbitration_id hex of the id -> 0x608
    try :
        msg = can.Message(arbitration_id=int(id,16),
                    data=data,
                    is_extended_id=False)
    except:
        print("The id cannot be \"\" or the data cannot be \"\"")

def sendData():#LW
    global bus
    try:
        if sistema == 'Linux':
            bus.send(msg)
            print("Message sent on {}".format(bus.channel_info))
        else:
            try:
                bus.send(msg)
                print(bus.state)
            except can.CanError:
                print("Trying to write to a readonly bus?")
    except can.CanError:
        print("Message NOT sent"+bus.state)

def findSerialNumberKorlan():
    global serialNumber
    try:
        output2 = sp.getoutput("wmic path CIM_LogicalDevice where \"Description like 'USB%'\" get DeviceID")
        pa=output2.split("\\")
        serialNumber = pa[2]
        print(serialNumber)
    except:
        print("no usb2can device connected")
def processMessage(msg):#LW
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


def processCreationNewMessages(filepath):#LW
    try:
        with open(filepath, 'r', encoding='iso-8859-1') as f:
            content = f.readlines()
    except:
        print("No messages inside")
        return False
    print("creating new messages")
    for i in range(0, 11):
        content.pop(0)

    for x in range(len(content)):
        a = content[x].split(";")
        try:
            name=a[1]
            name = name.replace(" ", "_")
            name = name[1:]
            name = name[:-1]
            name = name + "M.txt"
        except IndexError:
            name = "nonameM.txt"
        if sistema != 'Linux':
            sp.getoutput("tipe null >> "+name)
        else:
            sp.getoutput("touch "+name)
        b = a[0].split()
        id = b[0][:-1]
        data = b [4][:-1] +" "+b[5][:-1]+" "+b[6][:-1]+" "+b[7][:-1]+" "+b[8][:-1]+" "+b[9][:-1]+" "+b[10][:-1]+" "+b[11][:-1]+" "
        if sistema != 'Linux':
            sp.getoutput("Echo "+id+" "+data+" > "+name)
        else:
            sp.getoutput("echo "+id+" "+data+" > "+name)
        if sistema != 'Linux':
            sp.getoutput("move *M.txt Messages")
        else:
            sp.getoutput("mv *M.txt Messages")
    return True

def sendPremadeData(filename):#LW
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
    sData=id+"/"+data
    setId_Data(id,dataF)
    sendData()
    return sData

def processManData(id,data):#LW
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

def createNewPreMadeMessage(name):#LW
    global idG
    global dataG

    name = name + "M.txt"
    if sistema != 'Linux':
        sp.getoutput("Echo " + idG + " " + dataG + " > " + name)
        a = sp.getoutput("move *M.txt Messages")
    else:
        sp.getoutput("echo " + idG + " " + dataG + " > " + name)
        a=sp.getoutput("mv *M.txt Messages")
    if a == "" or platform.system() != 'Linux':
        return True
    else:
        print(a)
        return False

def waiter_thread(event):#LW
    global msg
    global processedMsg
    global processedMsgFiltered
    print("Starting the reading worker real thread")
    while True:
        msg = bus.recv()
        processedMsg = processMessage(msg)
        processedMsgFiltered = processedMsgFilter(msg)

def processThreadInfo():#doesn't work with threads, but usefull enough to save
    global msg2
    global msg
    if msg == msg2:
        return "NoNewMessages"
    elif msg !=None:
        msg2 = msg
        return processMessage(msg)
    else:
        return "NoMessages"

def initThreads():#LW
    stop_event = threading.Event()
    w = threading.Thread(target=waiter_thread, args=[stop_event])
    w.setDaemon(True)
    w.start()

def processedMsgFilter(msg):#LW
    finish = False
    i = 2
    imagen = str(hex(msg.arbitration_id))
    data = msg.data.hex()
    length = len(data)
    while finish == False:
        if i >= length:
            finish = True
        data = data[:i] + " " + data[i:]
        i = i + 3
    imagen = imagen + "/" + data
    imagen = imagen + " /" + str(msg.timestamp)
    return imagen


def filterDevices(deviceName,mesg):#LW
    switcher = {
        "steeringSensor": steeringSensor(mesg),
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve
    }
    # Get the function from switcher dictionary
    return switcher.get(deviceName, lambda: "Invalid month")

def steeringSensor(mesg):
    id = 0x305
    dataF =""
    dataTemp = 0x0
    patata = 0
    p = re.compile('[e-f]+')
    p2 = re.compile('[b-d]+')
    x = mesg.split("/")
    data = x[1].split(" ")
    timestamp = x[2]
    m = p.match(data[0])
    j = p2.match(data[0])
    for i in range(0,2):
        if m :#if it is 0xFsomething or 0xEsomething, we have to make FF minus that data and that *0.13
            if i == 0:
                dataTemp = data[i]
            else:
                dataF = dataTemp+data[i]
            patata = 1
        elif j:
            None
        else:
            dataF = dataF + data[i]
            patata = 0
        #process the data and translate it
    if patata == 1:
        dataF = str(round((0xFFFF-int(dataF,16))*0.13,2))
    else:
        dataF = round(int(dataF,16)*0.13,2)
    if patata == 1:
        n = "steeringSensor"+"              -"+str(dataF)+"º               "+timestamp
    else:
        n = "steeringSensor"+"               "+str(dataF)+"º               "+timestamp
    return n


def two():
    return "February"

def three():
    return "March"

def four():
    return "April"

def five():
    return "May"

def six():
    return "June"

def seven():
    return "July"

def eight():
    return "August"

def nine():
    return "September"

def ten():
    return "October"

def eleven():
    return "November"

def twelve():
    return "December"
import can
import platform
import subprocess as sp
import threading


msg = can.Message()
msg2 = can.Message()
processedMsg = None
idG = ""
dataG = ""
password = ""
ready = False
sistema = platform.system()
frequency =""

def setPassword(passW):
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


def setFrequency(fre):
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

def debugReadCan():
    global bus
    for msg in bus:
        print(msg.data)

def readOneCan():
    global bus
    msg = bus.recv()
    return processMessage(msg)

def testOneCan():
    global bus
    global processedMsg
    return processedMsg

def connectCan():
    global bus
    global password
    global frequency
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
            output = sp.getoutput("echo "+password+" | sudo -S ip link set can0 up type can bitrate "+frequency+" loopback on")
            output2 = sp.getoutput("echo "+password+" | sudo -S ip link set up can0")
            bustype = 'socketcan'
            can_interface = 'can0'
            bus = can.interface.Bus(can_interface, bustype=bustype)
       except:
           print("No usb2can connected")
    else:
        try:
            output = sp.getoutput("echo " + password + " | sudo -S ip link set can0 up type can bitrate " + frequency + " loopback off")
            output2 = sp.getoutput("echo " + password + " | sudo -S ip link set up can0")
            bustype = 'usb2can'
            can_interface = 'can0'
            bus = can.interface.Bus(can_interface, bustype=bustype)
        except:
            print("No usb2can connected")

    try:
        initThreads()
    except:
        print("Error threads")
    return output +"\n"+  output2

def setId_Data(id,data):
    global msg

    print(data) #arbitration_id hex del id -> 0x608 #data=[]cada hex en su correspondiente int
    try :
        msg = can.Message(arbitration_id=int(id,16),
                      data=data,
                      is_extended_id=False)
    except:
        print("The id cannot be \"\" or the data cannot be \"\"")

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
    try:
        with open(filepath, 'r', encoding='iso-8859-1') as f:
            content = f.readlines()
    except:
        print("No messages inside")
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
        sp.getoutput("touch "+name)
        b = a[0].split()
        id = b[0][:-1]
        data = b [4][:-1] +" "+b[5][:-1]+" "+b[6][:-1]+" "+b[7][:-1]+" "+b[8][:-1]+" "+b[9][:-1]+" "+b[10][:-1]+" "+b[11][:-1]+" "
        sp.getoutput("echo "+id+" "+data+" > "+name)
        sp.getoutput("mv *M.txt Messages")


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
    sData=id+"/"+data
    setId_Data(id,dataF)
    sendData()
    return sData

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

    name = name + "M.txt"
    sp.getoutput("echo " + idG + " " + dataG + " > " + name)
    a=sp.getoutput("mv *M.txt Messages")
    if a == "":
        return True
    else:
        print(a)
        return False

def waiter_thread(event):
    global msg
    global processedMsg
    print("Starting the reading worker real thread")
    while True:
        msg = bus.recv()
        processedMsg = processMessage(msg)

def processThreadInfo():#need to test
    global msg2
    global msg
    if msg == msg2:
        return "NoNewMessages"
    elif msg !=None:
        msg2 = msg
        return processMessage(msg)
    else:
        return "NoMessages"

def initThreads():
    stop_event = threading.Event()
#    continue_event = threading.Event()
    w = threading.Thread(target=waiter_thread, args=[stop_event])
#    u = threading.Thread(target=unflagger_thread, args=[stop_event, continue_event])
    w.setDaemon(True)
#    u.setDaemon(True)
    w.start()
#    u.start()

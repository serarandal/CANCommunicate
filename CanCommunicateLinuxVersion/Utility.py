import can
import platform
import subprocess as sp
import threading


msg = can.Message()
processedMsg = ""
idG = ""
dataG = ""
password = ""
ready = False
sistema = platform.system()

def setPassword(passW):
    global password
    with open("password.txt",'r')as f:
        data = f.read()
    if data == passW :
        None
    else:
        with open("password.txt",'w') as f:
            f.write(passW)
        password = passW

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

def connectCan(frequency):
    global bus
    global password
    with open("password.txt") as f:
        password = f.read()
    if sistema == 'Linux':
        output = sp.getoutput("echo "+password+" | sudo -S ip link set can0 up type can bitrate "+frequency+" loopback on")
        output2 = sp.getoutput("echo "+password+" | sudo -S ip link set up can0")
        bustype = 'socketcan'
        can_interface = 'can0'
        bus = can.interface.Bus(can_interface, bustype=bustype)
    else:
        output = sp.getoutput("echo " + password + " | sudo -S ip link set can0 up type can bitrate " + frequency + " loopback off")
        output2 = sp.getoutput("echo " + password + " | sudo -S ip link set up can0")
        bustype = 'usb2can'
        can_interface = 'can0'
        bus = can.interface.Bus(can_interface, bustype=bustype)
    initThreads()
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

    name = name + ".txt"
    sp.getoutput("echo " + idG + " " + dataG + " > " + name)
    sp.getoutput("mv *.txt Messages") # new to add a filter here

def pushThread():
    global ready
    global msg
    stop_event = threading.Event()
    f = threading.Thread(target=flagger_thread, args=[stop_event])
    f.setDaemon(True)
    f.start()
    if ready == True :
        ready = False
        return processMessage(msg)

def flagger_thread(event):
    event.set()
    ready = True
def waiter_thread(event):
    global msg
    global processedMsg
    print("Starting the reading worker real thread")
    while True:
        msg = bus.recv()
        processedMsg = processMessage(msg)
        #event2.set()
#def unflagger_thread(event,event2):
#    global ready
#    ready = True
#    if event2.wait():
#        event.clear()
#        event2.clear()
def initThreads():
    stop_event = threading.Event()
#    continue_event = threading.Event()
    w = threading.Thread(target=waiter_thread, args=[stop_event])
#    u = threading.Thread(target=unflagger_thread, args=[stop_event, continue_event])
    w.setDaemon(True)
#    u.setDaemon(True)
    w.start()
#    u.start()

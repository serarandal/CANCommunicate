# This is a sample Python script.
import can
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import subprocess as sp


def readCan():
    bustype = 'socketcan'
    can_interface = 'can0'
    bus = can.interface.Bus(can_interface, bustype=bustype)
    for msg in bus:
        print(msg.data)

def connectCan(frequency):

    output = sp.getoutput("echo password | sudo -S ip link set can0 up type can bitrate "+frequency)
    output2 = sp.getoutput("echo password | sudo -S ip link set up can0")
    return output +"\n"+  output2



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

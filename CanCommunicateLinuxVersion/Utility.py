# This is a sample Python script.
import can
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def readCan():
    bustype = 'socketcan'
    can_interface = 'can0'
    bus = can.interface.Bus(can_interface, bustype=bustype)
    for msg in bus:
        print(msg.data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

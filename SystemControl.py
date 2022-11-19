"""
file containing SystemControl
"""
from lift import *
from Motor import *
from sensorCamera import *
from workSation import *

class systemControl:
    def __init__(self,robotModel, lift, cameraSensor, Motor,workStation) -> None: #initializer
        self.robotModel = robotModel #self. makes it an attribute
        self.lift = lift
        self.cameraSensor = cameraSensor # _requestNum says pin should be private
        self.Motor = Motor
        self.workStation = workStation
        print("kivaRobot Construction")

    def systemControlCheck(self):
        print("Robot will check system control")

    def stateEntered(self):
        print("System enters State")


    def stateLeft(self):
        print("System Leaves statee")
    
    def codeScanned(self):
        print("sensors scanned barcode or objects")
    
    def sendCommand(self):
        print("send command to move")

    def getDirection(self):
        print("sends request for for directiont to shelf")



 
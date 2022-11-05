"""
This is Lab 1 - Workstation demo class
"""

class Workstation:

    def __init__(self,stationID, employeeName) -> None:
        self.stationID = stationID
        self.employeeName = employeeName


    def sendRequstToRobot(self):
        print("Emmploye sends a request to the robot from the work station")
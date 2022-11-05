"""
file contains parts clas plus its subclasses Scanner Lift Robotsensor Move
"""


class parts:
    def __init__(self) -> None:
        print("Parts constructor") #constructor 

    def checkpartResponse(self): #checkpartResponse class
        print("checks to see if part sent back a response")
    
    def sendRequest(self):
        print("send part request from robot") #sendRequeset class


"""
scanner is a subclass of parts
"""

class scanner(parts):
    def __init__(self) -> None:
        super().__init__()

    def scan(self):
        print("scans item")

    def sendScanResult(self):
        print("send the scan result to the robot")


"""
Lift is a subclass of parts
"""

class lift(parts):
    def __init__(self) -> None:
        super().__init__()

    def raiseLift(self):
        print("lift will be raised to pick the shelf up")

    def lock(self):
        print("once the lift raises and picks up the shelf, it will lock so it does not drop ")


    def lowerLift(self):
        print("lift will lower when it drops off the shelve")


"""
robotSensor is subclass of parts
"""

class robotSensor(parts):
    def __init__(self) -> None:
        super().__init__()

    def sensorRequest(self):
        print("request sensor to return value ")

    def sensorActivated(self):
        print("Sensor has been activated")

    def generateSensorResponse(self):
        print("Generates Sensor Response and sends it to the robot")

    def detectObject(self):
        print("Sensor detects Object")


"""
Gears is a subclass of parts
"""

class gears(parts):
    def __init__(self) -> None:
        super().__init__()

    def move_forward(self):
        print("robot moves forward")

    def move_backward(self):
        print("robot moves backward")

    def move_left(self):
        print("robot moves left")

    def move_right(self):
        print("robot moves right")

    def move_spin(self):
        print("Robot spins in a 360 defree circle")

    def move_stop(self):
        print("robot stops")





"""
File contains Sensor Camera Class and its sub classes
"""


class sensorCamera:
    def __init__(self,usbPort, objectTrue,objectFalse) -> None:
        self.usbPort = usbPort
        self.objectTrue.objectTrue
        self.objectFalse.objectFalse
        print("sensor camera constructor") #constructor 

    def isOn(self): #Scanner is on 
        print("scanner is on")
        
    
    def isOff(self):
        print("scanner turns off") #sendRequeset class

    def sendScanResult():
        print("send if scan detected an object")

    def scanCode():
        print("sends command to scan code from sublasses")


"""
front Sensor  is a subclass of sensor camera 
"""

class frontSensor(sensorCamera):
    def __init__(self, objectTrue, objectFalse) -> None:
        super().__init__(objectTrue, objectFalse)
  

    def isObject(self):
        print("Send back if scan detected object or not")
        
    def isBarcode(self):
        print("if sensor detecs barcode")

    def detectRoute(self):
        print("sensor read route ID tape on the ground")

    


"""
Lift is a subclass of parts
"""

class groundSensor(sensorCamera):
    def __init__(self,objectTrue, objectFalse) -> None:
        super().__init__(objectTrue, objectFalse)
        

    def detectCode(self):
        print("detects code on the ground")

    def scanBarcode(self):
        print("scans the bar code on the ground ")

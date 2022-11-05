"""
file containing kivaRobot
"""


class kivaRobot:
    def __init__(self,robotID, requestNum) -> None: #initializer
        self.robotID = robotID #self. makes it an attribute
        self.requestNum = requestNum # _requestNum says pin should be private
        print("kivaRobot Construction")

    def Move(self):
        print("Robot will move based on the direction that is told")

    def srequestShelveData(self):
        print("Requests shelf data")

    def setNewLocation(self):
        print("Sets new location")
    
    def initialize_sensor(self):
        print("sensors are initialized")
    
    def requestLiftCommand(self):
        print("Requests Lift Command")

    def request_scanner(self):
        print("sends request for scanner to send data")

    def scanShelve(self):
        print("sends request to scan shelve")

    def init_lift(self):
        print("initializes lift")

    def send_Sensor_result(self):
        print("gets the sensor result")

    
    
    


     
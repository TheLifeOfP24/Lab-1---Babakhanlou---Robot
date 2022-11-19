"""
File contains Motor Class and its sub classes
"""


class Motor:
    def __init__(self, angle, distance) -> None:
        
        self.angle = angle
        self.distance = distance
        print("Motorconstructor") #constructor 
        self.distance = 0
        self.angle = 0

    def Move(self,distance, angle): #Scanner is on 
        print("lets robot know how far and which direction to turn ")
        
    
    def stop(self):
        print("Motor Stops") #sendRequeset class

    def Off():
        print("motor Off")

    def On():
        print("Motor On")


"""
DcMotor sub class of Motor
"""

class DcMotor(Motor):
    def __init__(self, distance, angle) -> None:
        super().__init__(distance, angle)
        self.angle = 0
        self.distance = 0 
  

    def forward(self, distance):
        print("the distance it will move forward")
        
    def backwards(self,distance):
        print("distance it moves back")

    


"""
ServoMoto is a subclass of Motor
"""

class servoMotor(Motor):
    def __init__(self, distance, angle) -> None:
        super().__init__(distance, angle)
        self.angle = 0
        self.angle = 0
        

    def servoRotate(angle):
        print("detects code on the ground")



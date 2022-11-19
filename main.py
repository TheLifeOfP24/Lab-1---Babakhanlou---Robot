
"""Run the code in Main"""

from lift import *
from Motor import *
from sensorCamera import *
from workSation import *
from SystemControl import *



class SystemControl:
  def __init__(self, distance, angle, Motor): #initializes code
    self.distance = distance #constructors
    self.angle = angle
    self.Motor = Motor

  def printname(self):
    print(self.distance, self.angle, self.Motor)

class move(SystemControl):
  pass

x = move("5ft", "90°", "-Move Forwarrd 5 feet\n")
x.printname()

class frontSensor(SystemControl):
  pass

x = frontSensor("5ft", "90°", "-Object detected\n")
x.printname()

class Right(SystemControl):
  pass

x = Right("0ft", "180°", "-Car turned Left\n")
x.printname()

class Forward(SystemControl):
  pass

x = Forward("10ft", "90°", "-Move Forward\n")
x.printname()

class Left(SystemControl):
  pass

x = Left("5ft", "90°", "-Robot turns left\n")
x.printname()

class Stop(SystemControl):
  pass

x = Stop("0ft", "90°", "-Robot has Reached Location")
x.printname()

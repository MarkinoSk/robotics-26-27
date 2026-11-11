import math
import config
from enum import Enum

class TankState(Enum):
    IDLE = 0
    DRIVING = 1
    TURNING = 2




class Tank:
   def __init__(self,robot,wheelL_name,wheelR_name,encoderL_name,encoderR_name,gyro):
      self.wheelL=robot.getDevice(wheelL_name)
      self.wheelR=robot.getDevice(wheelR_name)
      self.wheelL.setPosition(float("inf"))
      self.wheelR.setPosition(float("inf"))
      self.wheelL.setVelocity(0)
      self.wheelR.setVelocity(0)

      self.encoderL=robot.getDevice(encoderL_name)
      self.encoderR=robot.getDevice(encoderR_name)
      self.encoderL.enable(config.TIME_STEP)
      self.encoderR.enable(config.TIME_STEP)

      self.gyro=gyro

      self.tankState=TankState.IDLE

      
      self.targetRRad=0
      self.targetLRad=0
      self.currentRRad=0
      self.currentLRad=0

      self.currentAngle=0
      self.targetAngle=0


   def setHullVelocity(self,velocityL,velocityR):
      self.wheelL.setVelocity(velocityL)
      self.wheelR.setVelocity(velocityR)




   def getEncoderValues(self):
      return self.encoderL.getValue(), self.encoderR.getValue()

   def update(self):
      if self.tankState==TankState.IDLE:
         return
      if self.tankState==TankState.TURNING:
         self.updateTurn()
      if self.tankState==TankState.DRIVING:
         self.updateDrive()

   

   def updateTurn(self):
      error = self.targetAngle - self.gyro.get_angle()
      
      if abs(error) < config.ACCEPTED_ANGLE:
         print("done")
         self.tankState = TankState.IDLE
         self.setHullVelocity(0,0)
         return
      
      speed = config.KP_TURN * error
      print("error: ",error," speed: ",round(speed, 2), end="")
      speed = max(-config.MAX_SPEED, min(config.MAX_SPEED, speed))
      print("   speed: ",round(speed, 2), end="")
      speed = math.copysign(max(abs(speed), config.MIN_TURN_SPEED), speed)
      print("   speed: ",round(speed, 2))

      self.setHullVelocity(speed, -speed) 


   def updateDrive(self):
      self.currentLRad,self.currentRRad=self.getEncoderValues()
      
      errorL=self.targetLRad-self.currentLRad
      errorR=self.targetRRad-self.currentRRad

      if abs(errorL)<config.ACCEPTED_OFFSET and abs(errorR)<config.ACCEPTED_OFFSET:
         self.setHullVelocity(0,0)
         self.tankState=TankState.IDLE
         print("done")
         return
      
      
      velocityL = config.KP_DRIVE * errorL
      velocityL = max(-config.MAX_SPEED, min(config.MAX_SPEED, velocityL))

      velocityR = config.KP_DRIVE * errorR
      velocityR = max(-config.MAX_SPEED, min(config.MAX_SPEED, velocityR))

      self.setHullVelocity(velocityL, velocityR)
         

   def driveTiles(self,tileCount=1):
      print("FWD")
      self.currentLRad=self.getEncoderValues()[0]
      self.currentRRad=self.getEncoderValues()[1]

      self.targetLRad=self.currentLRad+config.TILE_LENGTH_RAD*tileCount
      self.targetRRad=self.currentRRad+config.TILE_LENGTH_RAD*tileCount

      self.tankState=TankState.DRIVING


   def TurnDeg(self,angle):
      self.targetAngle=self.gyro.get_angle()+math.radians(angle)
      self.tankState=TankState.TURNING

   def stateName(self):
      return self.tankState.name
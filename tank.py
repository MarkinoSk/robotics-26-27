import math
import config
from enum import Enum

class TankState(Enum):
    IDLE = 0
    DRIVING = 1
    TURNING = 2




class Tank:
   def __init__(self,robot,wheelL_name,wheelR_name,encoderL_name,encoderR_name,gyro,timestep):
      self.wheelL=robot.getDevice(wheelL_name)
      self.wheelR=robot.getDevice(wheelR_name)
      self.wheelL.setPosition(float("inf"))
      self.wheelR.setPosition(float("inf"))
      self.wheelL.setVelocity(0)
      self.wheelR.setVelocity(0)

      self.encoderL=robot.getDevice(encoderL_name)
      self.encoderR=robot.getDevice(encoderR_name)
      self.encoderL.enable(timestep)
      self.encoderR.enable(timestep)

      self.gyro=gyro

      self.tankState=TankState.IDLE

      
      self.targetRRad=0
      self.targetLRad=0
      self.currentRRad=0
      self.currentLRad=0

      self.currentAngle=0
      self.targetAngle=0


   def setVelocity(self,velocity):
      self.wheelL.setVelocity(velocity)
      self.wheelR.setVelocity(velocity)

   def getEncoderValues(self):
      return self.encoderL.getValue(), self.encoderR.getValue()

   def update(self):
      self.gyro.update()
      
      if self.tankState==TankState.IDLE:
         return
      if self.tankState==TankState.TURNING:
         self.updateTurn()
      if self.tankState==TankState.DRIVING:
         self.updateDrive()

      

   def updateTurn(self):
      error = self.targetAngle - self.gyro.get_angle()
      if abs(error) < config.ACCEPTED_ANGLE:
         self.tankState = TankState.IDLE
         self.setVelocity(0)
         return
      
      speed = config.KP_TURN * error
      speed = max(-config.MAX_SPEED, min(config.MAX_SPEED, speed))
      speed = math.copysign(max(abs(speed), config.MIN_TURN_SPEED), speed)

      self.wheelL.setVelocity(-speed)
      self.wheelR.setVelocity(speed)   


   def updateDrive(self):
      self.currentLRad,self.currentRRad=self.getEncoderValues()
      
      errorL=self.targetLRad-self.currentLRad
      errorR=self.targetRRad-self.currentRRad

      if abs(errorL)<config.ACCEPTED_OFFSET and abs(errorR)<config.ACCEPTED_OFFSET:
         self.setVelocity(0)
         self.tankState=TankState.IDLE
         print("done")
         return
      
      
      velocityL = config.KP_DRIVE * errorL
      velocityL = max(-config.MAX_SPEED, min(config.MAX_SPEED, velocityL))

      velocityR = config.KP_DRIVE * errorR
      velocityR = max(-config.MAX_SPEED, min(config.MAX_SPEED, velocityR))

      self.wheelL.setVelocity(velocityL)
      self.wheelR.setVelocity(velocityR)
         

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
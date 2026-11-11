from controller import Robot 
import math
robot = Robot()

from gyro import Gyro
from maze import Maze
from distance_sensors import Distance_sensors
from tank import Tank
from color import Color
import config

from enum import Enum


# kamera_vlavo = robot.getDevice("cameraL")
# kamera_vlavo.enable(config.TIME_STEP)

# kamera_vpravo = robot.getDevice("cameraR")
# kamera_vpravo.enable(config.TIME_STEP)

# emitter = robot.getDevice("emitter")





# farba = robot.getDevice("colour_sensor")
# farba.enable(config.TIME_STEP)

# MAX_SPEED = min(
#     wheelL.getMaxVelocity(),
#     wheelR.getMaxVelocity()
# )








#MY classes
distance_sensors = Distance_sensors(robot)
maze= Maze()
color = Color(robot)
gyro = Gyro(robot)
tank=Tank(robot,"wLEFT motor","wRIGHT motor","wLEFT sensor","wRIGHT sensor",gyro)


#PREMENNE
moveBuffer=["R","F","F","R","F","F","L","F","F","F","L","F","F","R","F","F","R","F","F","R","F","L","F"]
moveBuffer=["R","R","F"]

bufferStep=""
done=False

startupSteps = 60 #about 2seconds of startup time for gyro to stabilize
steps = 0

#map stuff
class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3


x=0
y=0
direction=Direction.UP


while robot.step(config.TIME_STEP) != -1:
    tank.update()
    gyro.update()

    # values = distance_sensors.get_centered_distances_rounded_cm()
    # print("left: ",values["left"][0]," front: ",values["front"][0]," right: ",values["right"][0]," back: ",values["back"][0])


    #startup pause for gyro to stabilize
    if steps < startupSteps:
        steps += 1
        continue
    elif steps == startupSteps:
        gyro.reset()
        steps+=1
        continue
    #----

    if tank.stateName()=="IDLE" and len(moveBuffer)!=0:
        maze.update(distance_sensors.get_directional_distances(),x,y,direction,color.getColour())
    #     ##1 TILE CYCLE
    #     bufferStep=moveBuffer.pop(0)
    #     if bufferStep=="F":
    #         tank.driveTiles(1)
    #     elif bufferStep=="L":
    #         tank.TurnDeg(-90)
    #     elif bufferStep=="R":
    #         tank.TurnDeg(90)
    #     elif bufferStep=="B":
    #         tank.TurnDeg(180)

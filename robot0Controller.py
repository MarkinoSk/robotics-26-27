from controller import Robot 
import math
robot = Robot()

from gyro import Gyro
from maze import Maze
from distance_sensors import Distance_sensors
from tank import Tank
import config

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
gyro = Gyro(robot,"gyro")
maze= Maze()
tank=Tank(robot,"wLEFT motor","wRIGHT motor","wLEFT sensor","wRIGHT sensor",gyro,config.TIME_STEP)



SENSOR_NAMES = ["FL", "FR", "BL", "BR", "RB", "RF", "LB", "LF"]
distance_sensors = Distance_sensors(robot, SENSOR_NAMES,config.TIME_STEP)

#PREMENNE
moveBuffer=["R","F","F","R","F","F","L","F","F","F","L","F","F","R","F","F","R","F","F","R","F","L","F"]

bufferStep=""
done=False

startupSteps = 60 #about 2seconds of startup time for gyro to stabilize
steps = 0


while robot.step(config.TIME_STEP) != -1:
    tank.update()
    gyro.update()

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
        ##1 TILE CYCLE

        bufferStep=moveBuffer.pop(0)
        if bufferStep=="F":
            tank.driveTiles(1)
        elif bufferStep=="R":
            tank.TurnDeg(90)
        elif bufferStep=="L":
            tank.TurnDeg(-90)
        elif bufferStep=="U":
            tank.TurnDeg(180)
    else:
        print(gyro.get_angle())


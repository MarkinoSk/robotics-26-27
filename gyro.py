import math
import config

class Gyro:
    def __init__(self, robot):
        self.sensor = robot.getDevice("gyro")
        self.sensor.enable(config.TIME_STEP)

        self.dt = config.TIME_STEP / 1000.0
        self.angle = 0.0

    def update(self):
        angular_velocity = -self.sensor.getValues()[1]
        self.angle += angular_velocity * self.dt

    def get_angle(self):
        return (self.angle)

    def get_deg_angle(self):
        return math.degrees(self.angle)
    
    def reset(self):
        self.angle = 0.0
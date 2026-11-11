import config


class Color:
    def __init__(self,robot):
        
        self.colourSensor = robot.getDevice("colour_sensor")
        self.colourSensor.enable(config.TIME_STEP)
        

        def getColour(self):
            # r = self.colourSensor.imageGetRed(image, 1, 0, 0)
            # g = self.colourSensor.imageGetGreen(image, 1, 0, 0)
            # b = self.colourSensor.imageGetBlue(image, 1, 0, 0)

            return "WHITE"
import config


class Distance_sensors:
  
    def __init__(self, robot):
        self.sensors = {}
        self.sensor_names = config.SENSOR_NAMES

        for name in self.sensor_names:
            sensor = robot.getDevice(name)
            sensor.enable(config.TIME_STEP)
            self.sensors[name] = sensor


    def transform(self, rawValue):  ##INPUT IN METERS
        #quadratic polynomial with a physical offset to turn a distorted sensor reading into an accurate distance from the center of your robot.
        #made with AI. I cant expain the math
        return (0.068571 * (rawValue ** 2) + 0.336188 * rawValue + 0.006627)  + config.TOF_OFFSET 

        
    def get(self, name):
        return self.transform(self.sensors[name].getValue())

    def get_directional_distances(self):
        return {
                "left": (self.get("LF"),self.get("LB")),
                "front": (self.get("FL"),self.get("FR")),
                "right": (self.get("RF"),self.get("RB")),
                "back": (self.get("BL"),self.get("BR"))
        }

    def get_centered_distances_rounded_cm(self):
            return {
                "left": (round(self.get("LF")*100, 4), round(self.get("LB")*100, 4)),
                "front": (round(self.get("FL")*100, 4), round(self.get("FR")*100, 4)),
                "right": (round(self.get("RF")*100, 4), round(self.get("RB")*100, 4)),
                "back": (round(self.get("BL")*100, 4), round(self.get("BR")*100, 4)),
            }
class Distance_sensors:
  
    def __init__(self, robot,sensor_names, timestep):
        self.sensors = {}
        self.sensor_names=sensor_names
        for name in self.sensor_names:
            sensor = robot.getDevice(name)
            sensor.enable(timestep)
            self.sensors[name] = sensor

    def get(self, name):
        return self.sensors[name].getValue()

    def get_all(self):
        return {
            name: round(sensor.getValue(),4) for name, sensor in self.sensors.items()
        }
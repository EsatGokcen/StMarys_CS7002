# Facade
from light import Light
from thermostat import Thermostat
from security_camera import SecurityCamera

class SmartHomeFacade:
    def __init__(self):
        self.light = Light()
        self.thermostat = Thermostat()
        self.security_camera = SecurityCamera()

    def turn_on_lights(self):
        self.light.turn_on()

    def turn_off_lights(self):
        self.light.turn_off()

    def set_thermostat_temperature(self, temperature):
        self.thermostat.set_temperature(temperature)

    def arm_security_cameras(self):
        self.security_camera.arm()

    def disarm_security_cameras(self):
        self.security_camera.disarm()
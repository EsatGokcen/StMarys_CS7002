# Concrete Commands
from command_interface import Command

class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_on()

class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_off()

class AdjustBrightnessCommand(Command):
    def __init__(self, device, brightness):
        self.device = device
        self.brightness = brightness

    def execute(self):
        self.device.adjust_brightness(self.brightness)

class SetTemperatureCommand(Command):
    def __init__(self, device, temperature):
        self.device = device
        self.temperature = temperature

    def execute(self):
        self.device.set_temperature(self.temperature)
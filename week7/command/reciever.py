# Receiver: HouseholdDevice

class HouseholdDevice:
    
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f"Turning on the {self.name}...")
        # Actual implementation to turn the device on

    def turn_off(self):
        print(f"Turning off the {self.name}...")
        # Actual implementation to turn the device off

    def adjust_brightness(self, brightness):
        print(f"Adjusting {self.name} brightness to {brightness}...")
        # Actual implementation to adjust brightness

    def set_temperature(self, temperature):
        print(f"Setting {self.name} temperature to {temperature}°C...")
        # Actual implementation to set temperature
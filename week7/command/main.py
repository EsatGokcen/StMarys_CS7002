from concrete_commands import *
from reciever import HouseholdDevice
from invoker import ControlPanel

# Client code

if __name__ == "__main__":
    # Create household devices
    light = HouseholdDevice("Light")
    fan = HouseholdDevice("Fan")
    thermostat = HouseholdDevice("Thermostat")

    # Create command objects
    turn_on_light = TurnOnCommand(light)
    turn_off_light = TurnOffCommand(light)
    adjust_fan_speed = AdjustBrightnessCommand(fan, "medium")
    set_temperature = SetTemperatureCommand(thermostat, 22)

    # Create control panel
    control_panel = ControlPanel()

    # Add commands to control panel
    control_panel.add_command(turn_on_light)
    control_panel.add_command(adjust_fan_speed)
    control_panel.add_command(set_temperature)

    # Execute commands
    control_panel.execute_commands()
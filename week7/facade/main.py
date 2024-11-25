# Client code
from facade import SmartHomeFacade

if __name__ == "__main__":
    smart_home = SmartHomeFacade()

    # Perform common tasks using facade
    smart_home.turn_on_lights()
    smart_home.set_thermostat_temperature(22)
    smart_home.arm_security_cameras()
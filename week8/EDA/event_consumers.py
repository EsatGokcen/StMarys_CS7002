# Define EventConsumer classes

class GeneratorFailureConsumer:

    def handle_event(self, event):
        print("Generator Failure Detected:")
        print("Affected Generator:", event.data.get("generator_id"))

class VoltageFluctuationConsumer:

    def handle_event(self, event):
        print("Voltage Fluctuation Detected:")
        print("Voltage Level:", event.data.get("voltage"))

class EmergencyShutdownConsumer:
    
    def handle_event(self, event):
        print("Emergency Shutdown Detected")
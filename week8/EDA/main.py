from event import Event
from event_producer import EventProducer
from event_consumers import *

# Main function

if __name__ == "__main__":
    
    # Create EventProducer instance
    producer = EventProducer()

    # Create EventConsumers
    generator_failure_consumer = GeneratorFailureConsumer()
    voltage_fluctuation_consumer = VoltageFluctuationConsumer()
    emergency_shutdown_consumer = EmergencyShutdownConsumer()

    # Register consumers as listeners for specific events
    producer.add_listener("generator_failure_event", generator_failure_consumer.handle_event)
    producer.add_listener("voltage_fluctuation_event", voltage_fluctuation_consumer.handle_event)
    producer.add_listener("emergency_shutdown_event", emergency_shutdown_consumer.handle_event)

    # Simulate events being produced
    generator_failure_event = Event("generator_failure_event", {"generator_id": 1})
    voltage_fluctuation_event = Event("voltage_fluctuation_event", {"voltage": "High"})
    emergency_shutdown_event = Event("emergency_shutdown_event")

    # Emit events
    producer.emit_event(generator_failure_event)
    producer.emit_event(voltage_fluctuation_event)
    producer.emit_event(emergency_shutdown_event)
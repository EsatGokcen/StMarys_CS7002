# Define EventProducer class

class EventProducer:
    
    def __init__(self):
        self.listeners = {}

    def add_listener(self, event_name, listener):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(listener)

    def emit_event(self, event):
        event_name = event.name
        if event_name in self.listeners:
            for listener in self.listeners[event_name]:
                listener(event)
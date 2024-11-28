# Define Event class

class Event:
    
    def __init__(self, name, data=None):
        self.name = name
        self.data = data or {}
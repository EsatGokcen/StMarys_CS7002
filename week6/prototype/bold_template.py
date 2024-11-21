# concrete class

from message_template import MessagePrototype

class BoldTemplate(MessagePrototype):

    def __init__(self, content):
        self.content = content

    def clone(self):
        return BoldTemplate(self.content)
    
    def apply_formating(self):
        return f"{self.content}"
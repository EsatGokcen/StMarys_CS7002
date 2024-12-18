# concrete class

from message_template import MessagePrototype

class BoldTemplate(MessagePrototype):

    def __init__(self, content):
        self.content = content

    def clone(self):
        return BoldTemplate(self.content)
    
    def apply_formatting(self):
        return f"\033[1m{self.content}\033[1m"
# concrete class

from message_template import MessagePrototype

class ItalicTemplate(MessagePrototype):

    def __init__(self, content):
        self.content = content

    def clone(self):
        return ItalicTemplate(self.content)
    
    def apply_formatting(self):
        return f"{self.content}"
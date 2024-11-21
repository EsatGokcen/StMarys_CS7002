# concrete class

from message_template import MessagePrototype

class UnderlineTemplate(MessagePrototype):

    def __init__(self, content):
        self.content = content

    def clone(self):
        return UnderlineTemplate(self.content)
    
    def apply_formatting(self):
        return f"\x1B[4m{self.content}\x1B[4m"
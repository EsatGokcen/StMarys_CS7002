# Client code

template_registry = {}

def add_template(name, template):
    template_registry[name] = template

def get_template(name):
    return template_registry.get(name)
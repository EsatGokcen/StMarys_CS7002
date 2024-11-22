# Composite class
from component_interface import Shape

class CompositeShape(Shape):
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        self.shapes.remove(shape)

    def draw(self):
        result = f"Composite Shape:\n"
        for shape in self.shapes:
            result += f"\t{shape.draw()}\n"
        return result

    def transform(self, transformation):
        for shape in self.shapes:
            shape.transform(transformation)
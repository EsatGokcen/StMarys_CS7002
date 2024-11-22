# Leaf class
from component_interface import Shape

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        return f"Circle (x={self.x}, y={self.y}, radius={self.radius})"

    def transform(self, transformation):
        # Apply transformation to circle (e.g., rotation, scaling)
        pass
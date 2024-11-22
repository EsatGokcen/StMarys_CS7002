# Leaf class
from component_interface import Shape

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        return f"Rectangle (x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def transform(self, transformation):
        # Apply transformation to rectangle (e.g., rotation, scaling)
        pass
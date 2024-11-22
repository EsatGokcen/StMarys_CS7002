# Leaf class
from component_interface import Shape

class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self):
        return f"Triangle (x1={self.x1}, y1={self.y1}, x2={self.x2}, y2={self.y2}, x3={self.x3}, y3={self.y3})"

    def transform(self, transformation):
        # Apply transformation to triangle (e.g., rotation, scaling)
        pass
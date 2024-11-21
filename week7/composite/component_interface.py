from abc import ABC, abstractmethod

# Component Interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def transform(self, transformation):
        pass

# Leaf classes
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
# Client code
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
from composite_shape import CompositeShape

if __name__ == "__main__":
    # Create individual shapes
    circle = Circle(300, 300, 50)
    rectangle = Rectangle(10, 20, 30, 40)
    triangle = Triangle(100, 200, 150, 250, 200, 200)

    # Create composite shape and add individual shapes to it
    composite_shape = CompositeShape()
    composite_shape.add_shape(rectangle)
    composite_shape.add_shape(circle)

    # Create another composite shape and add individual shapes to it
    another_composite_shape = CompositeShape()
    another_composite_shape.add_shape(triangle)

    # Display composite shapes
    print(composite_shape.draw())
    print(another_composite_shape.draw())
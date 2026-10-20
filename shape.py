# pylint: disable=too-few-public-methods missing-module-docstring
# pylint: disable=too-few-public-methods missing-module-docstring

import math


class Shape:
    def __init__(self, color, name):
        self.name = name
        self.color = color

    def say_name(self):
        return f"My name is {self.name}."


class Rectangle(Shape):
    def __init__(self, color, name, width, height):
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        return f"My name is {self.name} and I am a rectangle."

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, color, name, radius):
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        return f"My name is {self.name} and I am a circle."

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Test kodları
if __name__ == "__main__":

    rectangle1 = Rectangle("Rectangle", "Blue", 5, 3)
    print(rectangle1.say_name())
    print(rectangle1.area())
    print(rectangle1.perimeter())

    circle1 = Circle("Circle", "Red", 4)
    print(circle1.say_name())
    print(circle1.area())
    print(circle1.perimeter())
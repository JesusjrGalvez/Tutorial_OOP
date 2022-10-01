class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from the Rectangle class.
# From __init__ only length is a parameter.
# area and perimeter method are also inherited.
class Square(Rectangle):
    def __init__(self, length):
        # This maps the square's length to the rectangle's length
        # and the square's length to the rectangle's width.
        super().__init__(length, length)


# A cube is a square in 3D.
# Here the cube is inheriting from the Square class.
class Cube(Square):
    # Note that it inherits the __init__ method the parent class (Square)
    # area is inherited from the Rectangle class through Square, i.e,
    # first is look for area in Square and then in Rectangle.
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


cube1 = Cube(5)
print("\n---")
print(cube1.area())
print(cube1.perimeter())
print("----")
print(cube1.surface_area())
print(cube1.volume())

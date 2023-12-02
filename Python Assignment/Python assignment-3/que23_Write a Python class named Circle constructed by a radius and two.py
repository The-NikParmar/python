'''
Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Compute the area of the circle."""
        return math.pi * self.radius**2

    def perimeter(self):
        """Compute the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

# Create an instance of the Circle class with a radius of 7
my_circle = Circle(7)

# Call the area method and display the result
print("Area of the circle:", my_circle.area())

# Call the perimeter method and display the result
print("Perimeter of the circle:", my_circle.perimeter())

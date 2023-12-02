'''
Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle
'''
class Rectangle:

    # Constructor to initialize the length and width attributes
    def __init__(self, l, w):
        self.length = l
        self.width = w

    # Method to display the area of the rectangle
    def show(self):
        print("Area of rectangle:", self.length * self.width)

r = Rectangle(12, 5)
r.show()


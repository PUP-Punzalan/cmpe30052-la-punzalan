"""
Title: Geometry
Submitted by: Amado Niño Rei Punzalan
Course & Section: BSCOE 2-1
Additional info: I added some extra methods to increase what the program can do.
"""

# Packages imported
import math

# Main class that stores all attributes and methods for the program
class REGULAR_POLYGON:
    # Constructor
    def __init__(self, n=int(3), side=float(1), x=float(0), y=float(0)):
        if n < 3:
            self.__no_of_side = 3
        else: self.__no_of_side = n

        if side < 1:
            self.__len_of_side = 1
        else: self.__len_of_side = side

        self.__x = x
        self.__y = y

    # Get methods
    def getPerimeter(self):
        return self.__no_of_side * self.__len_of_side

    def getArea(self):
        return round((self.__no_of_side * (self.__len_of_side * self.__len_of_side) / (4 * math.tan(math.pi / self.__no_of_side))), 2)

    def getNoOfSide(self): # additional method
        return self.__no_of_side

    def getLenOfSide(self): # additional method
        return self.__len_of_side

    def getXCoordinate(self): # additional method
        return self.__x

    def getYCoordinate(self): # additional method
        return self.__y

    # Set methods
    def setNoOfSide(self, no_of_side): # additional method
        if no_of_side < 3:
            self.__no_of_side = 3
        else: self.__no_of_side = no_of_side
        return self.__no_of_side

    def setLenOfSide(self, len_of_side): # additional method
        if len_of_side < 0:
            self.__len_of_side = 1
        else: self.__len_of_side = len_of_side
        return self.__len_of_side

    def setXCoordinate(self, x): # additional method
        self.__x = x
        return self.__x

    def setYCoordinate(self, y): # additional method
        self.__y = y
        return self.__y

# Objects
object1 = REGULAR_POLYGON()
object2 = REGULAR_POLYGON(6, 4)
object3 = REGULAR_POLYGON(10, 4, 5.6, 7.8)

# Print function
def printObjects():
    print(f"Object 1:\nPerimeter: {object1.getPerimeter()}\nArea: {object1.getArea()}\n")
    print(f"Object 2:\nPerimeter: {object2.getPerimeter()}\nArea: {object2.getArea()}\n")
    print(f"Object 3:\nPerimeter: {object3.getPerimeter()}\nArea: {object3.getArea()}\n")

printObjects()
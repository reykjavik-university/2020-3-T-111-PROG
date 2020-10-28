class Rectangle:
    def __init__(self, length=1, width=1):
        self.__length = length if length > 0 else 1
        self.__width = width if width > 0 else 1
        
    def __str__(self):
        return "Length: {}, Width: {}".format(self.__length, self.__width)

    def __repr__(self):
        return "Rectangle({},{})".format(self.__length, self.__width)

    def __eq__(self, other):
        return self.area() == other.area()

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return (self.__length * 2) + (self.__width * 2)

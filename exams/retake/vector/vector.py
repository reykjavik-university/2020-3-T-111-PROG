import math

class Vector:
    def __init__(self, a_list):
        self.__elements = a_list
    
    def __str__(self):
        return str(self.__elements)
    
    def __len__(self):
        return len(self.__elements)

    def __add__(self, other):
        result = Vector([])
        for i in range(len(self)):
            result.__elements.append(self.__elements[i] + other.__elements[i])
        return result
    
    def length(self):
        square_sum = 0
        for i in range(len(self)):
            square_sum += self.__elements[i]**2
        return math.sqrt(square_sum)
    
    def scaling(self, scalar):
        for i in range(len(self)):
            self.__elements[i] = self.__elements[i] * scalar
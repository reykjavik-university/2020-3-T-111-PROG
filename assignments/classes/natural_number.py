class NaturalNumber():

    def __init__(self, num = 0):
        if type(num) == int and num > 0:
            self.__num = num
        else:
            self.__num = None

    def __str__(self):
        return str(self.__num)

    def __add__(self, other):
        if self.__num == None or other.__num == None:
            return None
        else:
            return NaturalNumber(self.__num + other.__num)
    
    def __sub__(self, other):
        if self.__num == None or other.__num == None:
            return None
        else:
            return NaturalNumber(self.__num - other.__num)

    def __mul__(self, other):
        if self.__num == None or other.__num == None:
            return None
        else:
            return NaturalNumber(self.__num * other.__num)

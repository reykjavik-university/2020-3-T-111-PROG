class Pair():
  def __init__(self, val1=0, val2=0):
    self.val1 = val1
    self.val2 = val2
    
  def __str__(self):
    return "Value 1: {}, Value 2: {}".format(self.val1, self.val2)
    
  def __repr__(self):
    return self.__str__()
  
  def __add__(self,other):
    return Pair(self.val1 + other.val1, self.val2 + other.val2)
  
  
  
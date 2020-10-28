class MyString():
  def __init__(self, a_str = ""):
    self.my_str = str(a_str)
    self.my_len = len(a_str)
    
  def __str__(self):
    return self.my_str
    
  def __repr__(self):
    return self.my_str
    
  def __len__(self):
    return self.my_len
  
  def __gt__(self,other):
    return len(self) > len(other)
      
  def __sub__(self,other):
    if self > other:
      return len(self) - len(other)
    else:
      return len(other) - len(self) 
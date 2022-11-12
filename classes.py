from robot import Robot
      
class Decorator():
  def __init__(self,who):
    self.__who=who
  def getName(self):
    return self.getName()
  

class Building (Decorator):
  def __init__(self,who):
     super().__init__()
  def createHouse(self):
     print("____________Объект", "построил дом.*****************")
  
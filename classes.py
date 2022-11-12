from robot import Robot
      
class Decorator():
  def __init__(self,who):
    self.__who=who
  def getName(self):
    return self.__who.getName()
  

class FirstLearn(Decorator):
  def __init__(self,who):
     super().__init__(who)
     print("++++объект", self.getName(), "научился строить дом методом createHouse")
     print("++++объект", self.getName(), "научился строить сарай методом createBarn")
  def createHouse(self):
     print("____________Объект",self.getName(), "построил дом.*****************")
  def createBarn(self):
     print("____________Объект",self.getName(), "построил сарай.*****************")
  def getName(self):
    return super().getName()
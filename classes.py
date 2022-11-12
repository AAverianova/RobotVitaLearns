"""
Используя внешний класс Robot, создадим свой и расширим его.
"""
from robot import Robot

"""
вариант 1. Наследование

class myRobot(Robot):
    def __init__(self, number: str, name:str):
      super().__init__(number,name) # Наследование
      print("____________Объект создан.********************************")
    def print(self):
      super().print()
      print("Объект выведен на экран...........................")
    def setName(self, newName):
      super().setName(newName)
      print("____________Объекту", self.getNumber(), "сменили имя на", newName,".*********")

"""

"""
вариант 2. Используем внешний класс
"""  
class myRobot():
    def __init__(self, number: str, name:str):
      self.__r= Robot(number,name) # Используем внешний класс
      print("____________Объект создан.********************************")
    def print(self):
      self.__r.print()
      print("Объект выведен на экран...........................")
    def setName(self, newName):
      self.__r.setName(newName)
      print("____________Объекту", self.__r.getNumber(), "сменили имя на", newName,".*********")
    def getName(self):
      return self.__r.getName() 
    def getNumber(self):
      return self.__r.getNumber()


class Decorator():
  def __init__(self,who):
    self.__who=who
  def getName(self):
    return self.__who.getName()
  def setName(self, newName):
    return self.__who.setName(newName)
  def print(self):
    self.__who.print()


class FirstLearn(Decorator):
  def __init__(self,who):
     super().__init__(who)
     print("++++объект", self.getName(), "научился строить дом методом createHouse")
     print("++++объект", self.getName(), "научился строить сарай методом createBarn")
  def createHouse(self):
     print("Объект",self.getName(), "построил дом.*****************")
  def createBarn(self):
     print("Объект",self.getName(), "построил сарай.*****************")


class HasWork(Decorator):
  def __init__(self,who):
     super().__init__(who)
     self.__workExperience = 3
     self.__workPlace = "ООО Кошмарик"
     print("!!!!объект", self.getName(), "принят на работу в \"", self.__workPlace, "\"")
     print("!!!!объект", self.getName(), ", срок эксплуатации:", self.__workExperience, "лет.")
 
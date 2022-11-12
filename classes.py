"""
Классы расположены здесь
"""
printComments = True #Для вывода всех комментариев

#from abc import ABC, abstractmethod
class Thing:
  def __init__(self):
    pass
    

class Robot (Thing):
    def __init__(self, number: str, name:str)->None:
      self.__number = number
      self.__name = name # приватные поля
      if printComments:
        print("____________Объект создан.********************************")
    def print(self):
      print("Robot", self.__name, "has num = ", self.__number)
      if printComments:
        print("____________Объект выведен на экран.**********************")

    def setName(self, newName):
      self.__name=newName
      if printComments:
        print("____________Объекту", self.__number, "сменили имя на", newName,".*********")
      
class Decorator(Thing):
  def __init__(self,who):
    self.__who=who

class Building (Decorator):
  def __init__(self,who):
     super().__init__()
  def createHouse(self):
    
  
"""
Класс Робот написан сторонним разработчиком
"""

class Robot ():
    def __init__(self, number: str, name:str)->None:
      self.__number = number
      self.__name = name # приватные поля
    def print(self):
      print("Robot", self.__name, "has num = ", self.__number)
    def setName(self, newName):
      self.__name=newName
    def getName(self):
      return self.__name
    def getNumber(self):
      return self.__number
      

  
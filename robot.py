"""
Класс Робот написан сторонним разработчиком
"""

class Robot ():
    def __init__(self, number: str, name:str)->None:
      self.__number = number
      self.__name = name # приватные поля
      print("____________Объект создан.********************************")
    def print(self):
      print("Robot", self.__name, "has num = ", self.__number)
      print("____________Объект выведен на экран.**********************")
    def setName(self, newName):
      self.__name=newName
      print("____________Объекту", self.__number, "сменили имя на", newName,".*********")
    def getName(self):
      return self.__name
      

  
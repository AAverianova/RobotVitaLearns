"""
Классы расположены здесь
"""
printComments = True #Для вывода всех комментариев

from abc import ABC, abstractmethod


class Robot:
    def __init__(self, number: str, name:str)->None:
      self.__number = number
      self.__name = name # приватные поля
      if printComments:
        print("      **Объект создан.")
    def print(self):
      print("Robot", self.__name, "has num = ", self.__number)
      if printComments:
        print("      **Объект выведен на экран.")

    def setName(self, newName):
      self.__name=newName
      if printComments:
        print("      **Объекту", self.__number, "сменили имя на", newName)
      

"""
Классы расположены здесь
"""

from abc import ABC, abstractmethod


class Robot:
    def __init__(self, number: str, name:str)->None:
        self.number = number
        self.name = name
    def print(self):
      print("Robot ", self.name, "has num = ", self.number)

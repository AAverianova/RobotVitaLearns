from classes import *
print("Создаём робота...\n")

# Создание робота 
robot = Robot("АА001221-56", "В") 
robot.print()
#Первичное обучение
decor = FirstLearn(robot)
#Переименование робота
robot.setName("Вита")
robot.print()
# Проверка что  можно построить
decor.createHouse()
decor.createBarn()
#Переименование робота
robot.setName("Вита")
robot.print()



from classes import *
print("Создаём робота...\n")

# Создание робота 
robot = myRobot("АА001221-56", "В") 
robot.print()
#Первичное обучение
robot = FirstLearn(robot)
#Переименование робота
robot.setName("Вита")
robot.print()
# Проверка что  можно построить
robot.createHouse()
robot.createBarn()
# отправили на завод
robot = HasWork(robot)
# полявились доп. функции
# robot=NewFunction(robot)

#Переименование робота
robot.setName("Витлик")
robot.print()
# проверить новые функции
# robot.buildFloor()
# robot.breakFloor()


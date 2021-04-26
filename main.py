import sys

from examples import *
from manager import *

'''
    Main file
'''

print("Лабораторная работа №2\n"
      "Если хотите решать уравнение введите 1\n"
      "Если хотите решать систему введите 2")


try:
    userValue = int(input())
    if userValue == 1:
        print("Вы выбрали решение уравнения")
        noLinearExamples()
        taskNumber = int(input())
        print("Введите точность")
        eps = float(input())
        if 1 <= taskNumber <= 5:
            chooseUrv(taskNumber, eps)
        else:
            print("Нет доступного параметра")
            sys.exit(0)
    elif userValue == 2:
        print("Вы выбрали решение системы")
        systemExample()
        taskNumber = int(input())
        print("Введите точность")
        eps = float(input())
        if 1 <= taskNumber <= 5:
            chooseSystem(taskNumber, eps)
        else:
            print("Нет доступного параметра")
            sys.exit(0)
    else:
        print("Не доступного параметра")
except ValueError:
    print("Введенный аргумент не является числом")
except TypeError:
    print("Не поддерживаемая операция ")
except KeyboardInterrupt:
    print("Выход...")




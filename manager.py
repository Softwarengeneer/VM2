from mathMod.methods import *
from graph.painter import *


def chooseUrv(value, eps):
    try:
        print("Введите границы")
        left = float(input())
        right = float(input())
        if left > right:
            t = left
            left = right
            right = t
        if value == 1:
            if not doubChecker(first, left, right):
                print("Уравнение решений не имеет в рамках данного диапазона/метода")
                paintGraph(first)
            else:
                point1 = doubMethod(first, left, right, eps)
                point2 = calcMethod(first, firstP1, left, right, eps)
                pointChecker(first, left, right, point1, point2)

        if value == 2:
            if not doubChecker(second, left, right):
                print("Уравнение решений не имеет в рамках данного диапазона/метода")
                paintGraph(second)
            else:
                point1 = doubMethod(second, left, right, eps)
                point2 = calcMethod(second, secondP1, left, right, eps)
                pointChecker(second, left, right, point1, point2)


        if value == 3:
            if not doubChecker(third, left, right):
                print("Уравнение решений не имеет в рамках данного диапазона/метода")
                paintGraph(third)
            else:
                point1 = doubMethod(third, left, right, eps)
                point2 = calcMethod(third, thirdP1, left, right, eps)
                pointChecker(third, left, right, point1, point2)

        if value == 4:
            if not doubChecker(fourth, left, right):
                print("Уравнение решений не имеет в рамках данного диапазона/метода")
            else:
                point1 = doubMethod(fourth, left, right, eps)
                point2 = calcMethod(fourthP1, thirdP1, left, right, eps)
                pointChecker(fourth, left, right, point1, point2)
                print()

    except TypeError:
        print("Невозможность преобразования введенной строки к числу")


def chooseSystem(value, eps):
    try:
        print("Введите начальные приближения")
        left = float(input())
        right = float(input())
        if left > right:
            t = left
            left = right
            right = t
        if value == 1:
            result = newtonMethod(fun0, yakobian0, left, right, eps)
            systemChecker(result, value)
    except TypeError:
        print("Невозжность преобразования введенной строки к числу")


def pointChecker(function, left, right, point1, point2):
    if resultIntervalChecker(left, right, point1):
        print(point1)
    else:
        print("Решение не удовлетворяет заданному интервалу")
        point1 = 0
    if resultIntervalChecker(left, right, point2):
        print(point2)
    else:
        print("Решение не удовлетворяет заданному интервалу")
        point2 = 0
    paintSolve(function, point1, point2)


def systemChecker(result, number):
    if number == 1:
        print(result)
        paintSystem(valGr, valGr1, result)

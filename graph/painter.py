from mathMod.funcs import *

import pylab
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as ps

line = 0


# Отрисовка графика функции
def paintGraph(function):
    f1 = np.vectorize(function)
    list_of_points = np.arange(-7, 7, 1)
    plt.axhline(line, color='r')
    plt.plot(list_of_points, f1(list_of_points), color='g')
    plt.grid()
    plt.show()


# Отрисовка ответов методов
def paintSolve(function, point1, point2):
    plt.scatter(point1, 0, s=10, color='b')
    plt.scatter(point2, 0, s=10, color='c')
    paintGraph(function)


def paintSystem(function0, function1, result):
    f0 = np.vectorize(function0)
    f1 = np.vectorize(function1)
    list_of_points = np.arange(-7, 9, 1)
    plt.axhline(line, color='r')
    plt.plot(list_of_points, f0(list_of_points), color='g')
    plt.plot(list_of_points, f1(list_of_points), color='m')
    plt.scatter(result[0], result[1], s=15, color='b')
    plt.grid()
    plt.show()


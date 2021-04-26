from numpy import *
from mathMod.funcs import *

import numpy as np


def resultIntervalChecker(left, right, point):
    return left <= point <= right


def doubChecker(function, left, rigth):
    value = False
    for i in np.arange(left, rigth, 0.5):
        for j in np.arange(left, rigth, 0.5):
            if function(i) * function(j) < 0:
                value = True
    return value


# Метод деления пополам
def doubMethod(function, start_x, end_x, eps):
    if function(start_x) == 0:
        return start_x
    if function(end_x) == 0:
        return end_x
    while end_x - start_x > eps:
        dx = (end_x - start_x) / 2.0
        xi = start_x + dx
        if np.sign(function(start_x)) != np.sign(function(xi)):
            end_x = xi
        else:
            start_x = xi
    return xi


# Метод касательных
def calcMethod(function, Pr1, left, rigth, eps):
    if function(left) == 0:
        return left
    if function(rigth) == 0:
        return rigth
    x0 = (left + rigth) / 2
    xn = function(x0)
    xk = xn - function(xn) / Pr1(x0)
    while xk - xn > eps:
        xn = xk
        xk = xn - function(xn) / Pr1(x0)
    return xk


# Метод Ньютона
def newtonMethod(fun0, yakobian0, x0, y0, esp):
    if x0 == y0:
        y0 += 1
    arr_of_result = [x0, y0]
    f0 = fun0(x0, y0)
    check = sum(f0)
    if check == 0.0:
        result = [x0, y0]
        return result
    w0 = yakobian0(x0, y0)
    pr = np.matrix(w0)
    w01 = np.linalg.inv(pr)
    xn = arr_of_result - (w01.dot(f0))
    a = np.squeeze(np.asarray(xn))
    arr_of_esp = []
    for i in range(len(arr_of_result)):
        arr_of_esp.append(abs(a[i] - arr_of_result[i]))
    for j in range(len(arr_of_esp)):
        if arr_of_esp[i] < esp:
            return arr_of_result
    return newtonMethod(fun0, yakobian0, a[0], a[1], esp)

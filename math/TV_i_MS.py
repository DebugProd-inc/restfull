import numpy as np
import scipy
import scipy.spatial
import math
import test_values
import Working_With_JSON
import random as rn
import pynverse as pnv

# получение из выборки расстояний Махаланобиса при штатном
# функционировании квантили заднного уровня


# квантиль выборочной функции распределения (первый вариант)
def get_quantile(dj, confidence_probability):
    return np.quantile(dj, confidence_probability)


# МНК оценка коэфициентов
def parameter_estimation(X, Y):
    result = np.linalg.lstsq(X, Y, rcond=None)
    return result[0]


# выборочная функция распределения
def get_func(dj):
    dj.sort()
    f = []
    for i in range(0, len(dj)):
        p = i/len(dj)
        f.append(p)
    return f


# Создаёт матрицу X для МНК оценки. (первый столбец единицы)
"""def get_X_Matrix(dj):
    S = 3
    New_d = []
    for i in range(0, len(dj)):
        New_d.append([])
        for j in range(0, S + 1):
            New_d[i].append(dj[i]**j)
    print('X_matrix = ', np.matrix(New_d))
    return np.matrix(New_d)"""


# Класс функции распределения
class Class_distribution_func:
    # конструктор
    def __init__(self, dj):
        # степень полинома в распределении Вейбулла
        self.S = 3
        # запоминаем значения выборки дистанции (особо не надо)
        self.d = dj.sort()
        # по выборочной функции распределения
        # находим значения полинома для каждого из значений функции
        B_ = np.matrix(list(map(lambda x: (-(math.log(1-x))), get_func(dj))))
        # находим коэффициенты полинома (чтобы потом вычислять)
        self.parameters = parameter_estimation(
            np.vstack([dj, np.ones(len(dj))]).T,
            np.transpose(B_)
            )

    def B_Veybull(self, x):  # значение полинома для распределения Вейбулла
        return np.polyval(self.parameters, x)

    def get_value(self, x):  # значение функции распределения в точке
        return 1 - (math.e**(-self.B_Veybull(x)**self.S))

    def kim_quantile(self, alpha):
        p = self.parameters
        result = pnv.inversefunc(
            (lambda x: 1 - math.exp(-(np.polyval(p, x))**self.S)),
            y_values=alpha)
        return result


"""    def get_quantile(self, alfa):
        B_ = (-(math.log(1-alfa)))
        print('B_ = ', B_)
        # значение полинома (обратное от функции распределения)
        param = np.copy(self.parameters)
        # копируем параметры, чтобы не испортить начальные значения
        param[len(param)-1] -= B_
        param = np.reshape(param, (1, len(param)))
        # вычитаем из последнего коэффициента значение полинома от альфа
        # чтобы получить коэф. многочлена, для нахождения его корней
        roots = np.roots(param[0])
        print('param = ', param)
        # вычисление корней
        print(roots.__str__() + "==КОРНИ БЕЗ ФИЛЬТРА")
        roots = list(filter(
            lambda x: (x.imag == 0 and x.real >= 0), roots
            ))
        # фильтруем корни от отрицательных и комплексных
        roots = list(map(lambda x: (x.real), roots))
        print(roots.__str__() + " @@")
        print("len = " + str(len(roots)))
        result = min(roots)
        return result"""


# после проверок функциональности удалить:
a = np.random.uniform(2, 8, (1, 5))  # нормально распределённый массив
print('x1 = ', a)
Working_With_JSON.Write_Init_Data(a[0])
c = Class_distribution_func(a[0])
print('q1 = ', get_quantile(a[0], 0.95))
# print('q2 = ', c.get_quantile(0.95))
print('q3 = ', c.kim_quantile(0.95))

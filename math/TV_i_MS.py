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


# Класс функции распределения
class Class_distribution_func:
    # конструктор
    def __init__(self, dj):
        # степень полинома в распределении Вейбулла
        self.S = 5
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

    def get_quantile(self, alpha):
        result = pnv.inversefunc(
            (lambda x: 1 - math.exp(-(np.polyval(self.parameters, x))**self.S)),
            y_values=alpha)
        return result


# после проверок функциональности удалить:
a = np.random.uniform(2, 8, (1, 5))  # нормально распределённый массив

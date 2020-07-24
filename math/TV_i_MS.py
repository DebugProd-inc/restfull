import numpy as np
import scipy
import scipy.spatial
import math
import test_values
import Working_With_JSON

# получение из выборки расстояний Махаланобиса при штатном
# функционировании квантили заднного уровня
# S = 18  # степень полинома в распределении Вейбулла


# квантиль выборочной функции распределения
def get_quantile(dj, confidence_probability):
    return np.quantile(dj, confidence_probability)


# МНК оценка коэфициентов
def parameter_estimation(X, Y):
    X_ = X.transpose()
    Y = np.matrix(Y)
    result = np.dot(X_, X)
    result = np.linalg.inv(result)
    result = np.dot(result, X_)
    result = np.dot(result, Y)
# print('p.e = ', result)
    return result


# выборочная функция распределения
def get_func(dj):
    dj.sort()
    f = []
    for i in range(0, len(dj)):
        p = i/len(dj)
        f.append(p)
# print('g.f. = ', f)
    return f


# Создаёт матрицу X для МНК оценки. (первый столбец единицы)
def get_X_Matrix(dj):
    S = 1  # константа
    # S = len(dj)
    New_d = []
    for i in range(0, len(dj)):
        New_d.append([])
        for j in range(0, S + 1):
            New_d[i].append(dj[i]**j)
# print('X_matrix = ', np.matrix(New_d))
    return np.matrix(New_d)


# Класс функции распределения
class Class_distribution_func:
    # конструктор
    def __init__(self, dj):
        # запоминаем значения выборки дистанции (особо не надо)
        self.d = dj.sort()
        # по выборочной функции распределения
        # находим значения полинома для каждого из значений функции
        B_ = np.matrix(list(map(lambda x: (-(math.log(1-x))), get_func(dj))))
        # находим коэффициенты полинома (чтобы потом вычислять)
        self.parameters = parameter_estimation(
            get_X_Matrix(dj),
            np.transpose(B_)
            )

    def B_Veybull(self, x):  # значение полинома для распределения Вейбулла
        return np.polyval(self.parameters, x)

    def get_value(self, x):  # значение функции распределения в точке
        return 1 - (math.e**(-self.B_Veybull(x)))

    def get_quantile(self, alfa):
        B_ = (-(math.log(1-alfa)))
        # значение полинома (обратное от функции распределения)
        param = np.copy(self.parameters)
        # копируем параметры, чтобы не испортить начальные значения
        param[len(param)-1] -= B_
        param = np.reshape(param, (1, len(param)))
        # вычитаем из последнего коэффициента значение полинома от альфа
        # чтобы получить коэф. многочлена, для нахождения его корней
        roots = np.roots(param[0])
        # a = [] А ЭТО НАДО?
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
        return result  # выбор корня подвергается критике
        # я хз пока как делать правильно, так что пока так


a = test_values.x1  # np.array([1, 1.1, 1.9, 2, 1.2, 2.1])
Working_With_JSON.Write_Init_Data(a)
c = Class_distribution_func(a)
print(get_quantile(a, 0.8))
print(c.get_quantile(0.8))
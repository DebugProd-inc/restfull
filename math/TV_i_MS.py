import numpy as np
import scipy
import scipy.spatial
import math


# получение из выборки расстояний Махаланобиса при штатном
# функционировании квантили заднного уровня
S = 5  # степень полинома в распределении Вейбулла


# квантиль выборочной функции распределения
def get_quantile(dj, confidence_probability):
    return np.quantile(dj, confidence_probability)


# МНК оценка коэфициентов
def parameter_estimation(X, Y):
    print(Y)
    X_ = X.transpose()
    Y = np.matrix(Y)
    result = np.dot(X_, X)
    result = np.linalg.inv(result)
    result = np.dot(result, X_)
    result = np.dot(result, Y)
    return result


# выборочная функция распределения
def get_func(dj):
    dj.sort()
    f = []
    for i in range(0, len(dj)):
        p = i/len(dj)
        f.append(p)
    return f


# Создаёт матрицу X для МНК оценки. (первый столбец единицы)
def get_X_Matrix(dj):
    global S
    S = len(dj)
    New_d = []
    for i in range(0, len(dj)):
        New_d.append([])
        for j in range(0, S + 1):
            New_d[i].append(dj[i]**j)
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
        # вычисление корней
        roots = list(
            filter(lambda x: (x >= 0) and (isinstance(x, float)), roots)
            )
        # фильтруем корни от отрицательных и комплексных
        return roots  # выбор корня подвергается критике
        # я хз пока как делать правильно, так что пока так


# значения для проверки функциональности
a = np.array([1, 1.1, 1.9, 2, 1.2, 2.1])
c = Class_distribution_func(a)
print(c.get_quantile(0.8))

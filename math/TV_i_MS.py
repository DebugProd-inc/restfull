import numpy as np
import scipy
import scipy.spatial
import math
# from test_values import confidence_probability

# получение из выборки расстояний Махаланобиса при штатном
# функционировании квантили заднного уровня
S = 0  # степень полинома я хз как её реально найти, так что от балды


# квантиль выборочной функции распределения
def get_quantile(dj, confidence_probability):
    return np.quantile(dj, confidence_probability)


# МНК оценка коэфициентов
def parameter_estimation(X, Y):
    X_ = X.transpose()
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
        for j in range(S + 1, 0):
            New_d[i].append(dj[i]**j)
    return New_d


# Класс функции распределения
class Class_distribution_func:
    def __init__(self, dj):  # конструктор
        self.d = dj.sort()
        # запоминаем значения выборки дистанции (особо не надо)
        fun = lambda x: (-(math.log(1-x)))  # ему не нравится лямбда
        # но мне пофиг, потому что мне нравится)))))
        B_ = map(fun, get_func(dj))  # по выборочной функции распределения
        # находим значения полинома для каждого из значений функции
        self.parameters = parameter_estimation(
            get_X_Matrix(dj),
            np.transpose(B_)
            )
        # находим коэффициенты полинома (чтобы потом вычислять)

    def B_Veybull(self, x):  # значение полинома для распределения Вейбулла
        return np.polyval(self.parameters, x)

    def get_value(self, x):  # значение функции распределения в точке
        return 1 - (math.e**(-self.B_Veybull(x)))

    def get_quantile(self, alfa):
        B_ = (-(math.log(1-alfa)))
        # значение полинома (обратное от функции распределения)
        param = np.copy(self.parameters)
        # копируем параметры, чтобы не испортить начальные значения
        param[len(B_)-1] -= B_
        # вычитаем из последнего коэффициента значение полинома от альфа
        # чтобы получить коэф. многочлена, для нахождения его корней
        roots = np.roots(param)
        # вычисление корней
        roots = filter(lambda x: (x >= 0) and (isinstance(x, float)), roots)
        # фильтруем корни от отрицательных и комплексных
        return min(roots)  # выбор корня подвергается критике
        # я хз пока как делать правильно, так что пока так
